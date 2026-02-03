# # You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.



# A palindrome number is a number which reads the same both left to right and right to left.


# Example 1

# Input: n = 121

# Output: true

# Explanation: When read from left to right : 121.

# When read from right to left : 121.

# Example 2

# Input: n = 123

# Output: false

# Explanation: When read from left to right : 123.

# When read from right to left : 321.




n=input("enter the num : ")
def palindrome(n):
    if n==n[::-1]:
        print("True")
    else:
        print("false")
palindrome(n)

