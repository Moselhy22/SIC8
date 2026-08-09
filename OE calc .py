print ("please choose a operation","1= add","2=diff","3= multiplication","4=divsion")
userop=int(input())
print ("please enter your numbers")
usernum1=int(input())
usernum2=int(input())
if userop==1:
    print(usernum1+usernum2)
elif userop==2:
    print(usernum1-usernum2)
elif userop==3:
    print(usernum1*usernum2)
elif userop==4:
    print(usernum1/usernum2)
else:
    print ("invalid input for op")

    