import os
import time

source = ['c:\\fluffy-doodle',]
target_dir = 'c:\\back'
today = target_dir+os.sep+time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('input: ')
if len(comment) == 0:
    target = today + os.sep +now + '.zip'
else:
    target = today + os.sep + now + '_'+\
             comment.replace(' ','_')+'.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('mkdir')

zip_command = "zip -qr {0} {1}".format(target,' '.join(source))

if os.system(zip_command) == 0:
    print('sucsess')
else:
    print('error')