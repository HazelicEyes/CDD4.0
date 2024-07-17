package Encapsulamento;

public class Pet {
	private String nome;
	private String tipo;
	private int idade;
	private String cor;
	private boolean vacina; //get e set abaixo
	
	public void ajustarNome(String nome) { //set
		this.nome = nome;
	}
	public void ajustarTipo(String tipo) {
		this.tipo = tipo;
	}
	public void ajustarIdade(int idade) {
		this.idade = idade;
	}
	public void ajustarCor(String cor) {
		this.cor = cor;
	}
	public void ajustarVacina(boolean vacina) {
		this.vacina = vacina;
	}
	public String lerNome() { //get
		return nome;
	}
	public String lerTipo() {
		return tipo;
	}
	public int lerIdade() {
		return idade;
	}
	public String lerCor() {
		return cor;
	}
	public boolean lerVacina() {
		return vacina;
	}
	
	
}
