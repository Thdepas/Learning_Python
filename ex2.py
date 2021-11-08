
import string

sentence = input("Enter a sentence :  ")
letters = set(string.ascii_lowercase)

def pangram(sentense):
    return not set(letters) - set(sentense)
if (pangram(sentence))== True:
    print("Pangram style !")
else:
    print("It's not Pangram")

  

