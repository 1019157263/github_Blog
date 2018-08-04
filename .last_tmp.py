# -*- coding:utf-8 -*-

from HUAISQL import *
while True:
    print('数据库模拟系统')
    print('*'*50)
    print('功能列表')
    print('1:注册新用户')
    print('2:登录用户')
    print('3:显示用户列表')
    print('4:查询用户密码')
    print('5:自定义命令操作')
    print('q:退出系统')
    print('*'*50)
    #for i in range(50):xie(f'admin{i}',f'root{i}')
    a=input('请输入功能代码:')
    if a=='1':
        newname=input('请输入新的用户名:')
        newpwd=input('请设置密码')
        xie(newname,newpwd)
        print('用户名:%s，密码:%s，状态:新增成功' %(newname,newpwd))
    if a=='2':
        name=input('用户名:')
        pwd=input('密码:')
        if pwd==cha(name):
            print('用户%s登录成功' %(name))
        else:
            print('登录失败')  
    if a=='3':
        xian()
    if a=='4':
        cname=input('请输入要查询的用户名:')
        print('用户%s的密码是:%s' %(cname,cha(cname)))
    if a=='5':
        admin=input('请输入命令:')
        exec(admin)
    if a=='q':
        genxin()
        #from wodemo import *
        break