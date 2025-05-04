#python program to add two numbers

#the default input data type in python is string
# a = int(input("Enter the first number: ")) 
# b = int(input("Enter the second number: "))

# print(a+b)

####################################################################################################################################
#python program to print a table of a number


'''

n = int(input("Enter the number: "))

for i in range(1,11,1):
 print(str(i)+ "x" + str(n) + "=" + str(i*n))    
 
'''       
 
 
 
#print always print's statement on a new line
#By default python uses print("hello",end="\n") simply do print("hello",end="") basically use end parameter


###################################################################################################################################

#print this pyramid pattern 

'''

   *
  ***
 *****
*******


'''

row = int(input("Enter the number of rows : "))


for i in range(1,row+1):
  for j in range(0,row-i):
   print(" ",end="")
  for k in range(0,2*i-1):
   print("*",end="")
  print()
















