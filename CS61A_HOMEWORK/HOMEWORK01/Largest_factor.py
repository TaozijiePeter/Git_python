def largest_factor(x):
    for i in range(x-1,0,-1):
        if x%i==0:
            return i
x=int(input("请输入x的值："))
print(largest_factor(x))

