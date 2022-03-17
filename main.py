from colorama import Fore

team1score = 0
team2score = 0

print("")
print("Welcome to the Match Scoreboard!")
print("")
cont = input("Would you like to continue? Y/N: ").lower()
if cont == "y":
    team1 = input("Please enter a team name for" + (Fore.RED + " Team1: \033[39m")).lower()
    print("")
    team2 = input("Awesome! Now enter a team name for" + (Fore.BLUE + " Team2: ")).lower()
    print("")
    print("\033[1;32;488mINSTRUCTIONS: Enter the exact team name to add a point to there score. The score will be revealed at the end of the match! \033[39m")
    print("")
    nameScore = input("Enter the name of the team when they score a point!: ").lower()

while nameScore == team1 or nameScore == team2:
    if nameScore == team1:
        if team1score >= 11:
            print(f"The final is score is {team1score} - {team2score}!")
            break
        else:
            team1score = team1score + 1
    if nameScore == team2:
        if team2score >= 11:
            print(f"The final is score is {team1score} - {team2score}!")
            break
        else:
            team2score = team2score + 1
    nameScore = input("Enter the name of the team when they score a point!: ").lower()