word = input()
vowels = ['a','e','i','o','u','A','E','I','O','U','y','Y']

newW = [str.lower(l) for l in word if l not in vowels]
print('.'+'.'.join(newW))
