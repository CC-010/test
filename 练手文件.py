# coding=utf-8
print('hello,world')
def calc(numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
print(calc((1,2,3)))
def m(n,x):
        m=1
        for t in range(x):
                m=m*n
                t=t+1
        return m
for x in range(1,10):
	print(x)
n=int(input("输入n:"))
x=int(input("输入x:"))
print(m(n,x))
def jishu(n):
        sum=0
        for n in range(1,n+1):
                sum=sum+1/(n+1)
        return sum                
p=int(input("级数n :"))
print(jishu(p))
