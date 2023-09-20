package aplicaçãoGraficaConta;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

import conta.Conta;

public class AplicacaoGraficaConta {

	private JFrame frame;
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JLabel lblNumero;
	private JLabel lblCliente;
	private JButton button1;
	private JLabel lblValor;
	private JButton button3;
	private JButton button4;
	private JButton button2;
	private JLabel lblMensagem;
	
	private Conta conta;


	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					AplicacaoGraficaConta window = new AplicacaoGraficaConta();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public AplicacaoGraficaConta() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setTitle("Caixa Eletronico");
		frame.setBounds(100, 100, 413, 261);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);

		lblNumero = new JLabel("numero");
		lblNumero.setBounds(26, 30, 46, 14);
		frame.getContentPane().add(lblNumero);

		lblCliente = new JLabel("cpf");
		lblCliente.setBounds(26, 55, 46, 14);
		frame.getContentPane().add(lblCliente);

		textField = new JTextField();
		textField.setBounds(91, 27, 86, 20);
		frame.getContentPane().add(textField);
		textField.setColumns(10);

		textField_1 = new JTextField();
		textField_1.setBounds(91, 52, 86, 20);
		frame.getContentPane().add(textField_1);
		textField_1.setColumns(10);

		button1 = new JButton("criar conta");
		button1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				if(textField.getText().isEmpty() || textField_1.getText().isEmpty()) {
					lblMensagem.setText("campo vazio ");
					return;
				}
				String num = textField.getText();
				String cpf = textField_1.getText();
				conta = new Conta(num, cpf);
				lblMensagem.setText("conta criada ");
			}
		});
		button1.setBounds(212, 26, 99, 23);
		frame.getContentPane().add(button1);

		button2 = new JButton("exibir");
		button2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if(conta==null)
					lblMensagem.setText("conta inexistente");
				else
					lblMensagem.setText(conta.toString());
			}
		});
		button2.setBounds(212, 51, 89, 23);
		frame.getContentPane().add(button2);

		button3 = new JButton("creditar");
		button3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if(conta==null) {
					lblMensagem.setText("conta inexistente");
					return;
				}
				if(textField_2.getText().isEmpty()) {
					lblMensagem.setText("valor inexistente");
					return;
				}

				double valor = Double.parseDouble(textField_2.getText());
				conta.creditar(valor); 
				lblMensagem.setText("credito efetuado");
			}
		});
		button3.setBounds(188, 137, 89, 23);
		frame.getContentPane().add(button3);

		button4 = new JButton("debitar");
		button4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if(conta==null) {
					lblMensagem.setText("conta inexistente");
					return;
				}
				if(textField_2.getText().isEmpty()) {
					lblMensagem.setText("valor inexistente");
					return;
				}
				
				double valor = Double.parseDouble(textField_2.getText());
				try{
					conta.debitar(valor); 
					lblMensagem.setText("debito efetuado");
				}
				catch(Exception erro) {
					//System.out.println(erro.getMessage());
					lblMensagem.setText(erro.getMessage());
				}
				
			}
		});
		button4.setBounds(287, 137, 89, 23);
		frame.getContentPane().add(button4);

		lblValor = new JLabel("valor");
		lblValor.setBounds(26, 141, 46, 14);
		frame.getContentPane().add(lblValor);

		textField_2 = new JTextField();
		textField_2.setBounds(91, 138, 86, 20);
		frame.getContentPane().add(textField_2);
		textField_2.setColumns(10);

		lblMensagem = new JLabel("Mensagem ao usuario");
		lblMensagem.setBounds(26, 197, 344, 14);
		frame.getContentPane().add(lblMensagem);
	}
}