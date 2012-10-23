package gui;

import java.awt.Canvas;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KnightGame extends Canvas implements KeyListener{
	public KnightGame(){
		super();
		addKeyListener(this);
		setSize(800, 600);
		setIgnoreRepaint(true);
	}

	@Override
	public void keyPressed(KeyEvent e) {
		// TODO call engine or some other keypress method
	}

	@Override
	public void keyReleased(KeyEvent arg0) {
		// TODO call engine or some other keypress method
	}

	@Override
	public void keyTyped(KeyEvent arg0) {
		//probably won't be used
	}
}
