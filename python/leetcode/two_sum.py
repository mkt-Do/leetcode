from typing import List

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            v1 = nums[i]
            tail = nums[i + 1:]
            for v2 in tail:
                if v1 + v2 == target:
                    return [i, tail.index(v2) + (i + 1)]
        return []
