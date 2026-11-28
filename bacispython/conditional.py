na = "great"
n=int(input("Enter a number"))
if isinstance(na,str):
    print(f"naidile is {na}")
else:
    print("nothing") 

if n> 5:
    print(f"number {n} is greater than 5")
elif n>=0 and n<=5:
    print(f"number {n} is in range 0 to 5")
else :
    print("Negative number")      
