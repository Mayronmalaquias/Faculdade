#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

long long int* criaVet(long long int tam){
    long long int *aux;
    aux = (long long int*)calloc(tam, sizeof(long long int));
    for(int i = 0; i<tam; i++){
        aux[i] = i + 1;
    }
    return aux;
}


long long int* criaVetEmbaralhado(long long int tam){
    long long int *p, aleatorio, aux;
    p = (long long int*)calloc(tam, sizeof(long long int));
    for(int i = 0; i<tam; i++){
        p[i] = i + 1;
    }
    for(int i = 1; i<tam;i++){
        aleatorio = rand() % tam;
        aux = p[i];
        p[i] = p[aleatorio];
        p[aleatorio] = aux;
    }
    return p;
}

void buble(long long int *vet, long long int tam){
    long long int aux, trocou = 1;
    for(int pass = 0; pass < tam - 1 && trocou; pass++){
        trocou = 0;
        for(int i = 0; i < tam - 1 - i; i++){
            if(vet[i] > vet[i + 1]){
                aux = vet[i];
                vet[i] = vet[i + 1];
                vet[i + 1] = aux;
                trocou = 1;
            }
        }
    }
}

void mostrarVet(long long int *a, long long int tam){
    for(int i = 0; i < tam; i++){
        printf("%lld ", a[i]);
    }
    printf("\n");
}

int main (){
    long long int *a,*b;
    a = criaVet(10);
    b = criaVetEmbaralhado(10);
    mostrarVet(a, 10);
    mostrarVet(b, 10);
    buble(b, 10);
    mostrarVet(b, 10);
    return 0;
}