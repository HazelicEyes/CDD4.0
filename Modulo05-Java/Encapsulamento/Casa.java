package Encapsulamento;

public class Casa {

	public static void main(String[] args) {
		Pet gato = new Pet();
		gato.ajustarNome("Pretinho");
		gato.ajustarTipo("Gato");
		gato.ajustarIdade(2);
		gato.ajustarCor("Preto");
		gato.ajustarVacina(true);
		
		
		System.out.println(gato.lerNome());
		System.out.println(gato.lerCor());
	}

}
