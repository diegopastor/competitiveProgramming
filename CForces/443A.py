s = input()
s = [x for x in s if x != '{' and x != ',' and x != '}' and x != ' ']
print(len(set(s)))
