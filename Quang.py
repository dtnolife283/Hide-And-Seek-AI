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
    return findNumberOfWallAround(goal_row, goal_col, board, ROW, COL) * max(ROW, COL) // 16 - findDiagonalDistance(cur_row,cur_col, goal_row, goal_col)


def findManhattanDistance(cur_row, cur_col, goal_row, goal_col):
    return abs(cur_row - goal_row) + abs(cur_col - goal_col)

class PriorityQueueElement:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other: 'PriorityQueueElement'):
        return self.priority < other.priority


class Map:
    # constructor
    def __init__(self, board, row, col, weight, parent):  
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        return newMap

    def localSearch(self):
        des = []
        if self.checkHider(des):
            path = self.A_Star(des[0], des[1])
            return path, True
        seekerRow = self.seekerPosition[0]
        seekerCol = self.seekerPosition[1]
        tmpBoard = self.board.copy()
        
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

        curVal = count_20(self.board, self.row, self.col)
        newMap = self.moveSeeker()
        newVal = []
        for state in newMap:
            state.getVision()
            newVal.append(count_20(state.board, state.row, state.col))
        if curVal >= max(newVal):
            return None, False
        return newMap[newVal.index(max(newVal))], False
    
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
            for i in range(len(tmpPos)):
                self.board[tmpPos[i][0]][tmpPos[i][1]] = 19 if self.board[tmpPos[i][0]][tmpPos[i][1]] >= 10 else 0
            tmpPos.clear()
            tmpValue.clear()
            self.findHider(hiderPos1)   
            for i in range(len(hiderPos1)):
                tmpPos.append(self.chooseAnnouncePos(hiderPos1[i]))
                tmpValue.append(self.board[tmpPos[i][0]][tmpPos[i][1]])
                self.board[tmpPos[i][0]][tmpPos[i][1]] = 24 if self.board[tmpPos[i][0]][tmpPos[i][1]] >= 10 else 4
        
        else:
            for i in range(len(tmpPos)):
                self.board[tmpPos[i][0]][tmpPos[i][1]] = 24 if self.board[tmpPos[i][0]][tmpPos[i][1]] >= 10 else 4


    def moveHider (self, Pos):
        direction = [[0,0],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        i = random.randint(0, 8)
        newHiderRow = direction[i][0] + Pos[0]
        newHiderCol = direction[i][1] + Pos[1]
        while (newHiderRow < 0 or newHiderCol < 0 or newHiderRow >= self.row or newHiderCol >= self.col or self.board[newHiderRow][newHiderCol] == 1):
            i = random.randint(0, 7)
            newHiderRow = direction[i][0] + Pos[0]
            newHiderCol = direction[i][1] + Pos[1]
        Pos[0] = newHiderRow
        Pos[1] = newHiderCol

def count_20(board, row, col):
    count = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] >= 10 or board[i][j] == -1:
                count += 1
    return count




class Map2:
    # constructor
    def __init__(self, board, row, col, weight, parent):  
        self.board = [row[:] for row in board]
        self.row = row
        self.col = col
        self.weight = weight
        self.visited = 0
        seekerRow = 0
        seekerCol = 0
        for i in range (row):
            for j in range (col):
                if (self.board[i][j] == 3):
                    seekerRow = i
                    seekerCol = j
        self.seekerPosition = [seekerRow, seekerCol]

        for i in range (row):
            for j in range (col):
                if (self.board[i][j] == 2):
                    self.board[i][j] = 0
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
                if self.board[i][j] == 2:
                    des.append(i)
                    des.append(j)
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
            tmpMap = Map2(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map2(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map2(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map2(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map2(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map2(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map2(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
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
            tmpMap = Map2(tmpBoard, maxRow, maxCol, self.weight + increaseWeight, self)
            newMap.append(tmpMap)
        return newMap

    def moveSeeker2(self, hiderPos: list):
        newMap = []
        move = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        seekerRow = self.seekerPosition[0]
        seekerCol = self.seekerPosition[1]
        for i in move:
            tmpBoard = [row[:] for row in self.board]
            newRow = seekerRow + i[0]
            newCol = seekerCol + i[1]
            if not checkUnValidCell(newRow, newCol, tmpBoard, self.row, self.col):
                for i in range (newRow - 3, newRow + 4):
                    if i < 0 or i >= self.row:
                        continue
                    for j in range (newCol - 3, newCol + 4):
                        if j < 0 or j >= self.col:
                            continue
                        if tmpBoard[i][j] % 20 == 2:
                            tmpBoard[i][j] = -1
                        if tmpBoard[i][j] == 19 or tmpBoard[i][j] == 20:
                            tmpBoard[i][j] = -1
                tmpBoard[newRow][newCol] = 3
                tmpBoard[seekerRow][seekerCol] = -1
                weight = findManhattanDistance(newRow, newCol, hiderPos[0], hiderPos[1])
                tmpMap = Map2(tmpBoard, self.row, self.col, weight, self)
                newMap.append(tmpMap)
        min = newMap[0]
        for i in newMap:
            if i.weight < min.weight:
                min = i
        return min


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
    
    

def moveHider (map: Map, Pos):
    direction = [[0,0],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    i = random.randint(0, 8)
    newHiderRow = direction[i][0] + Pos[0]
    newHiderCol = direction[i][1] + Pos[1]
    while (newHiderRow < 0 or newHiderCol < 0 or newHiderRow >= map.row or newHiderCol >= map.col or map.board[newHiderRow][newHiderCol] == 1):
        i = random.randint(0, 7)
        newHiderRow = direction[i][0] + Pos[0]
        newHiderCol = direction[i][1] + Pos[1]
    Pos[0] = newHiderRow
    Pos[1] = newHiderCol
