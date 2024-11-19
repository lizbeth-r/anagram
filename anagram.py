def are_anagrams(string1, string2):
    # Normalize the strings by removing spaces, converting to lowercase, and sorting
    anagram1 = sorted(string1.replace(" ", "").lower())
    anagram2 = sorted(string2.replace(" ", "").lower())
    
    # Compare the sorted versions
    return anagram1 == anagram2


if __name__ == "__main__":
    string1 = input("Enter the first word or phrase:")
    string2 = input("Enter the second word or phrase:")

    if are_anagrams(string1, string2):
        print("They are anagrams")
    else:
        print("They are not anagrams")