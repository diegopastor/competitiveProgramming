#include <iostream>
#include <string>
using namespace std;

int main(){
    int n;  
    cin >> n;
    bool s = true;
    string end = "it";
    string phrase = "I hate "; 
    string hate = "that I hate ";
    string love = "that I love ";
    for(int i = 1; i < n; i++){
       if(s){
          phrase += love; 
          s = false;
       }
       else{
           phrase += hate;
           s = true;
       }
    }
    phrase += end;
    cout << phrase << endl;
}
