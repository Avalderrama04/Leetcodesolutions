# Last updated: 1/17/2026, 11:21:55 PM
1class Solution:
2    """
3    - use a hashmap to store nums and their indices {3:0, 4:1, 5:2, 6:3}
4    - subtract element in nums from the target: (i.e 7 - 3 = 4)
5    - we run into 4 -> have we seen its complement?: (i.e, 3)
6    - look up the complement, if it does not exist we add current number
7    - if we have seen the complement, return [hmap[complement], idx]
8
9    """
10    def twoSum(self, nums: List[int], target: int) -> List[int]:
11        hmap = {}
12        for idx, ele in enumerate(nums):
13            complement = target - ele
14            if complement in hmap:
15                return [hmap[complement],idx]
16            hmap[ele] = idx
17