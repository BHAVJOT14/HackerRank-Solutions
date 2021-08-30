#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
    int res = 0;
    
    for (int i = 1; i < n; i++) {
        for (int j = i+1; j < n+1; j++) {
            int tmp = i & j;
            if ((tmp < k) && (res < tmp))
                res = tmp;
        }
    }
    printf("%d\n", res);
    res = 0;
    
    for (int i = 1; i < n; i++) {
        for (int j = i+1; j < n+1; j++) {
            int tmp = i | j;
            if ((tmp < k) && (res < tmp))
                res = tmp;
        }
    }
    printf("%d\n", res);
    res = 0;
    
    for (int i = 1; i < n; i++) {
        for (int j = i+1; j < n+1; j++) {
            int tmp = i ^ j;
            if ((tmp < k) && (res < tmp))
                res = tmp;
        }
    }
    printf("%d\n", res);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
