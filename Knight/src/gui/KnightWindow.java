package gui;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.image.BufferedImage;

import javax.swing.JFrame;

public class KnightWindow extends JFrame{
	private final double FRAMES_PER_SECOND = 60;
	private final double TIME_PER_FRAME = 1000/60;
	private KnightGame game;
	
	public KnightWindow(){
		super("Knight");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		game = new KnightGame();
		add(game);
		pack();
		
		setVisible(true);
	}
	
	public void run(){
		//the image where the game state is rendered
		BufferedImage screen = new BufferedImage(800, 600, BufferedImage.TYPE_INT_RGB);
		//graphics object that renders to the buffered image
		Graphics g = screen.getGraphics();
		//graphics object that draws the buffered image to the window
		Graphics cg = game.getGraphics();
		
		while(true){
			//code to keep the updates and renders per second around 60
			double startTime = System.currentTimeMillis();
			
			//refresh the screen
			g.setColor(Color.blue);
			g.fillRect(0, 0, 800, 600);
			
			//render
			//update
			
			//draw the image to the window
			cg.drawImage(screen, 0, 0, null);
			
			//code to keep the updates and renders per second around 60
			double elapsedTime = System.currentTimeMillis() - startTime;
			if(elapsedTime < TIME_PER_FRAME){
				try{
					Thread.sleep((long)(TIME_PER_FRAME - elapsedTime));
				}catch(Exception e){
					System.out.println(e.getMessage());
				}
			}
		}
	}
}
