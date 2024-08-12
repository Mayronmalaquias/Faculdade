#include <stdio.h>
#include <stdlib.h>

typedef struct registro{
    int valor;
    struct registro *prox;
}registro;


typedef struct fila{
    int qtd;
    registro *inicio;
    registro *fim;
}fila;

registro* criaRegistro(){
    registro *p;
    p = (registro *)malloc(sizeof(registro));
    p->valor = 0;
    p->prox = NULL;
    return p;
}

fila* criaFila(){
    fila *p;
    p = (fila *)malloc(sizeof(fila));
    p->qtd = 0;
    p->inicio = NULL;
    p->fim = NULL;
    return p;
}

void push(int novo, fila *a){
    registro *aux;
    aux = criaRegistro();
    aux->valor = novo;
    if(a == NULL){
        printf("nao existe fila");
    }
    if(a->inicio == NULL && a->fim == NULL){
        a->inicio = aux;
        a->fim = aux;
    }else{
        a->fim->prox = aux;
        a->fim = aux;
    }

}

void pop(fila *a){
    registro *aux;
    if(a == NULL){
        printf("fila não existe");
    }
    if(a->inicio == NULL && a->fim == NULL){
        printf("\nnao ha elementos para percorrer");
    } else{
        aux = a->inicio;
        if(aux->prox == NULL){
            a->fim = NULL;
            a->inicio = NULL;
            free(aux);
            return;
        }
        a->inicio = a->inicio->prox;
        free(aux);
    }
}

void stackpop(fila *a){
    if(a == NULL){
        printf("fila nao existe");
    }
    registro *aux;
    if(a->inicio == NULL && a->fim == NULL){
        printf("nao ha elementos na fila");
    } else{
        aux = a->inicio;
        while(aux != NULL){
            printf("%d ", aux->valor);
            aux = aux->prox;
        }
        printf("\n");
    }
}

int empity(fila *a){
    if(a->inicio == NULL && a->fim == NULL){
        printf("PILHA VAZIA");
        return 0;
    }
    printf("existe pilha");
    return 1;
}


int main(){
    fila *miaFila;
    miaFila = criaFila();
    push(10, miaFila);
    push(2, miaFila);
    push(6, miaFila);
    push(20, miaFila);
    stackpop(miaFila);
    pop(miaFila);
    stackpop(miaFila);
    pop(miaFila);
    stackpop(miaFila);
    pop(miaFila);
    stackpop(miaFila);
    pop(miaFila);
    stackpop(miaFila);
    pop(miaFila);
    return 0;
}