#include <string>
#include <map>
#include <cstdio>
#include <array>
#include <string>
#include <algorithm>
#include <numeric>
const size_t MIN_IN_DAY = 60;

using std::map;
using std::array; 
using time_day_array_t = array<int,MIN_IN_DAY>;
using time_map_t = map<int,time_day_array_t>;



void
fill_in_time(size_t start, size_t end, time_day_array_t& day) {
    for(size_t i = start; i < end; ++i)
        ++day[i];
}


int
main() {
    int year, mon, day, hour, min;
    char remainingLine[1000];

    time_map_t time_map;

    int current_guard;
    size_t sleep_start, sleep_done;
    while(scanf("[%d-%d-%d %d:%d] %[^\n]\n", &year, &mon, &day, &hour, &min, remainingLine) != EOF) {
        std::string line(remainingLine);

        size_t hash_find;
        if ((hash_find = line.find("#")) != std::string::npos) {
            current_guard = stoi(line.substr(hash_find + 1, 100));
        } else if (line.find("wakes") != std::string::npos) {
            sleep_done = min;
            fill_in_time(sleep_start, sleep_done, time_map[current_guard]);    
        } else if (line.find("asleep") != std::string::npos) {
            sleep_start = min;
        }
    }

    // guard -> max_minute
    std::map<int,int> guardMinute;

    int max_asleep = 0;
    int best_guard1 = -1;

    // part 2 vars
    int best_minute = -1;
    int best_guard2 = -1;
    int times_asleep = -1;

    for(const auto& kv : time_map) {
        // part 1 stuff
        int asleep = std::accumulate(kv.second.begin(), kv.second.end(), 0); 
        if (asleep > max_asleep) {
            best_guard1 = kv.first;
            max_asleep = asleep;
        }

        auto max_ele = std::max_element(kv.second.begin(), kv.second.end());
        if (*max_ele > times_asleep) {
            best_guard2 = kv.first;
            times_asleep = *max_ele;
            best_minute = max_ele - kv.second.begin();
        }
    }

    const auto& kv = time_map[best_guard1];
    int best_minute1 = std::max_element(kv.begin(), kv.end()) - kv.begin();

    printf("%d * %d = %d\n", best_guard1, best_minute1, best_guard1 * best_minute1);
    printf("%d * %d = %d\n", best_guard2, best_minute, best_guard2 * best_minute);


    return EXIT_SUCCESS;
}
