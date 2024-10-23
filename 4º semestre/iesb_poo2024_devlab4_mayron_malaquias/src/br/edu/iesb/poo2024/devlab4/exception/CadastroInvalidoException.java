package br.edu.iesb.poo2024.devlab4.exception;

public class CadastroInvalidoException extends Exception {
	private static String mensagemErro = "[Erro]: O nome ou cpf do usuario deve ser um valor valido";
	
	public CadastroInvalidoException() {
		super(mensagemErro);
	}
}
