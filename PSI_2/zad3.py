# 1
print('{} {}'.format(1, 2))
#2
print('{:>10}'.format('test'))
#3
print('{:^10}'.format('test'))
#4
print('{:f}'.format(3.141592653589793))
#5
class Data(object):

    def __repr__(self):
        return 'räpr'
print('{0!r} {0!a}'.format(Data()))
