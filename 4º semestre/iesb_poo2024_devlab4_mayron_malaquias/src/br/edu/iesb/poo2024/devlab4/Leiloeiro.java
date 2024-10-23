package br.edu.iesb.poo2024.devlab4;

import br.edu.iesb.poo2024.devlab4.exception.CadastroInvalidoException;

public class Leiloeiro extends Pessoa {
	private int idLeiloeiro;
	private int salario;
	private int pcomisao;
	
	public Leiloeiro(String _nome, String _cpf)throws CadastroInvalidoException {
		super(_nome, _cpf);
	}
	
	public void finalizarLeilao(Leilao leilao) {
		if(isLogado) {
			leilao.isFechado();	
		}else {
			System.out.println("Voce precisa logar no sistema para essa acao");
		}
	}
	
	public Leilao iniciarLeilao(Leiloeiro leiloeiro, Item novoItem) {
		// colocar um input aqui MIXICOOOOOOOOO
		if(isLogado) {
			String nomeLeiloeiro = leiloeiro.getNome();
			String nomeItem = novoItem.getNomeItem();
			Leilao novoLeilao = new Leilao("26/07/2004", leiloeiro, novoItem);
			return novoLeilao;
		}else {
			System.out.println("Voce precisa logar no sistema para essa acao");
			return null;
		}
	}
	
	public void definirVencedor(Leilao leilao) {
		if(isLogado) {
			leilao.gerarVencedor();
		}else {
			System.out.println("Voce precisa logar no sistema para essa acao");
		}
	}
	
	public void visualizarLancesLeilao(Leilao leilao) {
		if(isLogado) {
			leilao.verLance();
		}else {
			System.out.println("Voce precisa logar no sistema para essa acao");
		}
	}
	
	public void notificaVencedor(Leilao leilao) {
		leilao.notificarVencedor();
	}
	
	public void instigarLeilao() {
		System.out.println("Alguem da mais? alguem da mais?");
	}
	
	public void prepararParaFinzalizar() {
		System.out.println("Dole 1\nDole 2\n Dole 3...");
	}
	
	
	
}

