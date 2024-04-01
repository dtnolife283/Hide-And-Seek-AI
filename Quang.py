# sub function for calculating in class Map
import random
import heapq

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
    return min(abs(cur_row - goal_row), abs(cur_col - goal_col))

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


class PriorityQueueElement:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other: 'PriorityQueueElement'):
        return self.priority < other.priority


class Map:
    # constructor
    def __init__(self, board, row, col, weight, parent):  
        self.board = board
        self.row = row
        self.col = col
        self.weight = weight
        self.visited = 0
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
        self.hiderPosition = []
        for i in range (row):
            for j in range (col):
                if (board[i][j] == 2):
                    hiderRow = i
                    hiderCol = j
                    hider = [hiderRow, hiderCol]
                    self.hiderPosition.append(hider)

        self.parent = parent

    def __str__(self):
        result = ""
        for i in range (self.row):
            for j in range (self.col):
                if self.board[i][j] == 22 or self.board[i][j] == 24:
                    result += str(self.board[i][j] - 20) + ' '
                elif self.board[i][j] > 10:
                    result += "S "
                elif self.board[i][j] == -1:
                    result += "V "
                else:
                    result += str(self.board[i][j]) + " "
            result += '\n'
        return result

    def getVision(self):
        row = self.seekerPosition[0]
        col = self.seekerPosition[1]

        for i in range (row - 3, row + 4):
            if i < 0 or i >= self.row:
                continue
            for j in range (col - 3, col + 4):
                if j < 0 or j >= self.col:
                    continue
                if self.board[i][j] != 3 and self.board[i][j] != 1:
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
    def checkAnnoucementorHider(self, des):
        row = self.seekerPosition[0]
        col = self.seekerPosition[1]
        for i in range (row - 3, row + 4):
            if i < 0 or i >= self.row:
                continue
            for j in range (col - 3, col + 4):
                if j < 0 or j >= self.col:
                    continue
                if self.board[i][j] == 24 or self.board[i][j] == 22:
                    self.board[i][j] -= 20
                    des.append(i)
                    des.append(j)
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
    def moveSeeker(self):
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
            for i in range (seekerRow - 3, seekerRow + 4):
                if i < 0 or i >= self.row:
                    continue
                for j in range (seekerCol - 3, seekerCol + 4):
                    if j < 0 or j >= self.col:
                        continue
                    if tmpBoard[i][j] == 19 or tmpBoard[i][j] == 20:
                        tmpBoard[i][j] = -1
                    elif tmpBoard[i][j] == 22 or tmpBoard[i][j] == 24:
                        tmpBoard[i][j] -= 20
            tmpBoard[seekerRow - 1][seekerCol - 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
            

        if not checkUnValidCell(seekerRow - 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol] == -1 + 20: 
                increaseWeight = 2
            for i in range (seekerRow - 3, seekerRow + 4):
                if i < 0 or i >= self.row:
                    continue
                for j in range (seekerCol - 3, seekerCol + 4):
                    if j < 0 or j >= self.col:
                        continue
                    if tmpBoard[i][j] == 19 or tmpBoard[i][j] == 20:
                        tmpBoard[i][j] = -1
                    elif tmpBoard[i][j] == 22 or tmpBoard[i][j] == 24:
                        tmpBoard[i][j] -= 20 
            tmpBoard[seekerRow - 1][seekerCol] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow - 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol + 1] == -1 + 20: 
                increaseWeight = 2
            for i in range (seekerRow - 3, seekerRow + 4):
                if i < 0 or i >= self.row:
                    continue
                for j in range (seekerCol - 3, seekerCol + 4):
                    if j < 0 or j >= self.col:
                        continue
                    if tmpBoard[i][j] == 19 or tmpBoard[i][j] == 20:
                        tmpBoard[i][j] = -1
                    elif tmpBoard[i][j] == 22 or tmpBoard[i][j] == 24:
                        tmpBoard[i][j] -= 20
            tmpBoard[seekerRow - 1][seekerCol + 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow][seekerCol + 1] == -1 + 20: 
                increaseWeight = 2
            for i in range (seekerRow - 3, seekerRow + 4):
                if i < 0 or i >= self.row:
                    continue
                for j in range (seekerCol - 3, seekerCol + 4):
                    if j < 0 or j >= self.col:
                        continue
                    if tmpBoard[i][j] == 19 or tmpBoard[i][j] == 20:
                        tmpBoard[i][j] = -1
                    elif tmpBoard[i][j] == 22 or tmpBoard[i][j] == 24:
                        tmpBoard[i][j] -= 20
            tmpBoard[seekerRow][seekerCol + 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol + 1] == -1 + 20: 
                increaseWeight = 2
            tmpBoard[seekerRow + 1][seekerCol + 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            for i in range (seekerRow - 3, seekerRow + 4):
                if i < 0 or i >= self.row:
                    continue
                for j in range (seekerCol - 3, seekerCol + 4):
                    if j < 0 or j >= self.col:
                        continue
                    if tmpBoard[i][j] == 19 or tmpBoard[i][j] == 20:
                        tmpBoard[i][j] = -1
                    elif tmpBoard[i][j] == 22 or tmpBoard[i][j] == 24:
                        tmpBoard[i][j] -= 20
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol] == -1 + 20: 
                increaseWeight = 2
            tmpBoard[seekerRow + 1][seekerCol] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            for i in range (seekerRow - 3, seekerRow + 4):
                if i < 0 or i >= self.row:
                    continue
                for j in range (seekerCol - 3, seekerCol + 4):
                    if j < 0 or j >= self.col:
                        continue
                    if tmpBoard[i][j] == 19 or tmpBoard[i][j] == 20:
                        tmpBoard[i][j] = -1
                    elif tmpBoard[i][j] == 22 or tmpBoard[i][j] == 24:
                        tmpBoard[i][j] -= 20
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol - 1] == -1 + 20: 
                increaseWeight = 2
            for i in range (seekerRow - 3, seekerRow + 4):
                if i < 0 or i >= self.row:
                    continue
                for j in range (seekerCol - 3, seekerCol + 4):
                    if j < 0 or j >= self.col:
                        continue
                    if tmpBoard[i][j] == 19 or tmpBoard[i][j] == 20:
                        tmpBoard[i][j] = -1
                    elif tmpBoard[i][j] == 22 or tmpBoard[i][j] == 24:
                        tmpBoard[i][j] -= 20
            tmpBoard[seekerRow + 1][seekerCol - 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow][seekerCol - 1] == -1 + 20: 
                increaseWeight = 2
            for i in range (seekerRow - 3, seekerRow + 4):
                if i < 0 or i >= self.row:
                    continue
                for j in range (seekerCol - 3, seekerCol + 4):
                    if j < 0 or j >= self.col:
                        continue
                    if tmpBoard[i][j] == 19 or tmpBoard[i][j] == 20:
                        tmpBoard[i][j] = -1
                    elif tmpBoard[i][j] == 22 or tmpBoard[i][j] == 24:
                        tmpBoard[i][j] -= 20
            tmpBoard[seekerRow][seekerCol - 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        return newMap    

    def moveSeekerII(self): 
        newMap = []
        seekerRow = self.seekerPosition[0]
        seekerCol = self.seekerPosition[1]
        maxRow = self.row
        maxCol = self.col
        hider = False
        announce = False
        self.visited = calc_visited(self.board, self.row, self.col)
        for i in range(seekerRow - 3, seekerRow + 4):
            if i < 0 or i >= self.row:
                continue
            for j in range(seekerCol - 3, seekerCol + 4):
                if j < 0 or j >= self.col:
                    continue
                if self.board[i][j] == 19 or self.board[i][j] == 20:
                    self.board[i][j] = -1
                if self.board[i][j] == 22:
                    hider = True
                    self.board[i][j] -= 20
                    goalHider = [i, j]
                if self.board[i][j] == 24:
                    announce = True
                    self.board[i][j] -= 20
                    goalAnnounce = [i, j]

        if hider:
            self.getVision()
            path = []
            if self.A_Star2(goalHider[0], goalHider[1], path):
                return path, True
        elif announce:
            self.getVision()
            path = []
            if self.A_Star2(goalAnnounce[0], goalAnnounce[1], path):
                return path, True
        
        if not checkUnValidCell(seekerRow - 1, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]

            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol - 1] == -1 + 20: 
                increaseWeight = 2

            tmpBoard[seekerRow - 1][seekerCol - 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            tmpMap.getVision()
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow - 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol] == -1 + 20: 
                increaseWeight = 2

            tmpBoard[seekerRow - 1][seekerCol] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            tmpMap.getVision()
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow - 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol + 1] == -1 + 20: 
                increaseWeight = 2

            tmpBoard[seekerRow - 1][seekerCol + 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            tmpMap.getVision()
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow][seekerCol + 1] == -1 + 20: 
                increaseWeight = 2

            tmpBoard[seekerRow][seekerCol + 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            tmpMap.getVision()
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol + 1] == -1 + 20: 
                increaseWeight = 2

            tmpBoard[seekerRow + 1][seekerCol + 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            tmpMap.getVision()
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol] == -1 + 20: 
                increaseWeight = 2

            tmpBoard[seekerRow + 1][seekerCol] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            tmpMap.getVision()
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol - 1] == -1 + 20: 
                increaseWeight = 2

            tmpBoard[seekerRow + 1][seekerCol - 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            tmpMap.getVision()
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow][seekerCol - 1] == -1 + 20: 
                increaseWeight = 2

            tmpBoard[seekerRow][seekerCol - 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        

        for i in range(len(newMap)):
            newMap[i].visited = calc_visited(newMap[i].board, newMap[i].row, newMap[i].col)
        
        max = newMap[0].visited
        pos = 0
        for i in range(1, len(newMap)):
            if newMap[i].visited > max:
                max = newMap[i].visited
                pos = i
        
        if max == self.visited:
            return None, False
        else:
            return newMap[pos], False
    
    def find_cell_nearby_seeker_not_visited(self):
        seekerRow = self.seekerPosition[0]
        seekerCol = self.seekerPosition[1]
        for i in range(seekerRow - 3, seekerRow + 4):
            if i < 0 or i >= self.row:
                continue
            for j in range(seekerCol - 3, seekerCol + 4):
                if j < 0 or j >= self.col:
                    continue
                if self.board[i][j] != 3 and self.board[i][j] != 1 and self.board[i][j] != -1 and self.board[i][j] != 22 and self.board[i][j] != 24:
                    return i, j
        return -1, -1


    # tmp == None => path to goal, else is position of Annouce or Hider
    def A_Star(self, goalRow, goalCol, path):
        tmp = []

        if self.checkAnnoucementorHider(tmp):
            return tmp
        
        if self.seekerPosition[0] == goalRow and self.seekerPosition[1] == goalCol:
            return None
        
        visited = set()
        visited.add(tuple(self.seekerPosition))
        queue = []
        heapq.heapify(queue)
        priorityValue = self.weight + findDiagonalDistance(self.seekerPosition[0], self.seekerPosition[1], goalRow, goalCol)
        newElement = PriorityQueueElement(priorityValue, self)
        heapq.heappush(queue, newElement)
        
        while (len(queue) != 0):
            cur = heapq.heappop(queue).value
            newMoves = cur.moveSeeker()
            if newMoves == []:
                return None
            
            for state in newMoves:
                state.getVision()
                if state.checkAnnoucementorHider(tmp):
                    while state.parent != None:
                        path.append(state)
                        state = state.parent
                    path.reverse()
                    return tmp
                if state.seekerPosition[0] == goalRow and state.seekerPosition[1] == goalCol:
                    while state.parent != None:
                        path.append(state)
                        state = state.parent
                    path.reverse()
                    return None
                if tuple(state.seekerPosition) in visited:
                    continue
                
                state.parent = cur
                priorityValue = state.weight + findDiagonalDistance(state.seekerPosition[0], state.seekerPosition[1], goalRow, goalCol)
                newElement = PriorityQueueElement(priorityValue, state)
                heapq.heappush(queue, newElement)
                visited.add(tuple(state.seekerPosition))
                
        return None

    # return true => find a path, false otherwise
    def A_Star2(self, goalRow, goalCol, path):
        
        if self.seekerPosition[0] == goalRow and self.seekerPosition[1] == goalCol:
            return True
        
        visited = set()
        visited.add(tuple(self.seekerPosition))
        queue = []
        heapq.heapify(queue)
        priorityValue = self.weight + findDiagonalDistance(self.seekerPosition[0], self.seekerPosition[1], goalRow, goalCol)
        newElement = PriorityQueueElement(priorityValue, self)
        heapq.heappush(queue, newElement)
        
        while (len(queue) != 0):
            cur = heapq.heappop(queue).value
            newMoves = cur.moveSeeker()
            
            for state in newMoves:
                state.getVision()
                
                if state.seekerPosition[0] == goalRow and state.seekerPosition[1] == goalCol:
                    while state.parent != None:
                        path.append(state)
                        state = state.parent
                    path.reverse()
                    return True
                if tuple(state.seekerPosition) in visited:
                    continue
                
                state.parent = cur
                priorityValue = state.weight + findDiagonalDistance(state.seekerPosition[0], state.seekerPosition[1], goalRow, goalCol)
                newElement = PriorityQueueElement(priorityValue, state)
                heapq.heappush(queue, newElement)
                visited.add(tuple(state.seekerPosition))
                
        return False
        
        
def calc_visited(board, row, col):
    visited = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] > 10 or board[i][j] == -1:
                visited += 1
    return visited

