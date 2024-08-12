/*
Autores:
Mayron Malaquias - 2312082003
Pedro Borges Alves - 2312082014
Pedro Mesquista de Sousa - 2312082041
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int recebe_palpite (){
    int palpite_jogador;
    scanf("%d",&palpite_jogador);
    return palpite_jogador;
}

int criadorNumeroAleatorio (int min, int max){
    int numero_aleatorio = rand() % max + min;
    return numero_aleatorio;
}

int verifica_palpite (int palpite_jogador, int numero_aleatorio) {
	if(palpite_jogador > numero_aleatorio){
		return 1;
	}else if(palpite_jogador < numero_aleatorio){
		return -1;
	}
	
	return 0;
}

void novo_Jogo () {
	int tentativas = 1;
	int verificacao = 1;
	int palpite_jogador;
	int numero_aleatorio = criadorNumeroAleatorio(1, 100);

	printf("DEBUG %d", numero_aleatorio);
	printf("\n\n");
	printf("Bem-Vindo ao jogo de advinhhacao!\n\n");
	
	
	while(verificacao != 0){
		printf("\nQual e o seu palpite? ");
        palpite_jogador = recebe_palpite();
		verificacao = verifica_palpite(palpite_jogador, numero_aleatorio);
		 
		if(verificacao == 1){
			printf("\nMuito Alto, tente novamente!");
		}else if (verificacao == -1){
			printf("\nMuito Baixo, tente novamente!");
		}else if (verificacao == 0){
			printf("\nParabens, voce acertou o numero apos %d tentativas", tentativas);
		}
		
		tentativas++;
	}
    
}

void limparTela () {
    system("clear");
}

int main() {
	char jogarNovamente;
  
    // necessário uma única vez para obtenção de número aleatório
  	srand(time(NULL));
  
  do {
    limparTela();
    novo_Jogo();
    printf("\nGostaria de jogar novamente? (s/n): ");
    scanf(" %c", &jogarNovamente);
  } while (jogarNovamente == 's' || jogarNovamente == 'S');

  return 0;
}	