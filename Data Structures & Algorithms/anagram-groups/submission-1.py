class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_freqs = {}
        # loop thru each string 
        for i in range(len(strs)):
            # initialise an array to track the freqs of each char in a string
            freq_arr = [0] * 26
            for j in range(len(strs[i])):
                # the value at freq_arr[i] represents the freq of the char in the string
                freq_arr[ord(strs[i][j]) - 97] += 1
            # anagrams should have the same freq_arr, 
            # so we use it as a key and the make the strings as the value
            if tuple(freq_arr) in char_freqs:
                # make a list to store the other strings that may match 
                char_freqs[tuple(freq_arr)].append(strs[i])
            else:
                char_freqs[tuple(freq_arr)] = [strs[i]]
        return list(char_freqs.values())

            
                
        
        
                

    



