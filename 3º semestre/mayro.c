#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

long long int* criaVet(int tam){
    long long int *vetor;
    vetor = (long long int *)calloc(tam, sizeof(long long int));
    for (int i = 0 ; i < tam; i++){
        vetor[i] = i + 1;
    }
    return vetor;
}

long long int* criaVetEmbaralhado(int tam){
    srand(time(NULL));
    long long int *vetor, aleatorio, aux;
    vetor = (long long int *)calloc(tam, sizeof(long long int));
    for (int i = 0 ; i < tam; i++){
        vetor[i] = i + 1;
    }
    for (int i = 0 ; i < tam; i++){
        aleatorio = rand() % tam;
        aux = vetor[i];
        vetor[i] = vetor[aleatorio];
        vetor[aleatorio] = aux;
    }
    return vetor;
}


void mostrarVetor(long long int *a, long long int tam){
    long long int aux;
    for(int i = 0; i<tam; i++){
        aux = a[i];
        printf("%lld ", aux);
    }
    printf("\n");
}


void buble(long long int *a, long long int tam){
    long long  int aux, i, pass;
    for(pass = 0; pass < tam - 1; pass++){
        for(i = 0; i < tam - 1 - pass; i++){
            if(a[i] > a[i + 1]){
                aux = a[i + 1];
                a[i + 1] = a[i];
                a[i] = aux;
            }
        }
    }
}

void quicksort(long long int *a, long long int inicio, long long int tam){
    if(inicio > tam){
        return;
    }
    long long int pivo, aux, pass, i, troca;
    aux = inicio;
    pivo = tam;
    while(aux != pivo){
        if(aux < pivo){
            if(a[aux] > a[pivo]){
                troca = a[aux];
                a[aux] = a[pivo];
                a[pivo] = troca;
                troca = aux;
                aux = pivo;
                pivo = troca;
            }
        }else{
            if(a[aux] < a[pivo]){
                troca = a[aux];
                a[aux] = a[pivo];
                a[pivo] = troca;
                troca = aux;
                aux = pivo;
                pivo = troca;
            }
        }
        if(aux > pivo){
            aux--;
        }else{
            aux++;
        }
    }    
    quicksort(a, inicio, pivo - 1);
    quicksort(a, aux + 1 , tam);
}



int main(){
    long long int *a, *b;
    a = criaVet(10);
    b = criaVetEmbaralhado(10);
    mostrarVetor(a, 10);
    mostrarVetor(b, 10);
    quicksort(b, 0, 10);
    mostrarVetor(b, 10);
    return 0;
}