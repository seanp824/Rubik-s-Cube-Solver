def rotate_U_clockwise(cube): 
    # Rotate U face (clockwise)
    u = cube['U']
    cube['U'] = [u[6], u[3], u[0], 
                 u[7], u[4], u[1], 
                 u[8], u[5], u[2]]
    
    # Copy top rows of side faces
    f = cube['F'][:]
    b = cube['B'][:] 
    l = cube['L'][:]
    r = cube['R'][:]

    # Rotate top rows: F → R → B → L → F
    cube['F'][0:3] = r[0:3]
    cube['R'][0:3] = b[0:3]
    cube['B'][0:3] = l[0:3]
    cube['L'][0:3] = f[0:3]

def rotate_U_counterclockwise(cube): 
    # Rotate U face (counterclockwise)
    u = cube['U']
    cube['U'] = [u[2], u[5], u[8], 
                 u[1], u[4], u[7], 
                 u[0], u[3], u[6]]
    
    # Copy top rows of side faces
    f = cube['F'][:]
    b = cube['B'][:] 
    l = cube['L'][:]
    r = cube['R'][:]

    # Rotate top rows: F ← R ← B ← L ← F
    cube['F'][0:3] = l[0:3]
    cube['L'][0:3] = b[0:3]
    cube['B'][0:3] = r[0:3]
    cube['R'][0:3] = f[0:3]

def rotate_D_clockwise(cube): 
    # Rotate D face (clockwise)
    d = cube['D']
    cube['D'] = [d[6], d[3], d[0], 
                 d[7], d[4], d[1], 
                 d[8], d[5], d[2]]

    # Copy bottom rows of side faces
    f = cube['F'][:]
    b = cube['B'][:]
    l = cube['L'][:]
    r = cube['R'][:]

    # Rotate bottom rows: F → R → B → L → F
    cube['F'][6:9] = l[6:9]
    cube['L'][6:9] = b[6:9]
    cube['B'][6:9] = r[6:9]
    cube['R'][6:9] = f[6:9]

def rotate_D_counterclockwise(cube): 
    # Rotate D face (counterclockwise)
    d = cube['D']
    cube['D'] = [d[2], d[5], d[8], 
                 d[1], d[4], d[7], 
                 d[0], d[3], d[6]]

    # Copy bottom rows of side faces
    f = cube['F'][:]
    b = cube['B'][:]
    l = cube['L'][:]
    r = cube['R'][:]

    # Rotate bottom rows: F ← R ← B ← L ← F
    cube['F'][6:9] = r[6:9]
    cube['R'][6:9] = b[6:9]
    cube['B'][6:9] = l[6:9]
    cube['L'][6:9] = f[6:9]

def rotate_L_clockwise(cube):
    # Rotate L face (clockwise)
    l = cube['L']
    cube['L'] = [l[6], l[3], l[0], 
                 l[7], l[4], l[1], 
                 l[8], l[5], l[2]]

    # Copy left columns
    u = cube['U'][:]
    f = cube['F'][:]
    d = cube['D'][:]
    b = cube['B'][:]

    # Rotate left columns: U → F → D → B → U
    cube['U'][0], cube['U'][3], cube['U'][6] = b[8], b[5], b[2]
    cube['B'][8], cube['B'][5], cube['B'][2] = d[0], d[3], d[6]
    cube['D'][0], cube['D'][3], cube['D'][6] = f[0], f[3], f[6]
    cube['F'][0], cube['F'][3], cube['F'][6] = u[0], u[3], u[6]

def rotate_L_counterclockwise(cube):
    # Rotate L face (counterclockwise)
    l = cube['L']
    cube['L'] = [l[2], l[5], l[8],
                 l[1], l[4], l[7],
                 l[0], l[3], l[6]]

    # Copy left columns
    u = cube['U'][:]
    f = cube['F'][:]
    d = cube['D'][:]
    b = cube['B'][:]

    # Rotate left columns: U ← F ← D ← B ← U (B reversed)
    cube['U'][0], cube['U'][3], cube['U'][6] = f[0], f[3], f[6]
    cube['F'][0], cube['F'][3], cube['F'][6] = d[0], d[3], d[6]
    cube['D'][0], cube['D'][3], cube['D'][6] = b[8], b[5], b[2]
    cube['B'][8], cube['B'][5], cube['B'][2] = u[0], u[3], u[6]

def rotate_R_clockwise(cube):
    # Rotate R face (clockwise)
    r = cube['R']
    cube['R'] = [r[6], r[3], r[0],
                 r[7], r[4], r[1],
                 r[8], r[5], r[2]]

    # Copy right columns
    u = cube['U'][:]
    f = cube['F'][:]
    d = cube['D'][:]
    b = cube['B'][:]

    # Rotate right columns: U → F → D → B → U (B reversed)
    cube['U'][2], cube['U'][5], cube['U'][8] = f[2], f[5], f[8]
    cube['F'][2], cube['F'][5], cube['F'][8] = d[2], d[5], d[8]
    cube['D'][2], cube['D'][5], cube['D'][8] = b[6], b[3], b[0]
    cube['B'][6], cube['B'][3], cube['B'][0] = u[2], u[5], u[8]


def rotate_R_counterclockwise(cube):
    # Rotate R face (counterclockwise)
    r = cube['R']
    cube['R'] = [r[2], r[5], r[8],
                 r[1], r[4], r[7],
                 r[0], r[3], r[6]]

    # Copy right columns
    u = cube['U'][:]
    f = cube['F'][:]
    d = cube['D'][:]
    b = cube['B'][:]

    # Rotate right columns: U ← F ← D ← B ← U (B reversed)
    cube['U'][2], cube['U'][5], cube['U'][8] = b[6], b[3], b[0]
    cube['B'][6], cube['B'][3], cube['B'][0] = d[2], d[5], d[8]
    cube['D'][2], cube['D'][5], cube['D'][8] = f[2], f[5], f[8]
    cube['F'][2], cube['F'][5], cube['F'][8] = u[2], u[5], u[8]

def rotate_F_clockwise(cube):
    # Rotate F face (clockwise)
    f = cube['F']
    cube['F'] = [f[6], f[3], f[0],
                 f[7], f[4], f[1],
                 f[8], f[5], f[2]]

    # Copy affected edge stickers
    u = cube['U'][:]
    l = cube['L'][:]
    d = cube['D'][:]
    r = cube['R'][:]

    # Rotate adjacent edges: U → R → D → L → U
    cube['U'][6], cube['U'][7], cube['U'][8] = l[8], l[5], l[2]
    cube['R'][0], cube['R'][3], cube['R'][6] = u[6], u[7], u[8]
    cube['D'][2], cube['D'][1], cube['D'][0] = r[0], r[3], r[6]
    cube['L'][8], cube['L'][5], cube['L'][2] = d[2], d[1], d[0]


def rotate_F_counterclockwise(cube):
    # Rotate F face (counterclockwise)
    f = cube['F']
    cube['F'] = [f[2], f[5], f[8],
                 f[1], f[4], f[7],
                 f[0], f[3], f[6]]

    # Copy affected edge stickers
    u = cube['U'][:]
    l = cube['L'][:]
    d = cube['D'][:]
    r = cube['R'][:]

    # Rotate adjacent edges: U ← R ← D ← L ← U
    cube['U'][6], cube['U'][7], cube['U'][8] = r[0], r[3], r[6]
    cube['R'][0], cube['R'][3], cube['R'][6] = d[2], d[1], d[0]
    cube['D'][2], cube['D'][1], cube['D'][0] = l[8], l[5], l[2]
    cube['L'][8], cube['L'][5], cube['L'][2] = u[6], u[7], u[8]

def rotate_B_clockwise(cube):
    # Rotate B face (clockwise)
    b = cube['B']
    cube['B'] = [b[6], b[3], b[0],
                 b[7], b[4], b[1],
                 b[8], b[5], b[2]]

    # Copy affected edge stickers
    u = cube['U'][:]
    l = cube['L'][:]
    d = cube['D'][:]
    r = cube['R'][:]

    # Rotate adjacent edges: U → R → D → L → U
    cube['U'][0], cube['U'][1], cube['U'][2] = r[2], r[5], r[8]
    cube['R'][2], cube['R'][5], cube['R'][8] = d[8], d[7], d[6]
    cube['D'][8], cube['D'][7], cube['D'][6] = l[6], l[3], l[0]
    cube['L'][6], cube['L'][3], cube['L'][0] = u[0], u[1], u[2]


def rotate_B_counterclockwise(cube):
    # Rotate B face (counterclockwise)
    b = cube['B']
    cube['B'] = [b[2], b[5], b[8],
                 b[1], b[4], b[7],
                 b[0], b[3], b[6]]

    # Copy affected edge stickers
    u = cube['U'][:]
    l = cube['L'][:]
    d = cube['D'][:]
    r = cube['R'][:]

    # Rotate adjacent edges: U ← R ← D ← L ← U
    cube['U'][0], cube['U'][1], cube['U'][2] = l[6], l[3], l[0]
    cube['L'][6], cube['L'][3], cube['L'][0] = d[8], d[7], d[6]
    cube['D'][8], cube['D'][7], cube['D'][6] = r[2], r[5], r[8]
    cube['R'][2], cube['R'][5], cube['R'][8] = u[0], u[1], u[2]

# Wrapped move functions that rotate + log
def U(cube, move_log):
    rotate_U_clockwise(cube)
    move_log.append('U')

def U_prime(cube, move_log):
    rotate_U_counterclockwise(cube)
    move_log.append("U'")

def D(cube, move_log):
    rotate_D_clockwise(cube)
    move_log.append('D')

def D_prime(cube, move_log):
    rotate_D_counterclockwise(cube)
    move_log.append("D'")

def L(cube, move_log):
    rotate_L_clockwise(cube)
    move_log.append('L')

def L_prime(cube, move_log):
    rotate_L_counterclockwise(cube)
    move_log.append("L'")

def R(cube, move_log):
    rotate_R_clockwise(cube)
    move_log.append('R')

def R_prime(cube, move_log):
    rotate_R_counterclockwise(cube)
    move_log.append("R'")

def F(cube, move_log):
    rotate_F_clockwise(cube)
    move_log.append('F')

def F_prime(cube, move_log):
    rotate_F_counterclockwise(cube)
    move_log.append("F'")

def B(cube, move_log):
    rotate_B_clockwise(cube)
    move_log.append('B')

def B_prime(cube, move_log):
    rotate_B_counterclockwise(cube)
    move_log.append("B'")

def print_cube(cube):
    # Nicely print each face
    for face in ['U', 'D', 'F', 'B', 'L', 'R']:
        print(f"{face}: {cube[face][0]} {cube[face][1]} {cube[face][2]}")
        print(f"   {cube[face][3]} {cube[face][4]} {cube[face][5]}")
        print(f"   {cube[face][6]} {cube[face][7]} {cube[face][8]}")
        print()

def is_daisy_complete(cube):
   
    ## Returns True if D1, D3, D5, D7 (the daisy positions around the D center)
    ## all have white stickers, meaning the white daisy is complete.
    
    return (
        cube['D'][1] == 'W' and
        cube['D'][3] == 'W' and
        cube['D'][5] == 'W' and
        cube['D'][7] == 'W'
    )

def solve_white_daisy(cube, move_log):
    max_attempts = 50  # safety net to prevent infinite loop
    attempt = 0

    while not is_daisy_complete(cube) and attempt < max_attempts:
        attempt += 1
        white_edges = find_white_edges(cube)
        progress_made = False

        for face, idx in white_edges:
            if face == 'D':
                # Already on D face, in daisy position — do nothing
                continue
            if face == 'U': 
                if idx == 1 and cube['D'][7] != 'W': 
                    B(cube, move_log)
                    B(cube, move_log)
                    progress_made = True
                    break
                elif idx == 3 and cube['D'][3] != 'W': 
                    L(cube, move_log)
                    L(cube, move_log)
                    progress_made = True
                    break
                elif idx == 5 and cube['D'][5] != 'W': 
                    R(cube, move_log)
                    R(cube, move_log)
                    progress_made = True
                    break
                elif idx == 7 and cube['D'][1] != 'W': 
                    F(cube, move_log)
                    F(cube, move_log)
                    progress_made = True
                    break
            if face == 'F': 
                if idx == 1 and cube['D'][5] != 'W': 
                    F(cube, move_log)
                    R_prime(cube, move_log)
                    F_prime(cube, move_log)
                    progress_made = True
                    break
                elif idx == 3 and cube['D'][3] != 'W': 
                    L(cube, move_log)
                    progress_made = True
                    break
                elif idx == 5 and cube['D'][5] != 'W': 
                    R_prime(cube, move_log)
                    progress_made = True
                    break
                elif idx == 7:
                    if cube['D'][5] != 'W': 
                        F_prime(cube, move_log)
                        R_prime(cube, move_log)
                        F(cube, move_log)
                        progress_made = True
                        break
                    if cube['D'][3] != 'W': 
                        F(cube, move_log)
                        L(cube, move_log)
                        F_prime(cube, move_log)
                        progress_made = True 
                        break 
                    else: 
                        F(cube, move_log)
                        F(cube, move_log)
            if face == 'R': 
                if idx == 1 and cube['D'][7] != 'W': 
                    R(cube, move_log)
                    B_prime(cube, move_log)
                    R_prime(cube, move_log)
                    progress_made = True
                    break
                elif idx == 3 and cube['D'][1] != 'W': 
                    F(cube, move_log)
                    progress_made = True
                    break
                elif idx == 5 and cube['D'][7] != 'W': 
                    B_prime(cube, move_log)
                    progress_made = True
                    break
                elif idx == 7:
                    if cube['D'][7] != 'W':
                        R_prime(cube, move_log)
                        B_prime(cube, move_log)
                        R(cube, move_log)
                        progress_made = True
                        break
                    elif cube['D'][1] != 'W': 
                        R(cube, move_log)
                        F(cube, move_log)
                        R_prime(cube, move_log)
                        progress_made = True 
                        break 
                    else: 
                        R(cube, move_log)
                        R(cube, move_log)
                        progress_made = True 
                        break
            if face == 'L':
                if idx == 1 and cube['D'][1] != 'W': 
                    L(cube, move_log)
                    F_prime(cube, move_log)
                    L_prime(cube, move_log)
                    progress_made = True
                    break
                elif idx == 3 and cube['D'][7] != 'W': 
                    B(cube, move_log)
                    progress_made = True
                    break
                elif idx == 5 and cube['D'][1] != 'W': 
                    F_prime(cube, move_log)
                    progress_made = True
                    break
                elif idx == 7:
                    if cube['D'][1] != 'W': 
                        L_prime(cube, move_log)
                        F_prime(cube, move_log)
                        L(cube, move_log)
                        progress_made = True
                        break
                    elif cube['D'][7] != 'W': 
                        L(cube, move_log)
                        B(cube, move_log)
                        L_prime(cube, move_log)
                        progress_made = True 
                        break 
                    else: 
                        L(cube, move_log)
                        L(cube, move_log)
                        progress_made = True 
                        break 
            if face == 'B':
                if idx == 1 and cube['D'][5] != 'W': 
                    B_prime(cube, move_log)
                    R(cube, move_log)
                    B(cube, move_log)
                    progress_made = True
                    break
                elif idx == 3 and cube['D'][5] != 'W': 
                    R(cube, move_log)
                    progress_made = True
                    break
                elif idx == 5 and cube['D'][3] != 'W': 
                    L_prime(cube, move_log)
                    progress_made = True
                    break
                elif idx == 7: 
                    if cube['D'][5] != 'W': 
                        B(cube, move_log)
                        R(cube, move_log)
                        B_prime(cube, move_log)
                        progress_made = True
                        break
                    if cube['D'][3] != 'W': 
                        B_prime(cube, move_log)
                        L_prime(cube, move_log) 
                        B(cube, move_log)
                        progress_made = True 
                        break 
                    else: 
                        B(cube, move_log)
                        B(cube, move_log)
                        progress_made = True 
                        break 

                 
        # If no progress made on any edge, rotate U to reshuffle
        if not progress_made:
            D(cube, move_log)

    # Final check
    if is_daisy_complete(cube):
        print(" White daisy complete!\n")
    else:
        print("Daisy solving stopped after max attempts.\n")

def is_white_cross_complete(cube):
    # Check if U1, U3, U5, U7 are white
    return (cube['U'][1] == 'W' and
            cube['U'][3] == 'W' and
            cube['U'][5] == 'W' and
            cube['U'][7] == 'W')

def solve_daisy_to_white_cross(cube, move_log):
    while not is_white_cross_complete(cube): 
        while cube['F'][7] != 'G' or cube['D'][1] != 'W': 
            D(cube, move_log)
        F(cube, move_log)
        F(cube, move_log)

        while cube['R'][7] != 'R' or cube['D'][5] != 'W':
            D(cube, move_log)
        R(cube, move_log)
        R(cube, move_log)

        while cube['B'][7] != 'B' or cube['D'][7] != 'W':
            D(cube, move_log)
        B(cube, move_log)
        B(cube, move_log)

        while cube['L'][7] != 'O' or cube['D'][3] != 'W': 
            D(cube, move_log)
        L(cube, move_log)
        L(cube, move_log)


        if is_white_cross_complete(cube):
            print("White cross complete!\n")
        else:
            print("⚠️ White cross solving stopped after max attempts or no progress.\n")

def find_white_edges(cube):
    white_edges = []
    for face, indices in {
        'U': [1, 3, 5, 7],
        'D': [1, 3, 5, 7],
        'F': [1, 3, 5, 7],
        'B': [1, 3, 5, 7],
        'L': [1, 3, 5, 7],
        'R': [1, 3, 5, 7]
    }.items():
        for i in indices:
            if cube[face][i] == 'W':
                white_edges.append((face, i))
    return white_edges

def is_white_corners_complete(cube):
    # Check U0, U2, U6, U8 are white
    return ([cube['U'][0], cube['L'][0], cube['B'][2]] == ['W', 'O', 'B'] and
            [cube['U'][2], cube['B'][0], cube['R'][2]] == ['W', 'B', 'R'] and
            [cube['U'][6], cube['L'][2], cube['F'][0]] == ['W', 'O', 'G'] and
            [cube['U'][8], cube['F'][2], cube['R'][0]] == ['W', 'G', 'R'])

def find_white_corners(cube):
    white_corners = []

    # U face corners: 0, 2, 6, 8
    for i in [0, 2, 6, 8]:
        if cube['U'][i] == 'W':
            white_corners.append(('U', i))

    # D face corners: 0, 2, 6, 8
    for i in [0, 2, 6, 8]:
        if cube['D'][i] == 'W':
            white_corners.append(('D', i))

    # Check side face corners:
    # F face: 0, 2 (top), 6, 8 (bottom)
    for i in [0, 2, 6, 8]:
        if cube['F'][i] == 'W':
            white_corners.append(('F', i))
    for i in [0, 2, 6, 8]:
        if cube['B'][i] == 'W':
            white_corners.append(('B', i))
    for i in [0, 2, 6, 8]:
        if cube['L'][i] == 'W':
            white_corners.append(('L', i))
    for i in [0, 2, 6, 8]:
        if cube['R'][i] == 'W':
            white_corners.append(('R', i))

    return white_corners

def solve_white_corners(cube, move_log): 
    # case 1: white corner on top, in position - do nothing 
    # case 2: white corner on top, not in position - bring to bottom, rotate until in position, then insert 
    # case 3: white corner facing out on top row 
    # case 4: white corner facing out on bottom row 
    # case 5: white corner on bottom of cube
    max_attempts = 50
    attempts = 0

    while not is_white_corners_complete(cube) and attempts < max_attempts: 
        attempts += 1 
        white_corners = find_white_corners(cube)
        progress_made = False

        for face, idx in white_corners: 
            if face == 'D': 
                result = get_white_corner_colors(cube, face, idx)
                if result is None: 
                    continue 
            
                white, side1, side2 = result
                side1 = side1.upper()
                side2 = side2.upper()

                if {'R', 'G'} == {side1, side2}:
                    # Align to FR corner
                    while {cube['D'][2], cube['F'][8], cube['R'][6]} != {white, side1, side2}:
                        D(cube, move_log)

                    for i in range(3): 
                        R_prime(cube, move_log)
                        D_prime(cube, move_log)
                        R(cube, move_log)
                        D(cube, move_log)
                    progress_made = True
                    continue

                elif {'R', 'B'} == {side1, side2}:
                    # Align to RB corner
                    while {cube['D'][8], cube['R'][8], cube['B'][6]} != {white, side1, side2}: 
                        D(cube, move_log)
                    for i in range(3): 
                        B_prime(cube, move_log)
                        D_prime(cube, move_log)
                        B(cube, move_log)
                        D(cube, move_log)
                    progress_made = True
                    continue
                
                elif {'B', 'O'} == {side1, side2}:
                    # Align to BL corner
                    while {cube['D'][6], cube['B'][8], cube['L'][6]} != {white, side1, side2}: 
                        D(cube, move_log)
                    for i in range(3): 
                        B(cube, move_log)
                        D(cube, move_log)
                        B_prime(cube, move_log)
                        D_prime(cube, move_log)
                    progress_made = True
                    continue

                elif {'O', 'G'} == {side1, side2}:
                    # Align to LF corner
                    while {cube['D'][0], cube['L'][8], cube['F'][6]} != {white, side1, side2}: 
                        D(cube, move_log)
                    for i in range(3):  
                        L(cube, move_log)
                        D(cube, move_log)
                        L_prime(cube, move_log)
                        D_prime(cube, move_log)
                    progress_made = True
                    continue
    
            elif face == 'U':
                result = get_white_corner_colors(cube, face, idx)
                if result is None:
                    continue

                white, side1, side2 = result
                side1 = side1.upper()
                side2 = side2.upper()

                # Determine which corner it is and knock it down accordingly
                if (idx == 0): # ULB
                    expected = {'W', 'B', 'O'}
                    actual = {cube['U'][0], cube['L'][0], cube['B'][2]}
                    if (actual == expected):
                        continue
                    else: 
                        for i in range(3): 
                            B(cube, move_log)
                            D(cube, move_log)
                            B_prime(cube, move_log)
                            D_prime(cube, move_log) 
                        progress_made = True
                        continue
                
                if (idx == 2): # URB
                    expected = {'W', 'B', 'R'}
                    actual = {cube['U'][2], cube['B'][0], cube['R'][2]}
                    if (actual == expected):
                        continue
                    else: 
                        for i in range(3): 
                            R(cube, move_log)
                            D(cube, move_log)
                            R_prime(cube, move_log)
                            D_prime(cube, move_log) 
                        progress_made = True
                        continue

                if (idx == 6): # ULF
                    expected = {'W', 'O', 'G'}
                    actual = {cube['U'][6], cube['F'][0], cube['L'][2]}
                    if (actual == expected):
                        continue
                    else: 
                        for i in range(3): 
                            L(cube, move_log)
                            D(cube, move_log)
                            L_prime(cube, move_log)
                            D_prime(cube, move_log) 
                        progress_made = True
                        continue

                if (idx == 8): # URF
                    expected = {'W', 'R', 'G'}
                    actual = {cube['U'][8], cube['F'][2], cube['R'][0]}
                    if (actual == expected):
                        continue
                    else: 
                        for i in range(3): 
                            R_prime(cube, move_log)
                            D_prime(cube, move_log)
                            R(cube, move_log)
                            D(cube, move_log) 
                        progress_made = True
                        continue

            elif face == 'F':
                result = get_white_corner_colors(cube, face, idx)
                if result is None: 
                    continue 
            
                white, side1, side2 = result
                side1 = side1.upper()
                side2 = side2.upper() 

                if (idx == 0): 
                    expected = {'W', 'O', 'G'}
                    actual = {cube['U'][6], cube['F'][0], cube['L'][2]}
                    if (actual == expected):
                        for i in range(2): 
                            F_prime(cube, move_log)
                            D_prime(cube, move_log)
                            F(cube, move_log)
                            D(cube, move_log)
                        progress_made = True 
                        continue 
                    else: 
                        L(cube, move_log)
                        D(cube, move_log)
                        L_prime(cube, move_log)
                        D_prime(cube, move_log)
                        progress_made = True
                        continue

                if (idx == 2): 
                    expected = {'W', 'G', 'R'}
                    actual = {cube['U'][8], cube['F'][2], cube['R'][0]}
                    if (actual == expected):
                        for i in range(2): 
                            F(cube, move_log)
                            D(cube, move_log)
                            F_prime(cube, move_log)
                            D_prime(cube, move_log)
                        progress_made = True 
                        continue 
                    else: 
                        R_prime(cube, move_log)
                        D_prime(cube, move_log)
                        R(cube, move_log)
                        D(cube, move_log)
                        progress_made = True
                        continue
                
                if (idx == 6): 
                    expected = {'W', 'O', 'G'}
                    actual = {cube['F'][6], cube['L'][8], cube['D'][0]}
                    currently_in_corner = {cube['F'][0], cube['L'][2], cube['U'][6]}
                    if (actual == expected):
                        F_prime(cube, move_log)
                        D_prime(cube, move_log)
                        F(cube, move_log)
                        D(cube, move_log)
                        progress_made = True
                        continue
                        
                    else: 
                        if currently_in_corner == expected: 
                            D(cube, move_log)
                            progress_made = True
                            continue
                        else: 
                            L(cube, move_log)
                            D(cube, move_log)
                            L_prime(cube, move_log)
                            D_prime(cube, move_log)
                            progress_made = True
                            continue

                if (idx == 8): 
                    expected = {'W', 'G', 'R'}
                    actual = {cube['F'][8], cube['R'][6], cube['D'][2]}
                    currently_in_corner = {cube['F'][2], cube['R'][0], cube['U'][8]}
                    if (actual == expected):
                        F(cube, move_log)
                        D(cube, move_log)
                        F_prime(cube, move_log)
                        D_prime(cube, move_log)
                        progress_made = True
                        continue
                        
                    else: 
                        if currently_in_corner == expected: 
                            D(cube, move_log)
                            progress_made = True
                            continue
                        else: 
                            for i in range(2): 
                                R_prime(cube, move_log)
                                D_prime(cube, move_log)
                                R(cube, move_log)
                                D(cube, move_log)
                            progress_made = True
                            continue
            elif face == 'R': 
                if (idx == 0):
                    expected = {'W', 'G', 'R'}
                    actual = {cube['U'][8], cube['F'][2], cube['R'][0]}
                    if (actual == expected):
                        for i in range(2): 
                            R_prime(cube, move_log)
                            D_prime(cube, move_log)
                            R(cube, move_log)
                            D_prime(cube, move_log)
                        progress_made = True 
                        continue 
                    else: 
                        F(cube, move_log)
                        D(cube, move_log)
                        F_prime(cube, move_log)
                        D_prime(cube, move_log)
                        progress_made = True
                        continue

                if (idx == 2): 
                    expected = {'W', 'R', 'B'}
                    actual = {cube['U'][2], cube['R'][2], cube['B'][0]}
                    if (actual == expected):
                        for i in range(2): 
                            R(cube, move_log)
                            D(cube, move_log)
                            R_prime(cube, move_log)
                            D_prime(cube, move_log)
                        progress_made = True 
                        continue 
                    else: 
                        B_prime(cube, move_log)
                        D_prime(cube, move_log)
                        B(cube, move_log)
                        D(cube, move_log)
                        progress_made = True
                        continue

                if (idx == 6): 
                    expected = {'W', 'R', 'G'}
                    actual = {cube['F'][8], cube['R'][6], cube['D'][2]}
                    currently_in_corner = {cube['F'][2], cube['R'][0], cube['U'][8]}
                    if (actual == expected):
                        R_prime(cube, move_log) 
                        D_prime(cube, move_log)
                        R(cube, move_log)
                        D(cube, move_log)
                        progress_made = True
                        continue
                        
                    else: 
                        if currently_in_corner == expected: 
                            D(cube, move_log)
                            progress_made = True
                            continue
                        else: 
                            for i in range(2): 
                                F(cube, move_log)
                                D(cube, move_log)
                                F_prime(cube, move_log)
                                D_prime(cube, move_log)
                            progress_made = True
                            continue
                    
                if (idx == 8): 
                    expected = {'W', 'R', 'B'}
                    actual = {cube['R'][8], cube['B'][6], cube['D'][2]}
                    currently_in_corner = {cube['R'][2], cube['U'][2], cube['B'][0]}
                    if (actual == expected):
                        R(cube, move_log)
                        D(cube, move_log)
                        R_prime(cube, move_log)
                        D_prime(cube, move_log)
                        progress_made = True
                        continue
                        
                    else:
                        if currently_in_corner == expected: 
                            D(cube, move_log)
                            progress_made = True
                            continue
                        else: 
                            for i in range(2): 
                                B_prime(cube, move_log)
                                D_prime(cube, move_log)
                                B(cube, move_log)
                                D(cube, move_log)
                            progress_made = True
                            continue
            elif face == 'B': 
                if (idx == 0):
                    expected = {'W', 'R', 'B'}
                    actual = {cube['U'][2], cube['R'][2], cube['B'][0]}
                    if (actual == expected):
                        for i in range(2): 
                            B_prime(cube, move_log)
                            D_prime(cube, move_log)
                            B(cube, move_log)
                            D(cube, move_log)
                        progress_made = True 
                        continue 
                    else: 
                        R(cube, move_log)
                        D(cube, move_log)
                        R_prime(cube, move_log)
                        D_prime(cube, move_log)
                        progress_made = True
                        continue
                if (idx == 2): 
                    expected = {'W', 'B', 'O'}
                    actual = {cube['U'][0], cube['B'][2], cube['L'][0]}
                    if (actual == expected):
                        for i in range(2): 
                            B(cube, move_log)
                            D(cube, move_log)
                            B_prime(cube, move_log)
                            D_prime(cube, move_log)
                        progress_made = True 
                        continue 
                    else: 
                        L_prime(cube, move_log)
                        D_prime(cube, move_log)
                        L(cube, move_log)
                        D(cube, move_log)
                        progress_made = True
                        continue
                if (idx == 6): 
                    expected = {'W', 'R', 'B'}
                    actual = {cube['B'][6], cube['R'][8], cube['D'][8]}
                    currently_in_corner = {cube['B'][0], cube['U'][2], cube['R'][2]}
                    if (actual == expected):
                        B_prime(cube, move_log)
                        D_prime(cube, move_log)
                        B(cube, move_log)
                        D(cube, move_log)
                        progress_made = True
                        continue
                    else: 
                        if currently_in_corner == expected: 
                            D(cube, move_log)
                            progress_made = True
                            continue
                        else: 
                            for i in range(2): 
                                R(cube, move_log)
                                D(cube, move_log)
                                R_prime(cube, move_log)
                                D_prime(cube, move_log)
                            progress_made = True
                            continue
                if (idx == 8): 
                    expected = {'W', 'O', 'B'}
                    actual = {cube['B'][8], cube['L'][6], cube['D'][6]}
                    currently_in_corner = {cube['B'][2], cube['L'][0], cube['U'][0]}
                    if (actual == expected):
                        B(cube, move_log)
                        D(cube, move_log)
                        B_prime(cube, move_log)
                        D_prime(cube, move_log)
                        progress_made = True
                        continue         
                    else:
                        if currently_in_corner == expected: 
                            D(cube, move_log)
                            progress_made = True
                            continue
                        else: 
                            for i in range(2): 
                                L_prime(cube, move_log)
                                D_prime(cube, move_log)
                                L(cube, move_log)
                                D(cube, move_log)
                            progress_made = True
                            continue
            elif face == 'L': 
                if (idx == 0):
                    expected = {'W', 'B', 'O'}
                    actual = {cube['L'][0], cube['B'][2], cube['U'][0]}
                    if (actual == expected):
                        for i in range(2): 
                            L_prime(cube, move_log)
                            D_prime(cube, move_log)
                            L(cube, move_log)
                            D(cube, move_log)
                        progress_made = True 
                        continue 
                    else: 
                        B(cube, move_log)
                        D(cube, move_log)
                        B_prime(cube, move_log)
                        D_prime(cube, move_log)
                        progress_made = True
                        continue
                if (idx == 2): 
                    expected = {'W', 'O', 'G'}
                    actual = {cube['U'][6], cube['F'][0], cube['L'][2]}
                    if (actual == expected):
                        for i in range(2): 
                            L(cube, move_log)
                            D(cube, move_log)
                            L_prime(cube, move_log)
                            D_prime(cube, move_log)
                        progress_made = True 
                        continue 
                    else: 
                        F_prime(cube, move_log)
                        D_prime(cube, move_log)
                        F(cube, move_log)
                        D(cube, move_log)
                        progress_made = True
                        continue
                if (idx == 6): 
                    expected = {'W', 'B', 'O'}
                    actual = {cube['B'][8], cube['L'][6], cube['D'][6]}
                    currently_in_corner = {cube['B'][2], cube['U'][0], cube['L'][0]}
                    if (actual == expected):
                        L_prime(cube, move_log)
                        D_prime(cube, move_log)
                        L(cube, move_log)
                        D(cube, move_log)
                        progress_made = True
                        continue
                    else: 
                        if currently_in_corner == expected: 
                            D(cube, move_log)
                            progress_made = True
                            continue
                        else: 
                            for i in range(2): 
                                B(cube, move_log)
                                D(cube, move_log)
                                B_prime(cube, move_log)
                                D_prime(cube, move_log)
                            progress_made = True
                            continue
                if (idx == 8): 
                    expected = {'W', 'G', 'O'}
                    actual = {cube['L'][8], cube['F'][6], cube['D'][0]}
                    currently_in_corner = {cube['L'][2], cube['F'][0], cube['U'][6]}
                    if (actual == expected):
                        L(cube, move_log)
                        D(cube, move_log)
                        L_prime(cube, move_log)
                        D_prime(cube, move_log)
                        progress_made = True
                        continue         
                    else:
                        if currently_in_corner == expected: 
                            D(cube, move_log)
                            progress_made = True
                            continue
                        else: 
                            for i in range(2): 
                                F_prime(cube, move_log)
                                D_prime(cube, move_log)
                                F(cube, move_log)
                                D(cube, move_log)
                            progress_made = True
                            continue

def is_middle_layer_solved(cube): 
    return (cube['F'][3] == cube['F'][4] and cube['F'][5] == cube['F'][4]
            and cube['R'][3] == cube['R'][4] and cube['R'][5] == cube['R'][4]
            and cube['B'][3] == cube['B'][4] and cube['B'][5] == cube['B'][4]
            and cube['L'][3] == cube['L'][4] and cube['L'][5] == cube['L'][4])

def find_top_edges(cube):
    return [
        (cube['U'][1], cube['B'][1], 'U1'),
        (cube['U'][3], cube['L'][1], 'U3'),
        (cube['U'][5], cube['R'][1], 'U5'),
        (cube['U'][7], cube['F'][1], 'U7')
    ]

def flip_cube(cube, move_log):
    def rotate_180(face):
        return [
            face[8], face[7], face[6],
            face[5], face[4], face[3],
            face[2], face[1], face[0]
        ]

    flipped_cube = {
        'U': rotate_180(cube['D']),
        'D': rotate_180(cube['U']),
        'F': rotate_180(cube['F']),
        'B': rotate_180(cube['B']),
        'L': rotate_180(cube['R']),
        'R': rotate_180(cube['L'])
    }

    move_log.append("X2")
    return flipped_cube

def rotate_clockwise(face):
    return [
        face[6], face[3], face[0],
        face[7], face[4], face[1],
        face[8], face[5], face[2]
    ]

def rotate_counterclockwise(face):
    return [
        face[2], face[5], face[8],
        face[1], face[4], face[7],
        face[0], face[3], face[6]
    ]


def rotate_cube_right(cube, move_log):
    move_log.append("Y")
    # take copies so faces don't alias each other
    F, R, B, L, U, D = (cube['F'][:], cube['R'][:], cube['B'][:],
                        cube['L'][:], cube['U'][:], cube['D'][:])
    cube['F'] = R
    cube['R'] = B
    cube['B'] = L
    cube['L'] = F
    cube['U'] = rotate_clockwise(U)
    cube['D'] = rotate_counterclockwise(D)

def rotate_cube_left(cube, move_log):
    move_log.append("Y'")
    F, R, B, L, U, D = (cube['F'][:], cube['R'][:], cube['B'][:],
                        cube['L'][:], cube['U'][:], cube['D'][:])
    cube['F'] = L
    cube['R'] = F
    cube['B'] = R
    cube['L'] = B
    cube['U'] = rotate_counterclockwise(U)
    cube['D'] = rotate_clockwise(D)

def right_algorithm(cube, move_log): 
    R(cube, move_log)
    U(cube, move_log)
    R_prime(cube, move_log)
    U_prime(cube, move_log)

def left_algorithm(cube, move_log): 
    L_prime(cube, move_log)
    U_prime(cube, move_log)
    L(cube, move_log)
    U(cube, move_log)

def right_insert(cube, move_log):
    # U R U' R' U' F' U F
    U(cube, move_log)
    R(cube, move_log)
    U_prime(cube, move_log)
    R_prime(cube, move_log)
    U_prime(cube, move_log)
    F_prime(cube, move_log)
    U(cube, move_log)
    F(cube, move_log)

def left_insert(cube, move_log):
    # U' L' U L U F U' F'
    U_prime(cube, move_log)
    L_prime(cube, move_log)
    U(cube, move_log)
    L(cube, move_log)
    U(cube, move_log)
    F(cube, move_log)
    U_prime(cube, move_log)
    F_prime(cube, move_log)

def solve_middle_layer(cube, move_log): 
    while is_middle_layer_solved(cube) == False: 
        top_edges = find_top_edges(cube)
        inserted = False 
        for color1, color2, pos in top_edges: 
            if 'Y' in [color1, color2]: 
                continue 
            
            if color2 == 'G': 
                attempts = 0
                while (cube['F'][1] != 'G' or cube['U'][7] not in ['O', 'R']) and attempts < 4:
                    U(cube, move_log)
                    attempts += 1
                if cube['F'][1] == 'G' and cube['U'][7] == 'R':
                    left_insert(cube, move_log)
                    inserted = True
                    break
                elif cube['F'][1] == 'G' and cube['U'][7] == 'O':
                    right_insert(cube, move_log)
                    inserted = True
                    break
            if color2 == 'R': 
                rotate_cube_left(cube, move_log)
                attempts = 0
                while (cube['F'][1] != 'R' or cube['U'][7] not in ['G', 'B']) and attempts < 4:
                    U(cube, move_log)
                    attempts += 1
                if cube['F'][1] == 'R' and cube['U'][7] == 'B':
                    left_insert(cube, move_log)
                    inserted = True
                elif cube['F'][1] == 'R' and cube['U'][7] == 'G':
                    right_insert(cube, move_log)
                    inserted = True
                rotate_cube_right(cube, move_log)
                if inserted: 
                    break
            if color2 == 'B': 
                rotate_cube_left(cube, move_log)
                rotate_cube_left(cube, move_log)
                attempts = 0
                while (cube['F'][1] != 'B' or cube['U'][7] not in ['R', 'O']) and attempts < 4:
                    U(cube, move_log)
                    attempts += 1
                if cube['F'][1] == 'B' and cube['U'][7] == 'O':
                    left_insert(cube, move_log)
                    inserted = True
                elif cube['F'][1] == 'B' and cube['U'][7] == 'R':
                    right_insert(cube, move_log)
                    inserted = True
                rotate_cube_right(cube, move_log)
                rotate_cube_right(cube, move_log)
                if inserted: 
                    break 
            if color2 == 'O': 
                rotate_cube_right(cube, move_log)
                attempts = 0
                while (cube['F'][1] != 'O' or cube['U'][7] not in ['G', 'B']) and attempts < 4:
                    U(cube, move_log)
                    attempts += 1
                if cube['F'][1] == 'O' and cube['U'][7] == 'G':
                    left_insert(cube, move_log)
                    inserted = True
                elif cube['F'][1] == 'O' and cube['U'][7] == 'B':
                    right_insert(cube, move_log)
                    inserted = True
                rotate_cube_left(cube, move_log)
                if inserted: 
                    break 
                    # If we didn’t insert anything this pass, we need a fallback:
        
        if not inserted:
            # Try to eject a wrong/blocked middle edge to the top.
            # Rotate the whole cube up to 4 times looking for a face
            # where the FR edge (F[5], R[3]) isn’t matching its centers.
            turned = 0
            ejected = False
            while turned < 4:
                if cube['F'][5] != cube['F'][4] or cube['R'][3] != cube['R'][4]:
                    right_insert(cube, move_log)  # ejects FR edge to U layer
                    ejected = True
                    break
                rotate_cube_right(cube, move_log)
                turned += 1
            # restore orientation
            for _ in range(turned):
                rotate_cube_left(cube, move_log)

            # If nothing to eject (very rare) just spin U once to reshuffle top
            if not ejected:
                U(cube, move_log)
            
def get_white_corner_colors(cube, face, idx):
    corner_map = {
        ('F', 0): [cube['F'][0], cube['U'][6], cube['L'][2]],
        ('F', 2): [cube['F'][2], cube['U'][8], cube['R'][0]],
        ('F', 6): [cube['F'][6], cube['D'][0], cube['L'][8]],
        ('F', 8): [cube['F'][8], cube['D'][2], cube['R'][6]],

        ('B', 0): [cube['B'][0], cube['U'][2], cube['R'][2]],
        ('B', 2): [cube['B'][2], cube['U'][0], cube['L'][0]],
        ('B', 6): [cube['B'][6], cube['D'][8], cube['R'][8]],
        ('B', 8): [cube['B'][8], cube['D'][6], cube['L'][6]],

        ('U', 0): [cube['U'][0], cube['B'][2], cube['L'][0]],
        ('U', 2): [cube['U'][2], cube['B'][0], cube['R'][2]],
        ('U', 6): [cube['U'][6], cube['F'][0], cube['L'][2]],
        ('U', 8): [cube['U'][8], cube['F'][2], cube['R'][0]],

        ('D', 0): [cube['D'][0], cube['F'][6], cube['L'][8]],
        ('D', 2): [cube['D'][2], cube['F'][8], cube['R'][6]],
        ('D', 6): [cube['D'][6], cube['B'][8], cube['L'][6]],
        ('D', 8): [cube['D'][8], cube['B'][6], cube['R'][8]],
    }

    return corner_map.get((face, idx), [])

def is_yellow_cross_solved(cube): 
    return (cube['U'][1] == 'Y'
        and cube['U'][3] == 'Y'
        and cube['U'][4] == 'Y'
        and cube['U'][5] == 'Y'
        and cube['U'][7] == 'Y')

def solve_yellow_cross(cube, move_log): 
    while not is_yellow_cross_solved(cube): 
        if (cube['U'][1] != 'Y'
        and cube['U'][3] != 'Y'
        and cube['U'][4] == 'Y'
        and cube['U'][5] != 'Y'
        and cube['U'][7] != 'Y') or (cube['U'][1] != 'Y'
        and cube['U'][3] == 'Y'
        and cube['U'][4] == 'Y'
        and cube['U'][5] == 'Y'
        and cube['U'][7] != 'Y'): 
            F(cube, move_log)
            R(cube, move_log)
            U(cube, move_log)
            R_prime(cube, move_log)
            U_prime(cube, move_log)
            F_prime(cube, move_log)
        elif (cube['U'][1] != 'Y'
        and cube['U'][3] != 'Y'
        and cube['U'][4] == 'Y'
        and cube['U'][5] == 'Y'
        and cube['U'][7] == 'Y'):
            B(cube, move_log)
            U(cube, move_log)
            L(cube, move_log)
            U_prime(cube, move_log)
            L_prime(cube, move_log)
            B_prime(cube, move_log)
        else: 
            U(cube, move_log)
    
    while cube['F'][4] != 'G': 
        rotate_cube_right(cube, move_log)
    
    while cube['F'][1] != 'G': 
        U(cube, move_log)

def are_yellow_corners_matched(cube): 
    return (cube['F'][0] == cube['F'][2]) and (cube['R'][0] == cube['R'][2]) and (cube['L'][0] == cube['L'][2]) and (cube['B'][0] == cube['B'][2])


def is_yellow_corners_solved(cube): 
    return (cube['D'][0] == 'Y'
        and cube['D'][2] == 'Y'
        and cube['D'][6] == 'Y'
        and cube['D'][8] == 'Y')

def solve_yellow_corners(cube, move_log): 
    while not is_yellow_corners_solved(cube): 
        while cube['D'][2] != 'Y': 
            right_algorithm(cube, move_log)
        D(cube, move_log)

def face_has_matching_corners(cube): 
    return (cube['F'][0] == cube['F'][2] or 
            cube['R'][0] == cube['R'][2] or
            cube['L'][0] == cube['L'][2] or 
            cube['B'][0] == cube['B'][2])

def align_yellow_algo(cube, move_log): 
        R_prime(cube, move_log)
        F(cube, move_log)
        R_prime(cube, move_log)
        B(cube, move_log)
        B(cube, move_log)
        R(cube, move_log)
        F_prime(cube, move_log)
        R_prime(cube, move_log)
        B(cube, move_log)
        B(cube, move_log)
        R(cube, move_log)
        R(cube, move_log)

def match_all_corners(cube, move_log):
    while not are_yellow_corners_matched(cube): 
        if face_has_matching_corners(cube): 
            while (cube['B'][0] != cube['B'][2]): 
                rotate_cube_right(cube, move_log)
            align_yellow_algo(cube, move_log)
        
        else: 
            align_yellow_algo(cube, move_log)
            match_all_corners(cube, move_log)
        

def align_yellow_corners(cube, move_log): 
    while len({cube['F'][0], cube['F'][2], cube['F'][4]}) != 1: 
            U(cube, move_log)


def top_edges_algo(cube, move_log): 
    R(cube, move_log)
    R(cube, move_log)
    U(cube, move_log)
    R(cube, move_log)
    U(cube, move_log)
    R_prime(cube, move_log)
    U_prime(cube, move_log)
    R_prime(cube, move_log)
    U_prime(cube, move_log)
    R_prime(cube, move_log)
    U(cube, move_log)
    R_prime(cube, move_log)

def are_top_edges_fixed(cube): 
    return (cube['F'][1] == cube['F'][4] and
            cube['R'][1] == cube['R'][4] and
            cube['L'][1] == cube['L'][4] and 
            cube['B'][1] == cube['B'][4]) 

def fix_top_edges(cube, move_log): 
    while not are_top_edges_fixed(cube): 
        attempts = 0
        while len({cube['B'][0], cube['B'][1], cube['B'][2]}) != 1 and attempts < 3: 
            rotate_cube_right(cube, move_log)
            attempts += 1 

        top_edges_algo(cube, move_log)
    
def beginners_method_solve_visual(cube):
    move_log = []

    solve_white_daisy(cube, move_log)
    solve_daisy_to_white_cross(cube, move_log)
    solve_white_corners(cube, move_log)
    flipped_cube = flip_cube(cube, move_log)
    solve_middle_layer(flipped_cube, move_log)
    solve_yellow_cross(flipped_cube, move_log)
    flipped_again = flip_cube(flipped_cube, move_log)
    solve_yellow_corners(flipped_again, move_log)
    third_flip = flip_cube(flipped_again, move_log)
    match_all_corners(third_flip, move_log)
    align_yellow_corners(third_flip, move_log)
    fix_top_edges(third_flip, move_log)

    print_cube(third_flip)
    return third_flip, move_log


def beginners_method_solve_text(cube): 
    move_log = []

    solve_white_daisy(cube, move_log)
    solve_daisy_to_white_cross(cube, move_log)
    solve_white_corners(cube, move_log)
    flipped_cube = flip_cube(cube, move_log)
    solve_middle_layer(flipped_cube, move_log)
    solve_yellow_cross(flipped_cube, move_log)
    flipped_again = flip_cube(flipped_cube, move_log)
    solve_yellow_corners(flipped_again, move_log)
    third_flip = flip_cube(flipped_again, move_log)
    match_all_corners(third_flip, move_log)
    align_yellow_corners(third_flip, move_log)
    fix_top_edges(third_flip, move_log)

    print_cube(third_flip)

    print("\nMoves:")
    print(' '.join(move_log))


def _parse_move(tok):
    """Return (base, quarters) or None if invalid.
       quarters: 1 = 90° cw, 2 = 180°, 3 = 90° ccw
    """
    if not tok:
        return None
    base = tok[0]
    if base not in "UDLRFBXYZ":
        return None
    if len(tok) == 1:
        return base, 1
    if len(tok) == 2 and tok[1] in ("'", "2"):
        return base, (3 if tok[1] == "'" else 2)
    return None  # anything else is treated as non-move

def _suffix_from_quarters(q):
    return "" if q == 1 else ("2" if q == 2 else "'")

def reduce_moves(moves):
    """Reduce a list of moves (strings). Unknown tokens are ignored."""
    out = []
    for tok in moves:
        parsed = _parse_move(tok)
        if not parsed:
            continue  # skip non-move tokens
        base, cur_q = parsed

        if out:
            last = out[-1]
            lb, lq = _parse_move(last)
            if lb == base:
                # same face/axis: combine by modulo-4
                nq = (lq + cur_q) % 4
                out.pop()
                if nq != 0:
                    out.append(base + _suffix_from_quarters(nq))
                continue

        out.append(base + _suffix_from_quarters(cur_q))
    return out


def main():
    cube = {
        'F': ['Y', 'Y', 'B', 'Y', 'G', 'O', 'G', 'B', 'W'],
        'R': ['O', 'Y', 'R', 'G', 'R', 'W', 'G', 'W', 'O'],
        'B': ['G', 'R', 'O', 'B', 'B', 'O', 'Y', 'G', 'W'],
        'L': ['Y', 'R', 'R', 'W', 'O', 'G', 'B', 'B', 'R'],
        'U': ['G', 'B', 'Y', 'W', 'W', 'O', 'B', 'R', 'W'],
        'D': ['W', 'Y', 'O', 'O', 'Y', 'G', 'R', 'R', 'B']
    }

    beginners_method_solve_text(cube)

if __name__ == "__main__":
    main()


    



