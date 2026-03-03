user_age=input("enter your age")#这个是字符串str
print("您的年龄为"+user_age)
#BMI=体重/身高^2
user_weight=float(input("请输入您的体重（kg）："))
user_height=float(input("请输入您的身高（m）："))
BMI=user_weight/user_height**2
print("BMI:"+str(BMI))
