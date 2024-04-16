class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_numbers[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

converter = Solution()
result = converter.romanToInt("MCMXCIV")
print("The integer value of 'MCMXCIV' is:", result)