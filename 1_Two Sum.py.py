class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for j,i in enumerate(nums):
            if (target - i) in dic:
                return([(dic[(target - i)]),j])  
            else:
                dic[i] = j