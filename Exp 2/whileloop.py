# print number 1 to n
# n = int(input("Enter the value of n: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1



# print even numbers
# n = int(input("Enter value of n:"))
# i=1
# while i<=n:
#     if i%2==0:{
#         print(i)
#     }
#     i +=1



#print odd numbers
# n = int(input("Enter value of n:"))
# i=1
# while i<=n:
#     if i%2!=0: {
#         print(i)
#     }
#     i +=1




# print sum of n natural numbers
# n = int(input("Enter value of n: "))
# i = 1
# total_sum = 0
# while i <= n:
#     total_sum += i  
#     i += 1          

# print(total_sum)




#print sum of even natural numbers
# n = int(input("Enter value of n:"))
# i = 1
# sum=0
# while i<= n:
#     if i%2==0:{ 
#         print(sum)
#     }
#     sum+=i
#     i+=1
    



#print sum of odd numbers upto n
# n = int(input("Enter n: "))

# i = 1
# sum = 0

# while i <= n:
#     sum = sum + i
#     i += 2

# print("Sum =", sum)




#print sum of even numbers up to n
# n = int(input("Enter n: "))

# i = 2
# sum = 0

# while i <= n:
#     sum = sum + i
#     i += 2

# print("Sum =", sum)




#Print natural numbers from n to 1 (Reverse)
# n = int(input("Enter n: "))

# while n >= 1:
#     print(n)
#     n -= 1



#Print Fibonacci series up to n terms
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1
# i = 1

# while i <= n:
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     i += 1




#Factorial of number
# n = int(input("Enter number: "))

# fact = 1

# while n > 0:
#     fact = fact * n
#     n -= 1

# print("Factorial =", fact)



#check the prime number
# n = int(input("Enter number: "))

# i = 2
# count = 0

# while i < n:
#     if n % i == 0:
#         count += 1
#     i += 1

# if count == 0 and n > 1:
#     print("Prime Number")
# else:
#     print("Not Prime Number")



#sum of digits
# n = int(input("Enter number: "))

# sum = 0

# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10

# print("Sum =", sum)
        


#check number is palindrome
# n = int(input("Enter number: "))

# temp = n
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#reverse a number
# n = int(input("Enter number: "))

# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print("Reverse =", rev)



#print multilpication table
# n = int(input("Enter number: "))

# i = 1

# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1



#largest of n numbers
# n = int(input("How many numbers? "))

# i = 1
# largest = None

# while i <= n:
#     num = int(input("Enter number: "))
#     if largest is None or num > largest:
#         largest = num
#     i += 1

# print("Largest =", largest)    



#smallest of n numbers
# n = int(input("How many numbers? "))

# i = 1
# smallest = None

# while i <= n:
#     num = int(input("Enter number: "))
#     if smallest is None or num < smallest:
#         smallest = num
#     i += 1

# print("Smallest =", smallest)