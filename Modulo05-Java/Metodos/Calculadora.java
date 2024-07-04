package Metodos;

import java.util.Scanner;

public class Calculadora {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		SomarMetodos calculo = new SomarMetodos();
		while(true) {
			System.out.println("\n--MENU--");
			System.out.println("(1) Somar -- (2) Subtrair -- (3) Multiplicação -- (4) Divisão"
					+ " -- (5) Sair");
			System.out.println("Digite um numero: ");
			int resposta = entrada.nextInt();
			
			if(resposta ==1) {
				System.out.println("Vai querer somar com 2 numeros ou com 3 numeros? ");
				int escolha = entrada.nextInt();
				if (escolha ==2) {
					System.out.println("Digite o primeiro numero: ");
					int a = entrada.nextInt();
					System.out.println("Digite o segundo numero: ");
					int b = entrada.nextInt();
					int soma = calculo.somar(a, b);
					System.out.printf("A soma de %d+%d é: "+ soma, a, b);
				}
				else if (escolha ==3) {
					System.out.println("Digite o primeiro numero: ");
					int a = entrada.nextInt();
					System.out.println("Digite o segundo numero: ");
					int b = entrada.nextInt();
					System.out.println("Digite o terceiro numero: ");
					int c = entrada.nextInt();
					int soma = calculo.somar(a,b,c);
					System.out.printf("A soma de %d+%d+%d é: "+ soma, a,b,c);
				}
				else
					System.out.println("Numero errado, digite apenas 2 ou 3");

			}
			else if(resposta ==2) {
				System.out.println("Vai querer subtrair com 2 numeros ou com 3 numeros? ");
				int escolha = entrada.nextInt();
				if (escolha ==2) {
					System.out.println("Digite o primeiro numero: ");
					int a = entrada.nextInt();
					System.out.println("Digite o segundo numero: ");
					int b = entrada.nextInt();
					int sub = calculo.subtrair(a, b);
					System.out.printf("A subtração de %d-%d é: "+ sub, a, b);
				}
				else if (escolha ==3) {
					System.out.println("Digite o primeiro numero: ");
					int a = entrada.nextInt();
					System.out.println("Digite o segundo numero: ");
					int b = entrada.nextInt();
					System.out.println("Digite o terceiro numero: ");
					int c = entrada.nextInt();
					int sub = calculo.subtrair(a,b,c);
					System.out.printf("A subtração de %d-%d-%d é: "+ sub, a,b,c);
				}
				else
					System.out.println("Numero errado, digite apenas 2 ou 3");
			}
			else if(resposta ==3) {
				System.out.println("Vai querer multiplicar com 2 numeros ou com 3 numeros? ");
				int escolha = entrada.nextInt();
				if (escolha ==2) {
					System.out.println("Digite o primeiro numero: ");
					int a = entrada.nextInt();
					System.out.println("Digite o segundo numero: ");
					int b = entrada.nextInt();
					int multi = calculo.multiplicar(a, b);
					System.out.printf("A multiplicação de %d por %d é: "+ multi, a, b);
				}
				else if (escolha ==3) {
					System.out.println("Digite o primeiro numero: ");
					int a = entrada.nextInt();
					System.out.println("Digite o segundo numero: ");
					int b = entrada.nextInt();
					System.out.println("Digite o terceiro numero: ");
					int c = entrada.nextInt();
					int multi = calculo.multiplicar(a,b,c);
					System.out.printf("A multiplicação de %d por %d por %d é: "+ multi, a,b,c);
				}
				else
					System.out.println("Numero errado, digite apenas 2 ou 3");
			}
			else if(resposta ==4) {
				System.out.println("Vai querer dividir com 2 numeros ou com 3 numeros? ");
				int escolha = entrada.nextInt();
				if (escolha ==2) {
					System.out.println("Digite o primeiro numero: ");
					int a = entrada.nextInt();
					System.out.println("Digite o segundo numero: ");
					int b = entrada.nextInt();
					int divi = calculo.dividir(a, b);
					System.out.printf("A divisão de %d por %d é: "+ divi, a, b);
				}
				else if (escolha ==3) {
					System.out.println("Digite o primeiro numero: ");
					int a = entrada.nextInt();
					System.out.println("Digite o segundo numero: ");
					int b = entrada.nextInt();
					System.out.println("Digite o terceiro numero: ");
					int c = entrada.nextInt();
					int divi = calculo.dividir(a,b,c);
					System.out.printf("A divisão de %d por %d por %d é: "+ divi, a,b,c);
				}
				else
					System.out.println("Numero errado, digite apenas 2 ou 3");
			}
			else if(resposta ==5) {
				System.out.println("Saindo...");
				break;
			}
			else {
				System.out.println("Numero errado");
			}
		}
	}

}
