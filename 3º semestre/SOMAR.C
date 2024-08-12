#include <stdio.h>

int soma(float a , float b){
    printf("%d\n", a + b);
    return a + b;
}
int main(){
    float a = soma(1737.22,418.70 );
    printf("%d", a);
    return 0;
}