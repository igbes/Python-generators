import unittest

def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x
        #print(id, sum)
        yield 
    yield sum
   
def multy_process(*args):
    R = {}
    r = {}
    max_number = args[0]
    for i in range(len(args)):
        key = 'id' + str(i + 1)
        R[key] = None
        r[key] = long_process(key, args[i])
        if args[i] > max_number: max_number = args[i]
    for i in range(max_number + 1):
        for key in r:
            if R[key] is None: R[key] = next(r[key])
    print(R)
    return R

class TestGenerator(unittest.TestCase):
    
    def test_multy_process(self):
        self.assertEqual(multy_process(10, 15, 26, 100, 8), {'id1': 45, 'id2': 105, 'id3': 325, 'id4': 4950, 'id5': 28})    
    
if __name__ == '__main__':
    unittest.main()
        