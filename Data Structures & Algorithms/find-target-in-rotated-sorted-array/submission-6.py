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

        l = 0
        r = len(nums) - 1

        if target >= nums[minIndex] and target <= nums[r]:
            l = minIndex 
        else:
            r = minIndex - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1

            elif nums[mid] < target:
                l = mid + 1

            else:
                return mid

        return -1
