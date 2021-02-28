a=float(input('Enter a:'))
b=float(input('Enter b:'))
c=float(input('Enter c:'))
d=b**2-4*a*c
if d>0:
    print(f"x1={(-b+d**1/2)/2*a} and x2={(-b-d**1/2)/2*a}")
elif d==0:
    print(f"x1 and x2 are equal:{-b/2*a}")
else:
    print('D is smaller than 0, there is no real roots')
print('Your calculation is done!')
