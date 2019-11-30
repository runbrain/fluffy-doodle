x=50
def func():
    global x
    print('x=',x)
    x =2
    print('change x on', x)
func()
print ('now x in global ',x)