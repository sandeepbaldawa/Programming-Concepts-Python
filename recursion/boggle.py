'''
Boggle game
Instead of prefix, one can use a trie for lookup which will make this faster
Brute Force:- Without prefix lookup => 8 ^ (n ^ 2) where n is the side size(assuming square), each time we fanout 8
Better :- Use prefix
Even better:- User Trie
'''
import random
import time
NEIGHBOURS = [(-1, -1),  (-1, 0), (-1, 1),
               (0, -1),            (0, 1),
               (1, -1),   (1, 0),  (1, 1)]

def solveBoggle(board):
    start_time = time.time()
    for row in range(len(board)):
        for col in range(len(board[0])):
            explore_words(board, row, col, board[row][col])
    print "Time Taken", time.time() - start_time
    print res

def explore_words(board, row, col, acc):
    "Recurse throw each row,col pair and mark as visited if word formed, else backtrack, works only if length >= 3"
    if acc in WORDS and len(acc) >= 3 and len(acc) <= (len(board) * len(board[0])) :
        #print visited
        res.add(acc)
        return

    if acc not in PREFIXES:
        return
    for dr, dc in NEIGHBOURS:
        nr , nc = row + dr, col + dc
        #print nr,nc
        if in_grid(board, nr, nc) and (nr,nc) not in visited:
            visited.add((nr, nc))
            explore_words(board, nr, nc, acc + board[nr][nc])
            visited.remove((nr, nc))


def in_grid(board, r, c):
    "Check if valid row and column"
    return r >= 0 and r < len(board) and c >= 0 and c < len(board[0])

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().lower().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset


WORDS, PREFIXES = readwordlist('words4k.txt')

assert prefixes("unit") == ["", "u", "un", "uni"]

# Test1
board = ["cat","sit"]
res, visited = set(), set()
solveBoggle(board)
assert res == set(['tat', 'sic', 'sat', 'tas', 'tit', 'ait', 'sit', 'ais', 'cat', 'cis', 'sac', 'att', 'sis', 'tis', 'tic'])


# Test2
board = ["at"]
res, visited = set(), set()
solveBoggle(board)
assert  res == set([])


# Test 3
board = [""]
res, visited = set(), set()
solveBoggle(board)
assert  res == set([])


# Test 4
board = ["mag"]
res, visited = set(), set()
solveBoggle(board)
assert  res == set(['ama', 'gag', 'gam', 'aga', 'mag'])

board = ["".join(random.choice(string.ascii_lowercase) for x in range(10)) for y in range(100)]
res, visited = set(), set()
solveBoggle(board)
