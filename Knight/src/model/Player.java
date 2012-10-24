package model;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;

public class Player {
	//the player's position
	private int x, y;
	//the player's speed
	private int dx, dy;
	//the player's sprite
	private BufferedImage sprite;
	
	public Player(){
		//set the player's position and speed
		x = 0;
		y = 0;
		dx = 0;
		dy = 0;
		
		//initialize the temporary sprite and draw it
		sprite = new BufferedImage(32, 96, BufferedImage.TYPE_INT_RGB);
		Graphics g = sprite.getGraphics();
		g.setColor(Color.white);
		g.fillRect(0, 0, 32, 96);
	}
	
	public Player(int x, int y){
		//set the player's position and speed
		this.x = x;
		this.y = y;
		dx = 0;
		dy = 0;
		
		//initialize the temporary sprite and draw it
		sprite = new BufferedImage(32, 96, BufferedImage.TYPE_INT_RGB);
		Graphics g = sprite.getGraphics();
		g.setColor(Color.white);
		g.fillRect(0, 0, 32, 96);
	}

	public int getX() {
		return x;
	}

	public void setX(int x) {
		this.x = x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
		this.y = y;
	}

	public int getDx() {
		return dx;
	}

	public void setDx(int dx) {
		this.dx = dx;
	}

	public int getDy() {
		return dy;
	}

	public void setDy(int dy) {
		this.dy = dy;
	}

	public BufferedImage getSprite() {
		return sprite;
	}
}
