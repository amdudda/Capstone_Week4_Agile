"""
Helper object that coverts a file to a list so that we can do lookups on it
"""

class Dictionary():
    # build the dictionary - takes a file name as an argument so it know which file to use to build the list
    def __init__(self,filename):
        self.words = []
        fin = open(filename)
        for line in fin:
            self.words.append(line.strip())
        fin.close()
    # end init

    def find(self,word):
        # this reuses a bisection search I built while practicisng my code over the summer.
        # it returns true if the word is in the list and false otherwise.

        def bisect(val, arr=[], index=0):
            # this function searches a sorted array via bisection and returns the index of the value if it exists
            # verify that we haven't hit length one with no match found
            if (len(arr) == 1 and arr[0] != val): return None
            middle = len(arr) // 2
            na = []     # 'na' for 'new array'
            # suss out whether we've found our item and if so, return our index
            if arr[0] == val:
                # debugging: print("precheck: " + str(index))
                # return the index position of hte value
                return index
            # else decide whether to check first half or second half
            else:
                if (val < arr[middle]):
                    na = arr[:middle]
                else:
                    index += middle
                    na = arr[middle:]
                # recursion: bisect again & keep going till we find our answer.
                return bisect(val, na, index)
        # end bisect

        # don't forget to convert to true/false!
        if (bisect(word,self.words) == None): return False
        else: return True
    # end find