package gui;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;

public class KnightWindow extends JFrame{
	KnightGame game;
	
	public KnightWindow(){
		super("Knight");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		game = new KnightGame();
		add(game);
		pack();
		
		setVisible(true);
	}
}
