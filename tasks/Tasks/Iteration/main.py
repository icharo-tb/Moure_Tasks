# FOR LOOP:

for i in range(1,101):
    print(i)

# WHILE LOOP:

n = 0
while True:
    n = n+1
    print(n)
    if n == 100:
        break

# LAMBDA:

count = lambda x: x if x<101 else x+1
count_list = [count(i) for i in range(1,101)]
for num in count_list:
    print(num)

# RECRUSIVE

def count_recursion(n):
    if n > 0:
        count_recursion(n-1)
        print(n,end='\n')
        return 'Done!'
pass
print(count_recursion(100))