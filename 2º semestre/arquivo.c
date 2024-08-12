#include <stdio.h>

void arquivosDoConsole() {
  printf("Hello World\n");
  // stdin - Arquivo de entrada do console
  // stdout - Arquivo de saída do console
  // stderr - Arquivo de erro do console
  fprintf(stdout, "Olá Gabriel!\n");
  char nome[50];
  scanf("%49s", nome);
  fprintf(stdout, "Olá %s!\n", nome);
  fscanf(stdin, "%49s", nome);
  fprintf(stdout, "Olá %s!\n", nome);
}

int main(void) {

  return 0;
}