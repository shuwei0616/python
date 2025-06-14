import re

pw = input("請輸入密碼：")
if len(pw) >= 8 and re.search(r"[A-Z]", pw) and re.search(r"[a-z]", pw) and re.search(r"[0-9]", pw):
    print("密碼強度：高")
else:
    print("密碼強度：弱")