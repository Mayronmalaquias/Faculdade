#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

long long int*criaVetEmbaralhado(long long int tam);
void mostrarVet(long long int *vet, long long int tam);
void bublesort(long long int *vet, long long int tam);
void quicksort(long long int *vet, long long int inicio, long long int fim);
void merge(long long int *vet, long long int inicio, long long int meio, long long int fim);
void mergesort(long long int *vet, long long int inicio, long long int fim);
void selection(long long int *vet, long long int tam);
void menu();



int main(){
    menu();
    return 0;
}

long long int* criaVetEmbaralhado(long long int tam){
    long long int *vet, aux, i, aleatorio;
    vet = (long long int *)calloc(tam,sizeof(long long int));
    for(i = 0; i<tam; i++){
        vet[i] = i + 1;
    }
    for(i = 0; i<tam;i++){
        aleatorio = rand() % tam;
        aux = vet[i];
        vet[i] = vet[aleatorio];
        vet[aleatorio] = aux;
    }
    return vet;
}

void mostrarVet(long long int *vet, long long int tam){
    for(int i = 0; i<tam;i++){
        printf("%lld ", vet[i]);
    }
    printf("\n");
}


void menu(){
    long long int tam, *a, *b, *c, *d, *e;
    printf("fale o tamanho do Vet: ");
    scanf("%lld", &tam);
    a = criaVetEmbaralhado(tam);
    b = criaVetEmbaralhado(tam);
    c = criaVetEmbaralhado(tam);
    d = criaVetEmbaralhado(tam);
    e = criaVetEmbaralhado(tam);
    printf("Vet embaralhado: ");
    mostrarVet(a, tam);
    printf("Vet ordenado com buble: ");
    bublesort(a, tam);
    mostrarVet(a, tam);
    printf("Vet embaralhado: ");
    mostrarVet(b,tam);
    printf("Vet ordenado com quick: ");
    quicksort(b, 0, tam);
    mostrarVet(b, tam);
    printf("Vet embaralhado: ");
    mostrarVet(c,tam);
    printf("Vet ordenado com merge: ");
    quicksort(c, 0, tam);
    mostrarVet(c, tam);
    printf("Vet embaralhado: ");
    mostrarVet(d, tam);
    printf("Vet ordenado com inserction: ");
    bublesort(d, tam);
    mostrarVet(d, tam);
    printf("Vet embaralhado: ");
    mostrarVet(e, tam);
    printf("Vet ordenado com selection: ");
    bublesort(e, tam);
    mostrarVet(e, tam);
}

void bublesort(long long int *vet, long long int tam){
    long long int aux, passou, pass, i;
    passou = 1;
    for(pass = 0; pass<tam-1;pass++){
        passou = 0;
        for(i = 0; i<tam - 1 - pass;i++){
            if(vet[i] > vet[i + 1]){
                aux = vet[i];
                vet[i] = vet[i + 1];
                vet[i + 1] = aux;
                passou = 1;
            }
        }
    }
}

void quicksort(long long int *vet, long long int inicio, long long int fim){
    long long int pivo, aux, troca;
    if(inicio > fim){
        return;
    }
    pivo = fim;
    aux = inicio;
    while(aux != pivo){
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
    quicksort(vet, inicio, pivo - 1);
    quicksort(vet, aux + 1, fim);
}


void merge(long long int *vet, long long int inicio, long long int meio, long long int fim){
    long long int *vetor, i, j, k;
    i = inicio;
    j = meio + 1;
    k = 0;
    vetor = (long long int *)calloc(fim - inicio + 1, sizeof(long long int));
    while(i <= meio && j <= fim){
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
    while (j<=fim){
        vetor[k] = vet[j];
        j++;
        k++;
    }
    for(int i = 0; i< (fim - inicio + 1); i++){
        vet[i] = vetor[i];
    }
    free(vetor);
    return;
}

void mergesort(long long int *vet, long long int inicio, long long int fim){
    long long int meio;
    meio = (fim + inicio)/ 2;
    if(inicio < fim){
        mergesort(vet, inicio, meio);
        mergesort(vet, meio + 1, fim);
        merge(vet, inicio, meio, fim);
    }
}

void inserction(long long int *vet, long long int tam){
    long long int i, j, aux;
    for(i = 1; i<tam;i++){
        aux = vet[i];
        for(j=i;j>=0 && vet[j - 1] > vet[j];j--){
            vet[j - 1] = vet[j];
        }
        vet[j] = aux;
    }
}

void selection(long long int *vet, long long int tam){
    long long int indMenor,aux, i, j;
    for(i = 0; i<tam; i++){
        indMenor = i;
        for(j = i + 1; j < tam; j++){
            if(vet[j] > vet[i]){
                indMenor = j;
            }
        }
        vet[i] = vet[indMenor];
    }
}