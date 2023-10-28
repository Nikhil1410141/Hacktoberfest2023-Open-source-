n=int(input("Number Of Students:"))
a={}
for i in range(n):
    r=input("Enter Name")
    v=[]
    for x in range (5):
        print("Enter marks in subject",x+1,":")
        q=int(input(""))
        v.append(q)
           
    a.update({r:v})
    
import pickle
def write():
    f=open("NIkhli.dat",'wb')
    pickle.dump(a,f)
    f.close

write()
print("DATA STORED SUCESSFULLY..............")
