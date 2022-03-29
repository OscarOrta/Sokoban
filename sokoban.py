print("Hola mundo")
class Sokoban: #Se crea la clase llamada sokoban
  """
  Definimos los componentes
  0-cajas
  1-paredes
  2-muñeco
  3-caminos
  4-metas
  5-muñeco_meta
  6-caja_meta
  """
  #mapa inicial del juego
  mapa = [
    [1,1,1,1,1,1,1,1,1],
    [1,3,3,1,1,1,1,1,1],
    [1,3,3,3,3,0,3,3,1],
    [1,3,1,1,3,3,2,3,1],
    [1,4,1,1,0,1,0,3,1],
    [1,4,1,1,3,3,3,3,1],
    [1,1,1,1,1,1,1,1,1],
  ] 

  #posicion inicial del muñeco en el  mapa 
  posicion_columna = 6 #Coloumna en la que se encuentra el muñeco
  posicion_fila = 3 #Fila en la que se encuntra el muñeco
  
  def __init__(self): #metodo para inicializar el objeto
    pass #inicializacion del juego

  def imprimirMapa(self): #metodo impresion del mapa
    for i in self.mapa: #Recorre cada posición del mapa 
      for c in i:
        if c == 3: #Si el elemento es un 3 (camino)
          print(" ", end ="") #imprime " " y no da salto de linea
        elif c==2: #Si el elemento es un 2 (muñeco)
          print(chr(64),end ="") #imprime @ " " y no da salto de linea
        elif c==1: #Si el elemento es 1 (pared)
          print("#",end ="") #imprime "|" y no da salto de linea
        elif c==0: #Si el elemento es un 0 (caja)
          print("°",end ="")#Imprime "#" y no da salto de linea
        elif c==4: #Si el elemento es un 4 (meta)
          print(chr(33),end ="")#imprime "!" y no da salto de linea 
      print() #imprime una linea en blanco



juego = Sokoban()
juego.imprimirMapa()


"""
  def moverDerecha(self): #metodo para mover el personaje a la derecha
    self.posicion_columna += 1 #Actualiza la posicion un lugar derecha
    self.mapa[self.posicion_columna]= 2 #Coloca el muñeco en la nueva posicion
    self.mapa[self.posicion_columna - 1] = 3 #Coloca un espacio donde estaba el muñeco
    self.imprimirMapa() #Imprimir el mapa actualizado
    
  def moverIzquierda(self): #metodo para mover el personaje a la izquierda
    self.posicion_columna -= 1 #Actualiza la posicion un lugar izquierda
    self.mapa[self.posicion_columna]= 2 #Coloca el muñeco en la nueva posicion
    self.mapa[self.posicion_columna + 1] = 3 #Coloca un espacio donde estaba el muñeco
    self.imprimirMapa() #Imprimir el mapa actualizado

juego = Sokoban() #Crea un objeto del juego sokoban
juego.imprimirMapa() #Imprime el mapa

instrucciones = "q Salir\nd Derecha\na Izquierda" #Variable con las instrucciones del juego

while True: #Bucle infinito
  print(instrucciones) #Imprime las instrucciones
  movimiento=input("Mover: ") #lee hacia donde se mueve el muñeco
  if movimiento == "d": #si el movimiento es igual a "d"
    juego.moverDerecha() #Llama al metodo mover a la derecha
  elif movimiento == "a": #si el movimiento es igual a "a"
    juego.moverIzquierda() #Llama al metodo mover a la izquierda
  elif movimiento == "q": #si el movimiento es igual a "q"
    print("Saliste del juego") #Mensaje de salida 
    break


juego = Sokoban()
juego.jugar()
"""
        

        