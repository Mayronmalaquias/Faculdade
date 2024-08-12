#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

long long int* criaVetEmbaralhado(long long int tam){
    long long int *vet, random, aux;
    vet = (long long int*)calloc(tam, sizeof(long long int));
    for(int i = 0; i<tam;i++){
        vet[i] = i + 1;
    }
    for(int i = 0; i<tam;i++){
        random = rand()%tam;
        aux = vet[i];
        vet[i] = vet[random];
        vet[random] = aux;
    }
    return vet;
}

void mostrarVet(long long int *vet, long long int tam){
    for(int i = 0; i<tam; i++){
        printf("%lld ", vet[i]);
    }
    printf("\n");
}

void bublesort(long long int *vet, long long int tam){
    long long int aux, pass, passou, troca;
    passou = 1;
    for(pass = 0; pass<tam - 1 && passou; pass++){
        passou = 0;
        for(int i = 0; i < tam - 1 - pass; i++){
            if(vet[i]>vet[i + 1]){
                aux = vet[i];
                vet[i] = vet[i + 1];
                vet[i + 1] = aux;
                passou = 1;
            }
        }
    }
}

void inserctionsort(long long int *vet, long long int tam){
    long long int aux, i , j;
    for(i = 1; i < tam; i++){
        aux = vet[i];
        for(j = i - 1; j>=0 && vet[j]>aux;j--){
            vet[j + 1] = vet[j];
        }
        vet[j + 1] = aux;
    }
}

void selectionsort(long long int *vet, long long int tam){
    long long int indMenor, aux, i, j;
    for(i = 0; i<tam;i++){
        indMenor = i;
        for(j = i + 1;j<tam; j++ ){
            if(vet[j]<vet[indMenor]){
                indMenor = j;
            }
        }
        aux = vet[i];
        vet[i] = vet[indMenor];
        vet[indMenor] = aux;
    }
}

void quicksort(long long int *vet, long long int inicio,long long int fim){
    long long int pivo, aux, troca;
    if(inicio > fim){
        return;
    }
    pivo = fim;
    aux = inicio;
    while (aux != pivo)
    {
        if(aux > pivo){
            if(vet[aux] < vet[pivo]){
                troca = vet[aux];
                vet[aux] = vet[pivo];
                vet[pivo] = troca;
                troca = aux;
                aux = pivo;
                pivo = troca;
            }
        }else{
            if(vet[aux] > vet[pivo]){
                troca = vet[aux];
                vet[aux] = vet[pivo];
                vet[pivo] = troca;
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
    quicksort(vet, aux + 1, fim);
    quicksort(vet, inicio, pivo - 1);
    
}

void merge(long long int *vet, long long int inicio, long long int meio, long long int fim){
    long long int *vetor, j, i, k;
    vetor = (long long int *)calloc(fim - inicio + 1, sizeof(long long int));
    i = inicio;
    j = meio + 1;
    k = 0;
    while(i <= meio && j<= fim){
        if(vet[i] < vet[j]){
            vetor[k] = vet[i];
            i++;
            k++;
        }else{
            vetor[k] = vet[j];
            j++;
            k++;
        }
    }
    while(i<=meio){
        vetor[k] = vet[i];
        i++;
        k++;
    }
    while(j<=fim){
        vetor[k] = vet[j];
        j++;
        k++;
    }
    for(int i = 0; i<(fim - inicio + 1);i++){
        vet[inicio + i] = vetor[i];
    }
    free(vetor);
    return;
}
void mergesort(long long int *vet, long long int inicio, long long int fim){
    long long int meio;
    if(inicio < fim){
        meio = (fim + inicio) / 2;
        mergesort(vet, inicio, meio);
        mergesort(vet, meio + 1, fim);
        merge(vet, inicio, meio,  fim);
    }
}



int main(){
    long long int *vet;
    vet = criaVetEmbaralhado(10);
    mostrarVet(vet, 10);
    //bublesort(vet, 10);
    //inserctionsort(vet, 10);
    //selectionsort(vet, 10);
    //quicksort(vet, 0, 10);
    mergesort(vet, 0, 10);
    mostrarVet(vet, 10);
    return 0;
}