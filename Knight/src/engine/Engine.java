package engine;

import java.awt.Graphics;
import java.awt.event.KeyEvent;

import model.Player;

public class Engine {
	final int GRAVITY = 5;
	private Player player;
	
	public Engine(){
		player = new Player(100, 450);
	}
	
	public void keyPressed(KeyEvent e){
		//figure out which key is pressed
		int code = e.getKeyCode();
		
		//modify the player's state based on which key was pressed
		if(code == KeyEvent.VK_LEFT){
			player.setDx(-25);
		}
		else if(code == KeyEvent.VK_RIGHT){
			player.setDx(25);
		}
		//space key is a jump, so spike player's Dy to negative for one iteration
		//but only if the player is touching the "ground".
		else if(code == KeyEvent.VK_SPACE && player.getY() == 450){
			player.setDy(-50);
		}
	}
	
	public void keyReleased(KeyEvent e){
		//figure out which key is released
		int code = e.getKeyCode();
		
		//modify the player's state based on which key was released
		//in this case only drop speed to zero if the key relevant
		//to the current dx was released.
		if(code == KeyEvent.VK_LEFT && player.getDx() < 0){
			player.setDx(0);
		}
		else if(code == KeyEvent.VK_RIGHT && player.getDx() > 0){
			player.setDx(0);
		}
	}
	
	//I'd like to change the movement so that the player stays on the
	//center of the screen and the background moves based on the player's
	//traversal through the game space, so a game space model will be needed.
	public void update(){
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
	}
	
	public void render(Graphics g){
		g.drawImage(player.getSprite(), player.getX(), player.getY(), null);
	}
}
