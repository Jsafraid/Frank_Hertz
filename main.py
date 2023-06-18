import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as signal


df = pd.read_excel('data.xlsx')

all_group = 5

# 存储所有电压和电流数据的列表
voltage = []
current = []

# 循环读取每一组数据的两列，并将其添加到相应的列表中
for i in range(all_group):
    voltage_column = '电压' + str(i + 1)
    current_column = '电流' + str(i + 1)

    # 检查列是否存在于数据框中，如果不存在则跳过该组数据
    if voltage_column in df.columns and current_column in df.columns:
        voltage.extend(df[voltage_column].tolist())
        current.extend(df[current_column].tolist())

# 将电流乘以10的负7次方，转换为实际的电流值
current = [i * 10e-7 for i in current]

# 绘制电压-电流曲线
plt.plot(voltage, current, 'b-')

# 使用峰值检测算法寻找波峰点
peaks, _ = signal.find_peaks(current, prominence=0.3e-7)

# 标记波峰点,显示坐标
peak_v = [voltage[idx] for idx in peaks]
peak_c = [current[idx] for idx in peaks]
plt.plot(peak_v, peak_c, 'ro', label='Peaks')

for i in range(len(peaks)):
    x = peak_v[i]
    y = peak_c[i]
    y_s = '{:.3f}'.format(y * 1000000)
    plt.annotate(f'({x:.2f}, {y_s})', xy=(x, y), xytext=(x + 0.1, y), color='red')


plt.plot(voltage, current, 'x', color='black', label='Data Points')
plt.legend()
plt.xlabel('Voltage (V)')
plt.ylabel('Current (nA)')
plt.show()
