#include <iostream>
using namespace std;

int main(){
    int b = 1;
    int n = 1;
    int mov[5];
    char ans = 'S';
    while(cin >> b >> n){
        ans = 'S';
        int res[b+5];
        for(int i = 0; i < b; i++){
            cin >> res[i];
        }
        for(int i = 0; i < n; i ++){
            cin >> mov[0] >> mov[1] >> mov[2];
            res[mov[0]-1] -= mov[2];
            res[mov[1]-1] += mov[2];
        }
        if(res[0] < 0 or res[1] < 0 or res[2] < 0){
            ans = 'N';
        }
        if(b != 0){
            cout << ans << '\n';
        }
    }
}
