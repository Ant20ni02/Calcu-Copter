from pygame import *
import sys
import random

#Marco Antonio Gardida Cortés A01423221
#Martín Daniel Uribe Reza A01423400

rf1 =["42", "48", "72"]
rf2 =["156.25 m^2", "78.13 m^2", "195.31 m^2"]
rf3 =["98.596 m^3", "31.4 m^3", "49.3 m^3"]
rf4 =["12", "6", "8"]
rf5 =["11", "94", "-12"]
rm1 =["9n-3", "6n-2", "8n-3"]
rm2 =["x^5", "x^6", "x^6"]
rm3 =["50.5", "78.5", "123.5"]
rm4 =["$2058.00", "$11,662.00", "2744.00"]
rm5 =["6.63","5.78", "7.41"]
rd1 =["12", "-27", "39"]
rd2 =["20 km/h", "50 km/h", "25 km/h"]
rd3 =["105°", "15°", "75°"]
rd4 =["13.6u", "7.55u", "19u"]
rd5 =["x=3", "x=4", "x=6"]


preguntas=["¿Cuál es el resultado de: 12×4-2(9÷3)?", "¿Cuál es el área de un cuadrado de 12.5 m de lado?", "¿Cuál es el volumen de un cilindro de radio 3 m y altura 10 m?", "¿Cuántas aristas tiene un cubo?", "¿Cuál es el resultado de: 5(32÷8?)+27-4×9", "¿Cuál es el perímetro de un triángulo de lado 3n-1?", "¿Cuál es el valor de x en la siguiente operación: x³x²?","¿Cuánto vale y si x vale 13 en: y=9.5x-73?", "¿Cuánto es el 15% de $13,720.00?", "¿Cuál es el promedio de: 8.4, 1.7, 3.5, 9.9, 7.7, 8.3, 6.9?", "¿Cuál es la pendiente de la recta y=12x-27","¿Cuál es la velocidad de algo que viajó 100 kilómetros en 5 horas?", "¿Cuál es el ángulo suplementario de 75°?", "¿Cuál es el valor de la hipotenusa del triángulo de lados 8u y 11u?", "Encuentra el valor positivo de x en: y=x^2+x-12"]
respuestas = [rf1,rf2,rf3,rf4,rf5,rm1,rm2,rm3,rm4,rm5,rd1,rd2,rd3,rd4,rd5]



def pintar_boton(screen,boton,palabra):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen,(255, 255, 255), boton,0)
    else:
        draw.rect(screen,(105,173,90), boton,0)
    texto = font.render(palabra, True, (0,0,0))
    screen.blit(texto,(boton.x+(boton.width-texto.get_width())/2,boton.y+(boton.height-texto.get_height())/2))
    




init()
#Recursos--------------------------------------------------------------------------------------------------------------------------
screen = display.set_mode((1280,720))
mixer.init()
sound_heli = mixer.Sound("sound_heli.wav")
soundtrack1 = mixer.Sound("sountrack1.wav")
soundtrack2 = mixer.Sound("sountrack2.wav")
mixer.music.load("explosion.wav")
fondo0 = image.load('Fondo0.png')
titulo = image.load('Titulo.png')
fondo1 = image.load('Fondo1.jpg')
fondo2 = image.load('Fondo2.jpg')
fondo3 = image.load('Fondo3.jpg')
heli = image.load('Heli.png')
intro1 = image.load('INTRO1.png')
fondo_pregunta = image.load('fondopregunta.jpg')
misil = image.load('misil.png')
explosion = image.load('explosion.png')
incorrecto1 = image.load('incorrecto1.png')
incorrecto2 = image.load('incorrecto2.png')
correcto = image.load('corecto.png')
fondoinstrucciones = image.load('instrucciones.png')
fondo0 = transform.scale(fondo0,(1280,720))
fondo1 = transform.scale(fondo1,(1280,720))
fondo2 = transform.scale(fondo2,(1280,720))
fondo3 = transform.scale(fondo3,(1280,720))
titulo = transform.scale(titulo,(640,173))
correcto = transform.scale(correcto,(640,655))
fondo_pregunta = transform.scale(fondo_pregunta,(1280,626))
intro1 = transform.scale(intro1,(128,72))
misil = transform.scale(misil,(179,34))
explosion = transform.scale(explosion,(400,256))
incorrecto1 = transform.scale(incorrecto1,(743,597))
incorrecto2 = transform.scale(incorrecto2,(743,597))
font = font.SysFont("Castellar",30)



#Variables---------------------------------------------------------------------------------------------------------------------------------
GuardadoF = 1
GuardadoM = 6
GuardadoD = 11

#Botones-----------------------------------------------------------------------------
facil = Rect(515,288,250,120)
medio = Rect(515,432,250,120)
dificil = Rect(515,576,250,120)
inst = Rect(956,576,300,120)
menu = Rect(5,665,120,50)
pregunta = Rect(130,665,200,50)
cerrarp = Rect(540,524,200,50)
aceptar = Rect(537,660,200,50)
aceptar2 = Rect(537,660,200,50)
#743 * 597   532,118

#----------------------------------------------------------------------------------------


def escena0(screen):
    sound_heli.stop()
    soundtrack2.stop()
    soundtrack1.play()
    while True:
        screen.blit(fondo0,(0,0))
        screen.blit(titulo,(320,10))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                if inst.collidepoint(mouse.get_pos()):
                    return 16
                if facil.collidepoint(mouse.get_pos()):
                    return GuardadoF
                if medio.collidepoint(mouse.get_pos()):
                    return GuardadoM
                if dificil.collidepoint(mouse.get_pos()):
                    return GuardadoD
        pintar_boton(screen,facil,"Fácil")
        pintar_boton(screen,medio,"Medio")
        pintar_boton(screen,dificil,"Difícil")
        pintar_boton(screen,inst,"Instrucciones")
        display.flip()
def escenaInst(screen):
    while True:
        screen.blit(fondoinstrucciones,(0,0))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                if menu.collidepoint(mouse.get_pos()):
                    return 0
        pintar_boton(screen,menu,"Menú")
        display.flip()
    
        
def juego(screen,i):
    soundtrack1.stop()
    soundtrack2.play()
    sound_heli.play()
    x,y= 0,306
    x1,y1 = 1280,113
    x2,y2 = 1280,343    #Misil mide 34 de alto
    x3,y3 = 1280,573
    ñ = 0
    xd = 0
    cuenta = 0
    answers = respuestas[i].copy()
    answer =[]
    while cuenta < 3:
        r = random.choice(answers)
        answers.remove(r)
        answer.append(r)
        cuenta += 1
    clock = time.Clock()
    if i >= 0 and i < 5:
        Timer = 30
    elif i >= 5 and i < 10:
        Timer= 45
    elif i >= 10 and i < 15:
        Timer = 60
    dt = 0
    correctoxd = 0
    while True:
        if i >= 0 and i < 5:
            screen.blit(fondo1,(0,0))
        elif i >= 5 and i < 10:
            screen.blit(fondo2,(0,0))
        elif i >= 10 and i < 15:
            screen.blit(fondo3,(0,0))
        if Timer != 0 and xd == 0:
            Timer -= dt
        temporizador = font.render("Tiempo Restante: "+str(int(round(Timer,0))),True,(0,0,0))
        screen.blit(temporizador,(5,5))
        for e in event.get():
            if e.type ==QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                if menu.collidepoint(mouse.get_pos()) and xd == 0:
                    return 0
                if pregunta.collidepoint(mouse.get_pos()) and xd == 0:
                    ñ = 0
                if cerrarp.collidepoint(mouse.get_pos()) and ñ==0:
                    ñ = 1
                if aceptar.collidepoint(mouse.get_pos()) and xd == 1 and correctoxd !=1 and correctoxd != 2 and correctoxd != 3:
                    return i+1
                if aceptar2.collidepoint(mouse.get_pos()) and xd == 1 and correctoxd == 1:
                    if i+2 == 6 or i+2 == 11 or i+2== 16:
                        return 0
                    else:
                        return i+2
                if aceptar2.collidepoint(mouse.get_pos()) and xd == 1 and correctoxd == 2:
                    if i+2 == 6 or i+2 == 11 or i+2== 16:
                        return 0
                    else:
                        return i+2
                if aceptar2.collidepoint(mouse.get_pos()) and xd == 1 and correctoxd == 3:
                    if i+2 == 6 or i+2 == 11 or i+2== 16:
                        return 0
                    else:
                        return i+2
                
        if key.get_pressed()[K_s] and y < 611 and ñ == 1 and xd == 0:
            y += 7.5
        if key.get_pressed()[K_w] and y > 0 and ñ == 1 and xd == 0 :
            y -= 7.5
        if key.get_pressed()[K_a] and x >= 0 and ñ == 1 and xd == 0:
            x -= 7.5
        if key.get_pressed()[K_d] and x <= 830 and ñ == 1 and xd == 0:
            x += 7.5
        screen.blit(heli,(x,y))
        pintar_boton(screen,pregunta,"Pregunta")
        pintar_boton(screen,menu,"Menú")
        draw.rect(screen,(0, 0, 255,255),(900,30,280,200),5)
        draw.rect(screen,(0, 0, 255,255),(900,260,280,200),5)
        draw.rect(screen,(0, 0, 255,255),(900,490,280,200),5) 
        r1 = font.render(answer[0], True, (255,255,255))
        screen.blit(r1,(900+(280-r1.get_width())/2,30+(200-r1.get_height())/2))
        r2 = font.render(answer[1], True, (255,255,255))
        screen.blit(r2,(900+(280-r2.get_width())/2,260+(200-r2.get_height())/2))
        r3 = font.render(answer[2], True, (255,255,255))
        screen.blit(r3,(900+(280-r3.get_width())/2,490+(200-r3.get_height())/2))
        if ñ == 0:
            screen.blit(fondo_pregunta,(0,47))
            pintar_boton(screen,cerrarp,"Cerrar")
            q = font.render(preguntas[i], True, (255,255,255))
            screen.blit(q,(0+(1280-q.get_width())/2,47+(626-q.get_height())/2))
        if answer[0] == respuestas[i][0]:
            if x >= 670 and 229 > y > 31:
                xd = 1
                correctoxd = 1
                screen.blit(correcto,(532,118))
                pintar_boton(screen,aceptar2,"Gracias")
            if x >= 670 and 359 > y > 261 or round(Timer) == 0.0:
                xd = 1
                if x >= 670 and 359 > y > 261:
                    while x2 >= x + 450:
                        x2 -= 75
                        screen.blit(misil,(x2,y2))
                    sound_heli.stop()
                    soundtrack2.stop()
                    screen.blit(explosion,(x+33,y-73))
                    screen.blit(incorrecto2,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor")
                else:
                    screen.blit(incorrecto1,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor")           
            if x >= 670 and 689 > y > 491 or round(Timer) == 0.0:
                xd = 1
                if x >= 670 and 689 > y > 491:
                    while x3 >= x + 450:
                        x3 -= 75
                        screen.blit(misil,(x3,y3))
                    sound_heli.stop()
                    soundtrack2.stop()
                    screen.blit(explosion,(x+33,y-73))
                    screen.blit(incorrecto2,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor")
                else:
                    screen.blit(incorrecto1,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor") 
        elif answer[1] == respuestas[i][0]:
            if x >= 670 and 229 > y > 31 or round(Timer) == 0.0 :
                xd = 1
                if x >= 670 and 229 > y > 31:
                    while x1 >= x + 450:
                        x1 -= 75
                        screen.blit(misil,(x1,y1))
                    sound_heli.stop()
                    soundtrack2.stop()
                    screen.blit(explosion,(x+33,y-73))
                    screen.blit(incorrecto2,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor")
                else:
                    screen.blit(incorrecto1,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor") 
            if x >= 670 and 359 > y > 261:
                xd = 1
                correctoxd = 2
                screen.blit(correcto,(532,118))
                pintar_boton(screen,aceptar2,"Gracias")
            if x >= 670 and 689 > y > 491 or round(Timer) == 0.0:
                xd = 1
                if x >= 670 and 689 > y > 491:
                    while x3 >= x + 450:
                        x3 -= 75
                        screen.blit(misil,(x3,y3))
                    sound_heli.stop()
                    soundtrack2.stop()
                    screen.blit(explosion,(x+33,y-73))
                    screen.blit(incorrecto2,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor")
                else:
                    screen.blit(incorrecto1,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor") 
        elif answer[2] == respuestas[i][0]:
            if x >= 670 and 229 > y > 31 or round(Timer) == 0.0 :
                xd = 1
                if x >= 670 and 229 > y > 31:
                    while x1 >= x + 450:
                        x1 -= 75
                        screen.blit(misil,(x1,y1))
                    sound_heli.stop()
                    soundtrack2.stop()
                    screen.blit(explosion,(x+33,y-73))
                    screen.blit(incorrecto2,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor")
                else:
                    screen.blit(incorrecto1,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor") 
            if x >= 670 and 359 > y > 261 or round(Timer) == 0.0:
                xd = 1
                if x >= 670 and 359 > y > 261:
                    while x2 >= x + 450:
                        x2 -= 75
                        screen.blit(misil,(x2,y2))
                    sound_heli.stop()
                    soundtrack2.stop()
                    screen.blit(explosion,(x+33,y-73)) 
                    screen.blit(incorrecto2,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor")
                else:
                    screen.blit(incorrecto1,(532,118))
                    pintar_boton(screen,aceptar,"Sí señor") 
            if x >= 670 and 689 > y > 491:
                xd = 1
                correctoxd = 3
                screen.blit(correcto,(532,118))
                pintar_boton(screen,aceptar2,"Gracias")
        display.flip()
        dt = clock.tick(30)/1000
        



#JUEGO EN SÍ___________________________________________________________________________________________
c = 0
while True:
    if c == 0:
        c=escena0(screen)
    elif c== 16:
        c=escenaInst(screen)
    elif c == 1:
        c = juego(screen,0)
    elif c== 2:
        GuardadoF = 2
        c = juego(screen,1)
    elif c== 3:
        GuardadoF = 3
        c = juego(screen,2)
    elif c== 4:
        GuardadoF = 4
        c = juego(screen,3)
    elif c== 5:
        GuardadoF = 5
        c = juego(screen,4)
    elif c== 6:
        c = juego(screen,5)
    elif c== 7:
        GuardadoM = 7
        c = juego(screen,6)
    elif c== 8:
        GuardadoM = 8
        c = juego(screen,7)
    elif c== 9:
        GuardadoM = 9
        c = juego(screen,8)
    elif c== 10:
        GuardadoM = 10
        c = juego(screen,9)
    elif c== 11:
        c = juego(screen,10)
    elif c== 12:
        GuardadoD = 12 
        c = juego(screen,11)
    elif c== 13:
        GuardadoD = 13
        c = juego(screen,12)
    elif c== 14:
        GuardadoD = 14
        c = juego(screen,13)
    elif c== 15:
        GuardadoD = 15
        c = juego(screen,14)
    display.flip()


