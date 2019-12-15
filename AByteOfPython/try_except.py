try:
    text = input('input something: ')
except EOFError:
    print('EOFError')
except KeyboardInterrupt:
    print('KeyboardInterrupt')
else:
    print('you input {0}'.format(text))