class Cycling:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cycling  — Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} crosses the finish line!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")


class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football — Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")


cycling = Cycling("Francis", 85)
football = Football("Pradeep", 2)

print("=== Sports Scoreboard ===\n")
for sport in (cycling, football):
    sport.info()
    sport.play()
    print()

print("--- Direct change attempt ---")
cycling.__score = 999
print(f"get_score() still shows: {cycling.get_score()}")

print("\n--- Updating scores ---")
cycling.set_score(100)
football.set_score(3)