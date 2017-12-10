#include <set>
#include <iostream>
#include <sstream>

using namespace std;

int main() {
    int count = 0;
    string str;

get_passphrase:
    while(getline(cin, str)) {
        stringstream sstr(str);
        set<string> myset;
        string current;
        while(sstr >> current) {
            auto res = myset.insert(current);
            if(res.second != true)
               goto get_passphrase; 
        }
        ++count;
    } 
    cout << count << endl;
    return 0;
}
