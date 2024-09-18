# 百分制成绩转换为等级制成绩。
# 要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。

scope = int(input('请输入分数：'))
if scope >= 90:
    grade = 'A'
elif scope >= 80:
    grade = 'B'
elif scope >= 70:
    grade = 'C'
elif scope >= 60:
    grade = 'D'
else:
    grade = 'E'

print(f'最终评分：{grade}')
