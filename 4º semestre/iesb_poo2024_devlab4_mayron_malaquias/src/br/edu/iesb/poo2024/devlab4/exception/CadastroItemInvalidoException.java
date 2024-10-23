package br.edu.iesb.poo2024.devlab4.exception;

public class CadastroItemInvalidoException extends Exception {
	private static String menssagemErro = "[Erro]: O cadastro do item está invalido "
			+ "o valor do item deve comecar acima de 1 real ou o nome esta nulo";
	
	public CadastroItemInvalidoException() {
		super(menssagemErro);
	}
}
