package gui;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.image.BufferedImage;

import javax.swing.JFrame;

public class KnightWindow extends JFrame{
	private KnightGame game;
	
	public KnightWindow(){
		super("Knight");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		game = new KnightGame();
		add(game);
		pack();
		
		setVisible(true);
	}
	
	public void runGame(){
		game.run();
	}
}
