import pandas as pd


def asd(money_sum, day, time, jia_fa, jia_zhoumo, jia_day, she):
    day_money = money_sum / day
    h = day_money / 8
    tongqin = day * day_money - time * h + (jia_fa * 2 + jia_zhoumo * 1.5 + jia_day) * h
    summ = tongqin + money_sum - she * 0.21
    return summ


def cont(lists):
    summ = 0
    x = 0
    for i in lists[0:-1]:
        summ += i
        x += 1
    return round(summ/x, 2)


dx = pd.read_excel(r'http://72.itmc.org.cn:80/JS001/data/user/13965/242/fj_employee_salary_work_books.xlsx', sheet_name='基本薪资')
dt = pd.read_excel(r'http://72.itmc.org.cn:80/JS001/data/user/13965/242/fj_employee_salary_work_books.xlsx', sheet_name='上班通勤')
dx["应出勤天数（天）"] = dt["应出勤天数（天）"]
dx["法定假日加班（小时）"] = dt["法定假日加班（小时）"]
dx["周末加班（小时）"] = dt["周末加班（小时）"]
dx["工作日加班（小时）"] = dt["工作日加班（小时）"]
dx["请假（小时）"] = dt["请假（小时）"]
dx["应出勤天数（天）"] = dt["应出勤天数（天）"]
dx = dx.fillna(0)
dx["月基本薪资"] = dx["基本薪资"] + dx["岗位工资"] + dx["绩效工资"]
dx["日薪"] = dx["月基本薪资"]/dx["应出勤天数（天）"]
dx["平均薪资"] = dx["月基本薪资"] - dx["社会保险缴费基数"] * 0.21 + dx["日薪"]/8*(dx["法定假日加班（小时）"]*2+dx["周末加班（小时）"]*1.5+dx["工作日加班（小时）"]-dx["请假（小时）"])
dd = round(dx.groupby("部门")["平均薪资"].mean(), 2)

print(dd.sort_values(ascending=False))







