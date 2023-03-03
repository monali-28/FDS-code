def list(A,a):
	for i in range (a):
 		x=input("Enter the name of student:")
 		if(x not in A):
 			A.append(x)
 		else:
 			while(x in A):
 			    print("Duplicate entry")
 			    x=input("Enter the name of student:")
 			    A.append(x)
# Cricket
C=[]
c=int(input("Enter no. of students playing Cricket: "))
list(C,c)

# Badminton
B=[]
b=int(input("Enter no. of students playing Badminton: "))
list(B,b)

# Football
F=[]
f=int(input("Enter no. of students playing Football: "))
list(F,f)

def uni(l1,l2,l3,l4):
    for i in range (len(l1)):
        l4.append(l1[i])

    for i in range(len(l2)):
        if(l2[i] not in l4):
            l4.append(l2[i])

    for i in range (len(l3)):
        if(l3[i] not in l4):
            l4.append(l3[i])
    return l4

def union(l1,l2,l3):
    for i in l1:
        if i not in l3:
            l3.append(i)
    for j in l2:
        if j not in l3:
            l3.append(j)
    return l3

def intersection(l1,l2,l3):
    for i in l1:
        for j in l2:
            if (i==j):
                l3.append(i)
    return l3

def diff(l1,l2,l3):
    for i in l1:
        if i not in l2:
            l3.append(i)
    return l3


univers=[]
c_union_b=[]
c_union_f=[]
intersec=[]
difference=[]
norF=[]
norB=[]
print("Student who play cricket :",C)
print("Student who play badminton :" ,B)
print("Student who play football : ",F)
print("Universal set is : ",uni(C,B,F,univers))
print("Student who play either cricket or badminton : ",union(C,B,c_union_b))
print("Student who play either cricket or football : ",union(C,F,c_union_f))
print("Student who play both cricket and badminton : ",intersection(C,B,intersec))
print("Student who play either cricket or badmintion but not both :",diff(c_union_b,intersec,difference))
print("Student who play neither cricket nor badminton : ",diff(univers,c_union_b,norF))
print("Student who play cricket and football but not badminton : ",diff(univers,c_union_f,norB))