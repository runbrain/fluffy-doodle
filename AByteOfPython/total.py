def total(initial=5,*num,**keywords):
    count=initial
    for number in num:
        count+=number
    for key in keywords:
        count+=keywords[key]
    return count
print (total(10,1,2,3,vegetable=50,fruits=100))