#include <iostream>
using namespace std;

int main(){
    int n, m; 
    int primes[15] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
    bool a = false;
    cin >> n >> m;
    for(int i = 0; i < 14; i++){
        if(primes[i] == n and primes[i+1] == m){
            a = true;
        }
    }
    if(a){
        cout << "YES" << '\n';
    }else{
        cout << "NO" << '\n';
    }
}
