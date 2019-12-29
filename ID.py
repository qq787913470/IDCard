#安装 pip install id-validator
# import time
import datetime
from id_validator import validator
#遍历所有日期，print通过校验的身份证号码
# #身份证前6位,出生年,身份证后4位
def vali_dator(id1,id2,id3):
    s = 0
    for i in create_assist_date(id2,"",""):
        theid = id1 + i + id3
        if validator.is_valid(theid):
            s+=1
            print(theid)
    print("共有-》"+str(s)+"个符合的身份证数据")
def create_assist_date(year = None,datestart = None,dateend = None):
	# 创建日期辅助表
    if year is not None:
        datestart = year + "0101"
        dateend = year + "1231"
    if datestart is None:
        datestart = '20160101'
    if dateend is None:
        dateend = datetime.datetime.now().strftime('%Y%m%d')
    # 转为日期格式
    datestart=datetime.datetime.strptime(datestart,'%Y%m%d')
    dateend=datetime.datetime.strptime(dateend,'%Y%m%d')
    date_list = []
    date_list.append(datestart.strftime('%Y%m%d'))
    while datestart<dateend:
    # 日期叠加一天
        datestart+=datetime.timedelta(days=+1)
        # 日期转字符串存入列表
        date_list.append(datestart.strftime('%Y%m%d'))
    # print(date_list)
    return date_list
if __name__ == '__main__':
    vali_dator('410526', '1991', '6499')
