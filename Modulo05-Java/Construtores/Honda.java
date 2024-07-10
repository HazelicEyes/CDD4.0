package Construtores;

public class Honda extends Carro {
	public String motor;
	
	public Honda() {
		
	}
	
	public Honda(String motor, String modelo, double preco) {
		super(modelo,preco);
		this.motor = motor;
	}
}
