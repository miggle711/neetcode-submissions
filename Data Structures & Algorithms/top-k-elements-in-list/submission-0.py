class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # track the frequencies of each number in a dict
        num_freq = {}
        for i in range(len(nums)):
            if nums[i] in num_freq:
                num_freq[nums[i]] += 1
            else:
                num_freq[nums[i]] = 1

        # + 1 in case the same num appears in every id
        freq_list = [[] for _ in range(len(nums) + 1)]

        # store the frequencies in a list
        for num, v in num_freq.items():
            freq_list[v].append(num)
        
        # loop from the back to get the top k
        res = []
        count = 0
        #print(f"freq_list: {freq_list}")
        for j in range(len(freq_list) - 1, 0, -1):
            if freq_list[j]:
                # loop through sublist
                for l in range(len(freq_list[j])):
                    if count == k:
                        break
                    count += 1
                    res.append(freq_list[j][l])
                    
        return res
                