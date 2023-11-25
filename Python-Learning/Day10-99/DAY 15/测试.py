import time
print(time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime()))

s = 'sgosg'
t=reversed(s)
print(list(t))

a = 1
b = 2
a,b=b,a
print(a,b)