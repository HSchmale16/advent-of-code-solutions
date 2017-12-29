#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include "utils.h"

using namespace std;

vector<string> split (const string &s, char delim) {
    stringstream ss (s);
    string item;
    vector<string> tokens;
    while (getline (ss, item, delim)) {
        tokens.push_back (item);
    }
    return tokens;
}

struct LadderPiece {
    int u, v;

    LadderPiece ()
    : u (0), v(0) {}

    LadderPiece (string s) {
        char c;
        stringstream sstr (s);
        sstr >> u >> c >> v;
    }

    bool operator== (const LadderPiece& p) {
        return u == p.u && v == p.v;
    }
};

struct SolutionTree {
    vector<SolutionTree> childs;
    LadderPiece value;
};

void sumTreeBranch (const SolutionTree& t, vector<unsigned>& v, int value) {
    if(t.childs.empty()) {
        v.push_back(value + t.value.u + t.value.v);
    }
    for (const SolutionTree& c : t.childs) {
        sumTreeBranch(c, v, value + t.value.u + t.value.v);
    }
}

void treeDepths(const SolutionTree& t, vector<unsigned>& v, int value) {
    if(t.childs.empty()) {
       v.push_back(value + 1);
    }
    for (const SolutionTree& c : t.childs) {
        treeDepths(c, v, value + 1);
    }
}

void buildTree (const vector<LadderPiece>& available, int last, SolutionTree& parent) {
    auto possible_nexts = filter (available, [&](LadderPiece p) { return p.u == last || p.v == last; });
    for (auto p : possible_nexts) {
        int next = (p.u == last) ? p.v : p.u;
        vector<LadderPiece> v (available.begin(), available.end());
        v.erase (find(v.begin(), v.end(), p));
        SolutionTree t;
        t.value = p;
        buildTree (v, next, t);
        parent.childs.push_back (t);
    }
}

int main (int argc, char** argv)
{
    string s;
    vector<LadderPiece> pieces;
    while (cin >> s) {
        pieces.push_back (LadderPiece(s));
    }
    SolutionTree t;
    buildTree (pieces, 0, t);
    

    vector<unsigned> strs, lens;
    sumTreeBranch(t, strs, 0);
    treeDepths(t, lens, 0);

    cout << *max_element(strs.begin(), strs.end()) << endl;
    unsigned max_length = *max_element(lens.begin(), lens.end());
    for(size_t i = 0; i < lens.size(); ++i) {
        if (lens[i] == max_length) {
            cout << strs[i] << " " << lens[i] << endl;
        }
    }
    
    return 0;
}
