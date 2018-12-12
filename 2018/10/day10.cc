#include <cstdlib>
#include <cstdio>


int
main() {
    int px, py, vx, vy;
    while(scanf("position=<%d,%d> velocity=<%d,%d>\n", &px, &py, &vx, &vy) != EOF) {
        printf("%d %d %d %d\n", px, py, vx, vy);
    }

    return EXIT_SUCCESS;
}
