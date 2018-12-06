#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>

using std::cin;
using std::cout;
using std::string;
using std::getline;
using std::endl;

inline bool
areOppositeCharacters(char a, char b) {
    return std::max(a, b) - std::min(a, b) == 32; 
}

size_t
collapse(string line) {
    bool reactionHappened;
    do {
        reactionHappened = false;
        for(auto it = line.begin(); it != line.end(); ++it) {
            if (areOppositeCharacters(*it, *(it + 1))) {
                line.erase(it, it+2);
                reactionHappened = true;
                break;
            }
        }
    } while(reactionHappened);
    return line.size();
}

string
removeUnitType(char c, string s) {
    char r1 = tolower(c), r2 = toupper(c);

    auto it = s.begin();
    while (it != s.end()) {
        if(*it == r1 || *it == r2)
            s.erase(it);
        else
            ++it;
    }
    return s;
}

int 
main() {
    string line;
    getline(cin, line);

    std::unordered_set<char> unit_chars;
    for(char c : line) {
        unit_chars.insert(tolower(c));
    } 

    size_t min_len = collapse(line);
    cout << "Part 1: " << min_len << endl;

    for(auto it = unit_chars.begin(); it != unit_chars.end(); ++it) {
        size_t guess = collapse(removeUnitType(*it, line));
        
        min_len = std::min(guess, min_len); 
    }

    cout << "Part 2: " << min_len << endl;
    return EXIT_SUCCESS; 
}
