import numpy as np
from matplotlib import pyplot as plt
from pycbc import waveform

# 设置黑洞质量范围和间隔
mass_range = np.arange(35, 161, 1)
mass_ratio_range = np.linspace(0.1, 1.0, 30)

# 存储引力波数据和生成参数的列表
gravitational_waves = []
parameters = []

# 生成引力波数据和参数
for mass1 in mass_range:
    for mass_ratio in mass_ratio_range:
        mass2 = mass1 * mass_ratio

        # 生成波形
        sample_rate = 4096
        duration = 4.0
        hp, _ = waveform.get_td_waveform(approximant='SEOBNRv4',
                                         mass1=mass1, mass2=mass2, delta_t=1.0 / sample_rate, f_lower=20)

        hp_array = np.array(hp)
        gravitational_waves.append(hp_array)
        parameters.append({'mass1': mass1, 'mass2': mass2})

# 获取最大波形长度
max_waveform_length = max(len(waveform) for waveform in gravitational_waves)

# 填充波形数据，使其具有相同的长度
padded_waves = np.array([np.pad(waveform, (0, max_waveform_length - len(waveform))) for waveform in gravitational_waves])

# 将引力波数据和参数转换为NumPy数组
gravitational_waves = np.array(padded_waves)
parameters = np.array(parameters)

# 存储为npy文件
np.save('gravitational_waves.npy', gravitational_waves)
np.save('parameters.npy', parameters)

# 从npy文件中加载引力波数据和生成参数
gravitational_waves = np.load('gravitational_waves.npy')
parameters = np.load('parameters.npy', allow_pickle=True)

# 可视化展示引力波波形
for i, gw in enumerate(gravitational_waves):
    mass1 = parameters[i]['mass1']
    mass2 = parameters[i]['mass2']

    # 绘制波形图
    time = np.arange(0, max_waveform_length) * (1.0 / sample_rate)
    plt.plot(time, gw, label=f'Mass1={mass1}, Mass2={mass2}')

plt.xlabel('Time (s)')
plt.ylabel('Strain')
plt.title('Gravitational Waveforms')
plt.grid()
plt.legend()
plt.show()
