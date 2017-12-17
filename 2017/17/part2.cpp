#include <list>
#include <iostream>
#include <algorithm>

using namespace std;

void print(list<int>& l) {
    for(const auto& i : l)
        cout << i << " ";
    cout << endl;
} 

list<int>::iterator move_fwd(list<int>::iterator iter, list<int>& l, size_t steps) {
    for(int i = 0; i < steps; ++i) {
        if(iter == l.end()) ++iter;
        ++iter; 
    }
    return iter;
}

int main(int argc, char** argv) {
    int steps = 328,
        max_value = 50'000'000,
        curpos = 0,
        after_val = 0;
    list<int> l = {0};
   
    auto iter = l.begin();
    for(size_t i = 1; i < max_value; ++i) {
        iter = move_fwd(iter, l, steps);
        l.insert(iter, i);
    }
    auto pos = find(l.begin(), l.end(), after_val);
    pos = move_fwd(pos, l, 1);
    cout << *pos << endl;

    return 0;
}
