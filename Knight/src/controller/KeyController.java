/**
 * A KeyListener that adds keys to a HashSet for as long as they are down
 * and does not remove them until it receives a keyReleased event.
 * Personal note: handling KeyEvents in this way gives VERY promising results.
 */
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
	
	/**
	 * When a key is down it will be added to the keysDown HashSet
	 * @param e
	 */
	@Override
	public void keyPressed(KeyEvent e) {
		int code = e.getKeyCode();
		keysDown.add(code);
	}
	
	/**
	 * When a key is released it will be removed from the keysDown HashSet
	 * @param e
	 */
	@Override
	public void keyReleased(KeyEvent e) {
		keysDown.remove(e.getKeyCode());
	}
	
	@Override
	public void keyTyped(KeyEvent e) {
		//not used
	}
	
	public HashSet<Integer> getKeysDown(){
		return keysDown;
	}
}
