
phrase = input('Enter a phrase :  ') 

def occurrence(phrase):
    result = len(phrase.split())
    print("There are " + str(result) + " words.")
    result2 = list(dict.fromkeys(phrase.split(" ")))
    for i in result2:
        print ("%s :" % i, phrase.count(i))

occurrence(phrase)





