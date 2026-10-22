# ARRAY

# arr = [1,2,3,4,5]
# # print(arr)
# print(arr.append(2))



arr = [10, 20, 30, 40, 50]
print("Array:", arr)

# accesing element
arr = [10, 20, 30, 40, 50]
print(arr[0])
print(arr[2])
# append
arr.append(40)
print(arr)
# insert
arr.insert(1, 15)
print(arr)
# delete
arr.remove(20)
print(arr)
# max element
print("Maximum:", max(arr))
# min element
print("Minimum:",min(arr))
# sum
print("Sum:",sum(arr))


# count
arr = [10, 20, 10, 30, 10]
print("10 occurs:", arr.count(10), "times")


# sorting array
arr = [50, 20, 40, 10, 30]
arr.sort()
print(arr)
# sorting in descending
arr.sort(reverse=True)
print(arr)


# pop
arr.pop(1)
print(arr)
# extend
arr.extend([40,50])
print(arr)
# copy array
new_arr = arr.copy()
print(new_arr)


arr = [10, 20, 30, 40, 50]
if 10 in arr:
    print("element found")
else:
    print("element not found")    
# average
average = sum(arr) / len(arr)
print("Average:", average)
# 2nd largest
print("2nd largest:",arr[-2])



