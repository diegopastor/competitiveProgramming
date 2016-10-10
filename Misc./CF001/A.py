def passwordNormalization(password):
    letters = []
    nums = []
    symbols = []
    for char in password:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            nums.append(char)
        else: 
            symbols.append(char)
    letters = ''.join(letters)
    nums = ''.join(nums)
    symbols = ''.join(symbols)
    normalized = letters + nums + symbols        
    return normalized


print(passwordNormalization("3a**.31,(12bsd123"))
