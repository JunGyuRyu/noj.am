#include <stdio.h>
int main() {
    int a, b, c, d, e;
    scanf("%d%d", &a, &b);
    c = b % 10;
    d = b % 100;
    d = d / 10;
    e = b % 1000;
    e = e / 100;
    printf("%d\n", a * c);
    printf("%d\n", a * d);
    printf("%d\n", a * e);
    printf("%d\n", a * b);
}