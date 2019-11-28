import os
import time

source = ['c:\\byte']
target_dir = ['c:\\back']
target = target_dir + os.sep +time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = 'zip -qr {0}{1}'.format(target,' '.join(source))

if os.system(zip_command) == 0:
    print('sucsess')
else:
    print('error')