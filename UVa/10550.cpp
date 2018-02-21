#include <iostream>
using namespace std;

int main(){
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    while(a || b || c || d){
        int deg = 1080;
        deg += (a - b) > 0 ? (a - b) * 9 : (a - b + 40) * 9;
        deg += (c - b) > 0 ? (c - b) * 9 : (c - b + 40) * 9;
        deg += (c - d) > 0 ? (c - d) * 9 : (c - d + 40) * 9;
        cout << deg << '\n';
        cin >> a >> b >> c >> d;
    }
}
