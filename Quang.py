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
    return findNumberOfWallAround(goal_row, goal_col, board, ROW, COL) * (ROW + COL) // 16 - findDiagonalDistance(cur_row,cur_col, goal_row, goal_col)


class PriorityQueueElement:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other: 'PriorityQueueElement'):
        return self.priority < other.priority


class Map:
    # constructor
    def __init__(self, board, row, col, weight, parent, step):  
        self.board = board.copy()
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
        self.step = step

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

    # check for surrounding Hider, if found return true
    def checkHider(self, des):
        row = self.seekerPosition[0]
        col = self.seekerPosition[1]
        for i in range (row - 3, row + 4):
            if i < 0 or i >= self.row:
                continue
            for j in range (col - 3, col + 4):
                if j < 0 or j >= self.col:
                    continue
                if self.board[i][j] == 22:
                    self.board[i][j] -= 20
                    des.append(i)
                    des.append(j)
                    return True
        return False

    # check for surrounding Announcement, if found return true
    def checkAnnouncement(self, des):
        row = self.seekerPosition[0]
        col = self.seekerPosition[1]
        for i in range (row - 3, row + 4):
            if i < 0 or i >= self.row:
                continue
            for j in range (col - 3, col + 4):
                if j < 0 or j >= self.col:
                    continue
                if self.board[i][j] == 24:
                    des.append([i, j])
        if len(des) > 0:
            return True
        return False

    #Find most value cell to go to: return a list of 2 element: Row and Column
    def findMostValueCell(self):
        max = -1e9
        pos = [0, 0]
        for i in range (self.row):
            for j in range (self.col):
                if (i == 0 and j == 0) or (i == self.row and j == self.col):
                    continue
                if self.board[i][j] == -1 or self.board[i][j] == 1 or self.board[i][j] == 3 or self.board[i][j] > 10:
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
                increaseWeight = 5
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self, self.step + 1)
            newMap.append(tmpMap)
            

        if not checkUnValidCell(seekerRow - 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol] == -1 + 20: 
                increaseWeight = 5
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self, self.step + 1)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow - 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow - 1][seekerCol + 1] == -1 + 20: 
                increaseWeight = 5
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self, self.step + 1)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow][seekerCol + 1] == -1 + 20: 
                increaseWeight = 5
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self, self.step + 1)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol + 1] == -1 + 20: 
                increaseWeight = 5
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self, self.step + 1)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol] == -1 + 20: 
                increaseWeight = 5
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self, self.step + 1)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow + 1][seekerCol - 1] == -1 + 20: 
                increaseWeight = 5
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self, self.step + 1)
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            
            increaseWeight = 1
            if self.board[seekerRow][seekerCol - 1] == -1 + 20: 
                increaseWeight = 5
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self, self.step + 1)
            newMap.append(tmpMap)
        return newMap


    def moveSeekerII(self): 
        newMap = []
        seekerRow = self.seekerPosition[0]
        seekerCol = self.seekerPosition[1]
        maxRow = self.row
        maxCol = self.col

        if not checkUnValidCell(seekerRow - 1, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            for hider in self.hiderPosition:
                if hider[0] == seekerRow - 1 and hider[1] == seekerCol - 1:
                    tmpBoard[hider[0]][hider[1]] = -1
                    tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow - 1][seekerCol - 1] = tmpBoard[seekerRow - 1][seekerCol - 1], tmpBoard[seekerRow][seekerCol]
                    hider[0] = -10
                    hider[1] = -10
                    resMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
                    return resMap
            tmpBoard[seekerRow - 1][seekerCol - 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, 0, None, 0, self.step + 1)
            tmpMap.getVision()
            for row in range(maxRow):
                for col in range(maxCol):
                    if tmpMap.board[row][col] == 20:
                        tmpMap.board[row][col] = -1
            newMap.append(tmpMap)
            

        if not checkUnValidCell(seekerRow - 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            for hider in self.hiderPosition:
                if hider[0] == seekerRow - 1 and hider[1] == seekerCol:
                    tmpBoard[hider[0]][hider[1]] = -1
                    tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow - 1][seekerCol] = tmpBoard[seekerRow - 1][seekerCol], tmpBoard[seekerRow][seekerCol]
                    hider[0] = -10
                    hider[1] = -10
                    resMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
                    return resMap
            tmpBoard[seekerRow - 1][seekerCol] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
            tmpMap.getVision()
            for row in range(maxRow):
                for col in range(maxCol):
                    if tmpMap.board[row][col] == 20:
                        tmpMap.board[row][col] = -1
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow - 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            for hider in self.hiderPosition:
                if hider[0] == seekerRow - 1 and hider[1] == seekerCol + 1:
                    tmpBoard[hider[0]][hider[1]] = -1
                    tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow - 1][seekerCol + 1] = tmpBoard[seekerRow - 1][seekerCol + 1], tmpBoard[seekerRow][seekerCol]
                    hider[0] = -10
                    hider[1] = -10
                    resMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
                    return resMap
            tmpBoard[seekerRow - 1][seekerCol + 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
            tmpMap.getVision()
            for row in range(maxRow):
                for col in range(maxCol):
                    if tmpMap.board[row][col] == 20:
                        tmpMap.board[row][col] = -1
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            for hider in self.hiderPosition:
                if hider[0] == seekerRow and hider[1] == seekerCol + 1:
                    tmpBoard[hider[0]][hider[1]] = -1
                    tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow][seekerCol + 1] = tmpBoard[seekerRow][seekerCol + 1], tmpBoard[seekerRow][seekerCol]
                    resMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
                    hider[0] = -10
                    hider[1] = -10
                    return resMap
            tmpBoard[seekerRow][seekerCol + 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
            tmpMap.getVision()
            for row in range(maxRow):
                for col in range(maxCol):
                    if tmpMap.board[row][col] == 20:
                        tmpMap.board[row][col] = -1
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol + 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            for hider in self.hiderPosition:
                if hider[0] == seekerRow + 1 and hider[1] == seekerCol + 1:
                    tmpBoard[hider[0]][hider[1]] = -1
                    tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow + 1][seekerCol + 1] = tmpBoard[seekerRow + 1][seekerCol + 1], tmpBoard[seekerRow][seekerCol]
                    hider[0] = -10
                    hider[1] = -10
                    resMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
                    return resMap
            tmpBoard[seekerRow + 1][seekerCol + 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
            tmpMap.getVision()
            for row in range(maxRow):
                for col in range(maxCol):
                    if tmpMap.board[row][col] == 20:
                        tmpMap.board[row][col] = -1
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            for hider in self.hiderPosition:
                if hider[0] == seekerRow + 1 and hider[1] == seekerCol:
                    tmpBoard[hider[0]][hider[1]] = -1
                    tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow + 1][seekerCol] = tmpBoard[seekerRow + 1][seekerCol], tmpBoard[seekerRow][seekerCol]
                    hider[0] = -10
                    hider[1] = -10
                    resMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
                    return resMap
            tmpBoard[seekerRow + 1][seekerCol] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
            tmpMap.getVision()
            for row in range(maxRow):
                for col in range(maxCol):
                    if tmpMap.board[row][col] == 20:
                        tmpMap.board[row][col] = -1
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow + 1, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            for hider in self.hiderPosition:
                if hider[0] == seekerRow + 1 and hider[1] == seekerCol - 1:
                    tmpBoard[hider[0]][hider[1]] = -1
                    tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow + 1][seekerCol - 1] = tmpBoard[seekerRow + 1][seekerCol - 1], tmpBoard[seekerRow][seekerCol]
                    hider[0] = -10
                    hider[1] = -10
                    resMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
                    return resMap
            tmpBoard[seekerRow + 1][seekerCol - 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
            tmpMap.getVision()
            for row in range(maxRow):
                for col in range(maxCol):
                    if tmpMap.board[row][col] == 20:
                        tmpMap.board[row][col] = -1
            newMap.append(tmpMap)
        
        if not checkUnValidCell(seekerRow, seekerCol - 1, self.board, maxRow, maxCol):
            tmpBoard = [row[:] for row in self.board]
            for hider in self.hiderPosition:
                if hider[0] == seekerRow and hider[1] == seekerCol - 1:
                    tmpBoard[hider[0]][hider[1]] = -1
                    tmpBoard[seekerRow][seekerCol], tmpBoard[seekerRow][seekerCol - 1] = tmpBoard[seekerRow][seekerCol - 1], tmpBoard[seekerRow][seekerCol]
                    hider[0] = -10
                    hider[1] = -10
                    resMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
                    return resMap
            tmpBoard[seekerRow][seekerCol - 1] = 3
            tmpBoard[seekerRow][seekerCol] = -1
            tmpMap = Map(tmpBoard, maxRow, maxCol, 0, None, self.step + 1)
            tmpMap.getVision()
            for row in range(maxRow):
                for col in range(maxCol):
                    if tmpMap.board[row][col] == 20:
                        tmpMap.board[row][col] = -1
            newMap.append(tmpMap)
        
        # for i in range(len(newMap)):
        #     newMap[i].weight = calc_value_smaller_20(newMap[i].board, maxRow, maxCol)
        
        pos = 0
        max = newMap[0].weight
        for i in range(1, len(newMap)):
            if newMap[i].weight > max:
                max = newMap[i].weight
                pos = i

        newMaxMap = []
        for i in range(len(newMap)):
            if newMap[i].weight == max:
                newMaxMap.append(newMap[i])

        if len(newMaxMap) == 1:
            return newMaxMap[0]
        else:
            # Move randomly
            pos = random.randint(0, len(newMaxMap) - 1)
            return newMaxMap[pos]
    
    #Return cái Path, nếu mà k có Path thì return none.
    def A_Star(self, goalRow, goalCol):
        path = []

        if self.seekerPosition[0] == goalRow and self.seekerPosition[1] == goalCol:
            return path
        
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
                    while state != None:
                        path.append(state)
                        state = state.parent
                    # path.append(self)
                    path.reverse()
                    return path
                
                if tuple(state.seekerPosition) in visited:
                    continue
                
                state.parent = cur
                priorityValue = state.weight + findDiagonalDistance(state.seekerPosition[0], state.seekerPosition[1], goalRow, goalCol)
                newElement = PriorityQueueElement(priorityValue, state)
                heapq.heappush(queue, newElement)
                visited.add(tuple(state.seekerPosition))
                
        return None
    
    def chooseAnnouncePos(self, pos):
        while True:
            while True:
                randomRow = random.randint(pos[0] - 2, pos[0] + 2)
                if randomRow < 0 or randomRow >= self.row:
                    continue
                break
            
            while True:
                randomCol = random.randint(pos[1] - 2, pos[1] + 2)
                if randomCol < 0 or randomCol >= self.col or (randomRow == pos[0] and randomCol == pos[1]):
                    continue
                break

            if self.board[randomRow][randomCol] % 20 != 2 and self.board[randomRow][randomCol] % 20 != 4 and self.board[randomRow][randomCol] != 1:
                break
        
        return (randomRow, randomCol)

    def findHider(self, hiderPos1):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] % 20 == 2:
                    hiderPos1.append((i, j))

    def createAnnounce(self, step, tmpValue, tmpPos):
        if step % 5 == 0:
            hiderPos1 = []
            tmpPos.clear()
            self.findHider(hiderPos1)   
            for i in range(len(hiderPos1)):
                tmpPos.append(self.chooseAnnouncePos(hiderPos1[i]))
                tmpValue.append(self.board[tmpPos[i][0]][tmpPos[i][1]])
                self.board[tmpPos[i][0]][tmpPos[i][1]] = 24 if self.board[tmpPos[i][0]][tmpPos[i][1]] >= 10 else 4
        
        else:
            for i in range(len(tmpPos)):
                self.board[tmpPos[i][0]][tmpPos[i][1]] = 24 if self.board[tmpPos[i][0]][tmpPos[i][1]] >= 10 else 4