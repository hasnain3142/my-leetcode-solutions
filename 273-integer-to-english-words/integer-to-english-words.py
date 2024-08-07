class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # Helper arrays to convert numbers to words
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return less_than_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return less_than_20[n // 100] + " Hundred " + helper(n % 100)
        
        res = ""
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                res = helper(num % 1000) + unit + " " + res
            num //= 1000
        
        return res.strip()
    
#         if num == 0:
#             return "Zero"
#         numdict = {
#                 0: "",
#                 1: "One",
#                   2: "Two",
#                   3: "Three",
#                   4: "Four",
#                   5: "Five",
#                   6: "Six",
#                   7: "Seven",
#                   8: "Eight",
#                   9: "Nine",
#                   10: "Ten",
#                   11: "Eleven",
#                   12: "Twelve",
#                   13: "Thirteen",
#                   14: "Fourteen",
#                   15: "Fifteen",
#                   16: "Sixteen",
#                   17: "Seventeen",
#                   18: "Eighteen",
#                   19: "Nineteen",
#                   20: "Twenty",
#                   30: "Thirty",
#                   40: "Forty",
#                   50: "Fifty",
#                   60: "Sixty",
#                   70: "Seventy",
#                   80: "Eighty",
#                   90: "Ninety"}
        
#         def two_digit(two_num):
#             ones = two_num%10
#             two_num = two_num//10

#             tens = two_num%10
#             tens_ones_dig = tens*10 + ones
#             two_num = two_num//10

#             if tens_ones_dig < 21:
#                 tens_ones = numdict[tens_ones_dig]
#             else:
#                 tens_ones = f"{numdict[tens*10]} {numdict[ones]}".strip()
            
#             return tens_ones
        
#         temp = num
#         num_word = []
#         two_num = temp % 100
#         tens_ones = two_digit(two_num)
#         num_word.append(tens_ones)
#         temp = temp // 100
  
#         unit_place = 3
#         while temp > 0:
#             if unit_place == 3:
#                 val = numdict[temp%10]
#                 if val:
#                     num_word.append(val + " Hundred")
#                 temp = temp//10
#                 unit_place += 1
#             elif unit_place == 4:
#                 val = two_digit(temp%100) 
#                 if val:
#                     num_word.append("Thousand")
#                     num_word.append(val)
 
#                 temp = temp//100
#                 unit_place += 2
#             elif unit_place == 6:
#                 val = numdict[temp%10]
#                 if val:
#                     if "Thousand" not in num_word:
#                         num_word.append("Thousand")
#                     num_word.append(val + " Hundred")
#                 temp = temp//10
#                 unit_place += 1
#             elif unit_place == 7:
#                 val = two_digit(temp%100) 
#                 if val:
#                     num_word.append("Million")
#                     num_word.append(val)
#                 temp = temp//100
#                 unit_place += 2
#             elif unit_place == 9:
#                 val = numdict[temp%10]
#                 if val:
#                     if "Million" not in num_word:
#                         num_word.append("Million")
#                     num_word.append(val + " Hundred")
#                 temp = temp//10
#                 unit_place += 1
#             elif unit_place == 10:
#                 val = numdict[temp%10]
#                 if val:
#                     num_word.append(val + " Billion")
#                 temp = temp//10
#                 unit_place += 1
            
            

#         num_word.reverse()
#         return " ".join(num_word).strip()