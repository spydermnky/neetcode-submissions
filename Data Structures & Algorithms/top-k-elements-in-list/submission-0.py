class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            key = num
            if key not in dict:
                dict[key] = 0
            dict[key] += 1
        dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
        return [key for key,val in dict[:k]]
        