num = int(input("enter your number now :"))
num2 = int(input("enter your number now :"))
sign = str(input("enter your sign:"))
if sign == "+" :
    print(num + num2)
elif sign == "-" :
    print(num - num2)
elif sign == "*" :
    print(num * num2)
elif sign == "/" : 
    print(num / num2)
else :
    print("not a sign")
