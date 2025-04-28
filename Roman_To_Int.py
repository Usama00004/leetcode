class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numeral symbols to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        
        # Iterate through the string
        for i in range(len(s)):
            # If the current value is less than the next value, subtract the current value
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]
        
        return total