package Polimorfismo;

public class Sobrecarga {

	public static void main(String[] args) {
		Soma calculo = new Soma();
		int soma1 = calculo.somar(1, 2);
		int soma2 = calculo.somar(1, 2, 3);
		
		System.out.println(soma1);
		System.out.println(soma2);
	}

}
