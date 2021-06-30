# -*- coding: utf-8 -*-
"""
# DP Approach
"""

@lru_cache(None)

def fun1(s):
  dp = [0]*len(s)
  for i in range(len(s)):
    if i==-1 or s[i]=='(':
      dp[i] = 0
    elif i>=1 and s[i]==')':
      dp[i] = dp[i-2] + 2
    p = i - dp[i-1] - 1
    if p> 0 and s[p]=='(':
      dp[i] =  dp[p-1] + 2 + dp[i-1]
    else:
      dp[i] = 0
  return max(dp)

s = ")()())"
fun1(s)

"""# Stack approach"""

def fun(s):
  stk = [-1]
  result = 0
  for i in range(len(s)):
    if s[i]=='(':
      stk.append(i)
    else:
      stk.pop()
      if len(stk)==0:
        stk.append(i)
      else:
        result = max(result,i - stk[-1])
  return result

## https://www.youtube.com/watch?v=tzbEtUM78RU