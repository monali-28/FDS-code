n = int(input(("Enter total number of students :-")))  
arr = []  
def enter(n, arr):
    for i in range(n):
        roll = int(input("Enter Roll No : "))
        arr.append(roll)

def binary_search(a,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=int((start+end)/2)
        if(arr[mid]==target):
            print("Roll no.",target,"is present at index",mid)
            break
        elif(target>arr[mid]):
            start=mid+1
        elif(target<arr[mid]):
            end=mid-1
    else:
        print("Roll no.",target,"not found in list")
        

def fibonacci_search(arr,key):
    n=len(arr)
    fibn_2=0
    fibn_1=1
    fibn=fibn_1+fibn_2
    while(fibn<=n):
        fibn_2=fibn_1
        fibn_1=fibn
        fibn=fibn_1+fibn_2

    offset=-1
    while(fibn_1!=0):
        i=min((offset+fibn_2),n-1)
        if(key>arr[i]):
            fibn=fibn_1
            fibn_1=fibn_2
            fibn_2=fibn-fibn_1
            offset=i
        elif(key<arr[i]):
            fibn=fibn_2
            fibn_1=fibn_1-fibn_2
            fibn_2=fibn-fibn_1
        elif(key==arr[i]):
            print("Roll no.",key,"is present at index",i)
            break
    else:
        print("Roll no.",key,"not found in list")
        
        
enter(n,arr)
print("Present student roll no. : ",arr)
while True:
    
    
    print("1.fibonacci_search \n2.binary_search\n3.Exit")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        key=int(input("Enter roll no to be search : "))    
        fibonacci_search(arr,key)
        
    elif ch == 2:
        key=int(input("Enter roll no to be search : "))
        
        binary_search(arr,key)
            
    elif ch == 3:
        print("Program Exited...")
        break;
        
    else:
        print("Invallid Choice...")
        print("Enter correct choice")
        ch=int(input("Enter your choice : "))
