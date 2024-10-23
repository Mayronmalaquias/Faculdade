package br.edu.iesb.poo2024.devlab5.exceptions.verifcadas.negociais;

public class CadastroInvalidoException extends Exception {
	private static String mensagemErro = "[Erro]: É necessario um CPF e nome valido para " +
			"a criação da conta corrente";

	public CadastroInvalidoException() {
		super(mensagemErro);
	}
}
