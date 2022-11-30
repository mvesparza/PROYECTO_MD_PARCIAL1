import pygame, sys, time, random

pygame.init()

#pantalla del juego de 500 por 500
cuadro_juego = pygame.display.set_mode((500, 500))

fuente = pygame.font.Font(None,30)

#pixeles o fotogramas por segundo
fps = pygame.time.Clock()

def comida():
    pos_aleatoria = random.randint(0,49)*10
    #                  x                y
    pos_comida = [pos_aleatoria, pos_aleatoria]
    return pos_comida


def main():
    #estructura de la serpiente
    cabeza_serpiente = [100, 50]
    cuerpo_serpiente = [[100,50],[90,50],[80,50]]

    cambio = "Derecha"
    valor = True
    pos_comida = comida()
    puntuacion = 0
    perdiste = "HAS PERDIDO"

    while valor:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                valor = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    cambio = "Derecha"
                if event.key == pygame.K_LEFT:
                    cambio = "Izquierda"
                if event.key == pygame.K_UP:
                    cambio = "Arriba"
                if event.key == pygame.K_DOWN:
                    cambio = "Abajo"
        if cambio == "Derecha":
            cabeza_serpiente[0] += 10
        if cambio == "Izquierda":
            cabeza_serpiente[0] -= 10
        if cambio == "Arriba":
            cabeza_serpiente[1] -= 10
        if cambio == "Abajo":
            cabeza_serpiente[1] += 10

        #acciones de la serpiente
        cuerpo_serpiente.insert(0,list(cabeza_serpiente))
        if cabeza_serpiente == pos_comida:
            pos_comida = comida()
            puntuacion += 1
            print(puntuacion)
        else:
            cuerpo_serpiente.pop() #pop elimina las  ultim posicion de un array

        cuadro_juego.fill((0,0,0))
        #dibujo de la serpiente
        for pos in cuerpo_serpiente:
            pygame.draw.rect(cuadro_juego,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(cuadro_juego,[169,6,6], pygame.Rect(pos_comida[0],pos_comida[1],10,10))
        texto = fuente.render(str(puntuacion),0,(255,255,255))
        cuadro_juego.blit(texto,(450,470))

        if puntuacion < 10:
            fps.tick(10)
        if puntuacion >= 10:
            fps.tick(20)
        
        if cabeza_serpiente[0] <= 0 or cabeza_serpiente[0] >= 500:
            valor = False
            print("Perdiste")
        if cabeza_serpiente[1] <= 0 or cabeza_serpiente[1] >= 500:
            valor = False
            print("Perdiste")
        
        pygame.display.flip()
        fps.tick(10)

main()

pygame.quit

