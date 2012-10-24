/**
 * KnightGame is Canvas subclass that serves as both the surface to draw to
 * and the container for the main game loop.
 */
package gui;

import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.image.BufferedImage;

import controller.KeyController;

import engine.Engine;

public class KnightGame extends Canvas{
	private final int FRAMES_PER_SECOND = 60;
	private final int TIME_PER_FRAME = 1000/FRAMES_PER_SECOND;
	private Engine engine;
	private KeyController controller;
	
	public KnightGame(){
		super();
		setSize(800, 600);
		setIgnoreRepaint(true);
		
		controller = new KeyController();
		addKeyListener(controller);
		engine = new Engine(controller);
	}
	
	public void run(){
		//the image where the game state is rendered
		BufferedImage screen = new BufferedImage(800, 600, BufferedImage.TYPE_INT_RGB);
		//graphics object that renders to the buffered image
		Graphics g = screen.getGraphics();
		//graphics object that draws the buffered image to the window
		Graphics cg = getGraphics();
		
		while(true){
			//code to keep the updates and renders per second around 60
			long startTime = System.currentTimeMillis();
			
			//refresh the screen
			g.setColor(Color.blue);
			g.fillRect(0, 0, 800, 600);
			
			engine.update();
			engine.render(g);
			
			//draw the image to the window
			cg.drawImage(screen, 0, 0, null);
			
			//code to keep the updates and renders per second around 60
			long elapsedTime = System.currentTimeMillis() - startTime;
			if(elapsedTime < TIME_PER_FRAME){
				try{
					Thread.sleep(TIME_PER_FRAME - elapsedTime);
				}catch(Exception e){
					System.out.println(e.getMessage());
				}
			}
		}
	}
}
