# Last updated: 1/17/2026, 10:21:30 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        hset = set()
4        for i in nums:
5            if i in hset:
6                return True
7            hset.add(i)
8        return False