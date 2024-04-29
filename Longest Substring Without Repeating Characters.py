class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substrings=[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp=s[i:j+1]
                if (len(set(temp))==len(temp)):
                    substrings.append(temp)
        max=0
        for i in substrings:
            if max<len(i):
                max=len(i)
        
        return max

#this has time complexity O(n^3) not optimal