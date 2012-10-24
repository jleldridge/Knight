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
		
	}
	
	public void keyReleased(KeyEvent e){
		
	}
	
	public void update(){
		
	}
	
	public void render(Graphics g){
		g.drawImage(player.getSprite(), player.getX(), player.getY(), null);
	}
}
