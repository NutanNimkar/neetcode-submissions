from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_map = Counter(chars)
        total_sum = 0

        for word in words:
            chars_map = Counter(chars)
            word_exists = False
            for c in word:
                if c in chars_map and chars_map[c] > 0:
                    word_exists = True
                    chars_map[c] -= 1
                else:
                    word_exists = False
                    break
            if word_exists:
                total_sum += len(word)
        return total_sum
                
            
