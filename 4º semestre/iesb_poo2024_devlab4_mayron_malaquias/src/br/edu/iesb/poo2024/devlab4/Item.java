package br.edu.iesb.poo2024.devlab4;


public class Item {
	private String nomeItem;
	private int valorInicial;
	private Comitente responsavel;
	
	public Item(String _nomeItem, int _valorInicial, Comitente _responsavel) {
		this.nomeItem = _nomeItem;
		this.valorInicial = _valorInicial;
		this.responsavel = _responsavel;
	}
	
	public void alterarValorInicial(int novoValor) {
		this.valorInicial = novoValor;
	}
	
	public String getNomeItem() {
		return this.nomeItem;
	}
	
	public int geValorInical() {
		return this.valorInicial;
	}
	
	public Comitente getComitente() {
		return this.responsavel;
	}
}

