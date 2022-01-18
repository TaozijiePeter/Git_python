def two_of_three(x,y,z):
    sum=x**2+y**2+z**2
    tmp=max(x,y,z)
    sum=sum-tmp**2
    return sum
x=int(input("请输入x的值： "))
y=int(input("请输入x的值： "))
z=int(input("请输入x的值： "))
print(two_of_three(x,y,z))
