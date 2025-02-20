from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        occur = set()

        for binary in nums:
            occur.add(int(binary, 2))

        max_num = "1" * len(nums)
        max_num = int(max_num, 2)

        for i in range(max_num + 1):
            if i not in occur:
                return f"{i:0{len(nums)}b}" 

        return -1

class Solution1:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))
