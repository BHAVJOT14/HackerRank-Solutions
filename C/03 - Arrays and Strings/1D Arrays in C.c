#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    int sizeArr;
    int sum = 0;
    int *arr;
    
    scanf("%d", &sizeArr);
    
    arr = (int*) malloc(sizeArr * sizeof(int));
    
    for (int i = 0; i <= sizeArr; i++) {
        scanf("%d", &arr[i]);
    }   
    
    for (int i = 0; i < sizeArr; i++) {
          sum += arr[i];
    }
    
    printf("%d\n", sum);
    
    free(arr);
    
    return 0;
}