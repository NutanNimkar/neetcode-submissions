from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        similar_map = defaultdict(set)

        for word1, word2 in similarPairs:
            similar_map[word1].add(word2)
            similar_map[word2].add(word1)
        
        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2:
                continue
            if word2 not in similar_map[word1]:
                return False
        return True
