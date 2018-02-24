#include <iostream>
using namespace std;

int main(){
    int board[3][3] = {{1,1,1},{1,1,1},{1,1,1}};
    int k = 0;
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(k % 2 == 0 and k > 0){
                board[i][j] = 1;
            }else{
                board[i][j] = 0;
            }
        }
    }
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << board[i][j];
        }
        cout << '\n';
    }
}
