from game import GameEngine
from bots import ZenoBot, RandBot

bot1 = RandBot("Bot1")
bot2 = ZenoBot("ZenoBot")

game = GameEngine(bot1, bot2)

score_board = {
    bot1.name: 0,
    bot2.name: 0,
    "draws": 0
}

for _ in range(0, 10000):

    winner = game.play_game()

    if winner:
        score_board[winner.name] += 1
    else:
        score_board["draws"] += 1

def print_results_table(results: dict[str, int]) -> None:
    # Find the maximum length of the winner names for formatting
    max_name_length = max(len(name) for name in results.keys())
    
    # Set column widths based on max name length and a fixed width for wins
    name_col_width = max(max_name_length, len("Winner")) + 2
    wins_col_width = max(len(str(max(results.values()))), len("Wins")) + 2
    
    # Table header
    print("+" + "-" * name_col_width + "+" + "-" * wins_col_width + "+")
    print(f"| {'Winner'.ljust(name_col_width - 1)} | {'Wins'.ljust(wins_col_width - 1)} |")
    print("+" + "-" * name_col_width + "+" + "-" * wins_col_width + "+")
    
    # Table rows for each winner and their win count
    for name, wins in results.items():
        print(f"| {name.ljust(name_col_width - 1)} | {str(wins).ljust(wins_col_width - 1)} |")
    
    # Table footer
    print("+" + "-" * name_col_width + "+" + "-" * wins_col_width + "+")

print_results_table(score_board)