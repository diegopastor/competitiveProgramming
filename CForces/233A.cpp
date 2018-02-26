#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int nums[n];
    int t = 0;
    if(n % 2 == 0){
        for(int i = 0; i < n; ++i){
            nums[i] = i+1;
        }
        for(int i = 0; i < n-1; i += 2){
           t = nums[i];
           nums[i] = nums[i+1];
           nums[i+1] = t;
        }
        for(int i = 0; i < n; ++i){
            cout << nums[i] << " ";
        }
        cout << '\n';
    }else{
        cout << -1 << '\n';
    }
}
