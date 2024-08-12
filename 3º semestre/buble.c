#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


long long int * criaVetor(long long int tamanho){
    long long int *vet;
    long long int i;
    vet = (long long int*)calloc(tamanho, sizeof(long long int));

    for(i = 0; i<tamanho; i++){
        vet[i] = i + 1;
    }

    return vet;
}


long long int *criaVetorEmbaralhado(long long int tamanho){
    srand(time(NULL));
    long long int *vet;
    long long int i;
    int sorteio, aux;
    vet = (long long int *)calloc(tamanho, sizeof(long long int));

    for (i = 0; i < tamanho; i++){
        vet[i] = i + 1;
    }
    for (i = 0; i < tamanho; i++){
        sorteio = rand() % tamanho;
        aux = vet[i];
        vet[i] = vet[sorteio];
        vet[sorteio] = aux;
    }
    return vet;
}

void mostrarVetor(long long int *vet, long long int tamanho){
    for(int i=0; i<tamanho; i++){
        printf("%lld ", vet[i]);
    }
    printf("\n");
}

void buble(long long int *vet, long long int tamanho){
    long long int aux, i, pass;
    int trocou = 1;
    for(pass = 0; pass < tamanho - 1 && trocou; pass++){
        trocou = 0;
        for(i = 0; i < tamanho - 1 - pass; i++){
            if(vet[i] > vet[i + 1]){
                trocou = 1;
                aux = vet[i];
                vet[i] = vet[i + 1];
                vet[i + 1] = aux;
            }
        }
    }
}


int main(){
    long long int *vet = criaVetorEmbaralhado(10);
    mostrarVetor(vet , 10);
    buble(vet, 10);
    printf("\n\n");
    mostrarVetor(vet, 10);
    return 0;
}