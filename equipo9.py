# ----------------------------------------------------------
#  Project: Adversarial Caterpillars
#
#  Date: 01-Dec-2022
#  Authors:
#          A01745096 Pablo González de la Parra
#          A01745865 José Ángel García Gómez
# ----------------------------------------------------------

from dagor import *


class JugadorOrugasEquipo9(JugadorOrugas):
    """Class that implements solution to player movement."""

    def casillaVacia(self, pos, ren, col):
        """Returns whether a cell is empty."""
        return pos[-1][ren][col] == " "

    def vecinos(self, posicion, ren, col, visited, cont=0):
        """Counts the number of adjacent possible neighbors to
        be moved to in current position"""
        renglones = len(posicion[1])
        columnas = len(posicion[1][0])
        mitad = int((renglones * columnas) * .5)
        newCont = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i, j in directions:
            newPos = (ren + i, col + j)
            if ren + i < 0:
                newPos = (len(posicion[1]) - 1, col)
            elif ren + i >= len(posicion[1]):
                newPos = (0, col)
            if col + j < 0:
                newPos = (ren, len(posicion[1][0]) - 1)
            elif col + j >= len(posicion[1][0]):
                newPos = (ren, 0)
            if newPos not in visited and \
                    posicion[1][newPos[0]][newPos[1]] == ' ':
                visited.append(newPos)
                cont += 1
                vecinos = self.vecinos(posicion, newPos[0],
                                       newPos[1], visited, cont)
                cont += vecinos
                if cont >= mitad:
                    return newCont
                newCont += vecinos + 1
        return newCont

    def posicionActual(self, posicion):
        """Determines current position of player´s head."""
        for renglones in range(len(posicion[1])):
            for columnas in range(len(posicion[1][renglones])):
                if posicion[1][renglones][columnas] == self.simbolo:
                    return renglones, columnas

    def find_best_move(self, posicion, max_depth=10):
        """Return's the best move of a player."""
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
        """Heuristic function that evaluates positions."""
        score = 0
        if (terminado):
            winner = self.triunfo(posicion)
            if (winner == self.simbolo):
                score = 1000000
            elif (winner == self.contrario.simbolo):
                score = -1000000
        else:
            posicion_actual = self.posicionActual(posicion)
            vecinos = self.vecinos(posicion, posicion_actual[0],
                                   posicion_actual[1], [])
            score += vecinos * 100
        return score

    def alphabeta(self, maximazing, posicion, max_depth,
                  alpha=float("-inf"), beta=float("inf")):
        """Minimax algorithm utilizing alphabeta pruning."""
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
        """Unused heuristic function"""
        pass

    def tira(self, posicion):
        """Moves each player's turn"""
        return self.find_best_move(posicion)
