#在线可执行的浏览器为 https://c.runoob.com/compile/9 选择 "python3 在线工具"，复制粘贴文档全文 并点击 "点击运行"。等待即可
import random
import sys

#分别对应 市内公车，市外公车，市内私车，市外私车
typeA=125
typeB=140
typeC=150
typeD=180
NAMES=["甲","乙","丙","丁","戊","己","庚","辛","子","丑","寅","卯","辰","午"]
#默认天数
DAYS=31


#range里的值 是假设 如果一个人只选择 一类出行方式，那么理论的最大值。
#比如125的情况下，1000块钱可以出行8次，因此取值范围就是0～8。那么就对应着range(9).
#140情况下，1000块支持出行7次。所以就是range(8).
#最后判断一下一个人，在一个月的出行计划总金额满足一定条件
#此函数返回某个人在满足金额限制的情况下，所有的出行可能性。

def one_man_choice():
    res=[]
    for a in range(9):
        for b in range(8):
            for c in range(7):
                for d in range(6):
                    sum = typeA * a + typeB * b + typeC * c + typeD *d
                    if (sum <= 1000 and sum >= 950):
                        res_tmp = [a,b,c,d,sum]
                        res.append(res_tmp)

    return res

#获取一个人在一个月的出行计划
#假设我已经确认某一个人要出行多少次各种类型。现在就要将这些次数，随机分配到一个月内。
#返回值是一个月，某个人的出行计划。
def get_one_plan(days,single_plan):
    month_plan=['0'] * days
    if(single_plan[0]) > 0:
        for i in range(single_plan[0]):
            target = random.randint(1,days)
            while (month_plan[target-1]!= '0'):
                target = random.randint(1, days)
            month_plan[target-1]='公车市内'
    if(single_plan[1]) > 0:
        for i in range(single_plan[1]):
            target = random.randint(1,days)
            while (month_plan[target-1]!= '0'):
                target = random.randint(1, days)
            month_plan[target-1]='公车市外'
    if(single_plan[2]) > 0:
        for i in range(single_plan[2]):
            target = random.randint(1,days)
            while (month_plan[target-1]!= '0'):
                target = random.randint(1, days)
            month_plan[target-1]='私车市内'
    if(single_plan[3]) > 0:
        for i in range(single_plan[3]):
            target = random.randint(1,days)
            while (month_plan[target-1]!= '0'):
                target = random.randint(1, days)
            month_plan[target-1]='私车市外'

    return month_plan


#对每一个人，都生成一遍个人的出行计划，合起来，成为整个团队的出行计划。

def get_all_plan(days,choices):
    choices_count=len(choices)
    month_plan={}
    for name in NAMES:
        choice = choices[random.randint(1,choices_count) - 1]
        sum=choice[4]
        plan=get_one_plan(days,choice)
        month_plan[name]=[plan,sum]
    return month_plan

#判断出行计划的合理性。
#输入是整个团队在某个月内的出行计划，以及对应月的天数。
#通过统计每一天多少人出行，判断是否合理。合理条件为：要么当天没有人出行，要么是2～5人出行。
def check_plan(days,month_plan):
    map_count=[0] * days
    res = True
    for value in month_plan.values():
        for i in range(len(value[0])):
            if(value[0][i]!='0'):
                map_count[i]+=1

    for count in map_count:
        if(count!=0 and (count > 5 or count < 2)):
            res = False
            break
    return (res,map_count)


#结果输出
def show_result(result):
    for i in result:
        list_tmp=[]
        str=""
        for index in range(len(result[i][0])):
            if(result[i][0][index] != '0'):
                str="%s号:%s" % (index+1,result[i][0][index])
                list_tmp.append(str)

        print("名字:[%s],金额:[%s],排班：%s."%(i,result[i][1],list_tmp))


#函数总入口
#通过不断生成随机计划，然后判断是否符合要求，如果要求满足，则退出循环并输出结果。
if __name__ == '__main__':
    if(len(sys.argv) == 1):
        days = DAYS
        print("默认天数为 %d" %days)

    if(len(sys.argv) > 1):
        input=sys.argv[1]
        if(input.isdigit() == False):
            print("请输入28～31 的数字")
            exit(1)
        days=int(input)
        if(days>31 or days < 28):
            print("范围错误，请输入28～31的数字")
            exit(1)
    print("天数为: %d" %days)
    choices=one_man_choice()
    while(True):
        result = get_all_plan(days,choices)
        (check_res,map_count)=check_plan(days,result)
        if (check_res == True):
            break
    print("当月每天的出行人数统计：%s" % map_count)
    show_result(result)


