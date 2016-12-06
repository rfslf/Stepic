p = int(input())
x = int(input())
y = int(input())
X = x+x*p/100
Y = y+y*p/100
R = (X//1)+Y//100
K = ((X*100) % 100)+Y % 100
print(int(R+K//100))
print(int(K % 100))
