a=int(input('vvedi chislo'))
def chisla(a):
    '''выводит четные числа'''
    for i in range(2, a, 2):
        print(i)
chisla(a)
print(chisla.__doc__)