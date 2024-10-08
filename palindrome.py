def palindrome():
    a = input("Enter a string :")
    print()
    length = len(a)
    p = a[::-1]
    print(p)
    if a == p:
     print ("palindrome")
    else:
print ("Not palindrome")

     