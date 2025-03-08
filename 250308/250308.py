def minimumRecolors(blocks: str, k: int) -> int:
    if len(blocks) == k:
        return blocks.count('W')
    
    minC = 101

    for i in range(len(blocks)-k + 1):
        minC = min(blocks.count('W', i, i+k), minC)
    return minC


blocks = "WWBBBWBBBBBWWBWWWB"
k = 16
minimumRecolors(blocks, k)