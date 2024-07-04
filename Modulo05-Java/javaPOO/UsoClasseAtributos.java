package javaPOO;

public class UsoClasseAtributos {

	public static void main(String[] args) {
		AtributosClasses cliente01 = new AtributosClasses();
		System.out.println(cliente01.fnome);
		System.out.println(cliente01.lnome);
		System.out.println(cliente01.idade);
		System.out.printf("O aluno %s %s tem %d anos", cliente01.fnome, 
				cliente01.lnome, cliente01.idade);
	}

}
