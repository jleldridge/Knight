package engine;

import java.awt.Graphics;
import java.awt.event.KeyEvent;

import model.Player;

public class Engine {
	private Player player;
	
	public Engine(){
		player = new Player(100, 450);
	}
	
	public void keyPressed(KeyEvent e){
		//figure out which key is pressed
		int code = e.getKeyCode();
		
		//modify the player's state based on which key was pressed
		if(code == KeyEvent.VK_LEFT){
			player.setDx(-10);
		}
		else if(code == KeyEvent.VK_RIGHT){
			player.setDx(10);
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
	
	public void update(){
		//change the horizontal position of the player based on their current speed.
		player.setX(player.getX() + player.getDx());
	}
	
	public void render(Graphics g){
		g.drawImage(player.getSprite(), player.getX(), player.getY(), null);
	}
}
