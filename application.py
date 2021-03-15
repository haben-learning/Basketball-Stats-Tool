import constants
import copy


PLAYERS_COPY = copy.deepcopy(constants.PLAYERS)
TEAMS_COPY = copy.deepcopy(constants.TEAMS)

panthers = []
experienced_panthers = []
inexperienced_panthers = []
bandits = []
experienced_bandits = []
inexperienced_bandits = []
warriors = []
experienced_warriors = []
inexperienced_warriors = []


# Updates each player's experience, height, and guardians information
def clean_data():
    for item in PLAYERS_COPY:
        if item['experience'][0] == 'Y':
            item['experience'] = True
        else:
            item['experience'] = False
        item['height'] = int(item['height'][0:3])
        item['guardians'] = item['guardians'].split("and")


# Takes the updated player information and balances each team with the
# appropriate number of experienced(3) and inexperienced players(3)
# while maintaining the 6 player limit for each team
def balance_teams():
    for player in PLAYERS_COPY:
        if player['experience'] and (len(experienced_panthers) < 3):
            experienced_panthers.append(player)
            panthers.append(player)
        elif player['experience'] is False and (len(inexperienced_panthers) < 3):
            inexperienced_panthers.append(player)
            panthers.append(player)
        elif player['experience'] and (len(experienced_bandits) < 3):
            experienced_bandits.append(player)
            bandits.append(player)
        elif (player['experience'] is False) and (len(inexperienced_bandits) < 3):
            inexperienced_bandits.append(player)
            bandits.append(player)
        elif player['experience'] and (len(experienced_warriors) < 3):
            experienced_warriors.append(player)
            warriors.append(player)
        elif (player['experience'] is False) and (len(inexperienced_warriors) < 3):
            inexperienced_warriors.append(player)
            warriors.append(player)


# Displays the teams stats for each category
def display_team_stats(team_name, team, experienced, inexperienced):
    print("Team: {}".format(team_name))
    print("-" * 15)
    print("Total players: {}".format(len(team)))
    print("Experienced players: {}".format(len(experienced)))
    print("Inexperienced players: {}".format(len(inexperienced)))
    heights = [height['height'] for height in team]
    print("Average height: {}\n".format(round(sum(heights) / len(heights), 1)))
    players_on_team = [name['name'] for name in team]
    print("Players on team:")
    print(", ".join(players_on_team), "\n")
    print("Guardians:")
    guardians = [", ".join(each_guardian['guardians']) for each_guardian in team]
    print(", ".join(guardians), "\n")


# Starts the stats tools and evaluates the selected option and provides user with the team's stats
if __name__ == "__main__":
    clean_data()
    balance_teams()
    while True:
        print("_" * 7, "BASKETBALL TEAM STATS TOOL", "_" * 7, '\n')
        print("_" * 7, "MENU", "_" * 7, "\n")
        print("Here are your options: \n", "A) View a teams stats\n", "B) Quit team stats tool\n")
        menu_options = input("Enter option here: ").upper()
        print()
        if menu_options == "A":
            print("The available teams stats to view are:\n"
                  "A) Panthers\n"
                  "B) Bandits\n"
                  "C) Warriors\n"
                  )
            select_a_team = input("Please choose a team to view their stats: ").upper()
            print()
            if select_a_team == "A":
                display_team_stats("Panthers", panthers, experienced_panthers, inexperienced_panthers)
                to_continue = input("Press ENTER to continue.......")
                if to_continue == "":
                    continue
            elif select_a_team == "B":
                display_team_stats("Bandits", bandits, experienced_bandits, inexperienced_bandits)
                to_continue = input("Press ENTER to continue.......")
                if to_continue == "":
                    continue
            elif select_a_team == "C":
                display_team_stats("Warriors", warriors, experienced_warriors, inexperienced_warriors)
                to_continue = input("Press ENTER to continue.......")
                print(to_continue)
        elif menu_options == "B":
            print("Thank you for using Basketball Stats Tool")
            break
