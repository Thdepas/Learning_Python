#!/usr/bin/env python3

digits = str(input("Enter digits : "))
n = input("Enter n : ")

def serie(check, n):
    if n > len(check):
        print ("Invalid length")
    else:               
        for i in range(len(check)):
            if len(check[i:i+n]) == n:
                print (check[i:i+n])

serie(digits, n)

 