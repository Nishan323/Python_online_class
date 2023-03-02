l=input("Input a letter of the alphabet:")
if l in ('a','e','i','u'):
    print("%s is a vowel."%l)
elif l=='y':
    print("Sometimes letter y stand for vowel, sometime stand for consonant. ")
else:
    print("%s is a consonant." %l)
