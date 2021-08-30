#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define MAX_LEN 128

int main() 
{
    char ch;
    char word[MAX_LEN];
    char sen[MAX_LEN];
    
    scanf("%c", &ch);
    scanf("%s\n", &word);
    scanf("%[^\n]%*c", &sen);
    
    printf("%c\n", ch);
    printf("%s\n", word);
    printf("%s\n", sen);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
