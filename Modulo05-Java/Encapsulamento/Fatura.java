package Encapsulamento;

public class Fatura {
	private String numero;
	private String descricao;
	private int quantidade;
	private double preco;
	
	public Fatura(String numero,String descricao,int quantidade,double preco) {
		this.numero = numero;
		this.descricao = descricao;
		this.quantidade = quantidade;
		this.preco = preco;
	}

	public String getNumero() {
		return numero;
	}
	
	public double getTotalFatura() {
		double total = preco * quantidade;
		if (total < 0) {
			total = 0; }
		
		if (total = 0.0) {
			return 0; }

	}
	
	public void setNumero(String numero) {
		this.numero = numero;
	}
	public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	public int getQuantidade() {
		return quantidade;
	}
	public void setQuantidade(int quantidade) {
		this.quantidade = quantidade;
	}
	public double getPreco() {
		return preco;
	}
	public void setPreco(double preco) {
		this.preco = preco;
	}
	
}
