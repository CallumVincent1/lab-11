class FootballPlayer:
    def __init__(self, name, age, team, position):
        self.name = name
        self.age = age
        self.team = team
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"team: {self.team}")
        print(f"Position: {self.position}")

    def play(self):
        print(f"{self.name} is playing for {self.team} as a {self.position}")


class Striker(FootballPlayer):
    def __init__(self, name, age, team, position, goals_scored):
        super().__init__(name, age, team, position)
        self.goals = goals_scored
        
    def score_goal(self):
        self.goals += 1
        print(f"{self.name} has scored a goal")

    def play(self):
        print(f"they are trying to score goals, they have scored {self.goals} goals so far")

