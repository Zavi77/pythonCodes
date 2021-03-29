#!/usr/bin/env python
# coding: utf-8

# # Given a string s, find the length of the longest substring without repeating characters.

# In[75]:


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lidict = {}
        li = []
        i = 0
        temp = 0
        while i < len(s):
            if s[i] not in li:
                li.append(s[i])
                i = i+1
            else:
                lidict["".join(li)] = len(li)
                li = []
                temp = temp +1
                i = temp

        lidict["".join(li)] = len(li)
        return max(lidict.values())


# In[83]:


s = Solution()
s.lengthOfLongestSubstring('abcabcbb')

