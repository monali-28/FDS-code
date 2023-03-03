n = int(input(("Enter total number of students :-")))
arr = []
def enter(n, arr):
    for i in range(n):
        percentage = float(input("Enter Percentage : "))
        while True:
            if percentage >= 0 and percentage <= 100:
                  break
        else:
            print("Invalid Marks ! Please enter correct marks!")
            percentage = float(input("Enter Percentage: "))
        arr.append(percentage)
def selection_sort(n, arr):  
    for i in range(n-1):  
        for j in range(i+1, n): 
            if arr[i] > arr[j]: 
                arr[i], arr[j] = arr[j], arr[i]  
def bubble_sort(n, arr):  
    for i in range(n):  
        for j in range(n-1):  
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]  
def display(n, arr):
    top = []  
    for i in range(n):  
        if i > n-6 :  
            top.append(arr[i])  
    print("List after Sorting is: \n ", arr)
    print("Top 5 scores are : \n", top[::-1])  
enter(n, arr) 
while True:  
		print("\n----Enter your choice from 1/2/3---- \n")
		print("1. Sorted list by Selection Sort\n")  
		print("2. Sorted list by Bubble Sort\n") 
		print("3. Exit\n")  
		choice = int(input("----Enter your choice from 1/2/3: ----\n"))   
		if choice == 1:  
			print("\n---Sorted List(Selection Sort)---")
			print("The Original List is:\n", arr)  
			selection_sort(n, arr)  
			display(n, arr)  
		elif choice == 2:
			print("\n---Sorted List(Bubble Sort)---")  
			print("The Original List is:\n", arr) 
			bubble_sort(n, arr) 
			display(n, arr)  
		elif choice == 3:  
			print("End of the Program!\n")  
	
