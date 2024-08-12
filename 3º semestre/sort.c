#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

long long int *criaVet(long long int tam){
    long long int *vet;
    vet = (long long int *)calloc(tam, sizeof(long long int));

    for(int i = 0; i<tam; i++){
        vet[i] = i + 1;
    }
    return vet;
}

long long int *criaVetEmbaralhado(long long int tam){
    long long int *vet, aleatorio, aux;
    vet = (long long int *)calloc(tam, sizeof(long long int));

    for(int i = 0; i < tam; i++){
        vet[i] = i + 1;
    }
    for(int i = 0; i < tam; i++){
        aleatorio = rand() % tam;
        aux = vet[i];
        vet[i] = vet[aleatorio];
        vet[aleatorio] = aux;
    }
    return vet;
}

void mostrarVet(long long int *a, long long int tam){
    for(int i = 0; i < tam; i++){
        printf("%lld ", a[i]);
    }
    printf("\n");
}

void buble(long long int *vet, long long int tam){
    long long int aux;
    int trocou = 1;
    for(int passou = 0; passou < tam - 1 && trocou; passou++){
        trocou = 0;
        for(int i = 0; i < tam - 1 - passou; i++){
            if(vet[i] > vet[i + 1]){
                aux = vet[i];
                vet[i] = vet[i + 1];
                vet[i + 1] = aux;
                trocou = 1;
            }
        }
    }
}

void quicksort(long long int *vet, long long int inicio, long long int fim){
    if(inicio > fim){
        return;
    }
    long long int aux, pivo, troca;
    aux = inicio;
    pivo = fim;
    while(pivo != aux){
        if(pivo > aux){
            if(vet[pivo] < vet[aux]){
                troca = vet[pivo];
                vet[pivo] = vet[aux];
                vet[aux] = troca;
                troca = pivo;
                pivo = aux;
                aux = troca;
            }
        }else {
            if(vet[pivo] > vet[aux]){
                troca = vet[pivo];
                vet[pivo] = vet[aux];
                vet[aux] = troca;
                troca = pivo;
                pivo = aux;
                aux = troca;
            }
        }
        if(pivo < aux){
            aux--;
        }else{
            aux++;
        }
    }

    quicksort(vet, inicio, pivo - 1);
    quicksort(vet, aux + 1, fim);
}

void merge(long long int *vet, long long int inicio, long long int meio, long long int fim){
    long long int i,j,*aux,k;
    aux = (long long int *)calloc(fim - inicio + 1, sizeof(long long int));
    i = inicio;
    j = meio + 1;
    k = 0;
    while(i<=meio && j<=fim){
        if(vet[i] <= vet[j]){
            aux[k] = vet[i];
            k++;
            i++;
        }else{
            aux[k] = vet[j];
            k++;
            j++;
        }
    }
    while(i<=meio){
        aux[k] = vet[i];
        k++;
        i++;
    }
    while(j<=fim){
        aux[k] = vet[j];
        k++;
        j++;
    }
    for(i=0;i<(fim - inicio + 1); i++){
        vet[inicio + i] = aux[i];
    }
    free(aux);
    return;
}

void mergesort(long long int *vet, long long int inicio, long long int fim){
    long long int meio;

    if(inicio < fim){
        meio = (inicio + fim) / 2;
        mergesort(vet, inicio, meio);
        mergesort(vet, meio + 1, fim);
        merge(vet, inicio, meio, fim);
    }
}

void inserctionsort(long long int * vet, long long int tam){
    long long int i, j, aux;
    for(i=1;i<tam;i++){
        aux = vet[i];
        for(j=i; j> 0 && vet[j - 1] > aux;j--){
            vet[j] = vet[j - 1];
        }
        vet[j] = aux;
    }
}

void selectionsort(long long int *vet, long long int tam){
    long long int i, j, ind_menor,aux;
    for(i = 0; i<tam;i++){
        ind_menor = i;
        for(j=i+1;j<tam;j++){
            if(vet[j]<vet[ind_menor]){
                ind_menor = j;
            }
        }
        aux = vet[i];
        vet[i] = vet[ind_menor];
        vet[ind_menor] = aux;
    }
}

void menu();

int main(){
    menu();
    /*
    long long int *a, *b, *c, *d, *e;
    







    a = criaVetEmbaralhado(10);
    b = criaVetEmbaralhado(10);
    c = criaVetEmbaralhado(10);
    d = criaVetEmbaralhado(10);
    e = criaVetEmbaralhado(10);
    printf("Vetor a: ");
    mostrarVet(a, 10);
    printf("Vetor b: ");
    mostrarVet(b, 10);
    printf("Vetor c: ");
    mostrarVet(c, 10);
    printf("Vetor d: ");
    mostrarVet(d, 10);
    printf("Vetor e: ");
    mostrarVet(e, 10);

    buble(a, 10);
    printf("Vetor a normal:");
    mostrarVet(a, 10);
    printf("Vetor b normal:");
    quicksort(b, 0, 10);
    mostrarVet(b, 10);
    printf("Vetor c normal:");
    mergesort(c, 0, 10);
    mostrarVet(c, 10);
    printf("Vetor d normal:");
    inserctionsort(d, 10);
    mostrarVet(d, 10);
    printf("Vetor e normal:");
    selectionsort(e, 10);
    mostrarVet(e, 10);
    */
    return 0;
}


void menu(){
    long long int tamanho, *a,*b,*c,*d,*e;
    printf("Eu  sou Mayron e esse eh o meu ordenamento\n");
    printf("Fale o tamanho do seu vetor: ");
    scanf("%lld", &tamanho);
    a = criaVetEmbaralhado(tamanho);
    b = criaVetEmbaralhado(tamanho);
    c = criaVetEmbaralhado(tamanho);
    d = criaVetEmbaralhado(tamanho);
    e = criaVetEmbaralhado(tamanho);
    printf("Vetor A embaralhado: ");
    mostrarVet(a, tamanho);
    buble(a, tamanho);
    printf("Vetor A ordenado com buble: ");
    mostrarVet(a, tamanho);
    printf("\n");

    printf("Vetor B embaralhado: ");
    mostrarVet(b, tamanho);
    quicksort(b, 0,  tamanho);
    printf("Vetor B ordenado com quicksort: ");
    mostrarVet(b, tamanho);
    printf("\n");

    printf("Vetor C embaralhado: ");
    mostrarVet(c, tamanho);
    mergesort(c, 0,  tamanho);
    printf("Vetor C ordenado com mergesort: ");
    mostrarVet(c, tamanho);
    printf("\n");


    printf("Vetor D embaralhado: ");
    mostrarVet(d, tamanho);
    inserctionsort(d,tamanho);
    printf("Vetor D ordenado com inserctionsort: ");
    mostrarVet(d, tamanho);
    printf("\n");

    printf("Vetor E embaralhado: ");
    mostrarVet(e, tamanho);
    selectionsort(e,tamanho);
    printf("Vetor E ordenado com selectionsort: ");
    mostrarVet(e, tamanho);
    printf("\n");
    return;
}