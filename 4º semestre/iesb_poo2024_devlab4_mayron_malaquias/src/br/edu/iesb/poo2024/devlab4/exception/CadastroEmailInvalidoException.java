package br.edu.iesb.poo2024.devlab4.exception;

public class CadastroEmailInvalidoException extends Exception{
	private static String mensagemErro = "[Erro]: O email deve ser um email valido";
	
	public CadastroEmailInvalidoException() {
		super(mensagemErro);
	} 
}
