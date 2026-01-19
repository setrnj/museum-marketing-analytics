import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('zh_CN')
np.random.seed(42)
random.seed(42)

products = [
    {"name": "千里江山图丝巾", "category": "服饰配饰", "price": 198},
    {"name": "故宫猫盲盒", "category": "潮玩盲盒", "price": 69},
    {"name": "敦煌飞天书签套装", "category": "文具礼品", "price": 35},
    {"name": "青铜器复刻摆件", "category": "家居装饰", "price": 299},
    {"name": "文物AR明信片", "category": "数字文创", "price": 25},
    {"name": "唐俑雪糕（虚拟券）", "category": "食品体验", "price": 18},
]

channels = ["小红书", "抖音", "微信公众号", "淘宝直播", "线下门店扫码"]

data = []
start_date = datetime(2025, 3, 1)
end_date = datetime(2025, 12, 31)

for i in range(10000):
    user_id = f"U{str(i+1).zfill(6)}"
    product = random.choice(products)
    channel = random.choices(channels, weights=[30, 25, 20, 15, 10])[0]
    
    browse_time = fake.date_time_between(start_date=start_date, end_date=end_date)
    
    if random.random() < 0.6:
        cart_time = browse_time + timedelta(minutes=random.randint(1, 120))
        if random.random() < 0.5:
            order_time = cart_time + timedelta(minutes=random.randint(5, 180))
            is_repurchase = random.random() < 0.3
            data.append({
                "user_id": user_id,
                "product_name": product["name"],
                "category": product["category"],
                "price": product["price"],
                "channel": channel,
                "browse_time": browse_time,
                "cart_time": cart_time,
                "order_time": order_time,
                "is_repurchase": is_repurchase
            })
        else:
            data.append({
                "user_id": user_id,
                "product_name": product["name"],
                "category": product["category"],
                "price": product["price"],
                "channel": channel,
                "browse_time": browse_time,
                "cart_time": cart_time,
                "order_time": pd.NaT,
                "is_repurchase": False
            })
    else:
        data.append({
            "user_id": user_id,
            "product_name": product["name"],
            "category": product["category"],
            "price": product["price"],
            "channel": channel,
            "browse_time": browse_time,
            "cart_time": pd.NaT,
            "order_time": pd.NaT,
            "is_repurchase": False
        })

df = pd.DataFrame(data)
df.to_csv("museum_users.csv", index=False, encoding="utf_8_sig")
print("✅ 数据生成成功！共 {} 条记录".format(len(df)))
print("📁 文件已保存为 museum_users.csv")
