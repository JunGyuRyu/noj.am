#include<stdio.h>
int main(){
    int a,b;
    scanf("%d%d",&a,&b);
    if(a>0){
        if(b>0){
            printf("1\n");
        }
        else{
            printf("4\n");
            }
    }
    else if(a<0){
        if(b>0){
            printf("2\n");
        }
        else{
            printf("3\n");
            }
    }
}