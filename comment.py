positivelist=[]
negativelist=[]
f1=open("positive.txt","r")
for x in f1:
    positivelist.append(x.strip("\n"))
f1.close()
f1=open("negative.txt","r")
for x in f1:
    negativelist.append(x.strip("\n"))
f1.close()

#a=['good','greate','like','notgood','notdefected','notdirty']
#neg=['bad','not','no','dislike','defeact','i an fine']
a=positivelist
neg=negativelist
negative=0
positive=0
b=raw_input("Enter your comment here : ")
b=b.strip("\r")
b=b.split(" ")
print(b)
for i in b:
    if i in positivelist:
        positive+=1
for i in b:    
    if i in negativelist:
        negative+=1
if negative > positive  :
    print 'negative'        
elif positive > negative :
    print "positive"   
elif  positive == negative :
 print 'nutral'
