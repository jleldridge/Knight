package controller;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.HashSet;

public class KeyController implements KeyListener {
	//hash set to hold the int values of any keys that are currently
	//down and are used by the game.
	private HashSet<Integer> keysDown;
	
	public KeyController(){
		keysDown = new HashSet<Integer>();
	}
	
	@Override
	public void keyPressed(KeyEvent e) {
		int code = e.getKeyCode();
		
		switch(code){
		case KeyEvent.VK_LEFT:
		case KeyEvent.VK_RIGHT:
		case KeyEvent.VK_SPACE:
			keysDown.add(code);
		}
	}
	
	/**
	 * When a key is down it will be added to the keysDown HashSet
	 * @param e
	 */
	@Override
	public void keyReleased(KeyEvent e) {
		keysDown.remove(e.getKeyCode());
	}
	
	/**
	 * When a key is released it will be removed from the keysDown HashSet
	 * @param e
	 */
	@Override
	public void keyTyped(KeyEvent e) {
		//not used
	}

}
