class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        def match(s, p):
            if not p:
                return not s
            if p[-1] == '*':
                if match(s, p[:-2]):
                    return True
                if s and (s[-1] == p[-2] or p[-2] == '.') and match(s[:-1], p):
                    return True
            if p[-1] == '+':
                if s and (s[-1] == p[-2] or p[-2] == '.') and match(s[:-1], p[:-1] + '*'):
                    return True
            if s and (p[-1] == s[-1] or p[-1] == '.') and match(s[:-1], p[:-1]):
                return True
            return False

        def match_dp(s, p):
            DP = [[False]*(len(s)+1) for _ in range(len(p)+1)]
            DP[0][0] = True
            for i in range(1, len(p)):
                DP[i+1][0] = DP[i-1][0] and p[i] == '*'
            for i in range(len(p)):
                for j in range(len(s)):
                    if p[i] == '*':
                        DP[i+1][j+1] = DP[i][j+1] or DP[i-1][j+1]
                        if p[i-1] == s[j] or p[i-1] == '.':
                            DP[i+1][j+1] |= DP[i+1][j]
                    else:
                        DP[i+1][j+1] = DP[i][j] and (p[i] == s[j] or p[i] == '.')
            return DP[-1][-1]
        return 1 if match_dp(s, p) else 0
