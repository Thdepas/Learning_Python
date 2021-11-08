
print("Lets check if those two words are anagrams !")
word_1 = input("Enter first string : ")
word_2 = input("Enter first string : ")

def check(word_1, word_2):

    if(sorted(word_1) == sorted(word_2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


check(word_1, word_2)
