def checkPalindrome(word):
    if word.lower() == word.lower()[::-1]:
        return True


def countpalindrome(str):
    count=0

    listOfwords = str.split(" ")

    for elements in listOfwords:
        if(checkPalindrome(elements)):
            count+=1
    return count



#countpalindrome(f"Nita speaks Malayalam")
#countpalindrome(f"Madam arora teaches malayalam")
m = input("Enter string: ")
print(f"The entered string is {m}")


n = countpalindrome(m)
print(f"The sentence has {n} palindrome words")



