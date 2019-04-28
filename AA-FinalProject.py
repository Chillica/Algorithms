import math
# S1: A quick brown dog jumps over the lazy fox.
# S2: A quick brown fox jumps over the lazy dog.

# With the two sentences above I will implement the calculation based on calculation
# values. 

def magnitude(v1):
    vResult = [abs(a * b) for a, b in zip(v1, v1)]
    mag = math.sqrt(sum(vResult, 0))
    return mag

def word_order(s1, s2):
    c1 = str.split(s1[:-1].lower())
    c2 = str.split(s2[:-1].lower())
    v1 = list(range(1,len(c1)+1))
    v2 = list()
    for word in range(len((c1))):
        for val in range(len(c2)):
            if(c1[word] == c2[val]):
                v2.append(val+1)
    vResult = [abs(a - b) for a, b in zip(v1, v2)]
    vResult2 = [abs(a * b) for a, b in zip(v1, v2)]
    mag1 = magnitude(vResult)
    mag2 = magnitude(vResult2)
    if(mag2 != 0):
        val = mag1 / mag2
    elif((mag1 + mag2) == 0):
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
    assert isclose(0.067091, word_order(s1, s2))
    assert isclose(0.000000, word_order(s1, s1))
    assert isclose(0.806225, word_order(s3, s4))
    assert isclose(1, word_order(s3, s5))
    assert isclose(1, word_order(s3, s6))