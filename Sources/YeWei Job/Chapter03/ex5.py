import time
import datetime

# 获取当前时间的秒数
current_time = time.time()

# 计算今天距离1970年1月1日过了多少天
days_since_epoch = int(current_time // 86400)

# 计算今天是星期几
today = datetime.datetime.now().weekday()

# 输出结果
print(f"Days since January 1, 1970: {days_since_epoch}")
print(f"Today is {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][today]}.")
