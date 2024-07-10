package Construtores;

public class Carro {
	private String cor;
	private double preco;
	private String modelo;
	
	public Carro() {
		
	}
	
	public Carro(String modelo, double preco) {
		this.cor = "PRETA";
		this.modelo = modelo;
		this.preco = preco;
	}
	
	public Carro(String cor, String modelo, double preco) {
		this.cor = cor;
		this.modelo = modelo;
		this.preco = preco;
	}
	public void acelerar() {
		System.out.println("O carro esta acelerando.");
	}
	public void freiar() {
		System.out.println("O carro freiou.");
	}

}
