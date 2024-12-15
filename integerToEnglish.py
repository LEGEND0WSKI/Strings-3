# Time:O(n)
# Space:O(1)
# Leetcode:Yes
# Issues:No
class Solution:
    def numberToWords(self, num: int) -> str:
        thousands=["","Thousand","Million", "Billion"]
        below20  =[" ","One","Two","Three","Four","Five",
                   "Six","Seven","Eight","Nine","Ten","Eleven",
                   "Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
                   "Seventeen","Eighteen","Nineteen"]
        tens     =["","","Twenty","Thirty","Forty","Fifty",
                   "Sixty","Seventy","Eighty","Ninety"]

        def helper(num):                                                        
            if num < 20:
                return below20[num]
            elif num<100:
                return tens[num//10] + " " + below20[num%10]
            else:
                return below20[num//100] + " Hundred " + helper(num%100)        #recursion only on 100 +
        # 0 case
        if num == 0 : return "Zero"
        
        # solution
        result = ""
        i = 0

        while num > 0:
            triplet = num%1000
            if triplet > 0:
                result = helper(triplet).strip() +" "+thousands[i]+" "+ result
            num = num//1000
            i+=1

        return result.strip()
