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