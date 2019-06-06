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
