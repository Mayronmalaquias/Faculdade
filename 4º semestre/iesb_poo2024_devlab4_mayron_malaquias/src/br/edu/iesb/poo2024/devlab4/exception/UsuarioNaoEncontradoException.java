package br.edu.iesb.poo2024.devlab4.exception;

public class UsuarioNaoEncontradoException extends Exception {
	private static String mensagemErro = "[Erro]: Usuario nao encontrado no sistema";
	
	public UsuarioNaoEncontradoException() {
		super(mensagemErro);
	}
}
