#include <vector>
#include <algorithm>
#include <cstdio>
#include <utility>
#include <cmath>

using namespace std;

inline size_t
taxicab(pair<int,int> a, pair<int,int> b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}

int
owner(pair<int,int> point, vector<pair<int,int>> points) {
    int minValue = 1000000;
    int prevMin = 0;
    int minOwner = -1;
    for (int i = 0; i < points.size(); ++i) {
        size_t dis = taxicab(point, points[i]);
        if (dis <= minValue) {
            prevMin = minValue;
            minValue = dis;
            minOwner = i;
        }
    }
    if (prevMin == minValue)
        return -1;
    return minOwner;
}

int
main() {
    vector<pair<int,int>> pairs;

    int x, y;
    while(scanf("%d, %d\n", &x, &y) != EOF) {
        pairs.push_back({x,y});
    }
    int grid[400][400] = {-1};
    
    for(int i = 0; i < pairs.size(); ++i) {
        grid[pairs[i].first][pairs[i].second] = i;
    }


    for (int i = 0; i < 400; ++i) {
        for(int j = 0; j < 400; ++j) {
            if (grid[i][j] == -1) {
                grid[i][j] = owner({i, j}, pairs);        
            }
        }
    }
    
    vector<bool> failures(pairs.size());
    for (int i = 0; i < 400; ++i) {
        failures[grid[i][0]] = true;
        failures[grid[0][i]] = true;
        failures[grid[399][i]] = true;
        failures[grid[i][399]] = true;
    } 

    vector<size_t> counts(pairs.size()); 

    for (int i = 0; i < 400; ++i) {
        for(int j = 0; j < 400; ++j) {
            counts[grid[i][j]]++;
        }
    }

    int maxValue = 0;

    for (int i = 0; i < pairs.size(); ++i) {
        if (!failures[i] && counts[i] > maxValue) {
            maxValue = counts[i];
        }
    }
    printf("%d\n", maxValue);

    return EXIT_SUCCESS;
}
