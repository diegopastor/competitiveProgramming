#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int tc;
    int nums[3];
    cin >> tc;
    for(int i = 1; i < tc+1; i++){
        cin >> nums[0] >> nums[1] >> nums[2];
        sort(nums,nums+3);
        cout << "Case " << i << ": " << nums[1] << '\n';
    }
}

