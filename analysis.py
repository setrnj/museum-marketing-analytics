import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体（兼容 Windows/Mac/Linux）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 确保输出目录存在
os.makedirs('output', exist_ok=True)

# 读取数据
df = pd.read_csv('museum_users.csv')

# 创建 is_paid 列：order_time 非空即为已支付
df['is_paid'] = df['order_time'].notna()

# 1. 各渠道支付转化率
conversion_rate = df.groupby('channel')['is_paid'].mean().sort_values(ascending=False)

# 绘图
plt.figure(figsize=(10, 6))
bars = plt.bar(conversion_rate.index, conversion_rate.values, color='steelblue')
plt.title('各渠道支付转化率对比', fontsize=16)
plt.ylabel('支付转化率', fontsize=12)
plt.xlabel('渠道', fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 1)

# 在柱子上显示数值
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.02,
             f'{height:.1%}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('output/channel_conversion.png', dpi=150, bbox_inches='tight')
plt.close()

# 2. 输出统计摘要到文本
with open('output/summary.txt', 'w', encoding='utf-8') as f:
    f.write("博物馆营销数据分析报告\n")
    f.write("="*30 + "\n\n")
    f.write(f"总用户数: {len(df)}\n")
    f.write(f"支付用户数: {df['is_paid'].sum()}\n")
    f.write(f"整体转化率: {df['is_paid'].mean():.1%}\n\n")
    
    f.write("各渠道转化率:\n")
    for channel, rate in conversion_rate.items():
        f.write(f"- {channel}: {rate:.1%}\n")

print("✅ 分析完成！结果保存在 output/ 目录：")
print("- output/channel_conversion.png")
print("- output/summary.txt")
