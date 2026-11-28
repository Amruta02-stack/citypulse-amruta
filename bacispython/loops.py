
print("for loop",[i for i in range(1,10,3)])

print("while loop")
count=0
loop = False
while loop is False:
    count+=1
    print(count)
    if count>5:
        loop = True

def sumint(a,b):
    ls=[23,45,2,7,24]
    ls.append(a+b)
    return ls

print("function",sumint(12,67))
