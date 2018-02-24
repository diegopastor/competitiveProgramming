#include <iostream>
using namespace std;

int main(){
    int board[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
    int k = 0;
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cin >> k; 
            for(int l = 0; l < k; l++){
                    if(i == 0 and j == 0){
                        board[i][j] += 1;
                        board[i][j+1] += 1;//Derecha
                        board[i+1][j] += 1;//Abajo
                    }
                    if(i == 0 and j == 1){
                        board[i][j] += 1;
                        board[i][j+1] += 1;//Derecha
                        board[i][j-1] += 1;//Izquierda
                        board[i+1][j] += 1;//Abajo
                    }
                    if(i == 0 and j == 2){
                        board[i][j] += 1;
                        board[i][j-1] += 1;//Izquierda
                        board[i+1][j] += 1;//Abajo
                    }
                    if(i == 1 and j == 0){
                        board[i][j] += 1;
                        board[i-1][j] += 1;//Arriba
                        board[i][j+1] += 1;//Derecha
                        board[i+1][j] += 1;//Abajo
                    }
                    if(i == 1 and j == 1){
                        board[i][j] += 1;
                        board[i-1][j] += 1;//Arriba
                        board[i+1][j] += 1;//Abajo
                        board[i][j+1] += 1;//Derecha
                        board[i][j-1] += 1;//Izquierda
                    }
                    if(i == 1 and j == 2){
                        board[i][j] += 1;
                        board[i-1][j] += 1;//Arriba
                        board[i][j-1] += 1;//Izquierda
                        board[i+1][j] += 1;//Abajo
                    }
                    if(i == 2 and j == 0){
                        board[i][j] += 1;
                        board[i-1][j] += 1;//Arriba
                        board[i][j+1] += 1;//Derecha
                    }
                    if(i == 2 and j == 1){
                        board[i][j] += 1;
                        board[i-1][j] += 1;//Arriba
                        board[i][j-1] += 1;//Izquierda
                        board[i][j+1] += 1;//Derecha
                    }
                    if(i == 2 and j == 2){
                        board[i][j] += 1;
                        board[i-1][j] += 1;//Arriba
                        board[i][j-1] += 1;//Izquierda
                    }
            }
        }
    }
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(board[i][j] % 2 == 0){
                cout << 1; 
            }else{
                cout << 0; 
            }
        }
        cout << '\n';
    }
}
