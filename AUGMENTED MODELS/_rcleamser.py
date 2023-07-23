import os
from _CONTROL_CENTER import directories


def cleanse():
    dir_list = directories()

    for dir_ in dir_list:
        list_ = os.listdir(f"../{dir_}")
        for filename in list_:
            with open(f"../{dir_}/{filename}", 'r') as fp:
                x = len(fp.readlines())
            if x < 43:
                fp.close()
                os.remove(f"../{dir_}/{filename}")

