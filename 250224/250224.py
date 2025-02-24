
def mostProfitablePath(edges, bob, amount):

    # Create an adjacency list
    from collections import defaultdict
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Using recursion dfs run bobs path and adjust the amounts
    def bobPath(node, level, parent):
        ret = [False, 0]
        for neighbor in tree[node]:
            if node == bob:
                amount[node] = 0
                return [True, level + 1]
            if neighbor != parent and (ret := bobPath(neighbor, level + 1, node))[0]:
                bobLen = ret[1]
                if level == bobLen // 2 and bobLen % 2:
                    amount[node] //= 2
                elif level >= bobLen // 2:
                    amount[node] = 0
                return ret
        return ret
    
    # run bob path from the root
    bobPath(0,0,None)
    print(amount)

    # Now just DFS for the best alice path on the adjusted amounts
    def dfsAlice(node, parent):
        ret = float(-1000000)
        for neighbor in tree[node]:
            if neighbor != parent:
                ret = max(ret, dfsAlice(neighbor, node))
        if ret == float(-1000000):
            ret = 0
        return ret + amount[node]

    return dfsAlice(0, None)


# Test code for example 1 
edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]
print(mostProfitablePath(edges, bob, amount))
