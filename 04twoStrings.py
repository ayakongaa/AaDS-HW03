def extraLetter(a: str, b: str) -> str:
    hashMapB = {}
    
    for char in b:
        hashMapB[char] = hashMapB.get(char, 0) + 1
    
    for char in a:
        if char in hashMapB:
            hashMapB[char] -= 1
    
    for letter, count in hashMapB.items():
        if count > 0:
            return letter
    
    return ""
    
print(extraLetter(input(), input()))
