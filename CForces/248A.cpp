#include <iostream>
using namespace std;

int main(){
    int n, a, b;
    int l = 0;
    int r = 0;
    cin >> n;
    for(int i = 0; i < n; ++i){
       cin >> a >> b; 
       l += a;
       r += b;
    }
    cout << min((n-l),(n-(n-l))) + min((n-r),(n-(n-r))) << '\n';
}
