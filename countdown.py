import time

seconds = int(input("請輸入倒數秒數："))
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)
print("時間到！")