package br.edu.iesb.poo2024.devlab5.exceptions.verifcadas.negociais;

public class ContaCorrente {
	private String CPF;
	private String name;
	private double saldo = 0.0;
	
	// EXEMPLO 4
	
	public ContaCorrente(String nome) throws CadastroInvalidoException {
		if(name == null || !name.equals("")) {
			throw new CadastroInvalidoException();
		}
		this.name = nome;
	}
	
	
	
	
	// exemplo 3
	public ContaCorrente(String CPF, String nome) 
		throws Exception{
		if(CPF == null || name == null || (!CPF.equals("")) || !name.equals("")) {
			throw new Exception("[Erro]: É necessario um CPF e nome valido para " + "a criação da conta corrente");
		}
		
		this.CPF = CPF;
		this.name = nome;
	}
	
	
	public String getCPF() {
		return CPF;
	}
	public void setCPF(String cPF) {
		CPF = cPF;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getSaldo() {
		return saldo;
	}
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}
	
	
}
