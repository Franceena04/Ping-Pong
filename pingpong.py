import pygame as pg

class Game:
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode([900,700])
        self.clock = pg.time.Clock()	
        self.caption = pg.display.set_caption("Ping Pong")
        self.image = pg.image.load("HD-wallpaper-table-tennis-red-flat-material-ping-pong-red-table-tennis.jpg")
        self.icon = pg.display.set_icon(self.image)
        self.FPS=60
        self.new_game()


    def new_game(self):
        self.game_status = "start"
        self.menu=Menu(self)
        self.ball=Ball(self)
        self.player = player_paddle(self,0,0,pg.K_w,pg.K_s,(60, 99, 142))
        self.opponent=player_paddle(self,880,625,pg.K_UP,pg.K_DOWN,(173, 49, 49))
        

    def start(self):
        keys=pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.game_status = "game"
        if self.game_status == "lose":
            self.new_game()
    
    def check_events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

    def draw(self):
         self.display.fill((56, 56, 56))
         pg.draw.rect(self.display,[128, 125, 125],pg.Rect(10,10,880,675))
         pg.draw.rect(self.display,[56, 56, 56],pg.Rect(20,20,860,655))
         pg.draw.aaline(self.display,(255, 255, 255),(pg.display.get_window_size()[0]/2,20),(pg.display.get_window_size()[0]/2,675))
         

    def update(self):
       self.start()
       self.player.run()
       self.opponent.run()
       self.ball.run() 
       self.clock.tick(self.FPS)
       pg.display.update()


    def run (self):
        while True:
             self.check_events()
             self.draw()
             self.update()
             

class Ball:
    def __init__(self,game):
        self.game=game
        self.radius=25
       
        self.speedx=4
        self.speedy=4
        self.color = (255,255,255)
        
    
    def draw(self):
        if self.game.game_status == "start":
            self.x=self.game.player.top +self.game.player.width
            self.y=(self.game.player.left +self.game.player.length/2) -self.radius / 2
            self.rect=pg.Rect(self.x,self.y,self.radius , self.radius)
            pg.draw.ellipse(self.game.display, self.color,self.rect )

        if self.game.game_status == "game":
            self.rect=pg.Rect(self.x,self.y,self.radius , self.radius)
            pg.draw.ellipse(self.game.display, self.color,self.rect ) 

    
    def collide(self):
        collide1 = pg.Rect.colliderect(self.rect,self.game.player.rect)
        collide2 = pg.Rect.colliderect(self.rect,self.game.opponent.rect)
        if collide1 or collide2:
            self.speedx *=-1
            


    def update(self):
        

        if self.x + self.radius >= pg.display.get_window_size()[0] or self.x  <=0:
            self.game.game_status="lose"

        if self.y + self.radius >= pg.display.get_window_size()[1] or self.y  <=0:
            self.speedy *=-1   
        
        
        

        self.collide()
        self.x+= self.speedx
        self.y+= self.speedy
        
    def run(self):
        self.draw()
        self.update()

    
    
         
class player_paddle: 
    def __init__(self,game,top,left,ctrl1,ctrl2,color):
        self.game = game
        self.color = (217,217,217)
        self.length=75  
        self.width=20
        self.top=top
        self.left=left
        self.speed=6
        self.up=ctrl1
        self.down=ctrl2
        self.color=color
        self.rect=pg.Rect(self.top ,self.left , self.width, self.length)
    
    def draw(self):
        self.rect=pg.Rect(self.top ,self.left , self.width, self.length)
        pg.draw.rect(self.game.display , self.color , self.rect)
        

    def update(self):
        keys=pg.key.get_pressed()

        if keys[self.up] and self.left>=0:
            self.left -= self.speed
        if keys[self.down] and self.left+self.length<=pg.display.get_window_size()[1]:
            self.left += self.speed

    def run(self):
        self.draw()
        self.update()

class Menu:
    def __init__(self,game):
        self.game = game
        self.display = self.game.display
        self.status = self.game.game_status

    def buttons (self,x,y,width,length,color):
        pg.draw.rect(self.display,color,pg.Rect(x,y,width,length))
    
    def pvp(self):
        pass

    def draw(self):
        pg.draw.rect(self.display,)
    
        


                


if __name__=='__main__':
     game=Game()
     game.run()
