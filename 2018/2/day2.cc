#include <string>
#include <iostream>
#include <vector>
#include <cassert>
#include <utility>

using std::cin;
using std::endl;
using std::cout;
using std::vector;
using std::string;

int
diff(const std::string& a, const std::string& b) {
    assert(a.size() == b.size());

    int count = 0;
    int start = 0;
    int i;
    for (i = 0; i < a.size() && start == 0; ++i)
        if(a[i] != b[i]) {
            ++count;
            start = i;
        }
    for (; i < a.size(); ++i)
        if(a[i] != b[i]) 
            ++count;

    return {start, count};
}

std::string
produceCommon(const string& a, const string& b) {
    assert(a.size() == b.size());

    string common;
    for(int i = 0; i < a.size(); ++i) {
        if(a[i] == b[i])
            common += a[i];
    }

    return common;
}


int
main() {
    vector<string> strs;

    std::string str;
    while(std::getline(cin, str))
        strs.push_back(str);

    int diffVal = -1; 
   
    for(int i = 0; i < strs.size(); ++i) {
        for(int j = i; j < strs.size(); ++j) {
            if (diff(strs[i], strs[j]).second == 1) {
                cout << produceCommon(strs[i], strs[j]) << endl; 
            } 
        }
    } 

    return EXIT_SUCCESS;
}
