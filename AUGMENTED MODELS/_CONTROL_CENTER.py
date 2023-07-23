from itertools import combinations, permutations


def set_date_s_size():
    TOMORROWS_DATE = "23-07-2023"
    GAMES_SAMPLE_SIZE = 50
    return [TOMORROWS_DATE, GAMES_SAMPLE_SIZE]


def wait_time():
    IMPLICIT_WAIT_TIME = 2.5
    return IMPLICIT_WAIT_TIME


def game_criteria(process_):
    DRAWABLES = ["_RUN_ALT_FOOTBALL_DRAW.py", "_RUN_ALT_SPORTS_DRAW.py", "_RUN_ALT_SPORTS_DRAW1.py"]
    ALTS = ["ALT_FOOTBALL.py", "A_S_P_SPORTS.py", "ALT_SPORTS1.py", "ALT_SPORTS2.py", 'xFOOTBALL.py']
    SINGLE_XLRS = ['BOXING.py', 'CRICKET.py', 'MMA.py']
    SINGLES = ['BEACH VOLLEYBALL.py', 'BADMINTON.py', "DARTS.py", "SNOOKER.py",
               'PESAPALLO.py', 'TENNIS.py', 'TABLE TENNIS.py', 'BASKETBALL.py', 'BASEBALL.py', 'NETBALL.py',
               'VOLLEYBALL.py', '_RUN_BASKETBALL.py']
    SINGLES_DRAWS = ['AMERICAN FOOTBALL.py', 'AUSSIE RULES.py', "ESPORTS.py",
                     'FIELD HOCKEY.py', 'WATERPOLO.py', 'RUGBY LEAGUE.py', 'BEACH SOCCER.py',
                     'RUGBY UNION.py', 'BANDY.py', 'FUSTAL.py', 'HANDBALL.py', 'FLOORBALL.py',
                     'KABADDI.py', 'FOOTBALL.py', 'HOCKEY.py', '_RUN_FOOTBALL.py']

    CONFIDENCE_INTERVALS = None
    BAYESIAN_DIFFERENCE = None
    FORM_VALUE_LIMIT = None

    CONFIDENCE_INTERVALS_DRAW = None
    BAYESIAN_DIFFERENCE_DRAW = None
    FORM_VALUE_LIMIT_DRAW = None

    CONFIDENCE_INTERVALS_ALT = None
    FORM_VALUE_LIMIT_ALT = None
    BAYESIAN_DIFFERENCE_ALT = None

    CONFIDENCE_INTERVALS_XLR = None
    FORM_VALUE_LIMIT_XLR = None
    BAYESIAN_DIFFERENCE_XLR = None

    # For Alt Matches
    if process_ in ALTS:
        CONFIDENCE_INTERVALS = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.875]
        BAYESIAN_DIFFERENCE = 0.8
        FORM_VALUE_LIMIT = 0.8
        print("A")

    elif process_ in SINGLES_DRAWS:
        CONFIDENCE_INTERVALS = [0.995, 0.99, 0.985, 0.98, 0.975, 0.97, 0.95]
        BAYESIAN_DIFFERENCE = 0.05
        FORM_VALUE_LIMIT = 0.0

        CONFIDENCE_INTERVALS_DRAW = [0.995, 0.99, 0.985, 0.98, 0.975, 0.97, 0.95]
        BAYESIAN_DIFFERENCE_DRAW = 0.05
        FORM_VALUE_LIMIT_DRAW = 0.4

        CONFIDENCE_INTERVALS_ALT = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.875]
        FORM_VALUE_LIMIT_ALT = 0.8
        BAYESIAN_DIFFERENCE_ALT = 0.8

        CONFIDENCE_INTERVALS_XLR = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.9]
        FORM_VALUE_LIMIT_XLR = 0.0
        BAYESIAN_DIFFERENCE_XLR = 0.75
        print("B")

    # For Run Matches
    elif process_ in SINGLES:
        CONFIDENCE_INTERVALS = [0.995, 0.99, 0.985, 0.98, 0.975, 0.97, 0.95]
        BAYESIAN_DIFFERENCE = 0.05
        FORM_VALUE_LIMIT = 0.0
        
        CONFIDENCE_INTERVALS_ALT = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.875]
        FORM_VALUE_LIMIT_ALT = 0.8
        BAYESIAN_DIFFERENCE_ALT = 0.8
        
        CONFIDENCE_INTERVALS_XLR = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.9]
        FORM_VALUE_LIMIT_XLR = 0.0
        BAYESIAN_DIFFERENCE_XLR = 0.75
        print("C")

    # For Drawable Matches
    elif process_ in DRAWABLES:
        CONFIDENCE_INTERVALS_DRAW = [0.995, 0.99, 0.985, 0.98, 0.975, 0.97, 0.95]
        BAYESIAN_DIFFERENCE_DRAW = 0.1
        FORM_VALUE_LIMIT_DRAW = 0.4

        CONFIDENCE_INTERVALS_ALT = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.875]
        FORM_VALUE_LIMIT_ALT = 0.8
        BAYESIAN_DIFFERENCE_ALT = 0.8

        CONFIDENCE_INTERVALS_XLR = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.9]
        FORM_VALUE_LIMIT_XLR = 0.0
        BAYESIAN_DIFFERENCE_XLR = 0.75
        print("D")

    elif process_ in SINGLE_XLRS:
        CONFIDENCE_INTERVALS = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.875]
        FORM_VALUE_LIMIT = 0.6
        BAYESIAN_DIFFERENCE = 0.8

        CONFIDENCE_INTERVALS_XLR = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.9]
        FORM_VALUE_LIMIT_XLR = 0.0
        BAYESIAN_DIFFERENCE_XLR = 0.75
        print("E")

    elif process_ == '_RUN_FOOTBALL_CORNERS.py':
        CONFIDENCE_INTERVALS = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.875]
        BAYESIAN_DIFFERENCE = 0.75
        FORM_VALUE_LIMIT = 0.0
        print("F")

    NUMBER_OF_MATCHES_ALREADY_PLAYED = 10
    FORM_SIZE_COUNT = 5
    FORM_DIFFERENCE = 0.6
    TEAM_POSITION_DIFFERENCE = 5
    POSITION_MARK = 5
    YEAR_OF_MATCHES = 22
    DISCRIMINANT_FOR_HOME_N_AWAY_TEAMS_INDEPENDENTLY = 5
    DISCRIMINANT_FOR_HOME_N_AWAY_TEAMS_AGAINST_EACH_OTHER = 5
    HOME_N_AWAY_INDEPENDENT_MATCH_SAMPLE = 1
    SELENIUM_CHROMEDRIVER_PATH = ["C:\Development\chromedriver_win31\chromedriver.exe",
                                  "C:\Development\chromedriver_win32\chromedriver.exe",
                                  "C:\Development\chromedriver_win33\chromedriver.exe",
                                  "C:\Development\chromedriver_win34\chromedriver.exe",
                                  "C:\Development\chromedriver_win35\chromedriver.exe",
                                  "C:\Development\chromedriver_win36\chromedriver.exe",
                                  "C:\Development\chromedriver_win37\chromedriver.exe",
                                  "C:\Development\chromedriver_win38\chromedriver.exe",
                                  "C:\Development\chromedriver_win39\chromedriver.exe",
                                  "C:\Development\chromedriver_win40\chromedriver.exe"]

    SELENIUM_FIREFOXDRIVER_PATH = ["C:\Development\geckodrivers\geckodriver.exe",
                                   "C:\Development\geckodrivers1\geckodriver.exe",
                                   "C:\Development\geckodrivers2\geckodriver.exe",
                                   "C:\Development\geckodrivers3\geckodriver.exe",
                                   "C:\Development\geckodrivers4\geckodriver.exe",
                                   "C:\Development\geckodrivers5\geckodriver.exe",
                                   "C:\Development\geckodrivers6\geckodriver.exe",
                                   "C:\Development\geckodrivers7\geckodriver.exe",
                                   "C:\Development\geckodrivers8\geckodriver.exe",
                                   "C:\Development\geckodrivers9\geckodriver.exe"]

    SELENIUM_EDGEDRIVER_PATH = ["C:\Development\edgedriver_win61\msedgedriver.exe",
                                "C:\Development\edgedriver_win62\msedgedriver.exe",
                                "C:\Development\edgedriver_win63\msedgedriver.exe",
                                "C:\Development\edgedriver_win64\msedgedriver.exe",
                                "C:\Development\edgedriver_win65\msedgedriver.exe",
                                "C:\Development\edgedriver_win66\msedgedriver.exe",
                                "C:\Development\edgedriver_win67\msedgedriver.exe",
                                "C:\Development\edgedriver_win68\msedgedriver.exe",
                                "C:\Development\edgedriver_win69\msedgedriver.exe",
                                "C:\Development\edgedriver_win70\msedgedriver.exe"]

    TOTAL_PROCESSES = ['AMERICAN FOOTBALL.py', 'AUSSIE RULES.py', 'BADMINTON.py', 'BANDY.py', 'BASEBALL.py',
                       'BEACH SOCCER.py', 'BEACH VOLLEYBALL.py', 'BOXING.py', 'CRICKET.py',
                       'DARTS.py', 'ESPORTS.py', 'FIELD HOCKEY.py', 'FLOORBALL.py', 'FUSTAL.py',
                       'HANDBALL.py', 'HOCKEY.py', 'KABADDI.py', 'MMA.py', 'NETBALL.py', 'PESAPALLO.py', 'RUGBY LEAGUE.py',
                       'RUGBY UNION.py', 'SNOOKER.py', 'TABLE TENNIS.py', 'TENNIS.py', 'VOLLEYBALL.py', 'WATERPOLO.py',
                       '_RUN_BASKETBALL.py', '_RUN_FOOTBALL.py', '_RUN_FOOTBALL_CORNERS.py', 'RUN1.py', 'RUN2.py',
                       'RUN3.py', 'RUN4.py', 'RUN5.py', 'RUN6.py']

    return [BAYESIAN_DIFFERENCE, BAYESIAN_DIFFERENCE_DRAW, BAYESIAN_DIFFERENCE_ALT, BAYESIAN_DIFFERENCE_XLR,
            CONFIDENCE_INTERVALS, CONFIDENCE_INTERVALS_DRAW, CONFIDENCE_INTERVALS_ALT, CONFIDENCE_INTERVALS_XLR,
            DISCRIMINANT_FOR_HOME_N_AWAY_TEAMS_AGAINST_EACH_OTHER, DISCRIMINANT_FOR_HOME_N_AWAY_TEAMS_INDEPENDENTLY,
            FORM_SIZE_COUNT, FORM_DIFFERENCE,
            FORM_VALUE_LIMIT, FORM_VALUE_LIMIT_DRAW, FORM_VALUE_LIMIT_ALT, FORM_VALUE_LIMIT_XLR,
            HOME_N_AWAY_INDEPENDENT_MATCH_SAMPLE, NUMBER_OF_MATCHES_ALREADY_PLAYED, TEAM_POSITION_DIFFERENCE,
            POSITION_MARK, YEAR_OF_MATCHES,
            SELENIUM_CHROMEDRIVER_PATH, TOTAL_PROCESSES, SELENIUM_FIREFOXDRIVER_PATH, SELENIUM_EDGEDRIVER_PATH]


def master_sport_list():
    MASTER_LIST = ["https://www.flashscore.com/american-football/",
                   "https://www.flashscore.com/aussie-rules/",
                   "https://www.flashscore.com/badminton/",
                   "https://www.flashscore.com/bandy/",
                   "https://www.flashscore.com/baseball/",
                   "https://www.flashscore.com/basketball/",
                   "https://www.flashscore.com/beach-soccer/",
                   "https://www.flashscore.com/beach-volleyball/",
                   "https://www.flashscore.com/boxing/",
                   "https://www.flashscore.com/cricket/",
                   "https://www.flashscore.com/darts/",
                   "https://www.flashscore.com/esports/",
                   "https://www.flashscore.com/field-hockey/",
                   "https://www.flashscore.com/floorball/",
                   "https://www.flashscore.com/football/",
                   "https://www.flashscore.com/futsal/",
                   "https://www.flashscore.com/handball/",
                   "https://www.flashscore.com/hockey/",
                   "https://www.flashscore.com/kabaddi/",
                   "https://www.flashscore.com/mma/",
                   "https://www.flashscore.com/netball/",
                   "https://www.flashscore.com/pesapallo/",
                   "https://www.flashscore.com/rugby-league/",
                   "https://www.flashscore.com/rugby-union/",
                   "https://www.flashscore.com/soccer/",
                   "https://www.flashscore.com/snooker/",
                   "https://www.flashscore.com/table-tennis/",
                   "https://www.flashscore.com/tennis/",
                   "https://www.flashscore.com/volleyball/",
                   "https://www.flashscore.com/water-polo/"]

    return [MASTER_LIST]


def master_sport_list1():
    FOOTBALL = "https://www.flashscore.com/football/"

    ALTERNATIVE_SPORTS1 = ["https://www.flashscore.com/basketball/",
                           "https://www.flashscore.com/beach-soccer/",
                           "https://www.flashscore.com/floorball/",
                           "https://www.flashscore.com/pesapallo/",
                           "https://www.flashscore.com/volleyball/"]

    ALTERNATIVE_SPORTS2 = ["https://www.flashscore.com/baseball/",
                           "https://www.flashscore.com/netball/",
                           "https://www.flashscore.com/hockey/"]

    SINGLE_PLAYER_SPORTS = ["https://www.flashscore.com/darts/",
                            "https://www.flashscore.com/badminton/",
                            "https://www.flashscore.com/beach-volleyball/",
                            "https://www.flashscore.com/snooker/",
                            "https://www.flashscore.com/tennis/",
                            "https://www.flashscore.com/table-tennis/"]

    DRAWABLE_GAMES1 = ["https://www.flashscore.com/soccer/",
                       "https://www.flashscore.com/bandy/",
                       "https://www.flashscore.com/water-polo/",
                       "https://www.flashscore.com/field-hockey/",
                       "https://www.flashscore.com/rugby-league/",
                       "https://www.flashscore.com/rugby-union/"]

    DRAWABLE_GAMES2 = ["https://www.flashscore.com/futsal/",
                       "https://www.flashscore.com/american-football/",
                       "https://www.flashscore.com/aussie-rules/",
                       "https://www.flashscore.com/handball/",
                       "https://www.flashscore.com/kabaddi/",
                       "https://www.flashscore.com/esports/"]

    return [FOOTBALL, ALTERNATIVE_SPORTS1, ALTERNATIVE_SPORTS2, SINGLE_PLAYER_SPORTS, DRAWABLE_GAMES1, DRAWABLE_GAMES2]


def directories():
    PROB_METRICS = ["BAYE", "RAND", "ZSCE", "ODDS", "DZSCE"]
    PROB_METRICS1 = ["CHAOTIC", "BAYESIAN", "ZSCORED", "ODDS"]
    COMBINERS = ["AVERAGE", "PRODUCT", "SQRT_AVERAGE", "SQRT_PRODUCT",
                 "CBRT_AVERAGE", "CBRT_PRODUCT", "FRT_AVERAGE", "FRT_PRODUCT"]
    COMB_PROB_METRICS1 = list(combinations(PROB_METRICS[:4], 2))
    COMB_PROB_METRICS2 = list(permutations(PROB_METRICS1, 2))[:6]
    COMB_PROB_METRICS3 = list(combinations(PROB_METRICS[:4], 3))
    COMB_PROB_METRICS4 = list(combinations(PROB_METRICS[:4], 4))
    COMB_PROB_METRICS5 = []
    for i in range(len(list(permutations(PROB_METRICS1, 3)))):
        METRICS = list(permutations(PROB_METRICS1, 3))
        if (i == 0) or (i == 1) or (i == 5) or (i == 6) or (i == 7) or (i == 11) or (i == 12) or (i == 13) or (i == 17) or (i == 18) or (i == 19) or (i == 23):
            COMB_PROB_METRICS5.append(METRICS[i])

    dir_list = []

    for COMBINER in COMBINERS[:4]:
        Z = COMBINER
        for COMB in COMB_PROB_METRICS1:
            X, Y = COMB
            dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

    for PROB in PROB_METRICS:
        X = PROB
        Y = "ANALYSIS"
        Z = "STANDARD"
        dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

    for COMB in COMB_PROB_METRICS2:
        X, Y = COMB
        Z = "COMBINATE"
        dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

    for COMB in COMB_PROB_METRICS5:
        X, Y, W = COMB
        Z = "COMBINATE"
        dir_list.append(f"RESULTS - {Z}_{X}_{Y}_{W}")

    for COMBINER in COMBINERS:
        Z = COMBINER
        if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[6] and Z != COMBINERS[7]:
            for COMB in COMB_PROB_METRICS3:
                W, X, Y = COMB
                dir_list.append(f"RESULTS - {Z}_{W}_{X}_{Y}")

    for COMBINER in COMBINERS:
        Z = COMBINER
        if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[4] and Z != COMBINERS[5]:
            for COMB in COMB_PROB_METRICS4:
                V, W, X, Y = COMB
                dir_list.append(f"RESULTS - {Z}_{V}_{W}_{X}_{Y}")

    return dir_list


def combinatorials():
    PROB_METRICS = ["BAYE", "RAND", "ZSCE", "ODDS", "DZSCE"]
    PROB_METRICS1 = ["CHAOTIC", "BAYESIAN", "ZSCORED", "ODDS"]
    COMBINERS = ["AVERAGE", "PRODUCT", "SQRT_AVERAGE", "SQRT_PRODUCT",
                 "CBRT_AVERAGE", "CBRT_PRODUCT", "FRT_AVERAGE", "FRT_PRODUCT"]
    COMB_PROB_METRICS1 = list(combinations(PROB_METRICS[:4], 2))
    COMB_PROB_METRICS2 = list(permutations(PROB_METRICS1, 2))[:6]
    COMB_PROB_METRICS3 = list(combinations(PROB_METRICS[:4], 3))
    COMB_PROB_METRICS4 = list(combinations(PROB_METRICS[:4], 4))
    COMB_PROB_METRICS5 = []
    for i in range(len(list(permutations(PROB_METRICS1, 3)))):
        METRICS = list(permutations(PROB_METRICS1, 3))
        if (i == 0) or (i == 1) or (i == 5) or (i == 6) or (i == 7) or (i == 11) or (i == 12) or (i == 13) or (i == 17) or (i == 18) or (i == 19) or (i == 23):
            COMB_PROB_METRICS5.append(METRICS[i])
    return [PROB_METRICS, PROB_METRICS1, COMBINERS, COMB_PROB_METRICS1,
            COMB_PROB_METRICS2, COMB_PROB_METRICS3, COMB_PROB_METRICS4,
            COMB_PROB_METRICS5]

