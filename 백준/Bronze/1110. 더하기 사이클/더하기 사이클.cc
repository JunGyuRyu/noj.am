#include<stdio.h>
int main() {
	int a,ten,one,i=0,j,num=9999;
	scanf("%d", &a);
	ten = a / 10;
	one = a % 10;
	for (i; num != a;++i) {
		j = ten + one;
		num = one * 10 + j % 10;
		ten = num / 10;
		one = num % 10;}
	printf("%d\n", i);}