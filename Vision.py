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

    top_length = seeker_row - start_vision_row
    bottom_length = end_vision_row - seeker_row - 1
    left_length = seeker_col - start_vision_col
    right_length = end_vision_col - seeker_col - 1

    NORTHEAST_LVI = (seeker_row - 1, seeker_col + 1) if seeker_row - 1 >= 0 and seeker_col + 1 < len(matrix[0]) else None
    NORTHWEST_LVI = (seeker_row - 1, seeker_col - 1) if seeker_row - 1 >= 0 and seeker_col - 1 >= 0 else None
    SOUTHEAST_LVI = (seeker_row + 1, seeker_col + 1) if seeker_row + 1 < len(matrix) and seeker_col + 1 < len(matrix[0]) else None
    SOUTHWEST_LVI = (seeker_row + 1, seeker_col - 1) if seeker_row + 1 < len(matrix) and seeker_col - 1 >= 0 else None

    NORTHEAST_LVII = (seeker_row - 2, seeker_col + 2) if seeker_row - 2 >= 0 and seeker_col + 2 < len(matrix[0]) else None
    NORTHWEST_LVII = (seeker_row - 2, seeker_col - 2) if seeker_row - 2 >= 0 and seeker_col - 2 >= 0 else None
    SOUTHEAST_LVII = (seeker_row + 2, seeker_col + 2) if seeker_row + 2 < len(matrix) and seeker_col + 2 < len(matrix[0]) else None
    SOUTHWEST_LVII = (seeker_row + 2, seeker_col - 2) if seeker_row + 2 < len(matrix) and seeker_col - 2 >= 0 else None

    if NORTHWEST_LVI:
        if tmpMatrix[NORTHWEST_LVI[0]][NORTHWEST_LVI[1]] == 1:
            row_seen = True
            col_seen = True
            if tmpMatrix[NORTHWEST_LVI[0] + 1][NORTHWEST_LVI[1]] == 1:
                col_seen = False
            if tmpMatrix[NORTHWEST_LVI[0]][NORTHWEST_LVI[1] + 1] == 1:
                row_seen = False
            if row_seen and col_seen:
                for i in range(start_vision_row, NORTHWEST_LVI[0]):
                    for j in range(start_vision_col, NORTHWEST_LVI[1]):
                        tmpMatrix[i][j] = -1
            elif row_seen and (not col_seen):
                for i in range(start_vision_row, NORTHWEST_LVI[0]):
                    for j in range(start_vision_col, NORTHWEST_LVI[1] + 1):
                        tmpMatrix[i][j] = -1
            elif (not row_seen) and col_seen:
                for i in range(start_vision_row, NORTHWEST_LVI[0] + 1):
                    for j in range(start_vision_col, NORTHWEST_LVI[1]):
                        tmpMatrix[i][j] = -1
            else:
                for i in range(start_vision_row, NORTHWEST_LVI[0] + 1):
                    for j in range(start_vision_col, NORTHWEST_LVI[1] + 1):
                        tmpMatrix[i][j] = -1
        else:
            if NORTHWEST_LVII:
                if tmpMatrix[NORTHWEST_LVII[0]][NORTHWEST_LVII[1]] == 1:
                    row_seen = True
                    col_seen = True
                    if tmpMatrix[NORTHWEST_LVII[0] + 1][NORTHWEST_LVII[1]] == 1:
                        col_seen = False
                    if tmpMatrix[NORTHWEST_LVII[0]][NORTHWEST_LVII[1] + 1] == 1:
                        row_seen = False
                    if row_seen and col_seen:
                        for i in range(start_vision_row, NORTHWEST_LVII[0]):
                            for j in range(start_vision_col, NORTHWEST_LVII[1]):
                                tmpMatrix[i][j] = -1
                    elif row_seen and (not col_seen):
                        for i in range(start_vision_row, NORTHWEST_LVII[0]):
                            for j in range(start_vision_col, NORTHWEST_LVII[1] + 1):
                                tmpMatrix[i][j] = -1
                    elif (not row_seen) and col_seen:
                        for i in range(start_vision_row, NORTHWEST_LVII[0] + 1):
                            for j in range(start_vision_col, NORTHWEST_LVII[1]):
                                tmpMatrix[i][j] = -1
                    else:
                        for i in range(start_vision_row, NORTHWEST_LVII[0] + 1):
                            for j in range(start_vision_col, NORTHWEST_LVII[1] + 1):
                                tmpMatrix[i][j] = -1


    if NORTHEAST_LVI:
        if tmpMatrix[NORTHEAST_LVI[0]][NORTHEAST_LVI[1]] == 1:
            row_seen = True
            col_seen = True
            if tmpMatrix[NORTHEAST_LVI[0] + 1][NORTHEAST_LVI[1]] == 1:
                row_seen = False
            if tmpMatrix[NORTHEAST_LVI[0]][NORTHEAST_LVI[1] - 1] == 1:
                col_seen = False
            if row_seen and col_seen:
                for i in range(start_vision_row, NORTHEAST_LVI[0]):
                    for j in range(NORTHEAST_LVI[1] + 1, end_vision_col):
                        tmpMatrix[i][j] = -1
            elif row_seen and (not col_seen):
                for i in range(start_vision_row, NORTHEAST_LVI[0]):
                    for j in range(NORTHEAST_LVI[1], end_vision_col):
                        tmpMatrix[i][j] = -1
            elif (not row_seen) and col_seen:
                for i in range(start_vision_row, NORTHEAST_LVI[0] + 1):
                    for j in range(NORTHEAST_LVI[1] + 1, end_vision_col):
                        tmpMatrix[i][j] = -1
            else:
                for i in range(start_vision_row, NORTHEAST_LVI[0] + 1):
                    for j in range(NORTHEAST_LVI[1], end_vision_col):
                        tmpMatrix[i][j] = -1
        else:
            if NORTHEAST_LVII:
                if tmpMatrix[NORTHEAST_LVII[0]][NORTHEAST_LVII[1]] == 1:
                    row_seen = True
                    col_seen = True
                    if tmpMatrix[NORTHEAST_LVII[0] + 1][NORTHEAST_LVII[1]] == 1:
                        col_seen = False
                    if tmpMatrix[NORTHEAST_LVII[0]][NORTHEAST_LVII[1] - 1] == 1:
                        row_seen = False
                    if row_seen and col_seen:
                        for i in range(start_vision_row, NORTHEAST_LVII[0]):
                            for j in range(NORTHEAST_LVII[1] + 1, end_vision_col):
                                tmpMatrix[i][j] = -1
                    elif row_seen and (not col_seen):
                        for i in range(start_vision_row, NORTHEAST_LVII[0]):
                            for j in range(NORTHEAST_LVII[1], end_vision_col):
                                tmpMatrix[i][j] = -1
                    elif (not row_seen) and col_seen:
                        for i in range(start_vision_row, NORTHEAST_LVII[0] + 1):
                            for j in range(NORTHEAST_LVII[1] + 1, end_vision_col):
                                tmpMatrix[i][j] = -1
                    else:
                        for i in range(start_vision_row, NORTHEAST_LVII[0] + 1):
                            for j in range(NORTHEAST_LVII[1], end_vision_col):
                                tmpMatrix[i][j] = -1
    
    if SOUTHEAST_LVI:
        if tmpMatrix[SOUTHEAST_LVI[0]][SOUTHEAST_LVI[1]] == 1:
            row_seen = True
            col_seen = True
            if tmpMatrix[SOUTHEAST_LVI[0] - 1][SOUTHEAST_LVI[1]] == 1:
                row_seen = False
            if tmpMatrix[SOUTHEAST_LVI[0]][SOUTHEAST_LVI[1] - 1] == 1:
                col_seen = False
            if row_seen and col_seen:
                for i in range(SOUTHEAST_LVI[0] + 1, end_vision_row):
                    for j in range(SOUTHEAST_LVI[1] + 1, end_vision_col):
                        tmpMatrix[i][j] = -1
            elif row_seen and (not col_seen):
                for i in range(SOUTHEAST_LVI[0] + 1, end_vision_row):
                    for j in range(SOUTHEAST_LVI[1], end_vision_col):
                        tmpMatrix[i][j] = -1    
            elif (not row_seen) and col_seen:
                for i in range(SOUTHEAST_LVI[0], end_vision_row):
                    for j in range(SOUTHEAST_LVI[1] + 1, end_vision_col):
                        tmpMatrix[i][j] = -1
            else:
                for i in range(SOUTHEAST_LVI[0], end_vision_row):
                    for j in range(SOUTHEAST_LVI[1], end_vision_col):
                        tmpMatrix[i][j] = -1
        else:
            if SOUTHEAST_LVII:
                if tmpMatrix[SOUTHEAST_LVII[0]][SOUTHEAST_LVII[1]] == 1:
                    row_seen = True
                    col_seen = True
                    if tmpMatrix[SOUTHEAST_LVII[0] - 1][SOUTHEAST_LVII[1]] == 1:
                        row_seen = False
                    if tmpMatrix[SOUTHEAST_LVII[0]][SOUTHEAST_LVII[1] - 1] == 1:
                        col_seen = False
                    if row_seen and col_seen:
                        for i in range(SOUTHEAST_LVII[0] + 1, end_vision_row):
                            for j in range(SOUTHEAST_LVII[1] + 1, end_vision_col):
                                tmpMatrix[i][j] = -1
                    elif row_seen and (not col_seen):
                        for i in range(SOUTHEAST_LVII[0] + 1, end_vision_row):
                            for j in range(SOUTHEAST_LVII[1], end_vision_col):
                                tmpMatrix[i][j] = -1    
                    elif (not row_seen) and col_seen:
                        for i in range(SOUTHEAST_LVII[0], end_vision_row):
                            for j in range(SOUTHEAST_LVII[1] + 1, end_vision_col):
                                tmpMatrix[i][j] = -1
                    else:
                        for i in range(SOUTHEAST_LVII[0], end_vision_row):
                            for j in range(SOUTHEAST_LVII[1], end_vision_col):
                                tmpMatrix[i][j] = -1
    
    if SOUTHWEST_LVI:
        if tmpMatrix[SOUTHWEST_LVI[0]][SOUTHWEST_LVI[1]] == 1:
            row_seen = True
            col_seen = True
            if tmpMatrix[SOUTHWEST_LVI[0] - 1][SOUTHWEST_LVI[1]] == 1:
                row_seen = False
            if tmpMatrix[SOUTHWEST_LVI[0]][SOUTHWEST_LVI[1] + 1] == 1:
                col_seen = False
            if row_seen and col_seen:
                for i in range(SOUTHWEST_LVI[0] + 1, end_vision_row):
                    for j in range(start_vision_col, SOUTHWEST_LVI[1]):
                        tmpMatrix[i][j] = -1
            elif row_seen and (not col_seen):
                for i in range(SOUTHWEST_LVI[0] + 1, end_vision_row):
                    for j in range(start_vision_col, SOUTHWEST_LVI[1] + 1):
                        tmpMatrix[i][j] = -1
            elif (not row_seen) and col_seen:
                for i in range(SOUTHWEST_LVI[0], end_vision_row):
                    for j in range(start_vision_col, SOUTHWEST_LVI[1]):
                        tmpMatrix[i][j] = -1
            else:
                for i in range(SOUTHWEST_LVI[0], end_vision_row):
                    for j in range(start_vision_col, SOUTHWEST_LVI[1] + 1):
                        tmpMatrix[i][j] = -1
        else:
            if SOUTHWEST_LVII:
                if tmpMatrix[SOUTHWEST_LVII[0]][SOUTHWEST_LVII[1]] == 1:
                    row_seen = True
                    col_seen = True
                    if tmpMatrix[SOUTHWEST_LVII[0] - 1][SOUTHWEST_LVII[1]] == 1:
                        row_seen = False
                    if tmpMatrix[SOUTHWEST_LVII[0]][SOUTHWEST_LVII[1] + 1] == 1:
                        col_seen = False
                    if row_seen and col_seen:
                        for i in range(SOUTHWEST_LVII[0] + 1, end_vision_row):
                            for j in range(start_vision_col, SOUTHWEST_LVII[1]):
                                tmpMatrix[i][j] = -1

    if top_length == 3:
        NORTH_LVI = (seeker_row - 1, seeker_col)
        if tmpMatrix[NORTH_LVI[0]][NORTH_LVI[1]] == 1:
            tmpMatrix[NORTH_LVI[0] - 1][NORTH_LVI[1]] = -1
            tmpMatrix[NORTH_LVI[0] - 2][NORTH_LVI[1]] = -1
            if left_length >= 1:
                tmpMatrix[NORTH_LVI[0] - 2][NORTH_LVI[1] - 1] = -1
            if right_length >= 1:
                tmpMatrix[NORTH_LVI[0] - 2][NORTH_LVI[1] + 1] = -1
        else:
            NORTH_LVII = (seeker_row - 2, seeker_col)
            if tmpMatrix[NORTH_LVII[0]][NORTH_LVII[1]] == 1:
                tmpMatrix[NORTH_LVII[0] - 1][NORTH_LVII[1]] = -1
        if left_length == 3:
            NORTH_LVII_LEFT = (seeker_row - 2, seeker_col - 1)
            if tmpMatrix[NORTH_LVII_LEFT[0]][NORTH_LVII_LEFT[1]] == 1:
                tmpMatrix[NORTH_LVII_LEFT[0] - 1][NORTH_LVII_LEFT[1]] = -1
                tmpMatrix[NORTH_LVII_LEFT[0] - 1][NORTH_LVII_LEFT[1] - 1] = -1
        if right_length == 3:
            NORTH_LVII_RIGHT = (seeker_row - 2, seeker_col + 1)
            if tmpMatrix[NORTH_LVII_RIGHT[0]][NORTH_LVII_RIGHT[1]] == 1:
                tmpMatrix[NORTH_LVII_RIGHT[0] - 1][NORTH_LVII_RIGHT[1]] = -1
                tmpMatrix[NORTH_LVII_RIGHT[0] - 1][NORTH_LVII_RIGHT[1] + 1] = -1
    elif top_length == 2:
        NORTH_LVI = (seeker_row - 1, seeker_col)
        if tmpMatrix[NORTH_LVI[0]][NORTH_LVI[1]] == 1:
            tmpMatrix[NORTH_LVI[0] - 1][NORTH_LVI[1]] = -1

    if bottom_length == 3:
        SOUTH_LVI = (seeker_row + 1, seeker_col)
        if tmpMatrix[SOUTH_LVI[0]][SOUTH_LVI[1]] == 1:
            tmpMatrix[SOUTH_LVI[0] + 1][SOUTH_LVI[1]] = -1
            tmpMatrix[SOUTH_LVI[0] + 2][SOUTH_LVI[1]] = -1
            if left_length >= 1:
                tmpMatrix[SOUTH_LVI[0] + 2][SOUTH_LVI[1] - 1] = -1
            if right_length >= 1:
                tmpMatrix[SOUTH_LVI[0] + 2][SOUTH_LVI[1] + 1] = -1
        else:
            SOUTH_LVII = (seeker_row + 2, seeker_col)
            if tmpMatrix[SOUTH_LVII[0]][SOUTH_LVII[1]] == 1:
                tmpMatrix[SOUTH_LVII[0] + 1][SOUTH_LVII[1]] = -1
        if left_length == 3:
            SOUTH_LVII_LEFT = (seeker_row + 2, seeker_col - 1)
            if tmpMatrix[SOUTH_LVII_LEFT[0]][SOUTH_LVII_LEFT[1]] == 1:
                tmpMatrix[SOUTH_LVII_LEFT[0] + 1][SOUTH_LVII_LEFT[1]] = -1
                tmpMatrix[SOUTH_LVII_LEFT[0] + 1][SOUTH_LVII_LEFT[1] - 1] = -1
        if right_length == 3:
            SOUTH_LVII_RIGHT = (seeker_row + 2, seeker_col + 1)
            if tmpMatrix[SOUTH_LVII_RIGHT[0]][SOUTH_LVII_RIGHT[1]] == 1:
                tmpMatrix[SOUTH_LVII_RIGHT[0] + 1][SOUTH_LVII_RIGHT[1]] = -1
                tmpMatrix[SOUTH_LVII_RIGHT[0] + 1][SOUTH_LVII_RIGHT[1] + 1] = -1
    elif bottom_length == 2:
        SOUTH_LVI = (seeker_row + 1, seeker_col)
        if tmpMatrix[SOUTH_LVI[0]][SOUTH_LVI[1]] == 1:
            tmpMatrix[SOUTH_LVI[0] + 1][SOUTH_LVI[1]] = -1
    
    if left_length == 3:
        WEST_LVI = (seeker_row, seeker_col - 1)
        if tmpMatrix[WEST_LVI[0]][WEST_LVI[1]] == 1:
            tmpMatrix[WEST_LVI[0]][WEST_LVI[1] - 1] = -1
            tmpMatrix[WEST_LVI[0]][WEST_LVI[1] - 2] = -1
            if top_length >= 1:
                tmpMatrix[WEST_LVI[0] - 1][WEST_LVI[1] - 2] = -1
            if bottom_length >= 1:
                tmpMatrix[WEST_LVI[0] + 1][WEST_LVI[1] - 2] = -1
        else:
            WEST_LVII = (seeker_row, seeker_col - 2)
            if tmpMatrix[WEST_LVII[0]][WEST_LVII[1]] == 1:
                tmpMatrix[WEST_LVII[0]][WEST_LVII[1] - 1] = -1
        if top_length == 3:
            WEST_LVII_TOP = (seeker_row - 1, seeker_col - 2)
            if tmpMatrix[WEST_LVII_TOP[0]][WEST_LVII_TOP[1]] == 1:
                tmpMatrix[WEST_LVII_TOP[0]][WEST_LVII_TOP[1] - 1] = -1
                tmpMatrix[WEST_LVII_TOP[0] - 1][WEST_LVII_TOP[1] - 1] = -1
        if bottom_length == 3:
            WEST_LVII_BOTTOM = (seeker_row + 1, seeker_col - 2)
            if tmpMatrix[WEST_LVII_BOTTOM[0]][WEST_LVII_BOTTOM[1]] == 1:
                tmpMatrix[WEST_LVII_BOTTOM[0]][WEST_LVII_BOTTOM[1] - 1] = -1
                tmpMatrix[WEST_LVII_BOTTOM[0] + 1][WEST_LVII_BOTTOM[1] - 1] = -1
    elif left_length == 2:
        WEST_LVI = (seeker_row, seeker_col - 1)
        if tmpMatrix[WEST_LVI[0]][WEST_LVI[1]] == 1:
            tmpMatrix[WEST_LVI[0]][WEST_LVI[1] - 1] = -1
    
    if right_length == 3:
        EAST_LVI = (seeker_row, seeker_col + 1)
        if tmpMatrix[EAST_LVI[0]][EAST_LVI[1]] == 1:
            tmpMatrix[EAST_LVI[0]][EAST_LVI[1] + 1] = -1
            tmpMatrix[EAST_LVI[0]][EAST_LVI[1] + 2] = -1
            if top_length >= 1:
                tmpMatrix[EAST_LVI[0] - 1][EAST_LVI[1] + 2] = -1
            if bottom_length >= 1:
                tmpMatrix[EAST_LVI[0] + 1][EAST_LVI[1] + 2] = -1
        else:
            EAST_LVII = (seeker_row, seeker_col + 2)
            if tmpMatrix[EAST_LVII[0]][EAST_LVII[1]] == 1:
                tmpMatrix[EAST_LVII[0]][EAST_LVII[1] + 1] = -1
        if top_length == 3:
            EAST_LVII_TOP = (seeker_row - 1, seeker_col + 2)
            if tmpMatrix[EAST_LVII_TOP[0]][EAST_LVII_TOP[1]] == 1:
                tmpMatrix[EAST_LVII_TOP[0]][EAST_LVII_TOP[1] + 1] = -1
                tmpMatrix[EAST_LVII_TOP[0] - 1][EAST_LVII_TOP[1] + 1] = -1
        if bottom_length == 3:
            EAST_LVII_BOTTOM = (seeker_row + 1, seeker_col + 2)
            if tmpMatrix[EAST_LVII_BOTTOM[0]][EAST_LVII_BOTTOM[1]] == 1:
                tmpMatrix[EAST_LVII_BOTTOM[0]][EAST_LVII_BOTTOM[1] + 1] = -1
                tmpMatrix[EAST_LVII_BOTTOM[0] + 1][EAST_LVII_BOTTOM[1] + 1] = -1
    elif right_length == 2:
        EAST_LVI = (seeker_row, seeker_col + 1)
        if tmpMatrix[EAST_LVI[0]][EAST_LVI[1]] == 1:
            tmpMatrix[EAST_LVI[0]][EAST_LVI[1] + 1] = -1

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