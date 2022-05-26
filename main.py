# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    print("Hello, check for anagrams")
    word = input("Enter word: ")
    anagram = input("Enter anagram: ")
    list1 = list(word)
    list2 = list(anagram)
    list1.sort()
    list2.sort()

    position = 0
    matches = True

    while position < len(word) and matches:
        if list1[position] == list2[position]:
            position += 1
        else:
            matches = False

    return matches

print(find_anagram('word', 'anagram'))


