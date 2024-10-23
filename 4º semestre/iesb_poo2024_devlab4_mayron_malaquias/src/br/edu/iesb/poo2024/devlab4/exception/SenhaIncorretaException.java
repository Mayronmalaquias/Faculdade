package br.edu.iesb.poo2024.devlab4.exception;

public class SenhaIncorretaException extends Exception {
	private static String mensagemErro = "[Erro]: senha do usuario incorreta";
	
	public SenhaIncorretaException() {
		super(mensagemErro);
	}
}
