import runpy
from _rprocess_checker import is_running
from _rcleamser import cleanse
from _random_samplers import sampler_
import time
from _CONTROL_CENTER import set_date_s_size, game_criteria
import os
import sys


process = os.path.basename(sys.argv[0])

CRITERIA = game_criteria(process)

start_time = time.time()
tmrw_date = set_date_s_size()[0]
sample_size = set_date_s_size()[1]

SPORTS = ['HOCKEY.py', 'KABADDI.py', 'WATERPOLO.py', 'RUGBY LEAGUE.py', 'RUGBY UNION.py']

for sport in SPORTS:
    runpy.run_path(path_name=sport)

processes_active = []
for i in range(len(CRITERIA[22])):
    if CRITERIA[22][i] != process:
        if is_running(CRITERIA[22][i]) is True:
            processes_active.append(CRITERIA[22][i])
print(processes_active)
if len(processes_active) == 0:
    try:
        cleanse()
    except FileNotFoundError:
        pass
    sampler_(sample_size, tmrw_date)

end_time = time.time()
print(f"run speed: {end_time - start_time}s")
