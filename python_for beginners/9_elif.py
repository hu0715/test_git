user_weight=float(input("请输入您的体重（kg）："))
user_height=float(input("请输入您的身高（m）："))
BMI=user_weight/user_height**2
if BMI<=18.5:
    print("偏瘦")
elif 18.5<BMI<=25:
    print("正常")
elif 30>=BMI>25:
    print("偏胖")
else:
    print("肥胖")