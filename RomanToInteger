class Solution:
    def romanToInt(self, s: str) -> int:
        x = len(s)
        result = 0
        z = 0
        print('roman numberal: ' + s)
        print('number length is: ' + str(len(s)))
        
        #create the list
        romlist = list(s)
        numlist = []
        print(romlist)
        
        #cycle through and determine the new values
        for x in reversed(romlist):
            if x == "I":
                y = 1
            if x == "V":
                y = 5
            if x == "X":
                y = 10
            if x == "L":
                y = 50
            if x == "C":
                y = 100
            if x == "D":
                y = 500
            if x == "M":
                y = 1000
            
            if y < z:
                y *= -1
            result += y
            #numlist.insert(-1, y)
            z = y
        return result
