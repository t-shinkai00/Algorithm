#include<stdio.h>
void selection_sort(int n, int a[]){
  int i, j, k, m, t;
  for(i = 0; i < n-1; i++){
    for(t = 0; t < n; t++)
      printf("%d ", a[t]);
    printf("\n");
    m = a[i]; k = i;
    for(j = i+1; j < n; j++){
      if(a[j] < m){
        m = a[j]; k = j;
      }
    }
    a[k] = a[i]; a[i] = m;
  }
}

int main(void){
  int arr[5]={3,5,2,1,4},t;
  selection_sort(5,arr);
  for(t = 0; t < 5; t++)
    printf("%d ", arr[t]);
  printf("\n");
  return 0;
}