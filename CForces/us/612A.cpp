#include <iostream>
#include <vector>
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
    vector<int> odds;
    cin >> n;
    int num = 0;
    unsigned long long sum = 0;
    for(int i = 0; i < n; i++){
        cin >> num;
        if(odd(num)){
            odds.push_back(num);
                if(odds.size() == 2){
                    sum += odds[0];
                    sum += odds[1];
                    odds.erase(odds.begin(),odds.end());
                }
        }else{
            sum += num;
        } 
    }
    
    cout << sum << '\n';
}

