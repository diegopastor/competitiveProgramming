"""
 894A - QAQ
"""

def QAQs(s):
    n = 0
    for i in range(len(s)):
        if s[i] == 'A':
            prevQs = len([l for l in s[:i+1] if l == 'Q'])
            postQs = len([l for l in s[i:] if l == 'Q'])
            if (prevQs > 0 and postQs > 0):
                n += (prevQs * postQs)
    return n

print(QAQs(input()))
