package engine;

import java.awt.Graphics;
import java.awt.event.KeyEvent;

import controller.KeyController;

import model.Player;

public class Engine {
	final int GRAVITY = 2;
	KeyController controller;
	private Player player;
	
	public Engine(KeyController controller){
		this.controller = controller;
		player = new Player(100, 450);
	}
	
	/**
	 * Checks which keys are down in the controller and sets
	 * player's state accordingly
	 */
	private void processKeys(){
		for(Integer code : controller.getKeysDown()){
			//modify the player's state based on which key was pressed
			if(code == KeyEvent.VK_LEFT){
				player.setDx(-10);
			}
			else if(code == KeyEvent.VK_RIGHT){
				player.setDx(10);
			}
			//space key is a jump, so spike player's Dy to negative for one iteration
			//but only if the player is touching the "ground".
			if(code == KeyEvent.VK_SPACE && player.getY() == 450){
				player.setDy(-30);
			}
		}
	}
	
	//I'd like to change the movement so that the player stays on the
	//center of the screen and the background moves based on the player's
	//traversal through the game space, so a game space model will be needed.
	public void update(){
		//change the player's state based on which keys are down
		processKeys();
		
		//change the horizontal position of the player based on their current dx.
		player.setX(player.getX() + player.getDx());
		//change the player's vertical position based on dy.
		player.setY(player.getY() + player.getDy());
		//reduce the player's speed by gravity
		player.setDy(player.getDy() + GRAVITY);
		//stop the player if they reach the ground
		if(player.getY() >= 450){
			player.setDy(0);
			player.setY(450);
		}
		
		//reset appropriate states changed by processKeys()
		player.setDx(0);
	}
	
	public void render(Graphics g){
		g.drawImage(player.getSprite(), player.getX(), player.getY(), null);
	}
}
