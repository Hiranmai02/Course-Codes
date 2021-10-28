import TicTacToe as ttt
import matplotlib.pyplot as plt

r1 = []
r2 = []
n = 10
# player = [1,2]

def count_wins(player, player2, n):
    std = []
    strat = []
    for i in range(n):
        r1 = []
        r2 = [] 
        for i in range(1000):
            r1.append(ttt.play_game())
            r2.append(ttt.play_strategic_game(player, player2))
        std.append(r1.count(player))
        strat.append(r2.count(player))
    return std, strat

std1, strat1 = count_wins(1,2,n)
std2, strat2 = count_wins(2,1,n)

plt.ylim([0,1000])
plt.plot(range(n), std1,'r.--')
plt.plot(range(n), strat1, 'r.-')
plt.plot(range(n), std2,'b.--')
plt.plot(range(n), strat2, 'b.-')
plt.xlabel('Number of sets (1 set = 1000 games)')
plt.ylabel('Number of games won')
plt.legend(['Standard 1', 'Strategic 1', 'Standard 2', 'Strategic 2'])
plt.show()