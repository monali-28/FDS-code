n=int(input("Enter total no. of student : "))
arr=[]
for i in range(n):
	percentage=float(input("Enter percentage : "))
	while True:
		if percentage>=0 and percentage <=100:
			break
	else:
		print(" Invalid Marks !... Enter correct marks : ")
		percentage=float(input("Enter percentage : "))
	arr.append(percentage)
print("orignal list is : ",arr)

def partition(arr,low,high):
	i = low 
	j=high-1
	pivot = arr[high]
	while i<j:
		while i<high and arr[i]<pivot:
			i+=1
		while j>low and arr[j]>=pivot:
			j-=1
		if i<j:
			arr[i],arr[j]=arr[j],arr[i]
	if arr[i]>pivot:
		arr[i],arr[high]=arr[high],arr[i]
	return i			
    
# function to perform quicksort
def quicksort(arr,low,high):
	if low < high:
		pi = partition(arr,low,high)
 
		quicksort(arr,low,pi-1)
 
		quicksort(arr,pi+1,high)		

quicksort(arr,0,n-1)
print("sorted list by quicksort\n",arr)
arr1=[]
print("Top 5 score are : ")
for i in range(n):
	if i>n-6:
		arr1.append(arr[i])
print(arr1[::-1])


	
