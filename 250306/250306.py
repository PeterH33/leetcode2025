from collections import defaultdict

def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
    
    flat = [item for row in grid for item in row]
    total = 0
    double = 0
    seen = {}
    for val in flat:
        total += val
        if val in seen.keys():
            double = val
        else:
            seen[val] = True
    n = len(grid)**2
    return [double, int(((n*(n+1))/2) - (total - double))]


grid = [[1,3],[2,2]]
findMissingAndRepeatedValues(grid)