#include <iostream>
using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    int ans = 0;
    int scores[n+2];
    for(int i = 0; i < n; i++){
        cin >> scores[i];
    }
    for(int j = 0; j < n; j++){
        if(scores[j] >= scores[k-1] && scores[j] > 0){
            ans += 1;
        }
    }
    cout << ans << '\n';
}

