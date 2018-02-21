#include <iostream>
using namespace std;

int main(){
    int price, coin;
    cin >> price >> coin;
    if(price % 10 == 0 or (price - coin) % 10 == 0){
        cout << 1 << '\n';
    }else{
        for(int i = 2; i < 11; i++){
            if((price * i) % 10 == 0 or (((price * i))-coin) % 10 == 0){
                cout << i << '\n';
                break;
            }
        }
    }
}

