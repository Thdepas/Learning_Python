from collections import OrderedDict

input = input("Enter some characters : ")

def RLE(input):

    char=OrderedDict.fromkeys(input, 0)
  
    for i in input:
        char[i] += 1
  
    output = ''
    for key,value in char.items():
         output = output + key + str(value)
    return output
    
print ("Encoded characters : " +  RLE(input))