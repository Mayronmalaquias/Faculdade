package br.edu.iesb.poo2024.devlab5;

import br.edu.iesb.poo2024.devlab5.exceptions.naoverificada.ExecaoNaoVerificada;
import br.edu.iesb.poo2024.devlab5.exceptions.verifcadas.ManipulaArquivoTexto;
import br.edu.iesb.poo2024.devlab5.exceptions.verifcadas.negociais.CadastroInvalidoException;
import br.edu.iesb.poo2024.devlab5.exceptions.verifcadas.negociais.ContaCorrente;

public class DevLab5Main {

	public static void main(String[] args) {
		
		// exmplo 1 : exeção não verificada
		System.out.println("Exemplo1: excecao nao verificada ou nao tratada");
		ExecaoNaoVerificada execaoNaoVerificada = new ExecaoNaoVerificada();
		execaoNaoVerificada.doExemplo1();
		
		/* -----------------------------------------------------------------*/
		
		//exemplo 2 : execao verificada
		System.out.println("Exemplo2: excecao verificada tratada");
		ManipulaArquivoTexto manipulaArquivoTexto = new ManipulaArquivoTexto();
		manipulaArquivoTexto.processarArquivoTexto("alunos_poo_nt.txt");
		
		
		/* -----------------------------------------------------------------*/
		
		// exemplo 2.1: excecap verificada  e nao tratada
		System.out.println("Exemplo 2.1: exceção verificada e nao tratada");
		try {
			manipulaArquivoTexto.processarArquivoTextoSemTratarExcecao("alunos_poo_nt.txt");
		} catch(Exception e){
			e.printStackTrace();
		}
		
		
		/* -----------------------------------------------------------------*/
		
		//Exemplo 3: exceção negocial a nivel de construtor
		System.out.println("Exemplo 3: exceção negocial a nivel de construtor");
		try {
			ContaCorrente contaCorrente = new ContaCorrente(null, null);
		} catch(Exception e){
			e.printStackTrace();
		}
		
		/* -----------------------------------------------------------------*/
		
		//Exemplo 4; exeção negocial  a nivel de construtor
		System.out.println("Exemplo 4: exceção negocial a nivel de construtor");
		try {
			ContaCorrente contaCorrente = new ContaCorrente("");
		} catch(CadastroInvalidoException cie){
			// TODO Auto-generate catch block
			cie.printStackTrace();
		}
	}

}
