a= int(input("give us no. of items u want to add in list"))
lis=[]
for i in range(a):
    b= input("add item")
    lis.append(b)

c=int(input("what comprehension do you want to make\npress 1: for list comphrehension\npress 2: for dictionary comphrehension\npress 3: for set comphrehension\npress 4: for genrator comphrehension"))
# print(lis)
if c==1:
    newlis=[i for i in lis]
    print(newlis)

elif c==2:
    newdict={i:lis.index(i) for i in lis}
    print(newdict)

elif c==3:
    newset= {i for i in lis}
    print(newset)

elif c==4:
    newgen= (i for i in lis)
    print(newgen)

    print(newgen.__next__())
    print(newgen.__next__())
