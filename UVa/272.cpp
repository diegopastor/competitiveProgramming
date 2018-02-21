#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    string quote;
    bool left = true;
    int pos = 0;
    while(getline(cin,quote)){
        while(quote.find("\"") != -1){;
            if(left){
                pos = quote.find("\"");
                quote.erase(pos, 1); 
                quote.insert(pos, ("``"));
                left = false;
            }else{
                pos = quote.find("\"");
                quote.erase(pos, 1); 
                quote.insert(pos, ("''"));
                left = true;
            }
        }
        cout << quote << '\n';
    }
}
