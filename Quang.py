


# sub function for calculating in class Map
def checkWall(row, col, board, maxRow, maxCol):
    if (row < 0 or row >= maxRow or col < 0 or col >= maxCol):
        return False
    if (board[row][col] == 1):
        return True
    return False

def checkUnValidCell(row, col, board, maxRow, maxCol):
    if (row < 0 or row >= maxRow or col < 0 or col >= maxCol):
        return True
    if (board[row][col] == 1):
        return True
    return False


def hideCell(row, col, board, maxRow, maxCol):
    if checkUnValidCell(row, col, board, maxRow, maxCol):
        return
    if board[row][col] > 10:
        board[row][col] -= 20


def findDiagonalDistance(cur_row, cur_col, goal_row, goal_col):
    heightDistance = abs(cur_row - goal_row)
    widthDistance = abs(cur_col - goal_col)
    if heightDistance > widthDistance:
        return heightDistance
    return widthDistance


def findNumberOfWallAround(row, col, board, maxRow, maxCol):
    cnt = 0
    for i in range(row - 1, row + 2):
        if (i < 0 or i >= maxRow):
                continue
        for j in range (col - 1, col + 2):
            if (j < 0 or j >= maxCol):
                continue
            if (board[i][j] == 1):
                cnt += 1
    return cnt


def calcCellValue(cur_row, cur_col, goal_row, goal_col, board, ROW, COL):
    if not(board[goal_row][goal_col] == 0 or board[goal_row][goal_col] == 2):
        return 0
    return findDiagonalDistance(cur_row, cur_col, goal_row, goal_col) + findNumberOfWallAround(goal_row, goal_col, board, ROW, COL) * (ROW + COL) // 18



def calcHeuristic(cur_row, cur_col, goal_row, goal_col):
    return min(abs(cur_row - goal_row), abs(cur_col - goal_col))


class Map:
    # constructor
    def __init__(self, board, row, col, weight):  
        self.board = board
        self.row = row
        self.col = col
        self.weight = weight

        seekerRow = 0
        seekerCol = 0
        for i in range (row):
            for j in range (col):
                if (board[i][j] == 3):
                    seekerRow = i
                    seekerCol = j
        self.seekerPosition = [seekerRow, seekerCol]

        hiderRow = 0
        hiderCol = 0
        for i in range (row):
            for j in range (col):
                if (board[i][j] == 2):
                    hiderRow = i
                    hiderCol = j
        self.hiderPosition = [hiderRow, hiderCol]

    def __str__(self):
        result = ""
        for i in range (self.row):
            for j in range (self.col):
                result += str(self.board[i][j]) + " "
            result += '\n'
        return result

    def getVision(self):
        row = self.seekerPosition[0]
        col = self.seekerPosition[1]
        #Add ten to all free cell
        for i in range (row - 3, row + 4):
            if i < 0 or i >= self.row:
                continue
            for j in range (col - 3, col + 4):
                if j < 0 or j >= self.col:
                    continue
                if self.board[i][j] != 1 and self.board[i][j] != 3:
                    self.board[i][j] += 20
        # di tu trong ra, neu gap wall thi chinh nhung o vision co the ve vi tri cu
        
        # LV1: top left
        if (checkWall(row - 1, col - 1, self.board, self.row, self.col)):
            hideCell(row - 2, col - 2, self.board, self.row, self.col) 
            hideCell(row - 3, col - 3, self.board, self.row, self.col)
            hideCell(row - 2, col - 3, self.board, self.row, self.col)
            hideCell(row - 3, col - 2, self.board, self.row, self.col)
        # LV1: top
        if (checkWall(row - 1, col, self.board, self.row, self.col)):
            hideCell(row - 2, col, self.board, self.row, self.col ) 
            hideCell(row - 3, col, self.board, self.row, self.col)
            hideCell(row - 3, col - 1, self.board, self.row, self.col)
            hideCell(row - 3, col + 1, self.board, self.row, self.col)
            if (checkWall(row - 1, col - 1, self.board, self.row, self.col)):
                hideCell(row - 2, col - 1, self.board, self.row, self.col)
            if (checkWall(row - 1, col + 1, self.board, self.row, self.col)):
                hideCell(row - 2, col + 1, self.board, self.row, self.col)
        # LV1: top right
        if (checkWall(row - 1, col + 1, self.board, self.row, self.col)):
            hideCell(row - 2, col + 2, self.board, self.row, self.col) 
            hideCell(row - 3, col + 3, self.board, self.row, self.col)
            hideCell(row - 2, col + 3, self.board, self.row, self.col)
            hideCell(row - 3, col + 2, self.board, self.row, self.col)
        # LV1: right
        if (checkWall(row, col + 1, self.board, self.row, self.col)):
            hideCell(row, col + 2, self.board, self.row, self.col) 
            hideCell(row, col + 3, self.board, self.row, self.col)
            hideCell(row - 1, col + 3, self.board, self.row, self.col)
            hideCell(row + 1, col + 3, self.board, self.row, self.col)
            if (checkWall(row - 1, col + 1, self.board, self.row, self.col)):
                hideCell(row - 1, col + 2, self.board, self.row, self.col)
            if (checkWall(row + 1, col + 1, self.board, self.row, self.col)):
                hideCell(row + 1, col + 2, self.board, self.row, self.col)
        # LV1: bot right
        if (checkWall(row + 1, col + 1, self.board, self.row, self.col)):
            hideCell(row + 2, col + 2, self.board, self.row, self.col) 
            hideCell(row + 3, col + 3, self.board, self.row, self.col)
            hideCell(row + 3, col + 2, self.board, self.row, self.col)
            hideCell(row + 2, col + 3, self.board, self.row, self.col)
        # LV1: bot
        if (checkWall(row + 1, col, self.board, self.row, self.col)):
            hideCell(row + 2, col, self.board, self.row, self.col) 
            hideCell(row + 3, col, self.board, self.row, self.col)
            hideCell(row + 3, col + 1, self.board, self.row, self.col)
            hideCell(row + 3, col - 1, self.board, self.row, self.col)
            if (checkWall(row + 1, col + 1, self.board, self.row, self.col)):
                hideCell(row + 2, col + 1, self.board, self.row, self.col)
            if (checkWall(row + 1, col - 1, self.board, self.row, self.col)):
                hideCell(row + 2, col - 1, self.board, self.row, self.col)
        # LV1: bot left
        if (checkWall(row + 1, col - 1, self.board, self.row, self.col)):
            hideCell(row + 2, col - 2, self.board, self.row, self.col) 
            hideCell(row + 3, col - 3, self.board, self.row, self.col)
            hideCell(row + 3, col - 2, self.board, self.row, self.col)
            hideCell(row + 2, col - 3, self.board, self.row, self.col)
        # LV1: left
        if (checkWall(row, col - 1, self.board, self.row, self.col)):
            hideCell(row, col - 2, self.board, self.row, self.col) 
            hideCell(row, col - 3, self.board, self.row, self.col)
            hideCell(row - 1, col - 3, self.board, self.row, self.col)
            hideCell(row + 1, col - 3, self.board, self.row, self.col)
            if (checkWall(row - 1, col - 1, self.board, self.row, self.col)):
                hideCell(row - 1, col - 2, self.board, self.row, self.col)
            if (checkWall(row + 1, col - 1, self.board, self.row, self.col)):
                hideCell(row + 1, col - 2, self.board, self.row, self.col)

        # Lv2: top top left left
        if (checkWall(row - 2, col - 2, self.board, self.row, self.col)):
            hideCell(row - 3, col - 3, self.board, self.row, self.col)
        # LV2: top top left 
        if (checkWall(row - 2, col - 1, self.board, self.row, self.col)):
            hideCell(row - 3, col - 1, self.board, self.row, self.col)
            hideCell(row - 3, col - 2, self.board, self.row, self.col)
        # LV2: top top 
        if (checkWall(row - 2, col, self.board, self.row, self.col)):
            hideCell(row - 3, col, self.board, self.row, self.col)

        # LV2: top top right
        if (checkWall(row - 2, col + 1, self.board, self.row, self.col)):
            hideCell(row - 3, col + 1, self.board, self.row, self.col)
            hideCell(row - 3, col + 2, self.board, self.row, self.col)
        # LV2: top top right right
        if (checkWall(row - 2, col + 2, self.board, self.row, self.col)):
            hideCell(row - 3, col + 3, self.board, self.row, self.col)
        
        # LV2: top right right
        if (checkWall(row - 1, col + 2, self.board, self.row, self.col)):
            hideCell(row - 2, col + 3, self.board, self.row, self.col)
            hideCell(row - 1, col + 3, self.board, self.row, self.col)
        # LV2: right right
        if (checkWall(row, col + 2, self.board, self.row, self.col)):
            hideCell(row, col + 3, self.board, self.row, self.col)
        # LV2: bot right right
        if (checkWall(row + 1, col + 2, self.board, self.row, self.col)):
            hideCell(row + 1, col + 3, self.board, self.row, self.col)
            hideCell(row + 2, col + 3, self.board, self.row, self.col)          
        # Lv2: bot bot right right
        if (checkWall(row + 2, col + 2, self.board, self.row, self.col)):
            hideCell(row + 3, col + 3, self.board, self.row, self.col)
        # LV2: bot bot right
        if (checkWall(row + 2, col + 1, self.board, self.row, self.col)):
            hideCell(row + 3, col + 1, self.board, self.row, self.col)
            hideCell(row + 3, col + 2, self.board, self.row, self.col)
        # LV2: bot bot
        if (checkWall(row + 2, col, self.board, self.row, self.col)):
            hideCell(row + 3, col, self.board, self.row, self.col)
        # LV2: bot bot left
        if (checkWall(row + 2, col - 1, self.board, self.row, self.col)):
            hideCell(row + 3, col - 1, self.board, self.row, self.col)
            hideCell(row + 3, col - 2, self.board, self.row, self.col)
        # Lv2: bot bot left left
        if (checkWall(row + 2, col - 2, self.board, self.row, self.col)):
            hideCell(row + 3, col - 3, self.board, self.row, self.col)
        # LV2: bot left left
        if (checkWall(row + 1, col - 2, self.board, self.row, self.col)):
            hideCell(row + 1, col - 3, self.board, self.row, self.col)
            hideCell(row + 2, col - 3, self.board, self.row, self.col)  
        # LV2: left left
        if (checkWall(row, col - 2, self.board, self.row, self.col)):
            hideCell(row, col - 3, self.board, self.row, self.col)
        #LV2: top left left
        if (checkWall(row - 1, col - 2, self.board, self.row, self.col)):
            hideCell(row - 1, col - 3, self.board, self.row, self.col)
            hideCell(row - 2, col - 3, self.board, self.row, self.col)

    # check for surrounding annoucement
    def checkAnnoucement(self):
        for i in range (self.row - 3, self.row + 4):
            if i < 0 or i >= self.row:
                continue
            for j in range (self.col - 3, self.col + 4):
                if j < 0 or j >= self.col:
                    continue
                if self.board[i][j] == 4 + 20:
                    return True 
        return False

    #Find most value cell to go to: return a list of 2 element: Row and Column
    def findMostValueCell(self):
        max = calcCellValue(self.seekerPosition[0], self.seekerPosition[1], 0, 0, self.board, self.row, self.col)
        pos = [0,0]
        for i in range (self.row):
            for j in range (self.col):
                if i == 0 and j == 0:
                    continue
                tmp = calcCellValue(self.seekerPosition[0], self.seekerPosition[1], i, j, self.board, self.row, self.col)
                if tmp > max:
                    max = tmp
                    pos[0] = i
                    pos[1] = j
        return pos

    # Move seeker: return a list of new Map
    def moveSeeker(self, goalRow, goalCol):
        newMap = []
        seekerRow = self.seekerPosition[0]
        seekerCol = self.seekerPosition[1]
        maxRow = self.row
        maxCol = self.col
        if not checkUnValidCell(seekerRow - 1, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol - 1] == -1 + 20: 
                increaseWeight = 2
            tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow - 1][seekerCol - 1] = tmpBoard[seekerRow - 1][seekerCol - 1], tmpBoard[seekerRow][seekerCol]
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight)
            if tmpMap.checkAnnoucement():
                newMap.clear()
                newMap.append(tmpMap)
                return newMap
            newMap.append(tmpMap)
            

        if not checkUnValidCell(seekerRow - 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol] == -1 + 20: 
                increaseWeight = 2
                tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow - 1][seekerCol] = tmpBoard[seekerRow - 1][seekerCol], tmpBoard[seekerRow][seekerCol]
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight)
            if tmpMap.checkAnnoucement():
                newMap.clear()
                newMap.append(tmpMap)
                return newMap
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow - 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol + 1] == -1 + 20: 
                increaseWeight = 2
            tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow - 1][seekerCol + 1] = tmpBoard[seekerRow - 1][seekerCol + 1], tmpBoard[seekerRow][seekerCol] 
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight)
            if tmpMap.checkAnnoucement():
                newMap.clear()
                newMap.append(tmpMap)
                return newMap
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            increaseWeight = 1
            if self.board[seekerRow][seekerCol + 1] == -1 + 20: 
                increaseWeight = 2
            tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow][seekerCol + 1] = tmpBoard[seekerRow][seekerCol + 1], tmpBoard[seekerRow][seekerCol]
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight)
            if tmpMap.checkAnnoucement():
                newMap.clear()
                newMap.append(tmpMap)
                return newMap
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol + 1] == -1 + 20: 
                increaseWeight = 2
            tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow + 1][seekerCol + 1] = tmpBoard[seekerRow + 1][seekerCol + 1], tmpBoard[seekerRow][seekerCol]
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight)
            if tmpMap.checkAnnoucement():
                newMap.clear()
                newMap.append(tmpMap)
                return newMap
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol] == -1 + 20: 
                increaseWeight = 2
            tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow + 1][seekerCol] = tmpBoard[seekerRow + 1][seekerCol], tmpBoard[seekerRow][seekerCol]
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight)
            if tmpMap.checkAnnoucement():
                newMap.clear()
                newMap.append(tmpMap)
                return newMap
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol - 1] == -1 + 20: 
                increaseWeight = 2
            tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow + 1][seekerCol - 1] = tmpBoard[seekerRow + 1][seekerCol - 1], tmpBoard[seekerRow][seekerCol]
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight)
            if tmpMap.checkAnnoucement():
                newMap.clear()
                newMap.append(tmpMap)
                return newMap
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            increaseWeight = 1
            if self.board[seekerRow][seekerCol - 1] == -1 + 20: 
                increaseWeight = 2
            tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow][seekerCol - 1] = tmpBoard[seekerRow][seekerCol - 1], tmpBoard[seekerRow][seekerCol]
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight)
            if tmpMap.checkAnnoucement():
                newMap.clear()
                newMap.append(tmpMap)
                return newMap
            newMap.append(tmpMap)
        return newMap
        
    #not done yet
    def A_Star(self, goalRow, goalCol):
        if self.seekerPosition[0] == goalRow and self.seekerPosition[1] == goalCol:
            return 
        
# read file
def read_matrix_to_2d_list(filename):
    with open(filename, 'r') as file:
        # Read the first line to get the dimensions 
        dimensions = [int(x) for x in file.readline().strip().split()]
        ROW = dimensions[0]
        COL = dimensions[1]
        board = []
        # Create an empty 2D list to store the matrix
        for line in file:
            # Split the line based on whitespace (you can adjust the delimiter if needed)
            row = [int(x) for x in line.strip().split()]
            board.append(row)
        result = Map(board, ROW, COL, 0)
        return result


  
def main():
    Map = read_matrix_to_2d_list("board.txt")
    Map.getVision()
    print(Map)

main()
    


    
# class Lv1:
#     def __init__(self, map):
#         self.map = map
        
