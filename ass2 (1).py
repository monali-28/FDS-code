n=  int(input("Enter the number of students :  "))
inp = []
sum = 0
for i in range(n):
	print("Roll Number ", (i+1), " : ")
	a = input("Enter marks (Ab - if absent) : ")
	while True:
		if(a >= "0" and a<= "50"):
			break
		elif(a == "Ab"):
			break;
		else:
			print("Invalid marks")
			print("Please enter valid marks : ")
			a = input("enter marks (Ab - if absent) : ")
		
	inp.append(a)
	
	
print("\n")


#Absent Students
ab = []
student = 0
for w in range(n):
	if(inp[w] == "Ab"):
		ab.append(w+1)
		student += 1
print("Absent Students Roll Numbers are : ",ab)
print("Total Count of Absent Students are : ", student)
#Average Score
for j in range(n):
	if(inp[j] == "Ab"):
		ab.append(n)
	else:
		sum = sum + int(inp[j])
print("Average is :",sum/n)

#Highest Score
for t in range(n):
	if(inp[t] == "Ab"):
		pass
	else:
		max = int(inp[t])
		break
		
for v in range(n):
	if(inp[v] == "Ab"):
		pass
	elif(int(inp[v]) > max):
		max = int(inp[v])
print("Maximum score is : ",max)


#Lowest Score
for b in range(n):
	if(inp[b] == "Ab"):
		pass
	else:
		min = int(inp[b])
		break

for s in range(n):
	if(inp[s] == "Ab"):
		pass
	elif(int(inp[s]) < min):
		min = int(inp[s])
print("Minimum score is : ",min) 



#Highest Frequency Marks
count = 0
freq = [0,0,0]
for q in range(n):
	count =  0
	if(inp[q] == "Ab"):
		pass
	else:
		freq[0] = int(inp[q])


	for p in range(n):
		if inp[q] == inp[p]:
			count += 1
	maxim = count
	if maxim > freq[1]:
		freq[1] = maxim
		freq[2] = freq[0]
print("Highest Frequency Marks of students are : ", freq[2], " and is scored by : ", freq[1]," students ")
	
