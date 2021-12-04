from typing import Dict


class Board:
    def __init__(self, id, numbers: Dict):
        self.id = id
        self.numbers = numbers
        self.colMarks = [0] * 5
        self.rowMarks = [0] * 5

def parseBoard(lines, boardId):
    nums = {}
    for row in range(0, len(lines)):
        col = 0
        for num in lines[row].strip().split():
            nums[int(num)] = (row, col)
            col = col + 1
    return Board(boardId, nums)

# First line of picks, then grids (5x5) separated by blank line.
def parse(lines):
    picks = map(int, lines[0].split(","))
    boards = []
    # 1 grid every 6 lines starting at lines[2]
    end = len(lines) - 4
    boardId = 1
    for s in range(2, end, 6):
        grid = parseBoard(lines[s:s+5], boardId)
        boards.append(grid)
        boardId += 1
    return picks, boards

def has5(x):
    return x == 5

def checkBoard(board: Board, pick):
    if pick in board.numbers:
        row, col = board.numbers[pick]
        board.rowMarks[row] += 1
        board.colMarks[col] += 1
    return any(filter(has5, board.rowMarks)) or any(filter(has5, board.colMarks))

# def calcScore(board: Board):


input = None
filename = "day4-sample.txt" # "day4-input.txt" 
with open(filename) as reader:
    input = reader.readlines()

picks, boards = parse(input)

winningBoard = None

for pick in picks:
    for board in boards:
        if checkBoard(board, pick):
            print("Winner!")
            winningBoard = board.id
            break
    if winningBoard != None:
        break

print(board.id)
result = calcScore(board)
print(result)