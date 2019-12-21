import time

try:
    f=open('poem.txt')
    while True:
        line = f.readline()
        if len(line)==0:
            break
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('чтение отменено')
finally:
    f.close()
    print('файл закрыт')