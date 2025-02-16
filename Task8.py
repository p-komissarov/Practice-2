print("Введите число друзей N и число конфет M: ")
n,m=input().split()
n=int(n)
m=int(m)
friends=1+n
sweets=(m//friends)
print(f"{sweets} конфет достанется каждому")