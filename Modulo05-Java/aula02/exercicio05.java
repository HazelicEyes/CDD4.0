package aula02;

import java.util.Scanner;

public class exercicio05 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite uma letra: ");
		char resposta = entrada.next().charAt(0);
		
		System.out.println(resposta == 'm' || resposta == 'M'? "Masculino": "Feminino");
//		if (resposta == 'M' || resposta == 'm') {
//			System.out.println("M - Masculino");
//		}
//		else if (resposta == 'F' || resposta == 'f') {
//			System.out.println("F - Feminino");
//		}
//		else {
//			System.out.println("Outro");
//		}

	}

}
