#include <cstdio>
#include <vector>

struct vec3 {
    int x, y, z;
};

struct particle {
    static int next_id;
    int id;
    vec3 p,v,a;

    particle() 
    : id(next_id++) {}
};
int particle::next_id = 0;


struct particleResult {
    bool notDone = false;
    particle p;
};

particleResult
readParticle(FILE* f) {
    const char* pattern = "p=<%d,%d,%d>, v=<%d,%d,%d>, a=<%d,%d,%d>";
    particle p;
    char res;
    res = fscanf(f, pattern, 
            &p.p.x, &p.p.y, &p.p.z, 
            &p.v.x, &p.v.y, &p.v.z, 
            &p.a.x, &p.a.y, &p.a.z);
    printf("%d %d\n", p.p.x, p.v.x);
    return particleResult{res != EOF, p};
}

int
main() {
    FILE* input = fopen("input.txt", "r"); 
    particleResult pr;
    std::vector<particle> particles;
    particles.reserve(5000);
    while((pr = readParticle(input)).notDone) {
        printf("%d\n", pr.p.p.x);
    }

}
