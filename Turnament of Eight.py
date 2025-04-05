import random
print("Tournament of eight")
list = [
   input("Enter Data 1 :"),
   input("Enter Data 2 :"),
   input("Enter Data 3 :"),
   input("Enter Data 4 :"),
   input("Enter Data 5 :"),
   input("Enter Data 6 :"),
   input("Enter Data 7 :"),
   input("Enter Data 8 :")
    ]

listA =[]

n = 0
while n<16 :
    a = (list[random.randint(0,7)])
    b = (list[random.randint(0,7)])

    while a == b:
        b = (list[random.randint(0,7)])
        break 
    
    listA.append(a)
    listA.append(b)
    n+=1

count = []
for word in listA :
   if word in count :
      pass
   else:
      count.append(word)


slist = [count[0], count[1], count[2], count[3]]
print("Semi Finalist : ",slist)

###################################################################
listB =[]
n = 0
while n<16 :
    a = (slist[random.randint(0,3)])
    b = (slist[random.randint(0,3)])

    while a == b:
        b = (slist[random.randint(0,3)])
        break 
    
    listB.append(a)
    listB.append(b)
    n+=1

countA = []
for word in listB :
   if word in countA :
      pass
   else:
      countA.append(word)

flist = [countA[0], countA[1]]

#################################################################
print("Finalist : ", flist)
print("winner :", flist[random.randint(0,1)] )

input("press Any key")



