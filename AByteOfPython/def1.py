def sayHello(name):
    print('hello {0}'.format(name))


coun=input('how many users?')
for i in range(1,int(coun)+1):
    n=input('{0} user name?'.format(i))
    sayHello(n)
print('end')
    