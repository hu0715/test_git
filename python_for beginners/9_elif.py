def calc_bmi_category_and_advice(bmi: float) -> tuple[str, str]:
    if bmi <= 18.5:
        return "偏瘦", "建议：适当增加热量摄入，并配合力量训练。"
    if 18.5 < bmi <= 25:
        return "正常", "建议：保持均衡饮食与规律运动。"
    if 25 < bmi <= 30:
        return "偏胖", "建议：适当控制饮食热量，增加有氧运动。"
    return "肥胖", "建议：优先从饮食与运动做起，必要时咨询医生或营养师。"


while True:
    try:
        user_weight = float(input("请输入您的体重（kg）："))
        user_height = float(input("请输入您的身高（m）："))
        if user_weight <= 0 or user_height <= 0:
            print("体重和身高必须是大于 0 的数字，请重新输入。")
            continue
    except ValueError:
        print("输入格式不正确，请输入数字（例如：60 或 1.70）。")
        continue

    bmi = user_weight / (user_height**2)
    category, advice = calc_bmi_category_and_advice(bmi)
    print(f"您的 BMI 为：{bmi:.2f}（{category}）")
    print(advice)

    again = input("是否继续计算？(y/n)：").strip().lower()
    if again not in {"y", "yes"}:
        break

