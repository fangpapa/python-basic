print('AAA')

# comment1

'''
comment2
'''

"""
comment3
"""

# type of
print(type('AAA'))
print(type(123))
print(type(123.0))

a = 'Hi'
print(a * 10)

b = 'ABCD'
print('C' in b)

# print 可以指定分隔符號sep
print("www", "google", "com", sep=".")

# if elif else
c = 10
d = 5
if c > d:
    print(1)
elif c < d:
    print(2)
elif c == 5:
    print(3)
else:
    print(4)

# and or
if c > 1 and d > 1:
    print(1)

if c > 1 or d > 1:
    print(2)

# list
testList = ['a', 1, True, 1.5]
print('type:', type(testList))
print('length:', len(testList))
print('get by index:', testList[3])
print('get by range', testList[0:3])
# print用逗號分開會串在一起印
print('get index by value:', testList.index(1.5))

del testList[0:2]
print('before del:', testList)

testList.append('ZZZ')
print('append:', testList)


def add_number(a, b):
    return a + b


print(add_number(1, 2))
