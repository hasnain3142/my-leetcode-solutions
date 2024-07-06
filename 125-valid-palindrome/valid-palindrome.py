class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphanum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
        
        left, right = 0, len(s)-1
        while right > left:
            print(left, right, s[left], s[right])
            while not alphanum(s[left]) and right > left:
                left += 1
            while not alphanum(s[right]) and right > left:
                right -= 1
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        return True
    
        
        
        
        
        
        
        # clean_s = []
        # for i in s:
        #     if i.isalnum():
        #         clean_s.append(i.lower())
        # print(clean_s)
        # return clean_s == clean_s[::-1]