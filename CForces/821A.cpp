#include <iostream>
#include <string>
using namespace std;

#define REP(i,a,b) for (int i = a; i < b; ++i)

int main(){
    int n;
    int good;
    bool ans = true;
    int current;
    cin >> n;
    int lab[n][n];
    REP(x,0,n){REP(y,0,n){cin >> lab[x][y];}}
    REP(i,0,n){
        REP(j,0,n){
            current = lab[i][j];
            good = 0;
            if(current == 1){
                continue;
            }else{
                REP(k,0,n){
                    REP(l,0,n){
                        if(lab[k][j] + lab[i][l] == current){
                            good += 1;
                            break;
                        }
                    }
                }
                if(!good){
                    ans = false;
                }
            }
        }
    }
    if(ans){
        cout << "Yes\n";
    }else{
        cout << "No\n";
    }
}
