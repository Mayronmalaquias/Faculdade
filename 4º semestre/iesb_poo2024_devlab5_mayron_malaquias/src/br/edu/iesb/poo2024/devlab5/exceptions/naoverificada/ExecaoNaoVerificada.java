package br.edu.iesb.poo2024.devlab5.exceptions.naoverificada;

public class ExecaoNaoVerificada {

	public void doExemplo1() {
		
		try {
			
			int divisaoErrada = 100 /0;
			
		}catch(ArithmeticException ae) {
			
			System.err.println(ae);
			ae.printStackTrace();
			
		}catch(Exception e) {
			
			e.printStackTrace();
			
		}
		
		
		finally {
			
			System.out.println("[log] esse codigo sempre será executado!" + getClass());
			
		}
		
	}
}
