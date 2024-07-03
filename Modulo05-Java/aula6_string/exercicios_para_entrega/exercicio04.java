package exercicios_para_entrega;

public class exercicio04 {

	public static void main(String[] args) {
		String texto1 = "Será que são iguais?";
		String texto2 = "Será que são iguais?";
		
		System.out.println(texto1.compareTo(texto2)== 0 ? 
				true + "\nOs textos são iguais ": false + "\nOs textos são diferentes");

	}

}
