class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                # mirrored row does not exist
                if j >= len(words):
                    return False

                # mirrored column does not exist
                if i >= len(words[j]):
                    return False

                # characters do not match
                if words[i][j] != words[j][i]:
                    return False

        return True