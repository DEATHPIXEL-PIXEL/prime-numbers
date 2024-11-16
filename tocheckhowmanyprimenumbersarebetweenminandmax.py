min= int(input("enter your first value :  "))
max= int(input("enter your last value :  "))
for i in range (min , max+1 ):
    flag = True
    for j in range (2, i ):
         if i%j==0:
              flag= False
              break 
    if (flag==True):
              print(i , end=" ")
