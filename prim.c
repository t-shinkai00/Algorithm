#include "stdio.h"

//定数
#define MAX_VALUE 1000000
#define INF MAX_VALUE-1
#define MAX_SIZE 7

int main()
{
	int closest[MAX_SIZE] = {0,0,0,0,0,0,0};
	int low_cost[MAX_SIZE] = {0,0,0,0,0,0,0};
	int total_cost = 0;
	//隣接行列
	int weight[MAX_SIZE][MAX_SIZE] = {
		{INF,   8,   5,   1, INF, INF, INF},
		{  8, INF, INF,   6,   2, INF, INF},
		{  5, INF, INF,   6, INF,   4, INF},
		{  1,   6,   6, INF,   4,   3,   5},
		{INF,   2, INF,   4, INF, INF,   3},
		{INF, INF,   4,   3, INF, INF,   7},
		{INF, INF, INF,   5,   3,   7, INF},
	};
	//初期化
	int i;
	for(i=1;i<MAX_SIZE;i++){
		low_cost[i] = weight[0][i];
	}
	//頂点の選択
	int min;
	int j,k;
	for(i=1;i<MAX_SIZE;i++){
		min = low_cost[1];
		k = 1;
		for(j=2;j<MAX_SIZE;j++){
			if(min > low_cost[j]){
				min = low_cost[j];
				k = j;
			}
		}
		total_cost += low_cost[k];
		printf("%d-%d  %d\n",k,closest[k],low_cost[k]);
		low_cost[k] = MAX_VALUE;
		for(j=1;j<MAX_SIZE;j++){
			if(low_cost[j] < MAX_VALUE && low_cost[j] > weight[k][j]){
				low_cost[j] = weight[k][j];
				closest[j] = k;
			}
		}
	}
	printf("total cost = %d\n",total_cost);
return 0;
}