#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    double d;
    long l;
    char ch;
    int i;
    float f;
    scanf("%d %ld %c %f %lf", &i, &l, &ch, &f, &d);
    printf("%d\n%ld\n%c\n%f\n%lf", i, l, ch, f, d);

    return 0;
}
