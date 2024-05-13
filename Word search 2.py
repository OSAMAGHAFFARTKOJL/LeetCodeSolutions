class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word

        m, n = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []

        def dfs(r, c, trie):
            ch = board[r][c]
            if ch not in trie:
                return

            curr = trie[ch]
            word = curr.pop('#', None)
            if word:
                res.append(word)
            
            board[r][c] = ''
            if r > 0:
                dfs(r-1, c, curr)
            if r < m-1:
                dfs(r+1, c, curr)
            if c > 0:
                dfs(r, c-1, curr)
            if c < n-1:
                dfs(r, c+1, curr)
            board[r][c] = ch

            if not curr:
                trie.pop(ch)
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        return res
