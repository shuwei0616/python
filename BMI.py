h = float(input('請輸入身高(cm)：'))/100
# 使用 float 轉換成浮點數後除以 100 ( 因為身高可能會有小數點 )

w = float(input('請輸入體重(kg)：'))
# 使用 float 轉換成浮點數 ( 因為體重可能會有小數點 )

bmi = w/(h*h)                           
print(f'你的 BMI 數值為：{bmi}')