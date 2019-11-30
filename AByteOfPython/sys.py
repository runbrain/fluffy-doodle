import sys

print('аргументы командной строки')
for i in sys.argv:
    print(i)

print('\n\npytonpath contain', sys.path,'\n')