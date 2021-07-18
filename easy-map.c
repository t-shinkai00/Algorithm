#include<stdio.h>
#include<string.h>
#define N 50
int i=0;
int map(){
    i=(i+1)%N;
    return i;
}
int main(void){
    int j;
    for(j=0;j<100;j++)
        printf("%d\n",map());
    return 0;
}