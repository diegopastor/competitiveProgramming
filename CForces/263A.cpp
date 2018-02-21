#include <iostream>
using namespace std;

int main(){
    int x;
    int y;
    int a;
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
           cin >> a;
           if(a == 1){
               x = i;
               y = j;
               break;
           }
        }
    }
    int ans = abs(x - 2) + abs(y - 2);
    cout << ans << '\n';
}

