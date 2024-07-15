package Polimorfismo;

public class Cachorro extends Animal{

	public Cachorro(String nome, int idade) {
		super(nome, idade);
	}
	public void emitirSom() {
		System.out.println("O cachorro esta latindo");
	}
}
