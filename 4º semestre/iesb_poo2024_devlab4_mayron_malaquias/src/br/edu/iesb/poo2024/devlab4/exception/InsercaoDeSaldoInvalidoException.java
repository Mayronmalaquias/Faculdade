package br.edu.iesb.poo2024.devlab4.exception;

public class InsercaoDeSaldoInvalidoException extends Exception {
	private static String mensagemErro = "[Erro]: O valor a ser inserido deve ser um valor valido!";
	
	public InsercaoDeSaldoInvalidoException() {
		super(mensagemErro);
	}

}
