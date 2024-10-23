package br.edu.iesb.poo2024.devlab4;
import java.util.ArrayList;
import java.util.List;

import br.edu.iesb.poo2024.devlab4.exception.CadastroInvalidoException;
import br.edu.iesb.poo2024.devlab4.exception.InsercaoDeSaldoInvalidoException;

public class Licitente extends Pessoa  {
	private String idLicitente;
	private List<String> lancesRealizados = new ArrayList<>();
	private int saldoDisponivel;
	private List<Integer> lances = new ArrayList<>();
	public Licitente(String nome, String cpf)throws CadastroInvalidoException {
		super(nome, cpf);
	}
	
	public void colocarSaldo(int newSaldo) throws InsercaoDeSaldoInvalidoException { // colocar uma exeção nesse metodo 
		if(isLogado) {
			if(newSaldo <= 0) {
				throw new InsercaoDeSaldoInvalidoException();
			}
			this.saldoDisponivel += newSaldo;
		}else {
			System.out.println("Voce precisa logar no sistema para fazer essa acao");
		}
	}
	
	public void visualizarSaldo() {
		if(isLogado) {
			System.out.println("Saldo atual de:" + this.saldoDisponivel);
		}else {
			System.out.println("Voce precisa logar no sistema para fazer essa acao");
		}
	}
	
	public void enviarLance(Leilao leilao, int valorLance, Licitente pessoa) {
		if(isLogado) {
			if(valorLance <= this.saldoDisponivel) {
				leilao.receberLance(valorLance, pessoa);
				this.lances.add(valorLance);
			}else {
				System.out.println("Voce nao possui saldo disponivel"); // exeção nesse metodo
			}
		}else {
			System.out.println("Voce precisa logar no sistema para fazer essa acao");
		}
	}
	public void receberEmail(Licitente pessoa) {
		if(pessoa.getEmail() == "sem_email") {
			System.out.println("A pessoa deve cadastrar o email");
		}else {
			System.out.println("email enviado para: " + pessoa.getEmail());
		}
	}
	
	public void modificarSaldo(int novoValor) {
		this.saldoDisponivel -= novoValor;
	}
	
	public void visualizarLances() {
		System.out.println(this.nome + " Fez os seguintes lances " + this.lances);
	}
	
	public void parcelarRecebimento(int numeroParcelas) {
		int valorRecebido = this.saldoDisponivel / numeroParcelas;
		System.out.println("O valor recebido do mes será: " + valorRecebido);
	}
	
}

