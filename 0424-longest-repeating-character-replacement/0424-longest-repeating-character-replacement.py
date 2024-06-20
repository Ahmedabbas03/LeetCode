from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        max_length = 0
        
        # starting pointer of the window
        window_start = 0
        max_repeating_char_count = 0
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            char_freq[right_char] += 1
            max_repeating_char_count = max(max_repeating_char_count, char_freq[right_char])
            
            # Current window size is window_end - window_start + 1
            # If the number of characters to change to make all the same is more than k, shrink the window
            if (window_end - window_start + 1) - max_repeating_char_count > k:
                left_char = s[window_start]
                char_freq[left_char] -= 1
                if char_freq[left_char] == 0:
                    char_freq.pop(left_char)
                    
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length
        
        