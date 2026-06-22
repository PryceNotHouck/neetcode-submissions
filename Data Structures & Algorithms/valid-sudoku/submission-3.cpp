// Redo - Single Pass
#include <map>
#include <set>

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        map<int, set<char>> rows;
        map<int, set<char>> cols;
        map<pair<int, int>, set<char>> squares;
        
        for(int i = 0; i < board.size(); i++) {
            for(int j = 0; j < board[0].size(); j++) {
                pair<int, int> square = {i / 3, j / 3};
                if(board[i][j] != '.') {
                    if(rows[i].contains(board[i][j]) ||
                    cols[j].contains(board[i][j]) ||
                    squares[square].contains(board[i][j])) {
                        return false;
                    }
                }
                
                rows[i].insert(board[i][j]);
                cols[j].insert(board[i][j]);
                squares[square].insert(board[i][j]);
            }
        }
        return true;
    }
};
