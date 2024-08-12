#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

long long int * criaVetor(long long int tam){
    long long int *p;
    p = (long long int*)calloc(tam, sizeof(long long int));
    long long int i;
    for(i = 0; i < tam; i++){
        p[i] = i + 1;
    }
    return p;
}

long long int * criaVetEmba(long long int tam){
    srand(time(NULL));
    long long int *vet;
    vet = (long long int*)calloc(tam, sizeof(long long int));
    long long int i, aux, sorteio;
    for(i = 0; i < tam; i++){
        vet[i] = i + 1;
    }
    for(i = 0; i < tam; i++){
        sorteio  = rand() % tam;
        aux = vet[i];
        vet[i] = vet[sorteio];
        vet[sorteio] = aux;
    }
    return vet;
}

void mostrarVet(long long int *vet, long long int tam){
    long long int i;
    for(i = 0; i<tam; i++){
        printf("%lld ", vet[i]);
    }
    printf("\n");
}

void buble(long long int *vet, long long int tam){
    long long int i, aux, pass;
    for(pass = 0; pass < tam - 1; pass++){
        for(i = 0; i < tam - 1 - pass; i++){
            if(vet[i] > vet[i + 1]){
                aux = vet[i];
                vet[i] = vet[i + 1];
                vet[i + 1] = aux;
            }
        }
    }
}

void quicksort(long long int *vet,long long int ini, long long int fim){
    if(ini > fim){
        return;
    }
    long long int pivo, aux, pass;
    pivo = fim;
    aux = ini;
    while(aux != pivo){
        if(aux > pivo){
            if(vet[aux] < vet[pivo]){
                pass = vet[pivo];
                vet[pivo] = vet[aux];
                vet[aux] = pass;
                pass = pivo;
                pivo = aux;
                aux = pass;
            }
        } else{
            if(vet[aux] > vet[pivo]){
                pass = vet[pivo];
                vet[pivo] = vet[aux];
                vet[aux] = pass;
                pass = pivo;
                pivo = aux;
                aux = pass;
            }
        }
        if(aux > pivo){
            aux--;
        }else{
            aux++;
        }
    }
    quicksort(vet, ini, pivo - 1);
    quicksort(vet, aux + 1 , fim);
}


int main(){
    long long int *a, *b;
  //  a = criaVetEmba(10);
//mostrarVet(a, 10);
  //  buble(a, 10);
 //   mostrarVet(a, 10);
    b = criaVetEmba(10);
    mostrarVet(b, 10);
    quicksort(b, 0, 10);
    mostrarVet(b, 10);
    return 0;
}