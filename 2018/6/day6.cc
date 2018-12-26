#include <array>
#include <map>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>

const size_t GRID_SIZE = 1000;
using std::array;


struct GridPoint {
    int owner = -1;
};

using Grid = std::array<std::array<GridPoint, GRID_SIZE>, GRID_SIZE>; 



struct Coord {
    int x, y;
    bool infinite = false;
    
    Coord (int x0, int y0) : x(x0), y(y0) {}
};

inline int
manhatten(const Coord& a, int x, int y) {
    return abs(a.x - x) + abs(a.y - y);
}

int
determineOwner(int x, int y, const std::vector<Coord>& coords) {
    // Distance -> List<CoordId> 
    std::map<int, std::vector<int>> distances; 
    for (int i = 0; i < coords.size(); ++i) {
        int dis = manhatten(coords[i], x, y);
        distances[dis].push_back(i); 
        if (distances[dis].size() > 1)
            return -1;
    }
    auto p = *distances.begin();
    return p.second[0];
} 

void
dumpGrid(const Grid& g) {
    for (auto rows : g) {
        for (auto col : rows) {
            printf("%02d ", col.owner);
        }
        printf("\n");
    }
}

array<int, 4>
determineInfiniteCoords (std::vector<Coord>& coords) {
    array<int, 4> vals;
    
    auto CompareX = [](auto a, auto b) {
        return a.x < b.x;
    };
    auto xmin = std::minmax_element(coords.begin(), coords.end(), CompareX); 

    auto CompareY = [](auto a, auto b) {
        return a.y < b.y;
    };
    auto ymin = std::minmax_element(coords.begin(), coords.end(), CompareY); 

    return vals;
}

int 
main() {
    std::vector<Coord> coords;
    Grid grid;

    {
        int x, y;
        while (scanf("%d, %d\n", &x, &y) != EOF) {
            coords.push_back(Coord(x, y));
        } 
    }



    auto x = determineInfiniteCoords(coords);
    for (int i = x[2]; i < x[3]; ++i) {
        for (int j = x[0]; j < x[1]; ++j) {
            int owner = determineOwner(i, j, coords);
            // flip flop so rendered right
            grid[j][i].owner = owner;
        }
    }

    // Count by owner
    std::map<int,size_t> counts; 
    for (int i = 0; i < GRID_SIZE; ++i) {
        for (int j = 0; j < GRID_SIZE; ++j) {
            counts[grid[i][j].owner]++;
        }
    }

    int max_area = 0;
    int max_value = -1;
    for (const auto& p : counts) {
        if (p.first != -1 && !coords[p.first].infinite && p.second < 11412) {
            if (p.second > max_area) {
                max_area = p.second;
                max_value = p.first;
            } 
        }
    } 
    
    printf("max-area=%d, max-value=%d\n", max_area, max_value);

    return 0;
}
