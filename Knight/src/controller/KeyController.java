/**
 * A KeyListener that adds keys to a HashSet for as long as they are down
 * and does not remove them until it receives a keyReleased event.
 * Personal note: handling KeyEvents in this way gives VERY promising results.
 */
package controller;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Stack;

public class KeyController implements KeyListener {
	//hash set to hold the int values of any keys that are currently
	//down and are used by the game.
	private Stack<Integer> keysDown;
	private boolean jump;
	
	public KeyController(){
		keysDown = new Stack<Integer>();
	}
	
	/**
	 * When a key is down it will be added to the keysDown HashSet
	 * @param e
	 */
	@Override
	public void keyPressed(KeyEvent e) {
		int code = e.getKeyCode();
		if(code == KeyEvent.VK_SPACE){
			jump = true;
		}
		else if(!keysDown.contains(code)){
			keysDown.push(code);
		}
	}
	
	/**
	 * When a key is released it will be removed from the keysDown HashSet
	 * @param e
	 */
	@Override
	public void keyReleased(KeyEvent e) {
		if(e.getKeyCode() == KeyEvent.VK_SPACE){
			jump = false;
		}
		else{
			//need to use Integer.valueOf so that the stack.remove(object)
			//method is used instead of the stack.remove(index) method
			keysDown.remove(Integer.valueOf(e.getKeyCode()));
		}
	}
	
	@Override
	public void keyTyped(KeyEvent e) {
		//not used
	}
	
	public Stack<Integer> getKeysDown(){
		return keysDown;
	}
	
	public boolean getJump(){
		return jump;
	}
}
