class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        retval = True
        temp_dict_row = {}
        temp_dict_col = {}
        temp_dict_box = {}
    
        # if rows are valid
        for i in range(9):
            for j in range(9):
                # print(board[i][j], i, j)
                # print(int(i / 3) * 3 + int(j / 3), (j%3 + i*3)%9)
                boxi = int(i / 3) * 3 + int(j / 3)
                boxj = (j%3 + i*3)%9
                # print(i, j)
                if board[i][j] != "." and board[i][j] in temp_dict_row:
                    retval = False
                    break
                else:
                    # num = board[i][j]
                    temp_dict_row[board[i][j]] = 1
                if board[j][i] != "." and board[j][i] in temp_dict_col:
                    retval = False
                    break
                else:
                    # num = board[i][j]
                    temp_dict_col[board[j][i]] = 1

                if board[boxi][boxj] != "." and board[boxi][boxj] in temp_dict_box:
                    retval = False
                    print(temp_dict_box)
                    break
                else:
                    # num = board[i][j]
                    temp_dict_box[board[boxi][boxj]] = 1
        
            temp_dict_row = {}
            temp_dict_col = {}
            temp_dict_box = {}
            


        # if columns are valid
        # for i in range(9):
        #     for j in range(9):
        #         # print(board[j][i], i, j)
        #         print(int(i / 3) * 3 + int(j / 3), i)
        #         if board[j][i] != "." and board[j][i] in temp_dict_col:
        #             retval = False
        #             break
        #         else:
        #             # num = board[i][j]
        #             temp_dict_col[board[j][i]] = 1
        #     temp_dict_col = {}

        # id boxes are valid
     
        return retval



        # 0 0 0
        # 0 1 1
        # 0 2 2 
        # 0 3 0
        # 0 4 1
        # 0 5 2 
        # 0 6 0 
        # 0 7 1
        # 0 8 2
        # 1 0 3 0
        # 1 1 4 1
        # 1 2 5 2
        # 1 3 3 0


        