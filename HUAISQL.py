import ast
import time
from pylsy import pylsytable
import random


#su=[ast.literal_eval(i) for i in open('su.txt','r')]#解析数据
su=[eval(i) for i in open('su.txt','r')]#解析数据


def xian():
#显示全部
    print('*'*50)
    n=0
    for i in su:
       print(str(n)+'__'+str(i))
       n+=1
    #print('\n'.join([str(o) for o in su]))#显示全部
    print('*'*50)
    
def xian_n():
   attributes=["标题","内容","时间"]
   table=pylsytable(attributes)
   table.add_data("标题",[i['name'][0:5] for i in su])
   table.add_data("内容",[i['pwd'][0:8] for i in su])
   table.add_data("时间",[i['nid'][len(i['nid'])-8:len(i['nid'])] for i in su])
   print(table)




    
def xie(name,pwd):
#增加账号
    name=name
    pwd=pwd
    f=open('su.txt','a')
    f.write(str({'nid':time.strftime("%Y-%m-%d %H:%M:%S"),'name':name,'pwd':pwd}))#写入数据
    f.write('\n')
    su.append({'nid':time.strftime("%Y-%m-%d %H:%M:%S"),'name':name,'pwd':pwd})
def cha(name):
#查密码
    for i in su:
        if i['name']==name:
            return i['pwd']

def genxin():
    #对数据删除改证，后更新到txt
    f=open('su.txt','w')
    f=open('su.txt','a')
    for i in su:
      f.write(str(i)+'\n')
    print('更新成功')
