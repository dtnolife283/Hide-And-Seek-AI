import os

def calculate_vision(matrix, seeker_or_hider, vision_range):
    tmpMatrix = [row[:] for row in matrix]  # Create a copy of the original matrix

    found = False
    for row in matrix:
        for cell in row:
            if cell == seeker_or_hider:
                seeker_row = matrix.index(row)
                seeker_col = row.index(cell)
                found = True
                break
        if found:
            break
    
    start_vision_row = max(0, seeker_row - vision_range)
    end_vision_row = min(len(matrix), seeker_row + vision_range + 1)

    start_vision_col = max(0, seeker_col - vision_range)
    end_vision_col = min(len(matrix[0]), seeker_col + vision_range + 1)

    NORTH_LVI = (seeker_row - 1, seeker_col) if seeker_row - 1 >= 0 else None
    SOUTH_LVI = (seeker_row + 1, seeker_col) if seeker_row + 1 < len(matrix) else None
    EAST_LVI = (seeker_row, seeker_col + 1) if seeker_col + 1 < len(matrix[0]) else None
    WEST_LVI = (seeker_row, seeker_col - 1) if seeker_col - 1 >= 0 else None
    NORTHEAST_LVI = (seeker_row - 1, seeker_col + 1) if seeker_row - 1 >= 0 and seeker_col + 1 < len(matrix[0]) else None
    NORTHWEST_LVI = (seeker_row - 1, seeker_col - 1) if seeker_row - 1 >= 0 and seeker_col - 1 >= 0 else None
    SOUTHEAST_LVI = (seeker_row + 1, seeker_col + 1) if seeker_row + 1 < len(matrix) and seeker_col + 1 < len(matrix[0]) else None
    SOUTHWEST_LVI = (seeker_row + 1, seeker_col - 1) if seeker_row + 1 < len(matrix) and seeker_col - 1 >= 0 else None

    NORTH_LVII = (seeker_row - 2, seeker_col) if seeker_row - 2 >= 0 else None
    SOUTH_LVII = (seeker_row + 2, seeker_col) if seeker_row + 2 < len(matrix) else None
    EAST_LVII = (seeker_row, seeker_col + 2) if seeker_col + 2 < len(matrix[0]) else None
    WEST_LVII = (seeker_row, seeker_col - 2) if seeker_col - 2 >= 0 else None
    NORTHEAST_LVII = (seeker_row - 2, seeker_col + 2) if seeker_row - 2 >= 0 and seeker_col + 2 < len(matrix[0]) else None
    NORTHWEST_LVII = (seeker_row - 2, seeker_col - 2) if seeker_row - 2 >= 0 and seeker_col - 2 >= 0 else None
    SOUTHEAST_LVII = (seeker_row + 2, seeker_col + 2) if seeker_row + 2 < len(matrix) and seeker_col + 2 < len(matrix[0]) else None
    SOUTHWEST_LVII = (seeker_row + 2, seeker_col - 2) if seeker_row + 2 < len(matrix) and seeker_col - 2 >= 0 else None
    NORTH_LVII_LEFT = (seeker_row - 2, seeker_col - 1) if seeker_row - 2 >= 0 and seeker_col - 1 >= 0 else None
    NORTH_LVII_RIGHT = (seeker_row - 2, seeker_col + 1) if seeker_row - 2 >= 0 and seeker_col + 1 < len(matrix[0]) else None
    SOUTH_LVII_LEFT = (seeker_row + 2, seeker_col - 1) if seeker_row + 2 < len(matrix) and seeker_col - 1 >= 0 else None
    SOUTH_LVII_RIGHT = (seeker_row + 2, seeker_col + 1) if seeker_row + 2 < len(matrix) and seeker_col + 1 < len(matrix[0]) else None
    EAST_LVII_UP = (seeker_row - 1, seeker_col + 2) if seeker_row - 1 >= 0 and seeker_col + 2 < len(matrix[0]) else None
    EAST_LVII_DOWN = (seeker_row + 1, seeker_col + 2) if seeker_row + 1 < len(matrix) and seeker_col + 2 < len(matrix[0]) else None
    WEST_LVII_UP = (seeker_row - 1, seeker_col - 2) if seeker_row - 1 >= 0 and seeker_col - 2 >= 0 else None
    WEST_LVII_DOWN = (seeker_row + 1, seeker_col - 2) if seeker_row + 1 < len(matrix) and seeker_col - 2 >= 0 else None

    if NORTHWEST_LVI:
        if tmpMatrix[NORTHWEST_LVI[0]][NORTHWEST_LVI[1]] == 1:
            for i in range(start_vision_row, NORTHWEST_LVI[0]):
                for j in range(start_vision_col, NORTHWEST_LVI[1]):
                    tmpMatrix[i][j] = -1
        else:
            if NORTHWEST_LVII:
                if tmpMatrix[NORTHWEST_LVII[0]][NORTHWEST_LVII[1]] == 1:
                    for i in range(start_vision_row, NORTHWEST_LVII[0]):
                        for j in range(start_vision_col, NORTHWEST_LVII[1]):
                            tmpMatrix[i][j] = -1
    
    if NORTH_LVI:
        if tmpMatrix[NORTH_LVI[0]][NORTH_LVI[1]] == 1:
            for i in range(start_vision_row, NORTH_LVI[0]):
                tmpMatrix[i][seeker_col] = -1
        else:
            if NORTH_LVII:
                if tmpMatrix[NORTH_LVII[0]][NORTH_LVII[1]] == 1:
                    for i in range(start_vision_row, NORTH_LVII[0]):
                        tmpMatrix[i][seeker_col] = -1
    
    if NORTHEAST_LVI:
        if tmpMatrix[NORTHEAST_LVI[0]][NORTHEAST_LVI[1]] == 1:
            for i in range(start_vision_row, NORTHEAST_LVI[0]):
                for j in range(seeker_col + 1, end_vision_col):
                    tmpMatrix[i][j] = -1
        else:
            if NORTHEAST_LVII:
                if tmpMatrix[NORTHEAST_LVII[0]][NORTHEAST_LVII[1]] == 1:
                    for i in range(start_vision_row, NORTHEAST_LVII[0]):
                        for j in range(seeker_col + 1, end_vision_col):
                            tmpMatrix[i][j] = -1

    if EAST_LVI:
        if tmpMatrix[EAST_LVI[0]][EAST_LVI[1]] == 1:
            for j in range(seeker_col + 1, end_vision_col):
                tmpMatrix[seeker_row][j] = -1
        else:
            if EAST_LVII:
                if tmpMatrix[EAST_LVII[0]][EAST_LVII[1]] == 1:
                    for j in range(seeker_col + 1, end_vision_col):
                        tmpMatrix[seeker_row][j] = -1
    
    if SOUTHEAST_LVI:
        if tmpMatrix[SOUTHEAST_LVI[0]][SOUTHEAST_LVI[1]] == 1:
            for i in range(seeker_row + 1, end_vision_row):
                for j in range(seeker_col + 1, end_vision_col):
                    tmpMatrix[i][j] = -1
        else:
            if SOUTHEAST_LVII:
                if tmpMatrix[SOUTHEAST_LVII[0]][SOUTHEAST_LVII[1]] == 1:
                    for i in range(seeker_row + 1, end_vision_row):
                        for j in range(seeker_col + 1, end_vision_col):
                            tmpMatrix[i][j] = -1
    
    if SOUTH_LVI:
        if tmpMatrix[SOUTH_LVI[0]][SOUTH_LVI[1]] == 1:
            for i in range(seeker_row + 1, end_vision_row):
                tmpMatrix[i][seeker_col] = -1
        else:
            if SOUTH_LVII:
                if tmpMatrix[SOUTH_LVII[0]][SOUTH_LVII[1]] == 1:
                    for i in range(seeker_row + 1, end_vision_row):
                        tmpMatrix[i][seeker_col] = -1
    
    if SOUTHWEST_LVI:
        if tmpMatrix[SOUTHWEST_LVI[0]][SOUTHWEST_LVI[1]] == 1:
            for i in range(seeker_row + 1, end_vision_row):
                for j in range(start_vision_col, SOUTHWEST_LVI[1]):
                    tmpMatrix[i][j] = -1
        else:
            if SOUTHWEST_LVII:
                if tmpMatrix[SOUTHWEST_LVII[0]][SOUTHWEST_LVII[1]] == 1:
                    for i in range(seeker_row + 1, end_vision_row):
                        for j in range(start_vision_col, SOUTHWEST_LVII[1]):
                            tmpMatrix[i][j] = -1
    
    if WEST_LVI:
        if tmpMatrix[WEST_LVI[0]][WEST_LVI[1]] == 1:
            for j in range(start_vision_col, WEST_LVI[1]):
                tmpMatrix[seeker_row][j] = -1
        else:
            if WEST_LVII:
                if tmpMatrix[WEST_LVII[0]][WEST_LVII[1]] == 1:
                    for j in range(start_vision_col, WEST_LVII[1]):
                        tmpMatrix[seeker_row][j] = -1

    if NORTH_LVII_LEFT:
        if tmpMatrix[NORTH_LVII_LEFT[0]][NORTH_LVII_LEFT[1]] == 1:
            if NORTH_LVII_LEFT[0] - 1 >= 0 and NORTH_LVII_LEFT[1] - 1 >= 0:
                tmpMatrix[NORTH_LVII_LEFT[0] - 1][NORTH_LVII_LEFT[1] - 1] = -1
                tmpMatrix[NORTH_LVII_LEFT[0] - 1][NORTH_LVII_LEFT[1]] = -1
    
    if NORTH_LVII_RIGHT:
        if tmpMatrix[NORTH_LVII_RIGHT[0]][NORTH_LVII_RIGHT[1]] == 1:
            if NORTH_LVII_RIGHT[0] - 1 >= 0 and NORTH_LVII_RIGHT[1] + 1 < len(matrix[0]):
                tmpMatrix[NORTH_LVII_RIGHT[0] - 1][NORTH_LVII_RIGHT[1] + 1] = -1
                tmpMatrix[NORTH_LVII_RIGHT[0] - 1][NORTH_LVII_RIGHT[1]] = -1
    
    if SOUTH_LVII_LEFT:
        if tmpMatrix[SOUTH_LVII_LEFT[0]][SOUTH_LVII_LEFT[1]] == 1:
            if SOUTH_LVII_LEFT[0] + 1 < len(matrix) and SOUTH_LVII_LEFT[1] - 1 >= 0:
                tmpMatrix[SOUTH_LVII_LEFT[0] + 1][SOUTH_LVII_LEFT[1] - 1] = -1
                tmpMatrix[SOUTH_LVII_LEFT[0] + 1][SOUTH_LVII_LEFT[1]] = -1
    
    if SOUTH_LVII_RIGHT:
        if tmpMatrix[SOUTH_LVII_RIGHT[0]][SOUTH_LVII_RIGHT[1]] == 1:
            if SOUTH_LVII_RIGHT[0] + 1 < len(matrix) and SOUTH_LVII_RIGHT[1] + 1 < len(matrix[0]):
                tmpMatrix[SOUTH_LVII_RIGHT[0] + 1][SOUTH_LVII_RIGHT[1] + 1] = -1
                tmpMatrix[SOUTH_LVII_RIGHT[0] + 1][SOUTH_LVII_RIGHT[1]] = -1
    
    if EAST_LVII_UP:
        if tmpMatrix[EAST_LVII_UP[0]][EAST_LVII_UP[1]] == 1:
            if EAST_LVII_UP[0] - 1 >= 0 and EAST_LVII_UP[1] + 1 < len(matrix[0]):
                tmpMatrix[EAST_LVII_UP[0] - 1][EAST_LVII_UP[1] + 1] = -1
                tmpMatrix[EAST_LVII_UP[0]][EAST_LVII_UP[1] + 1] = -1
    
    if EAST_LVII_DOWN:
        if tmpMatrix[EAST_LVII_DOWN[0]][EAST_LVII_DOWN[1]] == 1:
            if EAST_LVII_DOWN[0] + 1 < len(matrix) and EAST_LVII_DOWN[1] + 1 < len(matrix[0]):
                tmpMatrix[EAST_LVII_DOWN[0] + 1][EAST_LVII_DOWN[1] + 1] = -1
                tmpMatrix[EAST_LVII_DOWN[0]][EAST_LVII_DOWN[1] + 1] = -1
    
    if WEST_LVII_UP:
        if tmpMatrix[WEST_LVII_UP[0]][WEST_LVII_UP[1]] == 1:
            if WEST_LVII_UP[0] - 1 >= 0 and WEST_LVII_UP[1] - 1 >= 0:
                tmpMatrix[WEST_LVII_UP[0] - 1][WEST_LVII_UP[1] - 1] = -1
                tmpMatrix[WEST_LVII_UP[0]][WEST_LVII_UP[1] - 1] = -1
    
    if WEST_LVII_DOWN:
        if tmpMatrix[WEST_LVII_DOWN[0]][WEST_LVII_DOWN[1]] == 1:
            if WEST_LVII_DOWN[0] + 1 < len(matrix) and WEST_LVII_DOWN[1] - 1 >= 0:
                tmpMatrix[WEST_LVII_DOWN[0] + 1][WEST_LVII_DOWN[1] - 1] = -1
                tmpMatrix[WEST_LVII_DOWN[0]][WEST_LVII_DOWN[1] - 1] = -1
    

    updated_matrix = [row[:] for row in matrix]
    for i in range(start_vision_row, end_vision_row):
        for j in range(start_vision_col, end_vision_col):
            if tmpMatrix[i][j] == -1 or tmpMatrix[i][j] == 1:
                continue
            elif tmpMatrix[i][j] == seeker_or_hider:
                updated_matrix[i][j] = seeker_or_hider
            else:
                updated_matrix[i][j] = 10
    return updated_matrix


def read_matrix(file_txt):
    with open(file_txt, 'r') as file:
        HEIGHT, WIDTH = map(int, file.readline().split())
        matrix = []
        for _ in range(HEIGHT):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
    return matrix, HEIGHT, WIDTH


directory = "MAP"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, directory)
file_path = os.path.join(file_path, "2+ HIDERS")
files = [file for file in os.listdir(file_path) if file.endswith('.txt')]

for file in files:
    file_path = os.path.join(file_path, file)
    matrix, HEIGHT, WIDTH = read_matrix(file_path)
    vision_matrix = calculate_vision(matrix, 3, 3)

for row in vision_matrix:
    for cell in row:
        print(cell, end=' ')
    print()