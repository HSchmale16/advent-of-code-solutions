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

int sumTreeBranch (const SolutionTree& t, vector<unsigned>& v, int value) {
    if(t.childs.empty()) {
        v.push_back(value + t.value.u + t.value.v);
        return 0;
    }
    for (SolutionTree c : t.childs) {
        sumTreeBranch(c, v, value + t.value.u + t.value.v);
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
    

    vector<unsigned> vals;
    sumTreeBranch(t, vals, 0);

    cout << *max_element(vals.begin(), vals.end()) << endl;

    return 0;
}
