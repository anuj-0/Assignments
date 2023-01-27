
#Function to perform DFS Traversal on the board
def DFS(row, col, d_row, d_col, board, visited):
    visited[row][col] = True
    n = len(board)
    m = len(board[0])

    for i in range(4):
        n_row = d_row[i] + row
        n_col = d_col[i] + col
        if 0<=n_row<n and 0<=n_col<m:
            if board[n_row][n_col]=="O" and not visited[n_row][n_col]:
                DFS(n_row,n_col,d_row,d_col,board,visited)

#Function to solve the given problem
def solve(board):
    n = len(board)
    m = len(board[0]) # n,m are the dimensions of the board

    visited = [[False] * m for i in range(n)] # Maintaining a visited matrix to keep track if we have traversed through the vertex. 
    d_row = [-1,0,1,0]
    d_col = [0,-1,0,1] # List indices to move in the neighboring directions from the vertex 

    # We will be checking on the boundaries of the board first, as the "O"s on the boundary will never be 
    # marked because it is not completely surrrounded by "X"s  

    #Therefore the "O"s connected with the boundary "O"s will also be not marked.

    #Traversing through the non-visited "O"s on the First and last columns 
    for j in range(m):
        if not visited[0][j] and board[0][j]=="O": 
            DFS(0,j,d_row,d_col,board,visited)
        if not visited[n-1][j] and board[n-1][j]=="O":
            DFS(n-1,j,d_row,d_col, board,visited)
    
    #Traversing through the non-visited "O"s on the First and last rows 
    for i in range(n):
        if not visited[i][0] and board[i][0]=="O":
            DFS(i,0,d_row,d_col, board,visited)
        if not visited[i][m-1] and board[i][m-1]=="O":
            DFS(i,m-1,d_row,d_col, board,visited)

    #Finally marking the non-visited "O"s as "X" 
    for i in range(n):
        for j in range(m):
            if board[i][j] == "O" and not visited[i][j]:
                board[i][j] = "X"

if __name__ == "__main__":
    n=int(input("Number of rows: "))
    m=int(input("Number of columns: "))
    print("Enter the board: ")
    board=[]
    for i in range(0,n):
        temp=[]
        for j in range (0,m):
            temp.append(input())
        board.append(temp)
    for i in range(n):
        for j in range(m):
            print(f"{board[i][j]}",end=" ")
        print()
    solve(board)
    for i in range(n):
        for j in range(m):
            print(f"{board[i][j]}",end=" ")
    print()