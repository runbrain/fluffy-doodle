import antigravity
number = 32
guess = int(input('input integer : '))
if guess == number:
    print('congradulations you right')
elif guess < number:
    print('value is biger')
else:
    print('value is smaler')