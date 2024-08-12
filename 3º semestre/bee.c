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
    p = (registro*)malloc(sizeof(registro));
    p->valor = 0;
    p->prox = NULL;
    return p;
}

fila* criaFila(){
    fila *p;
    p = (fila*)malloc(sizeof(fila));
    p->inicio = NULL;
    p->fim = NULL;
    p->qtd = 0;
    return p;
}

void pushPar(int novo, fila *a) {
    if(a == NULL){
        return;
    }
    registro *aux, *ant=NULL, *pro;
    aux = criaRegistro();
    aux->valor = novo;
    if(a->inicio == NULL && a->fim == NULL){
        a->inicio = aux;
        a->fim = aux;
    }else{
        pro = a->inicio;
        while(pro != NULL && pro->valor < aux->valor){
            ant = pro;
            pro = pro->prox;
        }
        if (ant == NULL){
            aux -> prox = a -> inicio;
            a -> inicio = aux;
        } else if (pro == NULL) {
            a -> fim -> prox = aux;
            a -> fim = aux;
        } else {
            ant->prox = aux;
            aux->prox = pro;
            printf("");
        }
    }
}

void pushImpar(int novo, fila *a){
    if(a == NULL){
        return;
    }
    registro *aux, *ant, *pro;
    aux = criaRegistro();
    aux->valor = novo;
    if(a->inicio == NULL){
        a->inicio = aux;
    } else{
        pro = a->inicio;
        while(pro != NULL && aux ->valor > pro->valor){
            ant = pro;
            pro = pro->prox;
        }
        if (ant == NULL){
            aux -> prox = a -> inicio;
            a -> inicio = aux;
        } else if (pro == NULL) {
            a -> fim -> prox = aux;
            a -> fim = aux;
        } else {
            ant->prox = aux;
            aux->prox = pro; 
        }
    }
    
}

fila* concatenar(fila *a, fila *b){
    a->fim-> prox = b->inicio;
    return a;
}


void stackpop(fila *a){
    if(a == NULL){
        printf("lista nao existe");
    }
    registro *aux;
    aux = a->inicio;
    if(a->inicio == NULL && a->fim == NULL){
        printf("fila vazia");
    }else{
        while(aux != NULL){
            printf("%d\n", aux->valor);
            aux = aux->prox;
        }
    }
}

int main(){
    fila *a, *b;
    a = criaFila();
    pushPar(10, a);
    pushPar(10, a);
    pushImpar(4, b);
    pushPar(32, a);
    pushPar(34, a);
    pushImpar(543, b);
    pushPar(3456, a);
    pushPar(654, a);
    pushImpar(567, b);
    pushImpar(87, b);
    pushImpar(6789, b);
    pushPar(98, a);
    concatenar(a, b); 
    stackpop(a);
}