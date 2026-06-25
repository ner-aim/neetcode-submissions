class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefixForward = [1] * n
        prefixBackward = [1] * n

        prefixForward[0] = nums[0]
        prefixBackward[n - 1] = nums[n - 1]

        for i in range(1, n):
            prefixForward[i] = prefixForward[i - 1] * nums[i]
            prefixBackward[n - i - 1] = prefixBackward[n - i] * nums[n - i - 1]

        result = []

        for i in range(n):
            if i == 0:
                result.append(prefixBackward[1])
            elif i == n - 1:
                result.append(prefixForward[n - 2])
            else:
                result.append(prefixForward[i - 1] * prefixBackward[i + 1])

        return result