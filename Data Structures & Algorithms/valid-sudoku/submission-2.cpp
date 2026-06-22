#include <map>
#include <algorithm>

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // check all rows and cols
            // if a space == another space with same i --> row violation --> false
            // if a space == another space with same j --> col violation --> false

        // check all boxes
            // check each i + 2 and j + 2 as a sub-matrix
            // if any repeats --> false
        // else, true

        map<pair<int, char>, bool> row;
        map<pair<int, char>, bool> col;
        for(int i = 0; i < board.size(); i++) {
            for(int j = 0; j < board[i].size(); j++) {
                if(board[i][j] != '.') {
                    if(col.contains({j, board[i][j]}) || row.contains({i, board[i][j]})) {
                        return false;
                    } else {
                        row[{i, board[i][j]}] = true;
                        col[{j, board[i][j]}] = true;
                    }
                }
            }
        }

        for(int adjust = 0; adjust < 9; adjust += 3) {
            for(int boxRow = 0; boxRow < 3; boxRow++) {
                map<char, bool> check;
                for(int j = adjust; j < adjust + 3; j++) {
                    for(int i = boxRow * 3; i < (boxRow * 3) + 3; i++) {
                        if(board[i][j] != '.') {
                            if(check.contains(board[i][j])) {
                                return false;
                            } else {
                                check[board[i][j]] = true;
                            }
                        }
                    }
                }
            }
        }

        return true;
    }
};
