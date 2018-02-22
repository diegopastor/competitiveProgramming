#include <iostream>
using namespace std;

int main(){
    int k, xd, yd, xp, yp;
    cin >> k;
    while(k){
        cin >> xd >> yd;
        for(int i = 0; i < k; i++){
            cin >> xp >> yp;
            if(xp == xd or yp == yd){
                cout << "divisa" << '\n';
            }
            if(xp < xd and yp > yd){
                cout << "NO" << '\n';
            }
            if(xp > xd and yp > yd){
                cout << "NE" << '\n';
            }
            if(xp < xd and yp < yd){
                cout << "SO" << '\n';
            }
            if(xp > xd and yp < yd){
                cout << "SE" << '\n';
            }
        }
        cin >> k;
    }
}
