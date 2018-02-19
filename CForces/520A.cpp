#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int main(){
    int size;
    string sentence;
    cin >> size >> sentence;
    transform(sentence.begin(), sentence.end(), sentence.begin(), ::tolower);
    map <char, int> letters;

    for(char& c : sentence){
        letters[c] ++;
        /*
        if(letters.count(c) == 0){
            letters.insert(pair <char, int> (c, 0))
        }else{
            
        }
        */
    }
    if(letters.size() == 26){
        cout << "YES" << '\n';
    }else{
        cout << "NO" << '\n';
    }
}

