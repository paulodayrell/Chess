class UtilTable:
    @staticmethod
    def compareBoards(board1, board2):
        for x in range(8):
            for y in range(8):
                peca1 = board1.pecas_tabuleiro[x][y]
                peca2 = board2.pecas_tabuleiro[x][y]
                if peca1 != None and peca2 != None:
                    if peca1.colour != peca2.colour or peca1.name != peca2.name:
                        return False
                else:
                    if ((peca1 == None and peca2 != None) or (peca1 != None and peca2 == None)):
                        return False
        return True