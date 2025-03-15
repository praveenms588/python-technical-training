#WAP to print the second largest and second smallest no in a random list
n=int(input("Enter no of elements: "))
arr=[]
for i in range(n):
    arr.append(int(input(f"No {i}:")))

arr.sort()
arr=list(set(arr))
print(f"Second largest:{arr[len(arr)-2]}\nSecond smallest{arr[1]}")