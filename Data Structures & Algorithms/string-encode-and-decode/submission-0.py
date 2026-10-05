class Solution:

    def encode(self, strs: List[str]) -> str:
        e = []
        for s in strs:
            e.append(str(len(s)))
            e.append('#') # delim
            e.append(s)
    
        return "".join(e) 
            

    def decode(self, s: str) -> List[str]:
        
        res = []

        # store the individual chars of the length (can be multi-digit)
        len_arr = []

        # keeps track of the current length of the string we're decoding
        curr_len = 0

        # store the characteers of the current string we're processing
        curr_str = []
        chars_processed = 0 

        in_str = False


        for char in s:

            if not in_str and char.isdigit():
                len_arr.append(char)

            elif not in_str and char == '#':
                # convert len_arr to a length
                curr_len = int("".join(len_arr))
                len_arr = []
                in_str = True

            elif in_str:
                curr_str.append(char)
                chars_processed += 1
                if curr_len == chars_processed:
                    in_str = False
                    res.append("".join(curr_str))
                    chars_processed = 0
                    curr_str = []

        return res if len(res) > 0 else [""]





