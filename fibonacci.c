#include <stdio.h>

int fib(n){
    int i,c1=0,c2=1,s=1;//c1=fib[n-2],c2=fib[n-1],s=fib[n]
    if(n==0|n==1)return n;
    else{
        for(i=2;i<n;i++){
            c1=c2;
            c2=s;
            s=c1+c2;
        }
        return s;
    }
}
int main(void){
    int n;
    scanf("%d",&n);
    printf("%d\n",fib(n));
    return 0;
}