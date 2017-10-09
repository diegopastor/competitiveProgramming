#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=0;i<t;++i){
        int max = 0;
        string s = to_string(i+1);
        int input;
        while((cin.peek()!='\n') && (cin >> input)){
            cout << input;
            if(input > max){
                max = input;
            }
        }
        string m = to_string(max);
        cout << "Case "+s+": "+m+"\n";
    }
}
