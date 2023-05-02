#Find Armstrong Number

number = int(input("Enter the number: "))
temp = number
counter = 0
result = 0
a = 1
while a:
    temp = temp/10
    counter += 1
    if(temp <= 1):
        a=0
for i in range(1,counter+1):
    x = number%10
    number = int((number)/10)
    result += pow(x,counter)

if(int(temp*pow(10,counter)) == result):
    print(str(temp*pow(10,counter))+" is armstrong number.")
else:
    print(str(temp * pow(10, counter)) + " is not armstrong number.")
