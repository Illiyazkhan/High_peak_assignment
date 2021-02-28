#utility function for quick sort
def partition(arr, low, high): 
    i = (low-1)         
    pivot = arr[high][0]     
  
    for j in range(low, high): 
         if arr[j][0] <= pivot:  
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 

#function for quick Sort algorithm  
def quickSort(arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
        pi = partition(arr, low, high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

#Taking input from a fil named "input.txt"
file = open("input.txt","r")
l=file.readlines()
file.close()
n=l[0].split(":")[1]
n=int(n[1])
o=[]
for i in l[4:]:
	f=i[:len(i)].split(":")
	o.append((int(f[1][1:]),f[0]))

#Sorting the List	
quickSort(o,0,(len(o)-1))	

#Finding the minimum difference
mi=float('inf')
for i in range(len(o)-n+1):
	if(o[i+n-1][0]-o[i][0]<mi):
		mi=o[i+n-1][0]-o[i][0]
		a=i
		b=i+n
file1 = open("output.txt","w")
#Writing the output to file named "output.txt"
file1.write("The goodies selected for distribution are: \n\n")
for i in o[a:b]:
	
	file1.write(i[1]+": "+str(i[0])+"\n")
file1.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(mi))
file1.close()
