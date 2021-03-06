import os
import sys
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
  posicion_columna =  7
  posicion_fila =  4

  def __init__(self): #metodo para inicializar el objeto
    pass #inicializacion del juego
#t
  def cargarMapa(self): #cargar el mapa 
    self.mapa = [
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3], 
        [3,4,4,1,1,3,1,1,1,1,1,3,3,3],
        [3,4,4,1,1,3,1,2,1,1,2,1,1,3],
        [3,4,4,1,1,3,2,3,3,3,3,1,1,3],
        [3,4,4,1,1,1,1,0,1,3,3,1,1,3],
        [3,4,4,1,1,3,1,3,1,1,2,1,3,3],
        [3,3,3,3,3,3,1,3,3,2,1,2,1,3],
        [3,3,3,1,2,1,1,2,1,2,1,2,1,3],
        [3,3,3,1,1,1,1,3,1,1,1,1,1,3],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    ]
#v
  def imprimirMapa(self):#imprime el mapa
    for fila in self.mapa:
      print(fila)

  def encontrarPosicionC(self):
      for fila in range(len(self.mapa)): # Get rows number on the map
        for columna in range(len(self.mapa[fila])): # Get columns number on the map
          if self.mapa[fila][columna] == 0: # If the character is found
            self.posicion_fila = fila # Update the character row position
            self.posicion_columna = columna # Update the character col position
  #metodo para mover el personaje a la derecha
  def moverDerecha(self):
    if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 1:
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
      self.posicion_columna += 1
    #personaje, meta = espacio, personaje_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 4:
      print("personaje, meta = espacio, personaje_meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
      self.posicion_columna += 1    
    #personaje_meta, espacio = meta, personaje
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 1:
      print("personaje_meta, espacio = meta, personaje")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
      self.posicion_columna += 1
    #personaje, caja, espacio = espacio, personaje, meta 
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 2 and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 1:
      print("personaje, caja, espacio = espacio, personaje, meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
      self.mapa[self.posicion_fila][self.posicion_columna + 2] = 2
      self.posicion_columna += 1
    #personaje, caja, meta = espacio, personaje, caja_meta   
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 2 and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 4:
      print("personaje, caja, meta = espacio, personaje, caja_meta ")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
      self.mapa[self.posicion_fila][self.posicion_columna + 2] = 6
      self.posicion_columna += 1
    #personaje, caja_meta, espacio = espacio, personaje_meta, caja 
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 6 and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 1:
      print("personaje, caja_meta, espacio = espacio, personaje_meta, caja ")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
      self.mapa[self.posicion_fila][self.posicion_columna + 2] = 2
      self.posicion_columna += 1
    #personaje, caja_meta, meta = espacio, personaje_meta, caja_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 6 and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 4:
      print("personaje, caja_meta, meta = espacio, personaje_meta, caja_meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
      self.mapa[self.posicion_fila][self.posicion_columna + 2] = 6
      self.posicion_columna += 1     
    #personaje_meta, meta = meta, personaje_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 4:
      print("personaje_meta, meta = meta, personaje_meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
      self.posicion_columna += 1
    #personaje_meta, caja, espacio = meta, personaje, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 2 and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 1:
      print("personaje_meta, caja, espacio = meta, personaje, caja")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
      self.mapa[self.posicion_fila][self.posicion_columna + 2] = 2
      self.posicion_columna += 1 
    #personaje_meta, caja, meta = meta, personaje, caja_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 2 and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 4:
      print("personaje_meta, caja, meta = meta, personaje, caja_meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
      self.mapa[self.posicion_fila][self.posicion_columna + 2] = 6
      self.posicion_columna += 1 
    #personaje_meta, caja_meta, espacio = meta, personaje_meta, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 6 and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 1:
      print("personaje_meta, caja_meta, espacio = meta, personaje_meta, caja")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
      self.mapa[self.posicion_fila][self.posicion_columna + 2] = 2
      self.posicion_columna += 1       
    #personaje_meta, caja_meta, meta = meta, personaje_meta, caja_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 6 and self.mapa[self.posicion_fila][self.posicion_columna + 2] == 4:
      print("personaje_meta, caja_meta, meta = meta, personaje_meta, caja_meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 5
      self.mapa[self.posicion_fila][self.posicion_columna + 2] = 6
      self.posicion_columna += 1

      
  def moverIzquierda(self): #metodo para mover el personaje a la izquierda
    if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 1:
      print("movimiento izquierdo")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1 
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
      self.posicion_columna -= 1 
     #meta, personaje = personaje_meta, espacio
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 4:
      print("meta, personaje = personaje_meta, espacio")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1 #donde estaba un personaje cambia a espacio 
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5 #donde estaba una meta cambia a personaje_meta
      self.posicion_columna -= 1 #actualiza la posicion del personaje
    #espacio, personaje_meta = personaje, meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 1:
      print("espacio, personaje_meta = personaje, meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4 #donde estaba un personaje cambia a espacio 
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0 #donde estaba una meta cambia a personaje_meta
      self.posicion_columna -= 1 #actualiza la posicion del personaje
    #espacio, caja, personaje = caja, personaje, espacio
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 2 and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 1:
      print("espacio, caja, personaje = caja, personaje, espacio")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
      self.mapa[self.posicion_fila][self.posicion_columna - 2] = 2
      self.posicion_columna -= 1
    #meta, caja, prsonaje = caja_meta, personaje, espacio   
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 2 and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 4:
      print("meta, caja, prsonaje = caja_meta, personaje, espacio")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
      self.mapa[self.posicion_fila][self.posicion_columna - 2] = 6
      self.posicion_columna -= 1
    #espacio, caja_meta,personaje = caja, personaje_meta, espacio 
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 6 and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 1:
      print("espacio, caja_meta,personaje = caja, personaje_meta, espacio")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
      self.mapa[self.posicion_fila][self.posicion_columna - 2] = 2
      self.posicion_columna -= 1
    #meta,caja_meta,personaje = caja_meta, personaje_meta, espacio
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 6 and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 4:
      print("meta,caja_meta,personaje = caja_meta, personaje_meta, espacio")
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
      self.mapa[self.posicion_fila][self.posicion_columna - 2] = 6
      self.posicion_columna -= 1     
    #meta,personaje_meta = personaje_meta, meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 4:
      print("meta, personaje_meta = personaje_meta, meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
      self.posicion_columna -= 1
    #espacio,caja, personaje_meta = caja, personaje, meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 2 and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 1:
      print("espacio,caja, personaje_meta = caja, personaje, meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
      self.mapa[self.posicion_fila][self.posicion_columna - 2] = 2
      self.posicion_columna -= 1 
    #meta,caja,peronaje_meta = caja_meta, personaje,meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 2 and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 4:
      print("meta,caja,peronaje_meta = caja_meta, personaje,meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
      self.mapa[self.posicion_fila][self.posicion_columna - 2] = 6
      self.posicion_columna -= 1 
    #espacio, caja_meta, personaje_meta = caja, peronaje_meta,meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 6 and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 1:
      print("espacio, caja_meta, personaje_meta = caja, peronaje_meta,meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
      self.mapa[self.posicion_fila][self.posicion_columna - 2] = 2
      self.posicion_columna -= 1       
    #meta, caja_meta, peronaje_meta = caja_meta, personaje_meta, meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 6 and self.mapa[self.posicion_fila][self.posicion_columna - 2] == 4:
      print("meta, caja_meta, peronaje_meta = caja_meta, personaje_meta, meta")
      self.mapa[self.posicion_fila][self.posicion_columna] = 4
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 5
      self.mapa[self.posicion_fila][self.posicion_columna - 2] = 6
      self.posicion_columna -= 1

  def moverArriba(self): #metodo para mover el personaje hacia arriba
    if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 1: # If the character is on the floor and the next position is a floor
      self.mapa[self.posicion_fila][self.posicion_columna] = 1 # put floor character last position
      self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0 # move the character to next position
      self.posicion_fila -= 1 # update the character position
      #meta,personaje = personaje_meta, espacio
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 4:
        print("meta,personaje = personaje_meta, espacio")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
        self.posicion_fila -= 1
      #personaje,caja, espacio = espacio, personaje, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 2 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 1:
        print("personaje,caja, espacio = espacio, personaje, caja")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
        self.mapa[self.posicion_fila - 2][self.posicion_columna] = 2
        self.posicion_fila -= 1
      #personaje, caja, meta = espacio,personaje, caja_meta 
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 2 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 4:
        print("personaje, caja, meta = espacio,personaje, caja_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
        self.mapa[self.posicion_fila - 2][self.posicion_columna] = 6
        self.posicion_fila -= 1 
      #personaje, caja_meta, espacio = espacio, personaje_meta, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 6 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 1:
        print("personaje, caja_meta, espacio = espacio, personaje_meta, caja")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
        self.mapa[self.posicion_fila - 2][self.posicion_columna] = 2
        self.posicion_fila -= 1 
      #personaje, caja_meta, meta = espacio, personaje_meta, caja_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 6 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 4:
        print("personaje, caja_meta, meta = espacio, personaje_meta, caja_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
        self.mapa[self.posicion_fila - 2][self.posicion_columna] = 6
        self.posicion_fila -= 1
      #personaje_meta, espacio = meta, peronaje
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 1:
        print("personaje_meta, espacio = meta, peronaje")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
        self.posicion_fila -= 1
        
      #personaje_meta, meta = meta, peronaje_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 4:
        print("personaje_meta, meta = meta, peronaje_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
        self.posicion_fila -= 1
      #personaje_meta,caja, espacio, = meta, personaje, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 2 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 1:
        print("personaje_meta,caja, espacio, = meta, personaje, caja")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
        self.mapa[self.posicion_fila - 2][self.posicion_columna] = 2
        self.posicion_fila -= 1
      #personaje_meta, caja, meta = meta, personaje, caja_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 2 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 4:
        print("personaje_meta, caja, meta = meta, personaje, caja_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0
        self.mapa[self.posicion_fila - 2][self.posicion_columna] = 6
        self.posicion_fila -= 1
      #personaje_meta, caja_meta, espacio = meta, personaje_meta, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 6 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 1:
        print("personaje_meta, caja_meta, espacio = meta, personaje_meta, caja")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
        self.mapa[self.posicion_fila - 2][self.posicion_columna] = 2
        self.posicion_fila -= 1
      #personaje_meta, caja_meta, meta = meta, personaje_meta, caja_meta 
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 6 and self.mapa[self.posicion_fila -2][self.posicion_columna] == 4:
        print("personaje_meta, caja_meta, meta = meta, personaje_meta, caja_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 5
        self.mapa[self.posicion_fila - 2][self.posicion_columna] = 6
        self.posicion_fila -= 1
        
  def moverAbajo(self): #metodo para mover el personaje hacia abajo
    if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 1: # If the character is on the floor and the next position is a floor
        self.mapa[self.posicion_fila][self.posicion_columna] = 1 # put floor character last position
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0 # move the character to next position
        self.posicion_fila = self.posicion_fila + 1 # update the character position 
      #meta,personaje <- personaje_meta, espacio
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 4:
        print("meta,personaje <- personaje_meta, espacio")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
        self.posicion_fila += 1
      #personaje,caja, espacio <- espacio, personaje, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 2 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 1:
        print("personaje,caja, espacio <- espacio, personaje, caja")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
        self.mapa[self.posicion_fila + 2][self.posicion_columna] = 2
        self.posicion_fila += 1
      #personaje, caja, meta <- espacio,personaje, caja_meta 
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 2 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 4:
        print("personaje, caja, meta <- espacio,personaje, caja_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
        self.mapa[self.posicion_fila + 2][self.posicion_columna] = 6
        self.posicion_fila += 1 
      #personaje, caja_meta, espacio <- espacio, personaje_meta, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 6 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 1:
        print("personaje, caja_meta, espacio <- espacio, personaje_meta, caja")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
        self.mapa[self.posicion_fila + 2][self.posicion_columna] = 2
        self.posicion_fila += 1 
      #personaje, caja_meta, meta <- espacio, personaje_meta, caja_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 6 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 4:
        print("personaje, caja_meta, meta = espacio, personaje_meta, caja_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 1
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
        self.mapa[self.posicion_fila + 2][self.posicion_columna] = 6
        self.posicion_fila += 1
      #personaje_meta, espacio <- meta, peronaje
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 1:
        print("personaje_meta, espacio <- meta, peronaje")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
        self.posicion_fila += 1
        
      #personaje_meta, meta <- meta, peronaje_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 4:
        print("personaje_meta, meta <- meta, peronaje_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
        self.posicion_fila += 1
      #personaje_meta,caja, espacio, <- meta, personaje, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 2 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 1:
        print("personaje_meta,caja, espacio, <- meta, personaje, caja")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
        self.mapa[self.posicion_fila + 2][self.posicion_columna] = 2
        self.posicion_fila += 1
      #personaje_meta, caja, meta <- meta, personaje, caja_meta
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 2 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 4:
        print("personaje_meta, caja, meta <- meta, personaje, caja_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0
        self.mapa[self.posicion_fila + 2][self.posicion_columna] = 6
        self.posicion_fila += 1
      #personaje_meta, caja_meta, espacio <- meta, personaje_meta, caja
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 6 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 1:
        print("personaje_meta, caja_meta, espacio <- meta, personaje_meta, caja")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
        self.mapa[self.posicion_fila + 2][self.posicion_columna] = 2
        self.posicion_fila += 1
      #personaje_meta, caja_meta, meta <- meta, personaje_meta, caja_meta 
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 5 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 6 and self.mapa[self.posicion_fila +2][self.posicion_columna] == 4:
        print("personaje_meta, caja_meta, meta <- meta, personaje_meta, caja_meta")
        self.mapa[self.posicion_fila][self.posicion_columna] = 4
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 5
        self.mapa[self.posicion_fila + 2][self.posicion_columna] = 6
        self.posicion_fila += 1
  def powerUp(self):
    #metodo para romper una pared del lado derecho
    if self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna + 1] == 3:
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna + 1] = 0
      self.posicion_columna += 1
    #metodo para romper una pared del lado izquierdo  
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila][self.posicion_columna - 1] == 3:
      self.mapa[self.posicion_fila][self.posicion_columna] = 1
      self.mapa[self.posicion_fila][self.posicion_columna - 1] = 0
      self.posicion_columna -= 1   
    #metodo para romper una pared de abajo
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila + 1][self.posicion_columna] == 3: 
        self.mapa[self.posicion_fila][self.posicion_columna] = 1 
        self.mapa[self.posicion_fila + 1][self.posicion_columna] = 0 
        self.posicion_fila = self.posicion_fila + 1
    #metodo para romper una pared de arriba 
    elif self.mapa[self.posicion_fila][self.posicion_columna] == 0 and self.mapa[self.posicion_fila - 1][self.posicion_columna] == 3: 
        self.mapa[self.posicion_fila][self.posicion_columna] = 1 
        self.mapa[self.posicion_fila - 1][self.posicion_columna] = 0 
        self.posicion_fila = self.posicion_fila - 1
      
  def jugar(self): #metodo para poder jugar
    self.cargarMapa() #llama a la funcion cargarMapa
    self.encontrarPosicionC #encunetra la posicion del personaje
    while True:
      self.imprimirMapa()#imprime el mapa
      opciones = "d-derecha, s-abajo, w-arriba, a-izquierda, q-salir del juego, r-reiniciar nivel-"
      print(opciones)#nos muestra las opciones para jugar
      movimiento = input("moverse a: ")#pide al usario una entrada
      if movimiento == "d":#si la entrada es "d" llama al movimiento derecho
        self.moverDerecha()
      elif movimiento == "a":#si la entrada es "a" llama al movimiento izquierdo
        self.moverIzquierda()
      elif movimiento == "s":#si la entrada es "s" llama al movimiento mover abajo
        self.moverAbajo()
      elif movimiento == "w":#si la entrada es "w" llama al movimiento mover arriba
        self.moverArriba()
      elif movimiento == "r":# si la entrada es "r" se reiniciara el nivel para empezar desde cero 
        os.execv(sys.executable, ['python'] + sys.argv) 
      elif movimiento == "t":
        self.powerUp()
      elif movimiento == "q":#si la entrada es "q" el juego terminara 
        break
juego = Sokoban()#Crea un objeto del juego sokoban
juego.jugar()#Imprime el mapa

        

        