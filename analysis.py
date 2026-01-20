import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('museum_users.csv')

# 创建 is_paid 列：如果 order_time 不为空，则已支付
df['is_paid'] = df['order_time'].notna()

# 1. 各渠道支付转化率
conversion_rate = df.groupby('channel')['is_paid'].mean()

# 绘图
plt.figure(figsize=(10, 6))
plt.bar(conversion_rate.index, conversion_rate.values, color='steelblue')
plt.title('各渠道支付转化率对比')
plt.ylabel('支付转化率')
plt.xlabel('渠道')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('channel_conversion.png', dpi=150, bbox_inches='tight')
plt.close()

print("图表已生成：")
print("- channel_conversion.png")
