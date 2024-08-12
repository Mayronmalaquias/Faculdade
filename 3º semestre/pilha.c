#include <stdio.h>
#include <stdlib.h>

typedef struct registro{
    int valor;
    struct registro *prox;
} registro;

typedef struct pilha{
    int qtd;
    registro *topo;
}pilha;

pilha* criaPilha(){
    pilha *p;
    p = (pilha *)malloc(sizeof(pilha));
    p->qtd = 0;
    p->topo = NULL;
    return p;
}

registro* criaRegistro(){
    registro *p;
    p = (registro *)malloc(sizeof(registro));
    p->valor = 0;
    p->prox = NULL;
    return p;
}

void push(int novo,  pilha *a){
    registro *aux;
    aux = criaRegistro();
    aux->valor = novo;
    if (a == NULL){
        printf("não existe pilha");
        return;
    }
    if(a->topo == NULL){
        a->topo = aux;
    }else{
        aux->prox = a->topo;
        a->topo = aux;
    }
}

void pop(pilha *a){
    registro *aux;
    aux = a->topo;
    a->topo = aux->prox;
    free(aux);
}

void stackpop(pilha *a){
    registro *aux;
    if(a == NULL){
        printf("Pilha vazia");
        return;
    }
    aux = a->topo;
    if(a->topo  == NULL){
        printf("pilha vazia");
        return;
    } else{
        while(aux != NULL){
            printf("%d ", aux->valor);
            aux = aux->prox;
        }
        printf("\n");
    }

}

int empty(pilha *a){
    if(a->topo == NULL){
        printf("pilha vazia");
        return 0;
    }
    printf("pilha existe");
    return 1;    
}

int main() {
    pilha *b;
    b = criaPilha();
    push(7, b);
    push(2, b);
    push(5, b);
    push(23, b);
    stackpop(b);
    pop(b);
    stackpop(b);
    pop(b);
    stackpop(b);
    pop(b);
    stackpop(b);
    pop(b);
    stackpop(b);
    pop(b);
    stackpop(b);

    return 0;
}