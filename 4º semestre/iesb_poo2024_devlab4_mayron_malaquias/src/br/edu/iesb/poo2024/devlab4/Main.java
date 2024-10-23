package br.edu.iesb.poo2024.devlab4;

import br.edu.iesb.poo2024.devlab4.exception.CadastroInvalidoException;
import br.edu.iesb.poo2024.devlab4.exception.CadastroItemInvalidoException;
import br.edu.iesb.poo2024.devlab4.exception.InsercaoDeSaldoInvalidoException;


public class Main {
	public static void main(String[] args) {
		System.out.println("Mayron Malaquias Oliveira - 2312082003");
		
		//Exemplo de exeção negocial  a nivel de construtor
		
		Leiloeiro leiloeiro = null;
		Comitente comitente = null;
		Licitente licitente1 = null;
		Licitente licitente2 = null;
		
// --------------------------------------------------------------------------------------
		// Exemplo de exceção a nivel de construtor
		System.out.println("Exemplo: exceção negocial a nivel de construtor");
		try {
			Comitente jorgin = new Comitente("", "");
		} catch(CadastroInvalidoException cie){
			// TODO Auto-generate catch block
			cie.printStackTrace();
		}
// --------------------------------------------------------------------------------------
		
		try {
			comitente = new Comitente("Comitente", "123-456-789-10");
		} catch(CadastroInvalidoException cie){
			// TODO Auto-generate catch block
			cie.printStackTrace();
		}
		
		try {
			licitente1 = new Licitente("Licitente1", "234-567-890-12");
		} catch(CadastroInvalidoException cie){
			// TODO Auto-generate catch block
			cie.printStackTrace();
		}
		
		try {
			licitente2 = new Licitente("Licitente2", "345-678-901-23");
		} catch(CadastroInvalidoException cie){
			// TODO Auto-generate catch block
			cie.printStackTrace();
		}
		
		try {
			leiloeiro = new Leiloeiro("Leiloeiro", "456-789-012-34");
		} catch(CadastroInvalidoException cie){
			// TODO Auto-generate catch block
			cie.printStackTrace();
		}
		
		
// --------------------------------------------------------------------------------------
		//  2 exemplos de tratamentos de exceção em métodos
		System.out.println("Exemplo de tratamento no metodo");
		leiloeiro.logar("geiloeiro", "senha123");
		leiloeiro.logar("Leiloeiro", "enha123");
// --------------------------------------------------------------------------------------
		
		leiloeiro.logar("Leiloeiro", "senha123");
		licitente1.logar("Licitente1", "senha123");
		licitente2.logar("Licitente1", "senha123");
		comitente.logar("Comitente", "senha123");
		
// --------------------------------------------------------------------------------------
		// exemplo de exceção não tratada em Java.
		System.out.println("Exemplo de sem tratamento");
		try {
			licitente1.parcelarRecebimento(0);
		}catch(Exception e) {
			e.printStackTrace();
		}
		
// --------------------------------------------------------------------------------------
		
// --------------------------------------------------------------------------------------
		// 2 exemplos de tratamentos de exceção propagadas e que não são tratadas no método que a lança
		System.out.println("Exemplo de tratamento sem ser no metodo");
		Item cartaCha = null;
		try {
			cartaCha = comitente.inserirItem("Carta do charizard", 0, comitente);
		}catch(CadastroItemInvalidoException ie) {
			ie.printStackTrace();
		}
		
		try {
			cartaCha = comitente.inserirItem("Carta do charizard", 20000, comitente);
		}catch(CadastroItemInvalidoException ie) {
			ie.printStackTrace();
		}
		
		Leilao leilaoCartaCha = leiloeiro.iniciarLeilao(leiloeiro, cartaCha);
		try {
			licitente1.colocarSaldo(0);
		}catch(InsercaoDeSaldoInvalidoException se){
			se.printStackTrace();
		}
		
		
// --------------------------------------------------------------------------------------
		
		//Comitente jorgin = new Comitente("Jorge", "123-123-342-34");
		//Licitente mayron = new Licitente("Mayron", "708-780-601-70");
		//Licitente gus = new Licitente("gus", "987-654-321-11");
		//Leiloeiro pedrin = new Leiloeiro("Pedrin", "123-456-789-00");
		/*
		jorgin.logar("gustavoo", "senha123");
		jorgin.logar("gustavoo", "senha123");
		pedrin.logar("pedrin", "senha123");
		Item cartaCha = jorgin.inserirItem("carta do Charizard", 50000, jorgin);
		Leilao leilaoCartaCha = pedrin.iniciarLeilao(pedrin, cartaCha);
		
		pedrin.iniciarLeilao(pedrin, cartaCha);
		mayron.logar("mayron", "senha123");
		gus.logar("gustavo", "senha123");
		gus.cadastrarEmail("gustavo@iesb.edu.br");
		mayron.colocarSaldo(100000);
		mayron.visualizarSaldo();
		gus.colocarSaldo(200000);
		gus.visualizarSaldo();
		mayron.enviarLance(leilaoCartaCha, 51000, mayron);
		gus.enviarLance(leilaoCartaCha, 55000, gus);
		pedrin.instigarLeilao();
		mayron.enviarLance(leilaoCartaCha, 70000, mayron);
		pedrin.prepararParaFinzalizar();
		gus.enviarLance(leilaoCartaCha, 150000, gus);
		pedrin.finalizarLeilao(leilaoCartaCha);
		pedrin.definirVencedor(leilaoCartaCha);
		pedrin.visualizarLancesLeilao(leilaoCartaCha);
		pedrin.notificaVencedor(leilaoCartaCha);
		gus.visualizarSaldo();
		jorgin.visualizarSaldo();
		*/
	}
}
