a = int(input())
b = int(input())
c = int(input())
costcent = b*c % 100
costdola = a*c+b*c//100
print(costdola, costcent, sep=' ')