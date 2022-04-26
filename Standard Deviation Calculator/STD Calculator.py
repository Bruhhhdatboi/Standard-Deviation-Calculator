import math
import statistics
import collections

from sqlalchemy import true
numbers= []
for a in range(1,100):
    nu = float(input("Please enter a number (Type 0 to continue):"))
    if nu == 0:
        break
    else:
        numbers.append(nu)
nuofnu = len(numbers)
print("These are your numbers :" ,numbers)
sum1 = float(sum(numbers))
print("The sum of the numbers:" ,sum1)
mean=float(input("Please enter your mean average :"))
if mean ==0:
    mean = float(sum(numbers)/nuofnu)
mode1 =statistics.mode(numbers)
print("Your mean is :",mean)
print("Your mode is :",mode1)
median1 =statistics.median(numbers)
print("Your median is :",median1)
minnu = min(numbers)
print("Your smallest value is :",minnu)
maxnu = max(numbers)
print("Your largest value is :",maxnu)
intv= (maxnu-minnu)/8
print("Each interval for 8 intervals :",intv)
intvst= float(input("Please enter your starting value :"))
allintv= collections.defaultdict(list)
intvfreq = collections.Counter(allintv)
print(intvfreq)
print("The formula to calculate the Standard Deviation is: O~=sqrt(sum((each#-mean)^2))/N)")
print("Switch each number in the formula:(each#-mean)^2")
eachna=[]
for x in numbers:
    eachnu = (x-mean)**2
    print("Result with",x,":",eachnu)
    eachna.append(eachnu)
print("Add all of the #s above and use it to divide by the #of#: Sum(#above)/N")
print("Then squareroot the result you just got")
nodiv = sum(eachna)
nosqrt =(nodiv/nuofnu)
PTSD= math.sqrt(nosqrt)
print("The standard deviation :",PTSD)
#zcal = float(input("Do you want to calculate the z-score of a number :"))
while true:
        zcal = float(input("Do you want to calculate the z-score of a number (1 = yes, 0 = no):"))
        if zcal in range (0,2):
            break
        else:
            print("Invalid number.")
if zcal == 1:
            nuforz = float(input("Please enter a number to calculate z-score :"))
            zscore= (nuforz-mean)/PTSD
            print("Your zscore:" , zscore)
            print("Done!")
elif zcal == 0:
            print("Done!")