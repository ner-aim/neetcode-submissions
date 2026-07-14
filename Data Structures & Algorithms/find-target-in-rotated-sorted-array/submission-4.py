class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        minIndex = l

        if minIndex == 0:
            l = 0
            r = len(nums) - 1

        elif target >= nums[0] and target <= nums[minIndex - 1]:
            l = 0
            r = minIndex - 1
        else:
            l, r = minIndex, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1

            elif nums[mid] < target:
                l = mid + 1

            else:
                return mid

        return -1
