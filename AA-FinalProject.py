import math
# S1: A quick brown dog jumps over the lazy fox.
# S2: A quick brown fox jumps over the lazy dog.

# With the two sentences above I will implement the calculation based on calculation
# values. 
def word_order(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    c1 = str.split(s1[:-1])
    c2 = str.split(s2[:-1])
    
    v1 = list(range(1,len(c1)+1))
    #print(v1)
    v2 = list()
    for word in range(len((c1))):
        for val in range(len(c2)):
            if(c1[word] == c2[val]):
                v2.append(val+1)
    #print(v2)
    vResult = [abs(a - b) for a, b in zip(v1, v2)]
    vResult2 = [abs(a * b) for a, b in zip(v1, v2)]
    vSum = 0
    vSum2 = 0
    for index in range(len(vResult)):
        vSum += vResult[index]
    for index in range(len(vResult2)):
        vSum2 += vResult2[index]
    #print(c1)
    #print(c2)
    #print(vResult)
    #print(vResult2)
    #print(vSum)
    #print(vSum2)
    if(vSum2 != 0):
        val =  vSum / vSum2
    elif((vSum + vSum2) == 0):
        val = 1
    else:
        val =  0
    return val

def isclose(a, b, rel_tol=1e-04, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def test_word_order():
    s1 = "A quick brown dog jumps over the lazy fox."
    s2 = "A quick brown fox jumps over the lazy dog."
    s3 = "A quick brown cat jumps over the lazy dog."
    s4 = "The fat bird runs across a green bog."
    s5 = "Big fat bird runs across an orange bog."
    s6 = "Big fat bird is an orange bog."
    assert isclose(0.038461, word_order(s1, s2))
    assert isclose(0.000000, word_order(s1, s1))
    assert isclose(0.75, word_order(s3, s4))
    assert isclose(1, word_order(s3, s5))
    assert isclose(1, word_order(s3, s6))