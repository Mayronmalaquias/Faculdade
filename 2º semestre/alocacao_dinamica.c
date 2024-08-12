#include <stdio.h>
#include <stdlib.h>

// d) um array de 20 estruturas do tipo pessoa, com os seguintes atributos:
// • nome: String de 100 posições.
// • idade: inteiro positivo.
// • salário: real

struct Pessoa {
  char nome[100];
  int idade;
  float salario;
};
typedef struct Pessoa Pessoa;

// e) uma matriz 5x5 de inteiros.

void preencherMatriz(int n, int m, int matriz[n][m]) {
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      printf("Digite o valor da posição [%d][%d]: ", i, j);
      scanf("%d", &matriz[i][j]);
    }
  }
}

void exibirMatriz(int n, int m, int matriz[n][m]) {
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < m; j++) {
      printf("matriz[%d][%d]: %d\n", i, j, matriz[i][j]);
    }
  }
}

int **alocarMatriz(int n, int m) {
  int **matriz = (int **) malloc(n * sizeof(int *));
  if(matriz == NULL) { // if(!matriz)
    printf("Erro de alocação de memória.\n");
    return NULL;
  }
  for(int i = 0; i < n; i++) {
    matriz[i] = malloc(sizeof(int)*m);
    if(matriz[i] == NULL) {
      printf("Erro de alocação de memória.\n");
      return NULL;
    }
  }
  return matriz;
}


int main(void) {
  Pessoa *pessoas;
  pessoas = malloc(sizeof(Pessoa)*20);
  if(pessoas == NULL) { // if(!pessoas)
    printf("Erro de alocação de memória.\n");
    return 0;
  }
  // executamos o código normalmente
  int **pp;
  int *p;
  int n = 5;
  p = &n;
  pp = &p;
  printf("Endereço de ponteiro: %p (pp: %p)\n", &p, pp);
  printf("Endereço de n: %p (*p: %p)\n", &n, *pp);
  printf("Valor de n: %d (**pp: %d)\n", n, **pp);


  // e) uma matriz 5x5 de inteiros.
  int **matriz = alocarMatriz(2, 3);

  preencherMatriz(2, 3, matriz);
  exibirMatriz(2, 3, matriz);
  return 0;
}