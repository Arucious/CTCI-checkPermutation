# Given two strings check if one is a permutation of the other 

# both strings need to have the same characters and same number of characters
# two dictionaries with character counts for each string, then compare values 
def checkPermutation(firstInput, secondInput): 
    firstInputCount = {} 
    secondInputCount = {}
    for c in firstInput: 
        if c == " ": 
            continue
        if firstInputCount.get(c) is None: 
            firstInputCount.update({c:1})
        counter = firstInputCount.get(c)
        counter += 1
        firstInputCount.update({c:counter})
    for c in secondInput: 
        if c == " ": 
            continue
        if secondInputCount.get(c) is None: 
            secondInputCount.update({c:1})
        counter = secondInputCount.get(c)
        counter += 1
        secondInputCount.update({c:counter})
    for key in firstInputCount: 
        if key not in secondInputCount: 
            return False 
        elif secondInputCount[key] == firstInputCount[key]:
            secondInputCount.pop(key)
            continue 
    if len(secondInputCount) == 0: 
        return True
    else:
        return False

def main(): 
    string1 = "abcdef" 
    string2 = "bacdef"
    result = checkPermutation(string1, string2)
    print(f"These two are permutations is a {result} statement")

if __name__ == "__main__": 
    main()