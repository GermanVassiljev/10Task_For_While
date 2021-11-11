#1 Task
#t=0
#q=0
#while t<15:
 #   t+=1
  #  a=float(input("Sisesta arv: "))
 #   if a==round(a): 
 #       q=+1
#print("Täisarvude kogus: ",q)
#B=0
#or t in range(15):
  #  a=float(input("Sisesta arv: "))
   # if a==round(a):
   #     B=+1
#print("Täisarvude kogus: ",B)
#2 Task
#S=0
#A=int(input("Sisesta arv: "))
#for arv in range(1,A+1):
 #   S+=arv
#print("Summa: ",S)
#3 Task
#from random import *
#korrutis=1
#for i in range(8):
#    B=randint(-100,100)
#    print(B)
#    if B>0 :
#        korrutis*=B
#print("korrutis on ", korrutis)
#4 Task
#for i in range(10,21,1):
  #  print(i**2)
#6 Task
#Check1=0
#Check2=0
#Check3=0
#from random import *
#R=randint(5,10)
#while R>0:
#    R-=1
#    N=int(input("Sisesta arv: " ))
#    if N>0:
#        Check1+=1
#    elif N<0:
#        Check2+=1
#    else:
#        Check3+=1
#print("Pos: ", Check1)
#print("Neg: ", Check2)
#print("Nullid: ", Check3)
#Купи слона
print("Купи слона!")
Answer=str(input("Ответ: "))
if Answer.lower() == "слон":
    print("Слон твой!")
else:
    while True :
        print("Все говорят "+Answer+". А ты купи слона!")
        Answer=str(input("Ответ: "))
        if Answer.lower() == "слон":
            print("Слон твой!")
            break