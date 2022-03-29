class Sokoban:

  mapa = [
    [1,1,1,1,1,1,1,1,1],
    [1,3,3,3,3,3,3,3,1],
    [1,3,3,3,3,2,1,3,1],
    [1,3,3,3,3,3,3,3,1],
    [1,3,3,3,3,3,3,3,1],
    [1,1,1,1,1,1,1,1,1],
  ]
  #posicion inicial del muñeco en el mapa
  muneco_fila = 2
  muneco_columna = 5

  def imprimirMapa(self):
    #imprime el mapa completo
    for fila in self.mapa:
      print(fila)
      
  def moverDerecha(self):
    #movimiento del muñeco a la derecha
    # 00- muñeco, camino -> [2,3] -> [3,2]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 3:
      self.mapa[self.muneco_fila][self.muneco_columna] = 3 
      self.mapa[self.muneco_fila][self.muneco_columna + 1] = 2
      self.muneco_columna += 1 

  def moverAbajo(self):
    #movimiento del muñeco hacia abajo
    if self.mapa[self.muneco_fila][self.muneco_columna] == 2 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 3:
      self.mapa[self.muneco_fila][self.muneco_columna] = 3 
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 2
      self.muneco_columna += 1 

  def jugar(self):
    #controla el flujo del juego
    while True:
      self.imprimirMapa()
      opciones = "d-derecha, s-abajo"
      print(opciones)
      movimiento = input("moverse a: ")
      if movimiento == "d":
        self.moverDerecha()
      elif movimiento == "s":
        self.moverAbajo()
      elif movimiento == "q":
        break

juego = Sokoban()
juego.jugar()

        