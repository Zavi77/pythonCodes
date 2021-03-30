#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height) -> int:
        maxl = maxr = wt = 0
        for i in range(len(height)):
            if len(height[:i])>0:
                maxl = max(height[:i])
            if len(height[i:])>0:
                maxr = max(height[i:])
            w = min(maxl,maxr) - height[i]
            if w>0:
                wt = wt + w
        return wt


# In[113]:


s = Solution()
s.trap([4,2,0,3,2,5])

