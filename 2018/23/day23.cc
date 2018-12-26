#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

struct Bot {
    int x,y,z,r;
};

struct BotBounds {
    int lowX, highX;
    int lowY, highY;
    int lowZ, highZ;
};

inline int
manhatten(const Bot& a, const Bot& b) {
    return abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z); 
}

inline size_t 
number_in_range(const std::vector<Bot>& bots, const Bot& point) {
    size_t count = 0;    
    for (const auto& b : bots) {
        if (manhatten(b, point) <= point.r) {
            ++count;
        }
    } 
    return count;
}

inline size_t 
bot_range_of_point(const std::vector<Bot>& bots, const Bot& point) {
    size_t count = 0;    
    for (const auto& b : bots) {
        if (manhatten(b, point) <= b.r) {
            ++count;
        }
    } 
    return count;
}


BotBounds
determineBounds(const std::vector<Bot>& bots) {
    auto x = std::minmax_element(bots.begin(), bots.end(), [] (auto a, auto b) {
                return a.x < b.x;
            }); 
    auto y = std::minmax_element(bots.begin(), bots.end(), [] (auto a, auto b) {
                return a.y < b.y;
            }); 
    auto z = std::minmax_element(bots.begin(), bots.end(), [] (auto a, auto b) {
                return a.z < b.z;
            }); 

    return {x.first->x, x.second->x,
            y.first->y, y.second->y,
            z.first->z, z.second->z};
}

int
main() {
    int x, y, z, r;
    std::vector<Bot> bots;
    while (scanf("pos=<%d,%d,%d>, r=%d\n", &x, &y, &z, &r) != EOF) {
        bots.push_back({x,y,z,r});
    }

    auto max_range_bot = *std::max_element(bots.begin(), bots.end(), [](const auto a, const auto b) {
        return a.r < b.r;
    });

    size_t count = number_in_range(bots, max_range_bot); 
    printf("Part 1: %d\n", count);


    BotBounds bounds = determineBounds(bots);
    int distance; 
    int botCount = 0;
    for (int x = bounds.lowX; x <= bounds.highX; ++x) {
        for (int y = bounds.lowY; y <= bounds.highY; ++y) {
            for (int z = bounds.lowZ; z <= bounds.highZ; ++z) {
                size_t count = bot_range_of_point(bots, {x, y, z, 0});
                if (count > botCount) {
                    botCount = count;
                    distance = manhatten({x,y,z,0}, {0,0,0,0});
                }
            }
        }
    }
    printf("Part 2: %d\n", distance);

    return EXIT_SUCCESS;
}
