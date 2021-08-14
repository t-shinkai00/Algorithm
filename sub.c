#include <stdio.h>

int main() {
    int i, j, k, flag = 0;

    for (i = 0; i < 10; i++) {
        for (j = 0; j < 10; j++) {
            for (k = 0; k < 10; k++) {
                if ((i * 100 + j * 10 + k) - (k * 100 + j * 10 + i) == 594) {
                    printf("(i, j, k) = (%d, %d, %d)\n", i, j, k);
                    flag = 1;
                }
            }
        }
    }

    if (!flag) {
        printf("条件を満たすi、j、kの組み合わせはありません。\n");
    }
}