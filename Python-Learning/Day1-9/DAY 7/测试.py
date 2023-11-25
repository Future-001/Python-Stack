dic={'美女':234,'老师':999}
for i,j in enumerate(dic):
    print(1+i,j,dic[j])

s='中国与世界'
s1=s.encode('utf-8')
print(s1)
print(s1.decode('utf-8'))
b=b'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xb8\x8e\xe4\xb8\x96\xe7\x95\x8c'
print(b,b.decode('utf-8'))
# edcode('gbk')
g=b.decode('utf-8')
g1=g.encode('gbk')
print(g1,g1.decode('gbk'))
g2=(g1.decode('gbk')).encode('utf-8')
print(g2,g2.decode('utf-8'))

print()