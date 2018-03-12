#include <iostream>
#include <string>
using namespace std;

int main(){
    string x;
    int c = 0;
    while(true){
        ++c;
        cin >> x;
        if(x == "Hajj"){
            cout << "Case " << c << ":" << " Hajj-e-Akbar" << '\n';
        }
        if(x == "Umrah"){
            cout << "Case " << c << ":" << " Hajj-e-Asghar" << '\n';
        }
        if(x == "*"){
            break;
        }
    }
}
