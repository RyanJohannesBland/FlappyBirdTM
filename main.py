from board import Board


if __name__ == "__main__":
    board = Board()
    board.add_action(90, "spawn_pipe")
    board.add_action(90, "increase_game_speed")
    board.start_game_loop()
