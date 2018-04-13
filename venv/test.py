
#python for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
print('\r')
count=['1','2','3']
for c in count:
    print(c)

#python while循环
n=1
while n <= 5:
    print(n)
    n = n + 1
print('END')

#python 判断
n = 1
while n <= 11:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#python 词典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

#赋值
d['Adam'] = 67
print(d['Adam'])

#set 增加，和删除
s = set([1, 2, 3])
s.add(4)
s.remove(1)
print(s)


#set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2) #交集
print(s1 | s2) #并集




print('git')















