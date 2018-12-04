#include <cstdio>
#include <vector>
#include <map>
#include <unordered_map>
#include <numeric>

using std::map;
using std::unordered_map;
using std::vector;

struct pairhash {
    template<typename T, typename U>
    std::size_t operator()(const std::pair<T, U>& x) const {
        return (size_t)(x.first) << 32 | (size_t)(x.second); 
    }
};



using fabric_t = std::unordered_map<std::pair<int,int>,vector<int>,pairhash>;
using overlap_t = std::vector<bool>;

void
applyOverlap(overlap_t& overlap, const vector<int>& ids) {
    for(const int& id : ids)
        overlap[id] = true;
}


int
main() {
    // if true then has some overlap 
    overlap_t overlapping(100000);
    fabric_t fabric;

    int id, x, y, w, h; 
    while(scanf("#%d @ %d,%d: %dx%d\n", &id, &x, &y, &w, &h) != EOF) {
        for(int x0 = x; x0 < x + w; ++x0) {
            for(int y0 = y; y0 < y + h; ++y0) {
                fabric[{x0,y0}].push_back(id);
                if (fabric[{x0, y0}].size() > 1)
                   applyOverlap(overlapping, fabric[{x0, y0}]); 
            }
        }
    }
 
    int count = 0;
    for (auto pair : fabric) {
        if (pair.second.size() > 1)
           ++count; 
    }
    
    // absolutely gross but it works    
    int i;
    for(i = 1; i < overlapping.size() && overlapping[i]; ++i);


    printf("%d %d\n", count, i);

    return EXIT_SUCCESS;
}
