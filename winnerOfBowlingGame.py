class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1 = 0
        score2 = 0
        for i in range(len(player1)):
            if(i==1):
                if(player1[0] == 10):
                    score1 = score1 + player1[i] * 2
                elif(player1[0] != 10):
                    score1 = score1 + player1[i]
                if(player2[0] == 10):
                    score2 = score2 + player2[i] * 2
                elif(player2[0] != 10):
                    score2 = score2 + player2[i]
            elif(i>1):
                if(player1[i-1] == 10 or player1[i-2] == 10):
                    score1 = score1 + player1[i] * 2
                elif(player1[i-1] != 10 or player1[i-2] != 10):
                    score1 = score1 + player1[i]
                if(player2[i-1] == 10 or player2[i-2] == 10):
                    score2 = score2 + player2[i] * 2
                elif(player2[i-1] != 10 or player2[i-2] != 10):
                    score2 = score2 + player2[i]
            else:
                score1 = score1 + player1[i]
                score2 = score2 + player2[i]
            print(score1,score2)
        print(score1,score2)
        if(score1>score2):
            return 1
        elif(score1<score2):
            return 2
        else:
            return 0
