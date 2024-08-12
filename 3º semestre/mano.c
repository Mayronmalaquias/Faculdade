#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAM 10

int pilha[TAM];

int topo = 0;

void push(int valor){
    if(topo >= TAM){
        printf("pilha cheia");
    } else{
        pilha[topo++] = valor;
    }
}

void pop(){
    if (topo == 0){
        printf("sem elementos para remover!");
    } else {
        pilha[--topo];
    }
}

void mostrarPilha(){
    for (int i = 1; i <= topo; i++){
        printf("%d\n", pilha[topo - i]);
    } 
}
int main(){
    push(3);
    push(3);
    push(3);
    pop();
    push(78);
    mostrarPilha();

    return 0;
}