#include <iostream>
#include <string>
using namespace std;

#define REP(i,a,b) for (int i = a; i < b; ++i)

int main(){
    long l;
    cin >> l;
    string mov;
    while(l){
        string dir = "+x";
        for(int i = 0; i < l-1; i++){
            cin >> mov;
            if(mov == "No"){continue;}
            if(mov[1] == 'y' and dir[1] == 'z'){continue;}
            if(mov[1] == 'z' and dir[1] == 'y'){continue;}
            if(mov[1] == dir[1]){if(mov[0] == dir[0]){dir = "-x";continue;}else{dir = "+x";continue;}}
            if(dir == "-x"){
                if(mov == "+y"){dir = "-y";}
                if(mov == "-y"){dir = "+y";}
                if(mov == "+z"){dir = "-z";}
                if(mov == "-z"){dir = "+z";}
                continue;
            }
            dir = mov;
        }
        cout << dir << '\n';
        cin >> l;
    }
}
