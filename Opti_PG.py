import random
import sys

list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
list2=[1,2,3,4,5,6,7,8,9,0]
list3=[ '!','@','#','$',"%",'&']


def genrate(Flist):
    len = int(input("Enter Lnegth  "))
    password=[]
    for i in range(len):
        password.append(str(random.choice(Flist)))
    npassword = "".join(password)
    print("your Random Password is ", npassword)
    ch = int(input("1 = Shuffle Password \n 2 = Break  \n = "))
    if ch == 1:
        random.shuffle(password)
        npassword = "".join(password)
        print("New password ", npassword)
    elif ch == 2:
        sys.exit(0)
    else:
        print("Wrong Choice , Exiting")


print("Genrate  A Random Password ")

ch=int(input('''
1 = Alphabetic password
2 =  Numeric password
3 = Alphanumeric password
4 = Alphanumeric + Special Character
5 = break 

'''))

if ch==1:
    final_list=list1
    genrate(final_list)

elif ch==2:
    final_list=list2
    genrate(final_list)

elif ch==3:
    final_list=list1+list2
    genrate(final_list)

elif ch==4:
    final_list=list1+list2+list3
    genrate(final_list)

elif ch==5:
    sys.exit(0)

else:
    print("Wrong Input !! Terminating")