class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        visit, res = set(), set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, path):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r, c) in visit  or board[r][c] not in node.children:
                return 
            visit.add((r, c))
            ch = board[r][c]
            node = node.children[ch]
            path += ch
            if node.endOfWord:
                res.add(path)
            
            visit.add((r, c))
            dfs(r - 1, c, node, path)
            dfs(r + 1, c, node, path)
            dfs(r, c - 1, node, path)
            dfs(r, c + 1, node, path)

            visit.remove((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)

            


    


