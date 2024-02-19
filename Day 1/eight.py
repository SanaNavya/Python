#write a python programme to check whether given year is a leap year or not
ly=int(input("enter the year:-"))
if (ly%4==0 and ly%100!=0)or ly%400==0:
       print("leap year")
else:
           print("non leap year")
       
