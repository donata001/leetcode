class Solution(object):
    def restoreIpAddresses(self, s):
        def dfs(idx, path, n):
            if n > 4: return
            if n == 4 and idx == len(s):
                res.append(path)

            for i in xrange(1, 4):
                if idx+i>len(s):break
                substring = s[idx:idx+i]
                if (len(substring)>1 and substring[0] == '0') or (i==3 and substring>'255'):
                    continue
                dfs(idx+i, path+substring+"."*bool(n-3), n+1)

        if not s: return []
        res = []
        dfs(0, "", 0)
        return res


        