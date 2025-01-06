import sys
# t1 =()
# t2=(1)
# t3 =(3,)
# t4 =(1,2,3,4,'Book')
# t5 = (1,[3,4,5],('Banana','Apple','Kiwi'))
# print(t1)
# print(t2,type(t2))
# print(t3)
# print(t4)
# print(t5)

# str = 'Hello'
# t1 = tuple(str)
# print(str,type(str),id(str))
# print(t1,type(t1),id(t1))

# t1 = (1,2,3,4)
# print(t1[0])
# print(t1[3])
# print(t1[::-1])
# t2 = (1,2,3,(3,4,5,6,(7,4,5,6)))
# print(t2[3][4][3])

# l = [1,2,3]
# t =(1,2,3)
# print(type(l),sys.getsizeof(l))
# print(type(t),sys.getsizeof(t))

# s1 = set()
# s2 ={1,2,3}
# s3 = {1,2,(1,2,3,6)}
# s4 = {1,True,2,3,6.8}
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# s1 ={1,2,3}
# s2 ={1,2,3}
# print(s1 in s2)
# s1.add(5)
# print(s1)
s1 ={1,2,3,4}
s2 ={3,4,5,6}
print(s1|s2)
print(s1 &s2)
print(s1^s2)

fs = frozenset([1,2,3])
fs2 = frozenset([2,3])
print(fs2.issubset(fs))

s3 = s1.copy()
print(s1,id(s1))
print(s3,id(s3))



