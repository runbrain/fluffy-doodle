num = 23
run = True
while run:
    guess = int(input('vvedite int '))
    if guess == num:
        print('gratz')
        run = False
    elif guess < num:
        print('num biger')
    else:
        print('num smaler')
else:
    print('end of while')