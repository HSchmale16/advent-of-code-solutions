#include <stdint.h>
#include <stdio.h>

int64_t gen_A_1() {
    static int64_t prev = 703;
    int64_t factor = 16807;
    int64_t mod = 2147483647;
    return prev = prev * factor % mod;
}

int64_t gen_B_1() {
    static int64_t prev = 516;
    int64_t factor = 48271;
    int64_t mod = 2147483647;
    return prev = prev * factor % mod;
}

int64_t gen_A_2() {
    static int64_t prev = 703;
    int64_t factor = 16807;
    int64_t mod = 2147483647;
    do { prev = prev * factor % mod; } while (prev % 4 != 0);
    return prev;
}

int64_t gen_B_2() {
    static int64_t prev = 516;
    int64_t factor = 48271;
    int64_t mod = 2147483647;
    do { prev = prev * factor % mod; } while (prev % 8 != 0);
    return prev;
}

int main() {
    int64_t a, b, MASK_16 = (1 << 16) - 1, count = 0;
    for(int64_t i = 0; i < 5000000; ++i) {
        a = gen_A_2();
        b = gen_B_2();
        if((a & MASK_16) == (b & MASK_16)) ++count;
    }
    printf("%d\n", count);
    return 0;
}