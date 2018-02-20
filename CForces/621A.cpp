#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
typedef unsigned long long ull;
using namespace std;

bool odd(int n){
    if(n&1){
        return true;
    }else{
        return false;
    }
}

int main(){
    int n;
    cin >> n;
    ull num = 0;
    ull smallest = (ull) -1;
    ull sum = 0;
    for(int i = 0; i < n; i++){
        cin >> num;
        if(odd(num)){
            sum += num;
            smallest = min(smallest, num);
        }else{
            sum += num;
        } 
    }
    if(odd(sum)){
        sum -= smallest;
    }
    cout << sum << '\n';
}
