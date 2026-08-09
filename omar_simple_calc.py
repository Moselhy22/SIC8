x=input("enter num 1 \n")
y=input("enter num 2 \n")

operator=input("select your operator +,-,*,/ \n")

if operator=="+":
    print(int(x)+int(y))
elif operator=="-":
    print(int(x)-int(y))
elif operator=="*": 
    print(int(x)*int(y))
elif operator=="/":
    print(int(x)/int(y))