#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. #The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, #the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to #the number nine, which is written as IX. There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.

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
