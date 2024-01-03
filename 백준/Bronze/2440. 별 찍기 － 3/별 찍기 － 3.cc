#include<stdio.h>
int main(){
    int a;
    scanf("%d",&a);
    for(a;a>=1;a--){
    for(int i=1;i<=a;i++){
        printf("*");
    }
    printf("\n");
    }
}