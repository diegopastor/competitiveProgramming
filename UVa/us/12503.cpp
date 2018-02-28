#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(){
    int t, c;
    int ans;
    string inst; 
    cin >> t;
    for(int i = 0; i < t; ++i){
        ans = 0;
        cin >> c;
        for(int j = 0; j < c; j++){
            map<int, int> memory;
            getline(cin, inst);
            if(inst == "LEFT"){
                memory[j] = -1;
                ans -= 1;
            }
            if(inst == "RIGHT"){
                memory[j] = 1;
                ans += 1;
            }else{
                ans += memory[inst[inst.length()]];
            }
        }
        cout << ans << '\n';
    }
}
