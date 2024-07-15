package Herança;

public class Faculdade {
	public static void main(String[] args) {
		Aluno aluno1 = new Aluno("Henrique", "11111111111", "81-98888-4444");
		aluno1.matricula = "1111";
		
		Professor prof1 = new Professor("Wellington", "22222222222", "81-98888-4444");
		prof1.salario = 3.400;
		prof1.disciplina = "Matematica";
		
		Funcionario fun1 = new Funcionario("Pedro", "33333333333", "81-98888-4444");
		fun1.salario = 3.400;
		fun1.cargo = "Supervisor";
	}
}
