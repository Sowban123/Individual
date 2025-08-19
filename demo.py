mountain = [
    [4, 8, 7, 3],
    [2, 5, 9, 3],
    [6, 3, 2, 5],
    [4, 4, 1, 6]
]

rows, cols = len(mountain), len(mountain[0])
memo = [[None]*cols for _ in range(rows)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def ski(r, c):
    if memo[r][c]: return memo[r][c]
    length, drop = 1, 0
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0<=nr<rows and 0<=nc<cols and mountain[nr][nc]<mountain[r][c]:
            l, d = ski(nr, nc)
            l += 1
            d += mountain[r][c]-mountain[nr][nc]
            if l>length or (l==length and d>drop):
                length, drop = l, d
    memo[r][c] = (length, drop)
    return memo[r][c]

best_length, best_drop = 0, 0
for r in range(rows):
    for c in range(cols):
        l, d = ski(r,c)
        if l>best_length or (l==best_length and d>best_drop):
            best_length, best_drop = l, d

print("Longest path length:", best_length)
print("Largest drop:", best_drop)
