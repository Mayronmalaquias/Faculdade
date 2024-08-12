#include <stdio.h>
#include <stdlib.h>

typedef struct registro{
    int valor;
    registro *prox;
}registro;

typedef struct lista{
    int qtd;
    registro *inicio;
    registro *fim;
}lista;

lista *criaLista(){
    lista *p;
    p = (lista*)malloc(sizeof(lista));
    p->qtd = 0;
    p->inicio = NULL;
    p->fim = NULL;
    return p;
}

registro *criaRegistro(){
    registro *p;
    p = (registro *)malloc(sizeof(registro));
    p->valor = 0;
    p->prox = NULL;
    return p;
}

void inserir(lista *a, int novo){
    if(a==NULL){
        printf("lista não existe");
    }
    registro *p, *aux;
    p = criaRegistro();
    p->valor = novo;
    aux = a->inicio;
    if(a->inicio == NULL && a->fim == NULL){
        a->inicio = p;
        a->fim = p;
    } else{
        while(aux->prox != NULL){
            aux = aux->prox;
        }
        aux->prox = p;
        a->fim = p;
    }
}

void remover(lista *a){
    if (a == NULL){
        printf("lista n existe");
        return;
    }
    registro *aux;
    aux = a->inicio;
    printf("removi %d", aux->valor);
    a->inicio = aux->prox;
}

void mostrar(lista *a){
    if(a == NULL){
        printf("lista não existe");
        return;
    }
    registro *aux;
    aux = a->inicio;
    while(aux->prox != NULL){
        printf("%d", aux->valor);
    }
}

int main(){
    lista *b = criaLista();
    inserir(b, 3);
    inserir(b, 1);
    inserir(b, 5);
    inserir(b, 8);
    remover(b);
    mostrar(b);
}