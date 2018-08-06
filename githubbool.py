from jinja2 import Template
import os
from HUAISQL import *
f = open('index.html', 'r')
f=f.read()
#print(f)
template = Template(f)
k=template.render(li=su[::-1])

dict=eval(open('index.config','r').read())

l=open(dict['dz']+'index.html','w').write(k)
os.chdir(dict['dz'])
os.system('pwd')
os.system('git add .')
os.system('git commit -m 自动提交')
os.system('git push -f origin master')