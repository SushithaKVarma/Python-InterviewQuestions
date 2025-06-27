''' write a program to create,concat and print a string and accessing sub-string from a given string'''

s1=input("Enter the first string:")
s2=input("Enter the second stirng:")
print("The first string is:",s1)
print("The second string is:",s2)
print("The concatenated string is:",(s1+" "+s2))
s3=s1+s2
print("The substring of the the given string is ",s3[0:9])