# -*- coding:utf-8 -*-

from HUAISQL import *
while True:
    print('github博客系统')
    print('*'*50)
    print('功能列表')
    print('1:添加新文章')
    print('2:校验文章')
    print('3:显示文章列表')
    print('4:用标题查询文章')
    print('5:自定义命令操作')
    print('q:退出更新系统')
    print('*'*50)
    #for i in range(50):xie(f'admin{i}',f'root{i}')
    a=input('请输入功能代码:')
    if a=='1':
        newname=input('请输入新的标题:')
        newpwd=input('请设置内容')
        xie(newname,newpwd)
        print('标题:%s，内容:%s，状态:新增成功' %(newname,newpwd))
    if a=='2':
        name=input('标题:')
        pwd=input('文章内容:')
        if pwd==cha(name):
            print('文章%s校验成功' %(name))
        else:
            print('校验失败')  
    if a=='3':
        xian()
    if a=='4':
        cname=input('请输入要查询的标题:')
        print('标题%s的内容是:%s' %(cname,cha(cname)))
    if a=='5':
        admin=input('请输入命令:')
        exec(admin)
    if a=='q':
        genxin()
        #from wodemo import *
        from githubbool import *
      	# from githubbool import *
        break

