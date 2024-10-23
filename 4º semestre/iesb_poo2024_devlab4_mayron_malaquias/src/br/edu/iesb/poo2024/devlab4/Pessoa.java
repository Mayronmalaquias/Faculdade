package br.edu.iesb.poo2024.devlab4;

import java.util.HashMap;

import br.edu.iesb.poo2024.devlab4.exception.CadastroEmailInvalidoException;
import br.edu.iesb.poo2024.devlab4.exception.CadastroInvalidoException;
import br.edu.iesb.poo2024.devlab4.exception.UsuarioNaoEncontradoException;
import br.edu.iesb.poo2024.devlab4.exception.SenhaIncorretaException;
import br.edu.iesb.poo2024.devlab4.exception.CadastroEmailInvalidoException;


public abstract class Pessoa {
	protected String nome;
	private String cpf;
	private String email = "sem_email";
	private HashMap<String, String> loginData = new HashMap<>();
	protected boolean isLogado = false;

	
	
	
	public Pessoa(String _nome, String _cpf) throws CadastroInvalidoException {
		if(_nome == null || _cpf == null || _nome.equals("")|| _cpf.equals("")) {
			throw new CadastroInvalidoException();
		}
		this.nome = _nome;
		this.cpf = _cpf;
		simularBD();
	}
	
	public void cadastrarEmail(String newEmail) {
		System.out.println("registrando email.." + newEmail);
		this.email = newEmail;
	}
	
	public String getEmail() {
		return this.email;
	}
	
	public String getNome() {
		return this.nome;
	}
	
	public void logar(String userName, String senha) {
	    try {
	    	if (loginData.containsKey(userName)) {
	    		if (loginData.get(userName).equals(senha)) {
	    			System.out.println("Login bem-sucedido!");
	    			this.isLogado = true; 
	    		} else {
	    			throw new SenhaIncorretaException();
	    		}
	    	} else {
	    		throw new UsuarioNaoEncontradoException();
	    	}
	    }catch(UsuarioNaoEncontradoException ue){
			ue.printStackTrace();
	    }catch(SenhaIncorretaException se) {
			se.printStackTrace();
	    }
	}
	
	public void simularBD() {
		this.loginData.put("Comitente", "senha123");
		this.loginData.put("Licitente1", "senha123");
		this.loginData.put("Licitente2", "senha123");
		this.loginData.put("Leiloeiro", "senha123");
	}
	
	public void registrarUsuario(String name, String senha) {
		this.loginData.put(name, senha);
	}
	
	public void realizarLogout() {
		this.isLogado = false;
	}
}

