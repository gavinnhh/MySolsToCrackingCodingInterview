'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -) true
pales, pale -) true
pale, bale -) true

'''

def oneStepAway(s1, s2):
    if len(s1) - len(s2) > 1: 
        return False
    
    s = s1 + s2
    bitVector = 0
    count = 0
    for c in s:
        num = ord(c) - ord('a')
        bitVector ^= (1 << num)
    
    while bitVector != 0:  # count how many 1 in the bitVector in bin form
        bitVector &= bitVector - 1
        count += 1
        
    if count == 1 or count == 0:
        return True
    elif len(s1) == len(s2) and count == 2: # if length the same, then we do replacement
        return True
    else:
        return False

print(oneStepAway('abcd', 'abcg'))
print(oneStepAway('pale', 'ple'))
print(oneStepAway('plae', 'bae'))
