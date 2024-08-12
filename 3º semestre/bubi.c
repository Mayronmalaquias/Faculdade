#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

long long int * criaVetor(long long int tamanho){
    long long int *vet;
    long long int i;
    vet = (long long int *)calloc(tamanho, sizeof(long long int));
    for(i = 0; i < tamanho; i++){
        vet[i] = i + 1;
    }
    return vet;
}

long long int * criaVetorEmbaralhado(long long int tamanho){
    srand(time(NULL));
    long long int *vet;
    long long int i, sorteio, aux;
    int trocou = 1;
    vet = (long long int *)calloc(tamanho, sizeof(long long int));
    for(i = 0; i < tamanho; i++){
        vet[i] = i + 1;
    }
    for(i = 0; i < tamanho; i++){
        sorteio = rand() % tamanho;
        aux = vet[i];
        vet[i] = vet[sorteio];
        vet[sorteio] = aux;
    }
    return vet;
}

void buble(long long int *vet, long long int tamanho){
    long long int aux, pass, i;
    int trocou = 1;
    for(pass = 0; pass < tamanho - 1 && trocou; pass++){
        trocou = 0;
        for (i = 0; i < tamanho - 1 - pass; i++){
            if(vet[i] > vet[i + 1]){
                aux = vet[i];
                vet[i] = vet[i + 1];
                vet[i + 1] = aux;
                trocou = 1;
            }
        }
    }
}

void quicksort(long long int *vet, long long int fim, long long int inicio){
    if(inicio > fim){
        return;
    }
    long long int pivo, aux, troca;
    pivo = fim;
    aux = inicio;
    while(aux != pivo){
        if(aux > pivo){
            if(vet[aux] > vet[pivo]){
                troca = vet[aux];
                vet[aux] = vet[pivo];
                vet[pivo] = troca;
                troca = pivo;
                pivo = aux;
                aux = troca;
            }   
        } else{
            if(vet[aux]<vet[pivo]){
                troca = vet[aux];
                vet[aux] = vet[pivo];
                vet[pivo] = troca;
                troca = pivo;
                pivo = aux;
                pivo = troca;
            }

        }
        if(aux > pivo){
            aux--;
        } else{
            aux++;
        }
        quicksort(vet, inicio, pivo - 1);
        quicksort(vet, aux + 1, fim);
    }
    
}

void mostrarVetor(long long int *vet, long long tamanho){
    for (int i = 0; i < tamanho; i++){
        printf("%lld ", vet[i]);
    }
    printf("\n");
}

int main(){
    long long int *vet = criaVetorEmbaralhado(10);
    mostrarVetor(vet, 10);
    //buble(vet, 10);
    quicksort(vet, 0, 10);
    mostrarVetor(vet, 10);
    return 0;
}