class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = defaultdict(int)
        n = len(nums)
        result = []
        for i in range(n):
            hashMap[nums[i]] += 1

        frequency = [[] for i in range(n+1)]
        for number, count in hashMap.items():
            frequency[count].append(number)

        for i in range(len(frequency) - 1, 0, -1):
            for number in frequency[i]:
                result.append(number)
                if len(result) == k:
                    return result            