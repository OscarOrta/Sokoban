print("Hola mundo")
class Sokoban: #Se crea la clase llamada sokoban
  """
  Definimos los componentes
  0-personaje
  1-espacio
  2-caja
  3-paredes
  4-metas
  5-muñeco_meta
  6-caja_meta
  """
  #mapa inicial del juego
  mapa = [] 
  posicion_columna =  6
  posicion_fila = 3 
  
  def __init__(self): #metodo para inicializar el objeto
    pass #inicializacion del juego
#t
  def cargarMapa(self): #cargar el mapa 
    self.mapa = [
        [3,3,3,3,3,3,3,3,3], 
        [3,1,1,3,3,3,3,3,3],
        [3,1,1,1,1,2,1,1,3],
        [3,1,3,3,1,1,0,1,3],
        [3,4,3,3,2,1,2,1,3],
        [3,4,3,3,1,1,1,1,3],
        [3,3,3,3,3,3,3,3,3],
    ]
#v
  def imprimirMapa(self):#ta
    for fila in self.mapa:
      print(fila)
  def encontrarPosicionC(self):
      for fila in range(len(self.mapa)): # Get rows number on the map
        for columna in range(len(self.mapa[fila])): # Get columns number on the map
          if self.mapa[fila][columna] == 0: # If the character is found
            self.posicion_fila = fila # Update the character row position
            self.posicion_columna = columna # Update the character col position
  def moverDerecha(self): #metodo para mover el personaje a la derecha
    if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 1:
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
      self.posicion_columna += 1
    
  def moverIzquierda(self): #metodo para mover el personaje a la izquierda
    if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 1:
      self.mapa[self.posicion_fila][self.posicion_columna] = 1 
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
      self.posicion_columna = self.posicion_columna - 1 

  def moverArriba(self): #metodo para mover el personaje hacia arriba
      if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 1: # If the character is on the floor and the next position is a floor
          self.mapa[self.posicion_fila][self.posicion_columna] = 1 # put floor character last position
          self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0 # move the character to next position
          self.posicion_fila = self.posicion_fila - 1 # update the character position


  def moverAbajo(self): #metodo para mover el personaje hacia abajo
      if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 1: # If the character is on the floor and the next position is a floor
          self.mapa[self.posicion_fila][self.posicion_columna] = 1 # put floor character last position
          self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0 # move the character to next position
          self.posicion_fila = self.posicion_fila + 1 # update the character position 

    
  def jugar(self):
    self.cargarMapa()
    self.encontrarPosicionC
    while True:
      self.imprimirMapa()
      opciones = "d-derecha, s-abajo, w-arriba, a-izquierda, q-salir del juego"
      print(opciones)
      movimiento = input("moverse a: ")
      if movimiento == "d":
        self.moverDerecha()
      elif movimiento == "a":
        self.moverIzquierda()
      elif movimiento == "s":
        self.moverAbajo()
      elif movimiento == "w":
        self.moverArriba()
      elif movimiento == "q":
        break


juego = Sokoban()#Crea un objeto del juego sokoban
juego.jugar()#Imprime el mapa

        

        