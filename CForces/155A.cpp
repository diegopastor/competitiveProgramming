#include <iostream>
using namespace std;

int main(){
    int n, t;
    int mx = -1;
    int mn = 10001;
    int ans = -2;
    cin >> n;
    for(int i = 0; i < n; ++i){
        cin >> t;
        if(t > mx){
            mx = t;
            ans += 1;
        }
        if(t < mn){
            mn = t;
            ans += 1;
        }
    }
    cout << ans << '\n';
}
