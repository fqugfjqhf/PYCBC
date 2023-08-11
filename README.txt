# 引力波波形生成器

这段代码用于生成一系列二进制黑洞合并事件的引力波波形，并将波形数据和参数保存为 `.npy` 文件。你可以根据需要自行调整代码中的参数范围和近似方法。

## 需求

- Python 3.x
- `numpy` 库
- `matplotlib` 库
- `pycbc` 库

你可以使用以下命令安装所需的库：
```bash
pip install numpy matplotlib pycbc

自定义
你可以修改 generate_waveforms.py 脚本中的 mass_range 和 mass_ratio_range 变量，以指定你要为其生成波形的黑洞质量范围和质量比例范围。

默认情况下，脚本使用 SEOBNRv4 波形近似。你可以在 waveform.get_td_waveform() 函数中将其更改为其他可用的近似方法。