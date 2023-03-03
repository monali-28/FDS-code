n = int(input(("Enter total number of students :-")))  
arr = []  
def enter(n, arr):
    for i in range(n):
        roll = int(input("Enter Roll No : "))
        arr.append(roll)

def sentinelSearch(arr, n, key):
    
    # Last element of the array
    last = arr[n - 1]
 
    # Element to be searched is
    # placed at the last index
    arr[n - 1] = key
    i = 0
 
    while (arr[i] != key):
        i += 1
 
    # Put the last element back
    arr[n - 1] = last
 
    if ((i < n - 1) or (arr[n - 1] == key)):
        print(key, "is present at index", i)
    else:
        print("Element Not found")
        
def linearSearch(arr, key):
 
    for i in range(len(arr)):
 
        if arr[i] == key:
            return i
 
    return -1        
        
        
enter(n,arr)
print(arr)
while True:
    
    
    print("1.Linear Search \n2.Sentinal Search\n3.Exit")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        key=int(input("Enter roll no to be search : "))    
        sentinelSearch(arr,n,key)
        
    elif ch == 2:
        key=int(input("Enter roll no to be search : "))
        
        result = linearSearch(arr, key)
        if(result == -1):
            print("Element not found")
        else:
            print("Element found at index: ", result)
            
    elif ch == 3:
        print("Program Exited...")
        break;
        
    else:
        print("Invallid Choice...")
        print("Enter correct choice")
        ch=int(input("Enter your choice : "))
