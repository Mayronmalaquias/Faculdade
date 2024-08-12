typedef unsigned int uint;
#define LIMITE 10

typedef enum {
  A_FAZER,   // 0
  ANDAMENTO, // 1
  FINALIZADO // 2
} ETarefa;

typedef struct {
  uint id;
  ETarefa status;
  char titulo[500];
} Tarefa;

typedef struct {
  uint capacidade;
  uint size;
  Tarefa tarefas[LIMITE];
} Vetor;

void inicializar(Vetor *vetor, uint capacidade);

void criarTarefa(Tarefa *tarefa);
void inserirFim(Vetor *vetor, Tarefa tarefa);
void listar(Vetor *vetor);