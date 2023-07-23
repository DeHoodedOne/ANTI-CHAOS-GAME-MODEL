import os
import random as rdm
from datetime import datetime, timedelta
from _CONTROL_CENTER import directories


def sampler_():
    SAMPLE_SIZE = 80
    TOMOROW_DATE = "24-07-2023"

    path = os.getcwd()
    isExist_1 = os.path.exists(f"{path}/_LOCAL_SAMPLE.txt")
    isExist_2 = os.path.exists(f"{path}/_FINAL_SAMPLING.txt")

    if isExist_1:
        os.remove(f"{path}/_LOCAL_SAMPLE.txt")
    if isExist_2:
        os.remove(f"{path}/_FINAL_SAMPLING.txt")

    dir_list = directories()

    for dir_ in dir_list:
        list_ = os.listdir(f"../{dir_}")
        for filename in list_:
            if not filename.endswith(".py"):
                with open(f"../{dir_}/{filename}", 'r') as firstfile, open('_LOCAL_SAMPLE.txt', 'a') as secondfile:
                    for line in firstfile:
                        if line.startswith("CONFIDENCE") or line == "\n" or line.startswith("FRO"):
                            pass
                        else:
                            secondfile.write(line)
    try:
        with open('_LOCAL_SAMPLE.txt') as result:
            uniqlines = set(result.readlines())
            with open('_LOCAL_SAMPLE.txt', 'w') as rmdup:
                rmdup.writelines((set(uniqlines)))

        with open('_LOCAL_SAMPLE.txt', 'r') as games:
            collated_games = list((set(games.readlines())))
            rdm.shuffle(collated_games)
    except FileNotFoundError:
        collated_games = []
        print("Please Run the Scrapper")

    games_dict = {}
    for i in range(len(collated_games)):
        games_dict["|".join(collated_games[i].split('|')[:3])] = collated_games[i]

    sorted_games_list = list(games_dict.values())
    rdm.shuffle(sorted_games_list)
    playable_games = []
    today_ = datetime.now()
    yesterday_ = today_ - timedelta(1)
    today_date_ = today_.strftime("%d-%m-%Y")
    yesterday_date_ = yesterday_.strftime("%d-%m-%Y")
    if today_date_ == TOMOROW_DATE:
        for p_games in sorted_games_list:
            print(p_games)
            try:
                match_hour = int(p_games.split("|")[-4].split(":")[0])
                match_minute = int(p_games.split("|")[-4].split(":")[1])
                hour_ = int(today_.strftime("%H"))
                mins_ = int(today_.strftime("%M"))
                if (match_hour >= hour_ and match_minute > mins_) or (match_hour > hour_ and match_minute < mins_):
                    playable_games.append(p_games)
            except ValueError:
                print(p_games)
    elif today_date_ != TOMOROW_DATE and TOMOROW_DATE != yesterday_date_:
        playable_games = sorted_games_list

    rdm.shuffle(playable_games)
    print(len(playable_games))

    for j in range((len(playable_games) // SAMPLE_SIZE) + 1):
        try:
            selected_games = rdm.sample(playable_games, SAMPLE_SIZE)
        except ValueError:
            if len(playable_games) == 0:
                break
            else:
                selected_games = rdm.sample(playable_games, len(playable_games))
        with open('_FINAL_SAMPLING.txt', 'a') as file:
            file.write("COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                       "HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_SCDIFF|AT_SCDIFF|BTH_SCDIFF|BTA_SCDIFF|OUTCOME1|"
                       "OUTCOME2|OUTCOME3|OUTCOME4|OUTCOME5|OUTCOME6|OUTCOME7|OUTCOME3|OUTCOME8|OUTCOME9|OUTCOME10|"
                       "OUTCOME11|OUTCOME12|OUTCOME13|OUTCOME14|OUTCOME15|OUTCOME16|OUTCOME17|MATCH TIME|SPORT|MATCH DATE\n")
        selected_games.sort()
        sorted_selected_games = sorted(selected_games, key=lambda x: x.split("|")[-3])
        for selected_game in sorted_selected_games:
            with open('_FINAL_SAMPLING.txt', 'a') as file:
                file.write(selected_game)
            playable_games.pop(playable_games.index(selected_game))
        with open('_FINAL_SAMPLING.txt', 'a') as file:
            file.write("\n\n\n\n\n")
        print(len(playable_games))
    try:
        os.remove(f"{path}/_LOCAL_SAMPLE.txt")
    except FileNotFoundError:
        pass


sampler_()
