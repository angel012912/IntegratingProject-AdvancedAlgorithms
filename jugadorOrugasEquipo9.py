from dagor1 import *

class JugadorOrugasEquipo9v1(JugadorOrugas):
    def buscaEsquinas(self, posicion):
        count = 0
        for r in range (0, len(posicion[1])):
            if r == 0 or r == len(posicion[1]) - 1:
                if posicion[1][r][0].upper() == self.simbolo :
                    count += 1      
                if posicion[1][r][-1].upper() == self.simbolo :
                    count += 1 
        return count * 100

    def buscaBorde(self, posicion):
        count = 0
        for renglones in posicion[1]:
            if renglones[0].upper() == self.simbolo:
                count += 1
            if renglones[-1].upper() == self.simbolo:
                count += 1
        return count * 100
    
    def evaluarContraEsquinas(self, posicion):
        count = 0

        contraEsquinas = {}
        
        posiciones = {
                (0,0) : [(0, 1), (1, 0)],
                (0, -1) : [(0, -2), (1, -1)],
                (-1, 0) : [(-2, 0), (-1, 1)],
                (-1, -1) : [(-1, -2), (-2, -1)],
                }
        esquinas_contrarias = {
            (0,0) : [(-1,-1), (0,-1), (-1,0)],
            (0,-1) : [(-1,0), (0,0), (-1,-1)],
            (-1,0) : [(0,-1), (-1,-1), (0,0)],
            (-1,-1) : [(0,0), (-1,0), (0,-1)],
        }
        
        for pos in posiciones:
            if not self.casillaVacia(posicion, pos[0], pos[1]):
                contraEsquinas[pos] = None
                continue

            if  not (self.casillaVacia(posicion, posiciones[pos][0][0], posiciones[pos][0][1])) and not (self.casillaVacia(posicion, posiciones[pos][1][0], posiciones[pos][1][1])):
                contraEsquinas[pos] = True
            else:
                contraEsquinas[pos] = False
        
        for pos in esquinas_contrarias:
            if not contraEsquinas[pos]:
                continue
            if not contraEsquinas[esquinas_contrarias[pos][0]]:
                continue
            if contraEsquinas[esquinas_contrarias[pos][1]] is False:
                count += 1
            if contraEsquinas[esquinas_contrarias[pos][2]] is False:
                count += 1
        return count * 100

    def casillaVacia(self, pos, ren, col):
        return pos[-1][ren][col] == " "

    def vecinos(self, posicion, ren, col, visited, cont = 0):
        #Derecha, Izquierda, Abajo, Arriba
        renglones = len(posicion[1])
        columnas = len(posicion[1][0])
        mitad = int ((renglones * columnas) * .5)

        newCont = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i,j in directions:
            newPos = (ren + i, col + j)
            if ren + i < 0 :
                newPos = (len(posicion[1]) - 1, col)
            elif ren + i >= len(posicion[1]):
                newPos = (0, col)
            if col + j < 0:
                newPos = (ren, len(posicion[1][0]) - 1)
            elif col + j >= len(posicion[1][0]):
                newPos = (ren, 0)
            if newPos not in visited and posicion[1][newPos[0]][newPos[1]] == ' ':
                visited.append(newPos)
                cont += 1
                vecinos = self.vecinos(posicion, newPos[0], newPos[1], visited, cont )
                cont += vecinos
                if cont >= mitad:
                    return newCont
                newCont += vecinos + 1
        return newCont
        
    def posicionActual(self, posicion):
        for renglones in range(len(posicion[1])):
            for columnas in range(len(posicion[1][renglones])):
                if posicion[1][renglones][columnas] == self.simbolo:
                    return renglones, columnas 
    
    def find_best_move(self, posicion, max_depth= 10):
        posibles_movements = self.posiciones_siguientes(posicion)
        best_eval = float("-inf")
        best_move = choice(posibles_movements)

        for pos in posibles_movements:
            if (self.triunfo(pos) == self.simbolo): 
                return pos 
            else:
                result = self.alphabeta(False, pos, max_depth)
                if result > best_eval:
                    best_eval = result
                    best_move = pos
        return best_move

    def evaluate(self, posicion, terminado):
        score = 0
        if (terminado):
            winner = self.triunfo(posicion)
            if (winner == self.simbolo):
                score = 1000000 
            elif (winner == self.contrario.simbolo):
                score = -1000000 
        else:
            posicion_actual = self.posicionActual(posicion)
            vecinos = self.vecinos(posicion, posicion_actual[0], posicion_actual[1], [])
            score += vecinos * 100
            esquinas = self.evaluarContraEsquinas(posicion)
            score += esquinas
        return score
    
    def alphabeta(self, maximazing, posicion, max_depth, alpha = 
    float("-inf"), beta = float("inf")):
        if (self.juego.juego_terminado(posicion) or max_depth == 0):
            res = 0
            if (self.juego.juego_terminado(posicion)):
                res = self.evaluate(posicion, True)
            else:
                res = self.evaluate(posicion, False)
            return res
        if maximazing:
            for pos in self.posiciones_siguientes(posicion):
                result = self.alphabeta(False, pos, max_depth - 1, alpha, beta) 
                alpha = max(result, alpha)
                if (beta <= alpha):
                    break
            return alpha
        else:
            for pos in self.posiciones_siguientes(posicion):
                result = self.alphabeta(True, pos, max_depth - 1, alpha, beta) 
                beta = min(result, beta)
                if beta <= alpha:
                    break
            return beta

    def heuristica(self):
        pass        

    def tira(self, posicion):
      return self.find_best_move(posicion)

class JugadorOrugasEquipo9v2(JugadorOrugas):
    def buscaEsquinas(self, posicion):
        count = 0
        for r in range (0, len(posicion[1])):
            if r == 0 or r == len(posicion[1]) - 1:
                if posicion[1][r][0].upper() == self.simbolo :
                    count += 1      
                if posicion[1][r][-1].upper() == self.simbolo :
                    count += 1 
        return count * 100

    def buscaBorde(self, posicion):
        count = 0
        for renglones in posicion[1]:
            if renglones[0].upper() == self.simbolo:
                count += 1
            if renglones[-1].upper() == self.simbolo:
                count += 1
        return count * 100
    
    def evaluarContraEsquinas(self, posicion):
        count = 0

        contraEsquinas = {}
        
        posiciones = {
                (0,0) : [(0, 1), (1, 0)],
                (0, -1) : [(0, -2), (1, -1)],
                (-1, 0) : [(-2, 0), (-1, 1)],
                (-1, -1) : [(-1, -2), (-2, -1)],
                }
        esquinas_contrarias = {
            (0,0) : [(-1,-1), (0,-1), (-1,0)],
            (0,-1) : [(-1,0), (0,0), (-1,-1)],
            (-1,0) : [(0,-1), (-1,-1), (0,0)],
            (-1,-1) : [(0,0), (-1,0), (0,-1)],
        }
        
        for pos in posiciones:
            if not self.casillaVacia(posicion, pos[0], pos[1]):
                contraEsquinas[pos] = None
                continue

            if  not (self.casillaVacia(posicion, posiciones[pos][0][0], posiciones[pos][0][1])) and not (self.casillaVacia(posicion, posiciones[pos][1][0], posiciones[pos][1][1])):
                contraEsquinas[pos] = True
            else:
                contraEsquinas[pos] = False
        
        for pos in esquinas_contrarias:
            if not contraEsquinas[pos]:
                continue
            if not contraEsquinas[esquinas_contrarias[pos][0]]:
                continue
            if contraEsquinas[esquinas_contrarias[pos][1]] is False:
                count += 1
            if contraEsquinas[esquinas_contrarias[pos][2]] is False:
                count += 1
        return count * 100

    def casillaVacia(self, pos, ren, col):
        return pos[-1][ren][col] == " "


    def vecinos(self, posicion, ren, col, visited, cont = 0):
        #Derecha, Izquierda, Abajo, Arriba
        renglones = len(posicion[1])
        columnas = len(posicion[1][0])
        mitad = int ((renglones * columnas) * .5)
        newCont = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i,j in directions:
            newPos = (ren + i, col + j)
            if ren + i < 0 :
                newPos = (len(posicion[1]) - 1, col)
            elif ren + i >= len(posicion[1]):
                newPos = (0, col)
            if col + j < 0:
                newPos = (ren, len(posicion[1][0]) - 1)
            elif col + j >= len(posicion[1][0]):
                newPos = (ren, 0)
            if newPos not in visited and posicion[1][newPos[0]][newPos[1]] == ' ':
                visited.append(newPos)
                cont += 1
                vecinos = self.vecinos(posicion, newPos[0], newPos[1], visited, cont )
                cont += vecinos
                if cont >= mitad:
                    return newCont
                newCont += vecinos + 1
        return newCont
        
    def posicionActual(self, posicion):
        for renglones in range(len(posicion[1])):
            for columnas in range(len(posicion[1][renglones])):
                if posicion[1][renglones][columnas] == self.simbolo:
                    return renglones, columnas 
    
    def find_best_move(self, posicion, max_depth= 10):
        posibles_movements = self.posiciones_siguientes(posicion)
        best_eval = float("-inf")
        best_move = choice(posibles_movements)

        for pos in posibles_movements:
            if (self.triunfo(pos) == self.simbolo): 
                return pos 
            else:
                result = self.alphabeta(False, pos, max_depth)
                if result > best_eval:
                    best_eval = result
                    best_move = pos
        return best_move

    def evaluate(self, posicion, terminado):
        score = 0
        if (terminado):
            winner = self.triunfo(posicion)
            if (winner == self.simbolo):
                score = 1000000 
            elif (winner == self.contrario.simbolo):
                score = -1000000 
        else:
            posicion_actual = self.posicionActual(posicion)
            vecinos = self.vecinos(posicion, posicion_actual[0], posicion_actual[1], [])
            score += vecinos * 100
        return score
    
    def alphabeta(self, maximazing, posicion, max_depth, alpha = 
    float("-inf"), beta = float("inf")):
        if (self.juego.juego_terminado(posicion) or max_depth == 0):
            res = 0
            if (self.juego.juego_terminado(posicion)):
                res = self.evaluate(posicion, True)
            else:
                res = self.evaluate(posicion, False)
            return res
        if maximazing:
            for pos in self.posiciones_siguientes(posicion):
                result = self.alphabeta(False, pos, max_depth - 1, alpha, beta) 
                alpha = max(result, alpha)
                if (beta <= alpha):
                    break
            return alpha
        else:
            for pos in self.posiciones_siguientes(posicion):
                result = self.alphabeta(True, pos, max_depth - 1, alpha, beta) 
                beta = min(result, beta)
                if beta <= alpha:
                    break
            return beta

    def heuristica(self):
        pass        

    def tira(self, posicion):
      return self.find_best_move(posicion)
