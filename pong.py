from graphics import *
import time
import random
def main():
	inicio=GraphWin("iniciar", 600, 500)
	telainicio=Rectangle(Point(10,10),Point(590,490))
	telainicio.setFill("black")
	telainicio.draw(inicio)
	titulo=Text(Point(300,80),"PYPONG")
	titulo.setOutline("white")
	titulo.setSize(20)
	titulo.draw(inicio)
	jogar=Text(Point(300,360),'Aperte "ENTER" para jogar')
	jogar.setOutline("white")
	jogar.setSize(20)
	jogar.draw(inicio)
	sair=Text(Point(300,420),'Aperte "ESC" para sair do jogo')
	sair.setOutline("white")
	sair.setSize(20)
	sair.draw(inicio)
	#inicio.getMouse()
	
	fechar=inicio.getKey()
	proximo=inicio.getKey()
	if(fechar=="Escape"):
		inicio.close()
	elif(proximo=="Return"):
		inicio.close()
		jogo=GraphWin("jogar", 600, 500)
		telajogo=Rectangle(Point(10,10),Point(590,490))
		telajogo.setFill("black")
		telajogo.draw(jogo)
		placar1=Line(Point(10,100),Point(590,100))
		placar1.setFill("white")
		placar1.draw(jogo)
		placar2=Line(Point(300,10),Point(300,100))
		placar2.setFill("white")
		placar2.draw(jogo)
		placarIA=Text(Point(110,60),"Pontuação IA:")
		placarIA.setTextColor("red")
		placarIA.setSize(20)
		placarIA.draw(jogo)
		placarjog=Text(Point(410,60),"Pontuação P1:")
		placarjog.setTextColor("red")
		placarjog.setSize(20)
		placarjog.draw(jogo)
		jogador=Rectangle(Point(565,230),Point(580,290))
		jogador.setFill("blue")
		jogador.draw(jogo)
		IA=Rectangle(Point(25,230),Point(40,290))
		IA.setFill("green")
		IA.draw(jogo)
		bola=Circle(Point(295,245), 10)
		bola.setFill("white")
		bola.draw(jogo)
		pontosIA=0
		pontosP1=0
		vel_bola_x=0
		vel_bola_y=0
		vel_abso_bola=0
		vel_jogador_y=0
		pontosIA=0
		pontosP1=0
		placarP1=Text(Point(510,60),"")
		placarP1.setText(str(pontosP1))
		placarP1.setSize(20)
		placarP1.setTextColor("blue")
		placarP1.draw(jogo)
		placarIA=Text(Point(205,60),"")
		placarIA.setText(str(pontosIA))
		placarIA.setTextColor("green")
		placarIA.setSize(20)
		placarIA.draw(jogo)	
		abso=[0.1,0.2]
		iniciacao=[0.1,-0.1,0.2,-0.2]
		while True:
			vel_abso_bola=random.choice(abso)
		#Pré-Movimentação da bola:
			if vel_bola_x==0 and vel_bola_y==0:
				time.sleep(0.5)
				vel_bola_x=random.choice(iniciacao)
				vel_bola_y=random.choice(iniciacao)
			if bola.getCenter().y<110:
				vel_bola_y=vel_abso_bola
			elif bola.getCenter().x>560 and bola.getCenter().y<jogador.getP2().y and bola.getCenter().y>jogador.getP1().y:
				vel_bola_x=-vel_abso_bola
			elif bola.getCenter().y>480:
				vel_bola_y=-vel_abso_bola
			elif bola.getCenter().x<40 and bola.getCenter().y<IA.getP2().y and bola.getCenter().y>IA.getP1().y: 
				vel_bola_x=vel_abso_bola
		#Movimentação da IA:
			if IA.getCenter().y>80:
				if IA.getCenter().y<bola.getCenter().y:
					IA.move(0,0.1)
			if IA.getCenter().y<500:
				if IA.getCenter().y>bola.getCenter().y:
					IA.move(0,-0.1)
		#Contagem do Placar:
			if bola.getCenter().x+10<10:
				pontosP1=pontosP1+1	
				placarP1.undraw()
				placarP1=Text(Point(510,60),"")			
				placarP1.setText(str(pontosP1))
				placarP1.setSize(20)
				placarP1.setTextColor("blue")
				jogador.undraw()
				jogador=Rectangle(Point(565,230),Point(580,290))
				jogador.setFill("blue")
				IA.undraw()
				IA=Rectangle(Point(25,230),Point(40,290))
				IA.setFill("green")
				bola.undraw()
				bola=Circle(Point(295,245), 10)
				bola.setFill("white")
				vel_bola_x=0
				vel_bola_y=0
				jogador.draw(jogo)
				placarP1.draw(jogo)
				IA.draw(jogo)
				bola.draw(jogo)
				if pontosP1==7:
					bola.undraw()
					vitoria=Text(Point(320,280),"Parabéns, você venceu o jogo!")			
					vitoria.setSize(20)
					vitoria.setTextColor("green1")
					vitoria.draw(jogo)
					break
			if bola.getCenter().x+10>590:
				pontosIA=pontosIA+1	
				placarIA.undraw()
				placarIA=Text(Point(205,60),"")			
				placarIA.setText(str(pontosIA))
				placarIA.setSize(20)
				placarIA.setTextColor("green")
				jogador.undraw()
				jogador=Rectangle(Point(565,230),Point(580,290))
				jogador.setFill("blue")
				IA.undraw()
				IA=Rectangle(Point(25,230),Point(40,290))
				IA.setFill("green")
				bola.undraw()
				bola=Circle(Point(295,245), 10)
				bola.setFill("white")
				vel_bola_x=0
				vel_bola_y=0
				jogador.draw(jogo)
				placarIA.draw(jogo)
				IA.draw(jogo)
				bola.draw(jogo)
				if pontosIA==4:
					provocacao=Text(Point(170,110),"Isso é tudo que você tem? hahaha")
					provocacao.setTextColor("white")
					provocacao.setSize(15)
					provocacao.draw(jogo)
					time.sleep(2)
					provocacao.undraw()
				if pontosIA==7:
					bola.undraw()
					derrota=Text(Point(320,280),"Desculpe, você perdeu o jogo!")			
					derrota.setSize(20)
					derrota.setTextColor("red")
					derrota.draw(jogo)
					break	
		#Movimento geral de tudo:
			bola.move(vel_bola_x,vel_bola_y)
			mover=jogo.checkKey()
			if(mover!="Escape"):
				#if IA.getCenter().y>130:
				#	if mover=="w":
				#		IA.move(0,-7)
				if jogador.getCenter().y>130:
					if mover=="Up":
						jogador.move(0,-10)
				if jogador.getCenter().y<460:
					if mover=="Down":
						jogador.move(0,10)
				mover=jogo.checkKey()
		jogo.getMouse()
		jogo.close()
if __name__=="__main__":
	main()

