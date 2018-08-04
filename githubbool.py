from jinja2 import Template
import os
from HUAISQL import *
f = open('/sdcard/qpython/index.html', 'r')
f=f.read()
#print(f)
template = Template(f)
k=template.render(li=su)
l=open('/sdcard/qd/1019157263.github.io/index.html','w').write(k)
os.system('cd /sdcard/qd/1019157263.github.io')
os.system('pwd')
os.system('git add .')
os.system('git commit -m '+input('请输入版本号'))
os.system('git push -f origin master')