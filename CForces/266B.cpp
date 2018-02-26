#include <iostream>
#include <string>
using namespace std;

int main(){
    int n, t;
    string q; 
    cin >> n >> t >> q;
    for(int i = 0; i < t; i++){
        for(int j = 0; j < q.length()-1; j++){
            if(q[j] == 'B' and q[j+1] == 'G'){
                q[j] = 'G';
                q[j+1] = 'B';
                j++;
            }
        }
    }
    cout << q << '\n';
}
