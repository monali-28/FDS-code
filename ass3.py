n=int(input("Enter the number of books in the library: "))  
book_list=[]  
cost_list=[] 
lst_500more=[]  
lst_500less=[]  
nonduplicate=[]  
for i in range(n):  
    book=input("\nEnter the name of the book: ")  
    cost=int(input("Enter the the cost of the book: "))  
    book_list.append(book)  
    cost_list.append(cost)  
def more_500(lst1,lst2,lst3):  
    for i in range(len(lst1)):  
        if(lst1[i]>=500):  
            lst3.append(lst2[i])   
            print(lst3)  

def less_500(lst1,lst2,lst3):  
    for i in range(len(lst1)):  
        if(lst1[i]<500):  
            lst3.append(lst2[i])   
            print(lst3)  

def sorted_list(lst):  
    for i in range(len(lst)):  
        for j in range(i,len(lst)):  
            if(lst[i]>lst[j]):  
                lst[i],lst[j]=lst[j],lst[i]  
                print(lst)  
def duplicate(lst):  
    temp=[]  
    for i in lst:  
        if i not in temp:  
            temp.append(i)   
            print(temp)  
print("\n The books list with its cost are as follows:") 
(book_list,cost_list)
print("\nBooks which costs 500 & more than 500:")  
print(more_500(cost_list,book_list,lst_500more))
print("\nBooks which costs less than 500:")  
print(less_500(cost_list,book_list,lst_500less))
print("\nSorted list of cost is:")  
print(sorted_list(cost_list)  )
print("\nList of books after removing duplicate books:")  
print(duplicate(book_list)) 


