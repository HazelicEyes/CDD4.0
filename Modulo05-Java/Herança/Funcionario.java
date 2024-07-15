package Herança;

public class Funcionario extends Pessoa{

	public Funcionario(String nome, String cpf, String telefone) {
		super(nome, cpf, telefone);
	}
	public double salario;
	public String cargo;
}
