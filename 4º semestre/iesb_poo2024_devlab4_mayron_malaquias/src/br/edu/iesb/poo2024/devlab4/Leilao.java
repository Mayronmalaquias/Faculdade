package br.edu.iesb.poo2024.devlab4;
import java.util.ArrayList;
import java.util.List;

public class Leilao {
	private String dataInicio;
	private String dataFim;
	private Licitente vencedor;
	private Leiloeiro leiloeiroResponsavel;
	private List<Integer> lances = new ArrayList<>();
	private Item itemLeiloado;
	private int valorAtual;
	private String nomeAtual;
	private boolean isFinalizado = false;
	
	public Leilao(String _dataInicio, Leiloeiro _leiloeiroResponsavel, Item _itemLeiloado) {
		this.dataInicio = _dataInicio;
		this.leiloeiroResponsavel = _leiloeiroResponsavel;
		this.itemLeiloado = _itemLeiloado;
	}
	
	public void gerarVencedor() {
		if(lances.isEmpty()) {
			System.out.println("nao houve proposta");
		}else {
			int valorLance = lances.get(lances.size() - 1);
			System.out.println("O " + vencedor.getNome() + " ganhou o " + itemLeiloado.getNomeItem() + " pelo valor de:" + valorLance);
			vencedor.modificarSaldo(valorLance);
			Comitente comitente = itemLeiloado.getComitente();
			comitente.modificarSaldo(valorLance);
		}
	}
	
	public void receberLance(int valor, Licitente pessoa) {
		if(this.isFinalizado == false) {
			if(valor > this.valorAtual && valor >= itemLeiloado.geValorInical()) {
				this.valorAtual = valor;
				this.vencedor = pessoa;
				this.lances.add(this.valorAtual);
				System.out.println("Seu lance foi enviado!!");
			}else {
				if(this.valorAtual > itemLeiloado.geValorInical()) {
					System.out.println("Voce deve cobrir o lance atual de: " + this.valorAtual);					
				}else {
					System.out.println("Voce deve cobrir o Valor inicial de: " + itemLeiloado.geValorInical());
				}
			}			
		}else {
			System.out.println("Sinto muito o leilao fechou");
		}
	}
	public void isFechado() {
		System.out.println("Vendidoooo para o " + vencedor.getNome());
		this.isFinalizado = true;
	}
	
	public void notificarVencedor() {
		vencedor.receberEmail(vencedor);
	}
	
	public void verLance() {
		System.out.println(this.lances);
	}
	
	public void setItem(Item novoItem) {
		this.itemLeiloado  = novoItem;
	}
}
