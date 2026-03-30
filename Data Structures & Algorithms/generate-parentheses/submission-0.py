class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def addParenthesis(o, c, comb):
            if c == 0 and o == 0:
                res.append(comb)
            
            if o > 0:
                addParenthesis(o - 1, c, comb + '(')
            if c > o:
                addParenthesis(o, c - 1, comb + ')')  
        addParenthesis(n,n,"")
        
        return res



            
