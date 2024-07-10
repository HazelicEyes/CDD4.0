package Construtores;

public class Aplicacao {

	public static void main(String[] args) {
		Carro prototipoDeCarro = new Carro();
		Carro civicPreto = new Carro("New Civic", 40000);
		Carro golfAmarelo = new Carro("Preto", "Golf",38000);
		civicPreto.acelerar();

	}

}
