u = [5304, 5643, 11960, 4850] 
v = [154, 156, 219, 147]
_ = ''
i = []
while (_:=input('')) != '':
    i.append(_)
j=[]
for x in i:
    j.append(sum([10**(len(x)-1-y) * (ord(x[y]) - ord('0')) for y in range(len(x))]))
assert len(j) == 8
def det(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def tr(M):
    return M[0][0]+M[1][1]
i=len(j)//2
for _ in range(i):
    assert det([[j[2*_],0],[0,j[2*_+1]]])==u[_]and tr([[j[2*_],0],[0,j[2*_+1]]])==v[_]and j[2*_]>j[2*_+1]
print(f"AIRCTF{'{'}{''.join([chr(x)for x in j])}{'}'}")