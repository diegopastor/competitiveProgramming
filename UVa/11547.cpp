#include <iostream>
using namespace std;

int main(){
    int t; 
    long long n;
    cin >> t;
    for(int i = 0; i < t; ++i){
        cin >> n;
        n = ((((n*567)/9+7492)*235)/47)-498;
        n = abs(n);
        cout << n/10%10 << '\n';
    }
}
