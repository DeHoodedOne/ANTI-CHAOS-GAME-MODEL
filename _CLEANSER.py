import os
from itertools import combinations, permutations


def cleanse():
    PROB_METRICS = ["BAYE", "RAND", "ZSCE", "ODDS", "DZSCE"]
    PROB_METRICS1 = ["CHAOTIC", "BAYESIAN", "ZSCORED", "ODDS"]
    COMBINERS = ["AVERAGE", "PRODUCT", "SQRT_AVERAGE", "SQRT_PRODUCT", "CBRT_AVERAGE", "CBRT_PRODUCT", "FRT_AVERAGE", "FRT_PRODUCT"]
    COMB_PROB_METRICS1 = list(combinations(PROB_METRICS[:4], 2))
    COMB_PROB_METRICS2 = list(permutations(PROB_METRICS1, 2))[:6]
    COMB_PROB_METRICS3 = list(combinations(PROB_METRICS[:4], 3))
    COMB_PROB_METRICS3_ = []
    for i in range(len(list(permutations(PROB_METRICS1, 3)))):
        METRICS = list(permutations(PROB_METRICS1, 3))
        if (i == 0) or (i == 1) or (i == 5) or (i == 6) or (i == 7) or (i == 11) or (i == 12) or (i == 13) or (i == 17) or (i == 18) or (i == 19) or (i == 23):
            COMB_PROB_METRICS3_.append(METRICS[i])
    COMB_PROB_METRICS4 = list(combinations(PROB_METRICS[:4], 4))
    dir_list = []

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

    for COMBINER in COMBINERS[:4]:
        Z = COMBINER
        for COMB in COMB_PROB_METRICS1:
            X, Y = COMB
            dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

    for COMB in COMB_PROB_METRICS2:
        X, Y = COMB
        Z = "COMBINATE"
        dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

    for COMB in COMB_PROB_METRICS3_:
        X, Y, W = COMB
        Z = "COMBINATE"
        dir_list.append(f"RESULTS - {Z}_{X}_{Y}_{W}")

    for PROB in PROB_METRICS:
        X = PROB
        Y = "ANALYSIS"
        Z = "STANDARD"
        dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

    for dir_ in dir_list:
        list_ = os.listdir(f"{dir_}")
        for filename in list_:
            with open(f"{dir_}/{filename}", 'r') as fp:
                x = len(fp.readlines())
                print(f'{filename}:', x)
            if x < 43:
                fp.close()
                os.remove(f"{dir_}/{filename}")

    # dir_list = ["LISTS - SPORTS DATA"]
    #
    # for dir_ in dir_list:
    #     list_ = os.listdir(f"{dir_}")
    #     for filename in list_:
    #         with open(f"{dir_}/{filename}", 'r') as fp:
    #             x = len(fp.readlines())
    #             print('Total lines:', x)
    #             # if x < 2:
    #             fp.close()
    #             os.remove(f"{dir_}/{filename}")


cleanse()
