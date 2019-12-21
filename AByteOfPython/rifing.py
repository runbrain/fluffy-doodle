class ShortInputException(Exception):
    '''user exception class'''
    def __init__(self, lenght, atleast):
        Exception.__init__(self)
        self.lenght = lenght
        self.atleast = atleast

try:
    text = input('input something: ')
    if len(text)<3:
        raise ShortInputException(len(text),3)
except EOFError:
    print('EOF')
except ShortInputException as ex:
    print('SIE длинна введеной строки --{0}; \
        ожидалось как минимум, {1}'.format(ex.lenght,ex.atleast))
except KeyboardInterrupt as ex:
    print('interrupt{0}'.format(ex))
else:
    print('no exception')