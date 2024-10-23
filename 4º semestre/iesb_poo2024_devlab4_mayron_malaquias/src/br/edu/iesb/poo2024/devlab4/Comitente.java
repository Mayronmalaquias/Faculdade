package br.edu.iesb.poo2024.devlab4;


import br.edu.iesb.poo2024.devlab4.exception.CadastroInvalidoException;
import br.edu.iesb.poo2024.devlab4.exception.CadastroItemInvalidoException;

public class Comitente extends Pessoa {
	private int idComitente;
	private int saldoDisponivel;
	
	public Comitente (String nome, String cpf)throws CadastroInvalidoException {
		super(nome, cpf);
	}
	
	public void visualizarSaldo() {
		if(isLogado) {
			System.out.println("Voce possuiu saldo de: " + this.saldoDisponivel);			
		}else {
			System.out.println("Voce precisa estar logado para essa acao");
		}
	}
	
	public Item inserirItem(String nome, int valorInicial, Comitente comitente) throws CadastroItemInvalidoException {
		if(isLogado) {
			if(valorInicial < 1 || nome == null || nome.equals("") ) {
				throw new CadastroItemInvalidoException();
			}
			Item novoItem = new Item(nome, valorInicial, comitente);
			return novoItem;			
		}else {
			System.out.println("Voce precisa estar logado para essa acao");
			return null;
		}
	}
	
	public void modificarSaldo(int novoValor) {
		this.saldoDisponivel += novoValor;
	}
}

