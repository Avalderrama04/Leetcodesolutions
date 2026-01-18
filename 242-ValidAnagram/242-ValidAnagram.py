# Last updated: 1/17/2026, 10:44:27 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        freqmap1 = {}
4        freqmap2 = {}
5
6        for i in s:
7            if i not in freqmap1:
8                freqmap1[i] = 1
9            else:
10                freqmap1[i] += 1
11        
12        for j in t:
13            if j not in freqmap2:
14                freqmap2[j] = 1
15            else:
16                freqmap2[j] += 1
17        return freqmap1 == freqmap2