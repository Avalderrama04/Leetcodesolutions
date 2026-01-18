# Last updated: 1/17/2026, 11:23:41 PM
class Solution:
    """
    - use a hashmap to store nums and their indices {3:0, 4:1, 5:2, 6:3}
    - subtract element in nums from the target: (i.e 7 - 3 = 4)
    - we run into 4 -> have we seen its complement?: (i.e, 3)
    - look up the complement, if it does not exist we add current number
    - if we have seen the complement, return [hmap[complement], idx]

    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for idx, ele in enumerate(nums):
            complement = target - ele
            if complement in hmap:
                return [hmap[complement],idx]
            hmap[ele] = idx
