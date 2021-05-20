grid = []

for i in range(9):
    grid += [[0] * 9]

grid[0][2] = 1
grid[0][3] = 2
grid[0][5] = 7
grid[1][1] = 6
grid[1][2] = 2
grid[2][6] = 9
grid[2][7] = 4
grid[3][3] = 9
grid[3][4] = 8
grid[3][8] = 3
grid[4][0] = 5
grid[5][0] = 7
grid[5][4] = 3
grid[5][7] = 2
grid[5][8] = 1
grid[6][3] = 1
grid[6][5] = 2
grid[7][1] = 7
grid[7][3] = 8
grid[7][6] = 4
grid[7][7] = 1
grid[8][0] = 3
grid[8][2] = 4
grid[8][8] = 8

for i in range(9):
    if i == 3 or i == 6:
        print("---------------------")

    line = list()

    for j in range(9):
        if grid[i][j] != 0:
            line.append(str(grid[i][j]) + " ")
        else:
            line.append("  ")

        if j == 2 or j == 5:
            line.append("| ")

    print("".join(line))

for a in range(0,8):
    eingabe = input()
    eingabe = eingabe.split()
    for b in range(0,8):
        if b == 0:
            grid[b][0] = eingabe[b][0]
            grid[b][1] = eingabe[b][1]
            grid[b][4] = eingabe[b][2]
            grid[b][6] = eingabe[b][3]
            grid[b][7] = eingabe[b][4]
            grid[b][8] = eingabe[b][5]
        elif b == 1:
            grid[b][0] = eingabe[b][0]
            grid[b][3] = eingabe[b][1]
            grid[b][4] = eingabe[b][2]
            grid[b][5] = eingabe[b][3]
            grid[b][6] = eingabe[b][4]
            grid[b][7] = eingabe[b][5]
            grid[b][8] = eingabe[b][6]
        elif b == 2:
            grid[b][0] = eingabe[b][0]
            grid[b][1] = eingabe[b][1]
            grid[b][2] = eingabe[b][2]
            grid[b][3] = eingabe[b][3]
            grid[b][4] = eingabe[b][4]
            grid[b][5] = eingabe[b][5]
            grid[b][8] = eingabe[b][6]
        elif b == 3:
            grid[b][0] = eingabe[b][0]
            grid[b][1] = eingabe[b][1]
            grid[b][2] = eingabe[b][2]
            grid[b][5] = eingabe[b][3]
            grid[b][6] = eingabe[b][4]
            grid[b][7] = eingabe[b][5]
        elif b == 4:
            grid[b][1] = eingabe[b][0]
            grid[b][2] = eingabe[b][1]
            grid[b][3] = eingabe[b][2]
            grid[b][4] = eingabe[b][3]
            grid[b][5] = eingabe[b][4]
            grid[b][6] = eingabe[b][5]
            grid[b][7] = eingabe[b][6]
            grid[b][8] = eingabe[b][7]
        elif b == 5:
            grid[b][1] = eingabe[b][0]
            grid[b][2] = eingabe[b][1]
            grid[b][3] = eingabe[b][2]
            grid[b][5] = eingabe[b][3]
            grid[b][6] = eingabe[b][4]
        elif b == 6:
            grid[b][0] = eingabe[b][0]
            grid[b][1] = eingabe[b][1]
            grid[b][2] = eingabe[b][2]
            grid[b][4] = eingabe[b][3]
            grid[b][6] = eingabe[b][4]
            grid[b][7] = eingabe[b][5]
            grid[b][8] = eingabe[b][6]
        elif b == 7:
            grid[b][0] = eingabe[b][0]
            grid[b][2] = eingabe[b][1]
            grid[b][4] = eingabe[b][2]
            grid[b][5] = eingabe[b][3]
            grid[b][6] = eingabe[b][4]
            grid[b][8] = eingabe[b][5]
        elif b == 8
            grid[b][1] = eingabe[b][0]
            grid[b][3] = eingabe[b][1]
            grid[b][4] = eingabe[b][2]
            grid[b][5] = eingabe[b][3]
            grid[b][6] = eingabe[b][4]
            grid[b][7] = eingabe[b][5]