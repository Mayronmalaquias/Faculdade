#include "tarefa.h"
#include <stdio.h>

void inicializar(Vetor *vetor, uint capacidade) {
  // Exceção
  if(capacidade > LIMITE) {
    // printf("Capacidade Inválida!\n");
    fprintf(stderr, "Capacidade Inválida!\n");
    return;
  }
  vetor->capacidade = capacidade;
  vetor->size = 0;
}

void criarTarefa(Tarefa *tarefa) {
  printf("Informe o título da tarefa: ");
  scanf("%500[^\n]%*c", tarefa->titulo);
  tarefa->status = A_FAZER; // 0
}


void inserirFim(Vetor *vetor, Tarefa tarefa) {
  // Exceção
  if(vetor->size >= vetor->capacidade) {
    // printf("Vetor Cheio!\n");
    fprintf(stdout, "Vetor Cheio!\n");
    return;
  }
  vetor->tarefas[vetor->size] = tarefa;
  if(vetor->size == 0) vetor->tarefas[0].id = 0;
  else vetor->tarefas[vetor->size].id = vetor->tarefas[vetor->size - 1].id + 1;
  vetor->size++;
}

void deletarFim (Vetor *vetor) {
    if(vetor->size == 0) {
        fprintf(stdout,"Vetor vazio!\n");
        return;
    }
    vetor ->size--;
}

void listar(Vetor *vetor) {
    if (vetor->size == 0){
        fprintf(stdout, "vetor vazio");
        return;
    }
    for (int i = 0; i < vetor->size; i++) {
        switch ()
        fprintf(stdout, "Id eh: %d", vetor->tarefas[i].id);
        fprintf(stdout, "status eh: %d", vetor->tarefas[i].status);
        fprintf(stdout, "Titulo eh: %s", vetor->tarefas[i].titulo);

    }
}

