import math

class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = max(1, n.bit_length())
        in_time = [0] * n
        out = [0] * n
        dep = [0] * n
        up = [[0] * LOG for _ in range(n)]
        ch = [ord(c) - 97 for c in s]
        pm = [0] * (n + 1)
        t = 0

        def dfs(u, p, d, m):
            nonlocal t
            t += 1
            in_time[u] = t
            dep[u] = d
            up[u][0] = p
            for i in range(1, LOG):
                up[u][i] = up[up[u][i - 1]][i - 1]
            nm = m ^ (1 << ch[u])
            pm[in_time[u]] = nm
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1, nm)
            out[u] = t

        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u
            for i in range(LOG - 1, -1, -1):
                if dep[u] - (1 << i) >= dep[v]:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        dfs(0, 0, 0, 0)
        bs = int(math.sqrt(n)) + 1
        bl = [0] * (n // bs + 2)
        ans = []

        for q in queries:
            p = q.split()
            u = int(p[1])
            if p[0] == "update":
                nc = ord(p[2]) - 97
                diff = (1 << ch[u]) ^ (1 << nc)
                L, R = in_time[u], out[u]
                sb, eb = L // bs, R // bs
                if sb == eb:
                    for i in range(L, R + 1):
                        pm[i] ^= diff
                else:
                    for i in range(L, (sb + 1) * bs):
                        pm[i] ^= diff
                    for b in range(sb + 1, eb):
                        bl[b] ^= diff
                    for i in range(eb * bs, R + 1):
                        pm[i] ^= diff
                ch[u] = nc
            else:
                v = int(p[2])
                l = lca(u, v)
                mu = pm[in_time[u]] ^ bl[in_time[u] // bs]
                mv = pm[in_time[v]] ^ bl[in_time[v] // bs]
                mask = mu ^ mv ^ (1 << ch[l])
                ans.append((mask & (mask - 1)) == 0)

        return ans