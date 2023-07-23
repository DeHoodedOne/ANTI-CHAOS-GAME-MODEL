import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException, ElementClickInterceptedException, UnexpectedAlertPresentException, \
    WebDriverException, NoSuchWindowException, TimeoutException, InvalidSessionIdException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FFService
from time import sleep
import winsound
import math
import random as rdm
import statistics as stats
import scipy.stats
import numpy as np
import time
import traceback
from datetime import datetime
from _CONTROL_CENTER import set_date_s_size, game_criteria, master_sport_list, combinatorials, wait_time
import os
import sys


process = os.path.basename(sys.argv[0])

tmrw_date = set_date_s_size()[0]
sample_size = set_date_s_size()[1]

now = datetime.now()
date_time = now.strftime("%d-%m-%Y")

CRITERIA = game_criteria(process)

BAY_DIFF = CRITERIA[0]
BAY_DIFF_ALT = CRITERIA[2]
BAY_DIFF_XLR = CRITERIA[3]
CONFINTVLS = CRITERIA[4]
CONFINTVLS_ALT = CRITERIA[6]
CONFINTVLS_XLR = CRITERIA[7]
DSCRM_BT = CRITERIA[8]
DSCRM_H_A = CRITERIA[9]
FORM_COUNT = CRITERIA[10]
FORM_DIFF = CRITERIA[11]
FORM_VALUE = CRITERIA[12]
FORM_VALUE_ALT = CRITERIA[14]
FORM_VALUE_XLR = CRITERIA[15]
INDP_MATCH_SAMPLE = CRITERIA[16]
NMP = CRITERIA[17]
POS_DIFF = CRITERIA[18]
POS_MARK = CRITERIA[19]
YEAR = CRITERIA[20]
ABS_XLR = 0.6
ABS_ALT = 0.4

DG_AVG_ALT = 0.4
DGB_AVG_ALT = 0.4
DG_DIF_ALT = 0.4
DG_AVG_XLR = 0.6
DGB_AVG_XLR = 0.6
DG_DIF_XLR = 0.6

METRICS = combinatorials()

PROB_METRICS = METRICS[0]
PROB_METRICS1 = METRICS[1]
COMBINERS = METRICS[2]
COMB_PROB_METRICS1 = METRICS[3]
COMB_PROB_METRICS2 = METRICS[4]
COMB_PROB_METRICS3 = METRICS[5]
COMB_PROB_METRICS4 = METRICS[6]
COMB_PROB_METRICS5 = METRICS[7]

OUTCOMES = ["HW", "AW", "ov2.5", "ov3.5", "sh1_1.5", "sh1_2.5", "sh2_1.5", "sh2_2.5", "12"]
OUTCOMES_ALT_XLR = ["HW", "AW", "12"]

start_time = time.time()
SPORT_ = master_sport_list()[0][2]

# ms_edge_path = CRITERIA[24][3]
# options = EdgeOptions()
# options.add_extension("_AdblockPlus.crx")
# options.add_argument("start-maximized")
# driver = webdriver.Edge(executable_path=ms_edge_path, options=options)

# firefox_path = CRITERIA[23][3]
# adblock = "_dablocker_ultimate.xpi"
# service = FFService(firefox_path)
# driver = webdriver.Firefox(service=service)
# driver.install_addon(adblock, temporary=True)
# driver.maximize_window()

chrome_path = CRITERIA[21][3]
service = Service(chrome_path)
options = webdriver.ChromeOptions()
options.add_extension("_AdblockPlus.crx")
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(wait_time())
try:
    driver.get(SPORT_)
    sleep(10)
except WebDriverException:
    try:
        driver.get(SPORT_)
        sleep(10)
    except WebDriverException:
        traceback.print_exc()

sport = SPORT_.split('/')[3]
if driver.current_url == SPORT_:
    try:
        window_before = driver.window_handles[0]
        window_ads0 = driver.window_handles[1]
        driver.switch_to.window(window_before)
        driver.switch_to.window(window_ads0)
        driver.close()
        driver.switch_to.window(window_before)
    except IndexError:
        try:
            window_before = driver.window_handles[1]
            window_ads0 = driver.window_handles[0]
            driver.switch_to.window(window_before)
            driver.switch_to.window(window_ads0)
            driver.close()
            driver.switch_to.window(window_before)
        except IndexError:
            window_before = driver.window_handles[0]
            driver.switch_to.window(window_before)
else:
    try:
        window_before = driver.window_handles[1]
        window_ads0 = driver.window_handles[0]
        driver.switch_to.window(window_before)
        driver.switch_to.window(window_ads0)
        driver.close()
        driver.switch_to.window(window_before)
    except IndexError:
        try:
            window_before = driver.window_handles[0]
            window_ads0 = driver.window_handles[1]
            driver.switch_to.window(window_before)
            driver.switch_to.window(window_ads0)
            driver.close()
            driver.switch_to.window(window_before)
        except IndexError:
            window_before = driver.window_handles[0]
            driver.switch_to.window(window_before)

if driver.current_url != SPORT_:
    try:
        driver.get(SPORT_)
        sleep(10)
    except WebDriverException:
        try:
            driver.get(SPORT_)
            sleep(10)
        except WebDriverException:
            traceback.print_exc()


def cookie_click1():
    try:
        accept_cookiez = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_cookiez.click()
    except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
        pass
    driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()


def cookie_click():
    try:
        accept_cookiez = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_cookiez.click()
    except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
        pass
    if date_time != tmrw_date:
        driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()
    driver.find_element(By.CSS_SELECTOR, ".filters__group .filters__tab:last-child").click()


def alert_handler():
    try:
        alerts = driver.switch_to.alert
        alerts.accept()
        driver.switch_to.default_content()
        cookie_click1()
    except NoAlertPresentException:
        cookie_click1()


def alert_handler1():
    try:
        alerts = driver.switch_to.alert
        alerts.accept()
        driver.switch_to.default_content()
        cookie_click()
    except NoAlertPresentException:
        cookie_click()


try:
    accept_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_cookies.click()
except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
    pass

if date_time != tmrw_date:
    try:
        cookie_click1()
    except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
        try:
            driver.refresh()
            sleep(1.5)
            cookie_click1()
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
            cookie_click1()
        except UnexpectedAlertPresentException:
            alert_handler()
try:
    driver.find_element(By.CSS_SELECTOR, ".filters__group .filters__tab:last-child").click()
except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
    try:
        driver.refresh()
        sleep(1.5)
        cookie_click()
    except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
        cookie_click()
    except UnexpectedAlertPresentException:
        alert_handler1()

calender_day_ = int(driver.find_element(By.ID, 'calendarMenu').text.split("/")[0])
selected_day_ = int(tmrw_date.split("-")[0])
if calender_day_ > selected_day_:
    driver.find_element(By.CSS_SELECTOR, '[title="Previous day"]').click()
elif calender_day_ < selected_day_:
    driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()
else:
    pass

driver.find_element(By.XPATH, '//*[@id="hamburger-menu"]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="hamburger-menu-window"]/div/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="hamburger-menu"]/div[1]/div/div[3]/div[2]/div[2]/label[2]').click()
driver.find_element(By.CSS_SELECTOR, '[class="modal__window modal__window--settings"] [class="close modal__closeButton"]').click()


def team_data():
    country = driver.find_element(By.CSS_SELECTOR, '.tournamentHeaderDescription .tournamentHeader__country').text.split(':')[0]
    league = driver.find_element(By.CSS_SELECTOR, '.tournamentHeaderDescription .tournamentHeader__country').text.split(':')[1].split(' - ')[0]
    try:
        home_team = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__home  .participant__participantName a').text
    except NoSuchElementException:
        home_teamw = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[0].text
        home_teamv = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[1].text
        home_team = f"{home_teamw}/{home_teamv}"
    try:
        away_team = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__away  .participant__participantName a').text
    except NoSuchElementException:
        away_teamw = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[0].text
        away_teamv = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[1].text
        away_team = f"{away_teamw}/{away_teamv}"
    leagues.append(league)
    countries.append(country)
    away_teams.append(away_team)
    home_teams.append(home_team)


def pts_pos_mp():
    try:
        first_entry = int(driver.find_elements(By.CSS_SELECTOR, '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[0].text.strip())
    except IndexError:
        try:
            driver.refresh()
            sleep(1.5)
            first_entry = int(driver.find_elements(By.CSS_SELECTOR, '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[0].text.strip())
        except IndexError:
            first_entry = 0

    if selected_teams_names[0].text == home_teamx:
        try:
            home_t_position = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[0].text.split('.')[0].strip()
            home_positions.append(int(home_t_position))
        except IndexError:
            home_positions.append(0)
        if first_entry > 9:
            try:
                home_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[0].text.strip()
                home_nums_matches_played.append(int(home_t_mp))
            except IndexError:
                home_nums_matches_played.append(0)
        try:
            home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[0].text.strip()
            home_points.append(int(home_t_point))
        except IndexError:
            try:
                home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[0].text.strip()
                home_points.append(float(home_t_point))
            except IndexError:
                home_points.append(0)
    else:
        try:
            away_t_position = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[0].text.split('.')[0].strip()
            away_positions.append(int(away_t_position))
        except IndexError:
            away_positions.append(0)
        if first_entry > 9:
            try:
                away_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[0].text.strip()
                away_nums_matches_played.append(int(away_t_mp))
            except IndexError:
                away_nums_matches_played.append(0)
        try:
            away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[0].text.strip()
            away_points.append(int(away_t_point))
        except IndexError:
            try:
                away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[0].text.strip()
                away_points.append(float(away_t_point))
            except IndexError:
                away_points.append(0)
    try:
        if selected_teams_names[1].text == away_teamx:
            try:
                away_t_position = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[1].text.split('.')[0].strip()
                away_positions.append(int(away_t_position))
            except IndexError:
                away_positions.append(0)
            if first_entry > 9:
                try:
                    away_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[4].text.strip()
                    away_nums_matches_played.append(int(away_t_mp))
                except IndexError:
                    away_nums_matches_played.append(0)
            try:
                away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[1].text.strip()
                away_points.append(int(away_t_point))
            except IndexError:
                try:
                    away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[1].text.strip()
                    away_points.append(float(away_t_point))
                except IndexError:
                    away_points.append(0)
        else:
            try:
                home_t_position = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[1].text.split('.')[0].strip()
                home_positions.append(int(home_t_position))
            except IndexError:
                home_positions.append(0)
            if first_entry > 9:
                try:
                    home_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[4].text.strip()
                    home_nums_matches_played.append(int(home_t_mp))
                except IndexError:
                    home_nums_matches_played.append(0)
            try:
                home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[1].text.strip()
                home_points.append(int(home_t_point))
            except IndexError:
                try:
                    home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[1].text.strip()
                    home_points.append(float(home_t_point))
                except IndexError:
                    home_points.append(0)
    except IndexError:
        if selected_teams_names[0].text == home_teamx:
            away_positions.append(0)
            away_nums_matches_played.append(0)
            away_points.append(0)
        elif selected_teams_names[0].text == away_teamx:
            home_points.append(0)
            home_nums_matches_played.append(0)
            home_positions.append(0)


def z_scorer(htpts, atpts):
    try:
        teams_pts = driver.find_elements(By.CSS_SELECTOR, '.ui-table__row  .table__cell--points ')
        test = teams_pts[0]
    except IndexError:
        teams_pts = driver.find_elements(By.CSS_SELECTOR, '.ui-table__row  .table__cell--pct ')
    team_pts = []
    for t in range(len(teams_pts)):
        pts = float(teams_pts[t].text.strip())
        team_pts.append(pts)
    try:
        mean_ = stats.mean(team_pts)
        stdv = stats.pstdev(team_pts)
        if mean_ > 0 and stdv > 0:
            home_zsc = scipy.stats.norm.cdf(htpts, loc=mean_, scale=stdv)
            away_zsc = scipy.stats.norm.cdf(atpts, loc=mean_, scale=stdv)
            diff_zsc = abs(home_zsc - away_zsc)
            home_z_prob.append(home_zsc)
            away_z_prob.append(away_zsc)
            diff_z_prob.append(diff_zsc)
        else:
            while True:
                home_z = rdm.random()
                away_z = rdm.random()
                if (home_z + away_z) <= 1:
                    home_z_prob.append(home_z)
                    away_z_prob.append(away_z)
                    diff_z_prob.append(abs(home_z - away_z))
                    break
    except stats.StatisticsError:
        while True:
            home_z = rdm.random()
            away_z = rdm.random()
            if (home_z + away_z) <= 1:
                home_z_prob.append(home_z)
                away_z_prob.append(away_z)
                diff_z_prob.append(abs(home_z - away_z))
                break


def append_zeroes(home_pos, away_pos):
    def zeroth_break(home_z_, away_z_, diff_z_, CLEARANCE_z):
        if 0 < home_z_ < 1 and 0 < away_z_ < 1:
            home_z_prob.append(home_z_)
            away_z_prob.append(away_z_)
            diff_z_prob.append(diff_z_)
        else:
            home_z_ = rdm.random()
            away_z_ = 1 - home_z_
            diff_z_ = abs(home_z_ - away_z_)
            if diff_z_ < CLEARANCE_:
                home_z_ = rdm.random() * rdm.random()
                away_z_ = 1 - home_z_
                diff_z_ = abs(home_z_ - away_z_)
                if diff_z_ < CLEARANCE_:
                    home_z_ = math.sqrt(rdm.random() * rdm.random())
                    away_z_ = 1 - home_z_
                    diff_z_ = abs(home_z_ - away_z_)
                    if diff_z_ < CLEARANCE_:
                        home_z_ = 0.5 * (rdm.random() + rdm.random())
                        away_z_ = 1 - home_z_
                        diff_z_ = abs(home_z_ - away_z_)
                        if diff_z_ < CLEARANCE_:
                            home_z_ = math.sqrt(0.5 * (rdm.random() + rdm.random()))
                            away_z_ = 1 - home_z_
                            diff_z_ = abs(home_z_ - away_z_)
            home_z_prob.append(home_z_)
            away_z_prob.append(away_z_)
            diff_z_prob.append(diff_z_)

    away_points.append(0)
    home_points.append(0)
    CLEARANCE = 0.7
    CLEARANCE_ = 0.875
    while True:
        try:
            home_z = 1 - (int(home_pos) / (int(home_pos) + int(away_pos)))
            away_z = 1 - (int(away_pos) / (int(home_pos) + int(away_pos)))
            diff_z = abs(home_z - away_z)
            if diff_z < CLEARANCE:
                home_z = (1 - (int(home_pos) / (int(home_pos) + int(away_pos)))) * rdm.random()
                away_z = (1 - (int(away_pos) / (int(home_pos) + int(away_pos)))) * rdm.random()
                diff_z = abs(home_z - away_z)
                if diff_z < CLEARANCE:
                    home_z = math.sqrt((1 - (int(home_pos) / (int(home_pos) + int(away_pos)))) * rdm.random())
                    away_z = math.sqrt((1 - (int(away_pos) / (int(home_pos) + int(away_pos)))) * rdm.random())
                    diff_z = abs(home_z - away_z)
                    if diff_z < CLEARANCE:
                        home_z = 0.5 * ((1 - (int(home_pos) / (int(home_pos) + int(away_pos)))) + rdm.random())
                        away_z = 0.5 * ((1 - (int(away_pos) / (int(home_pos) + int(away_pos)))) + rdm.random())
                        diff_z = abs(home_z - away_z)
                        if diff_z < CLEARANCE:
                            home_z = math.sqrt(0.5 * ((1 - (int(home_pos) / (int(home_pos) + int(away_pos)))) + rdm.random()))
                            away_z = math.sqrt(0.5 * ((1 - (int(away_pos) / (int(home_pos) + int(away_pos)))) + rdm.random()))
                            diff_z = abs(home_z - away_z)
                            if diff_z < CLEARANCE:
                                home_z = 1 - ((int(home_pos) / (int(home_pos) + int(away_pos))) * rdm.random())
                                away_z = 1 - ((int(away_pos) / (int(home_pos) + int(away_pos))) * rdm.random())
                                diff_z = abs(home_z - away_z)
                                if diff_z < CLEARANCE:
                                    home_z = 1 - math.sqrt((int(home_pos) / (int(home_pos) + int(away_pos))) * rdm.random())
                                    away_z = 1 - math.sqrt((int(away_pos) / (int(home_pos) + int(away_pos))) * rdm.random())
                                    diff_z = abs(home_z - away_z)
                                    if diff_z < CLEARANCE:
                                        home_z = 1 - 0.5 * ((int(home_pos) / (int(home_pos) + int(away_pos))) + rdm.random())
                                        away_z = 1 - 0.5 * ((int(away_pos) / (int(home_pos) + int(away_pos))) + rdm.random())
                                        diff_z = abs(home_z - away_z)
                                        if diff_z < CLEARANCE:
                                            home_z = 1 - math.sqrt(0.5 * ((int(home_pos) / (int(home_pos) + int(away_pos))) + rdm.random()))
                                            away_z = 1 - math.sqrt(0.5 * ((int(away_pos) / (int(home_pos) + int(away_pos))) + rdm.random()))
                                            diff_z = abs(home_z - away_z)
                                            if diff_z < CLEARANCE:
                                                zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE)
                                                break
                                        else:
                                            zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE)
                                            break
                                    else:
                                        zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE)
                                        break
                                else:
                                    zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE)
                                    break
                            else:
                                zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE)
                                break
                        else:
                            zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE)
                            break
                    else:
                        zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE)
                        break
                else:
                    zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE)
                    break
            else:
                zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE)
                break
        except ZeroDivisionError:
            home_z = rdm.random()
            away_z = 1 - home_z
            diff_z = abs(home_z - away_z)
            if diff_z < CLEARANCE_:
                home_z = rdm.random() * rdm.random()
                away_z = 1 - home_z
                diff_z = abs(home_z - away_z)
                if diff_z < CLEARANCE_:
                    home_z = math.sqrt(rdm.random() * rdm.random())
                    away_z = 1 - home_z
                    diff_z = abs(home_z - away_z)
                    if diff_z < CLEARANCE_:
                        home_z = 0.5 * (rdm.random() + rdm.random())
                        away_z = 1 - home_z
                        diff_z = abs(home_z - away_z)
                        if diff_z < CLEARANCE_:
                            home_z = math.sqrt(0.5 * (rdm.random() + rdm.random()))
                            away_z = 1 - home_z
                            diff_z = abs(home_z - away_z)
                            if diff_z < CLEARANCE_:
                                zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE_)
                                break
                        else:
                            zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE_)
                            break
                    else:
                        zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE_)
                        break
                else:
                    zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE_)
                    break
            else:
                zeroth_break(home_z_=home_z, away_z_=away_z, diff_z_=diff_z, CLEARANCE_z=CLEARANCE_)
                break


def h2h_aggregator():
    valid_games = 0
    count_2_5 = 0
    count_3_5 = 0
    count_sh1_1_5 = 0
    count_sh1_2_5 = 0
    count_sh2_1_5 = 0
    count_sh2_2_5 = 0
    count_12 = 0
    count_HW = 0
    count_AW = 0
    count_00 = 0

    date___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__date')
    if len(date___) > 0:
        home_x = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
        away_x = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
        home_score = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__result span:first-child')
        away_score = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__result span:last-child')
        for m in range(DSCRM_BT):
            try:
                if YEAR <= int(date___[m].text.split('.')[-1].strip()) < 90:
                    valid_games += 1
                    if (int(home_score[m].text) > int(away_score[m].text)) and (home_x[m].text == home_teamx):
                        count_HW += 1
                    if (int(home_score[m].text) > int(away_score[m].text)) and (home_x[m].text == away_teamx):
                        count_AW += 1
                    if (int(away_score[m].text) > int(home_score[m].text)) and (away_x[m].text == away_teamx):
                        count_AW += 1
                    if (int(away_score[m].text) > int(home_score[m].text)) and (away_x[m].text == home_teamx):
                        count_HW += 1
                    if (int(home_score[m].text) + int(away_score[m].text)) >= 0:
                        count_00 += 1
                    if (int(home_score[m].text) + int(away_score[m].text)) >= 3:
                        count_2_5 += 1
                    if (int(home_score[m].text) + int(away_score[m].text)) >= 4:
                        count_3_5 += 1
                    if ((int(home_score[m].text) + 1.5) > int(away_score[m].text)) and (home_x[m].text == home_teamx):
                        count_sh1_1_5 += 1
                    if ((int(away_score[m].text) + 1.5) > int(home_score[m].text)) and (away_x[m].text == home_teamx):
                        count_sh1_1_5 += 1
                    if ((int(home_score[m].text) + 1.5) > int(away_score[m].text)) and (home_x[m].text == away_teamx):
                        count_sh2_1_5 += 1
                    if ((int(away_score[m].text) + 1.5) > int(home_score[m].text)) and (away_x[m].text == away_teamx):
                        count_sh2_1_5 += 1
                    if ((int(home_score[m].text) + 2.5) > int(away_score[m].text)) and (home_x[m].text == home_teamx):
                        count_sh1_2_5 += 1
                    if ((int(away_score[m].text) + 2.5) > int(home_score[m].text)) and (away_x[m].text == home_teamx):
                        count_sh1_2_5 += 1
                    if ((int(home_score[m].text) + 2.5) > int(away_score[m].text)) and (home_x[m].text == away_teamx):
                        count_sh2_2_5 += 1
                    if ((int(away_score[m].text) + 2.5) > int(home_score[m].text)) and (away_x[m].text == away_teamx):
                        count_sh2_2_5 += 1
                    if int(home_score[m].text) != int(away_score[m].text):
                        count_12 += 1
                else:
                    print(f"Date Error at 1H2H: {date___[m].text}")
                    valid_games += 1
            except ValueError:
                print(f"Value Error at 1H2H: {date___[m].text} | {home_x[m].text} vs {away_x[m].text}")
                print(f"Score1H2H - {home_score[m].text} : {away_score[m].text}")
                valid_games += 1
            except IndexError:
                valid_games += 1
    else:
        valid_games = DSCRM_BT

    return [valid_games, count_HW, count_AW, count_2_5, count_3_5, count_sh1_1_5, count_sh1_2_5, count_sh2_1_5, count_sh2_2_5, count_12, count_00]


def h2h_prob_calc(h2h_probz):
    prob_HW = float(h2h_probz[1] / h2h_probz[0])
    prob_AW = float(h2h_probz[2] / h2h_probz[0])
    prob_2_5i = float(h2h_probz[3] / h2h_probz[0])
    prob_3_5i = float(h2h_probz[4] / h2h_probz[0])
    prob_sh1_1_5i = float(h2h_probz[5] / h2h_probz[0])
    prob_sh1_2_5i = float(h2h_probz[6] / h2h_probz[0])
    prob_sh2_1_5i = float(h2h_probz[7] / h2h_probz[0])
    prob_sh2_2_5i = float(h2h_probz[8] / h2h_probz[0])
    prob_12i = 0.99
    prob_00i = float(h2h_probz[10] / h2h_probz[0])

    h2h_probs = [prob_HW, prob_AW, prob_2_5i, prob_3_5i, prob_sh1_1_5i, prob_sh1_2_5i, prob_sh2_1_5i, prob_sh2_2_5i, prob_12i, prob_00i]
    probs_H2H = []
    for prob in h2h_probs:
        if prob == 1.0:
            prob -= 0.01
        elif prob == 0:
            prob += 0.01
        probs_H2H.append(prob)
    return [probs_H2H[0], probs_H2H[1], probs_H2H[2], probs_H2H[3], probs_H2H[4], probs_H2H[5], probs_H2H[6], probs_H2H[7], probs_H2H[8], probs_H2H[9]]


def h2h_appender(prb_HW, prb_AW, prb_2_5, prb_3_5, prb_sh1_1_5, prb_sh1_2_5, prb_sh2_1_5, prb_sh2_2_5, prb_12, prb_00):
    prob_HWs.append(prb_HW)
    prob_AWs.append(prb_AW)
    prob_2_5s.append(prb_2_5)
    prob_3_5s.append(prb_3_5)
    prob_sh1_1_5s.append(prb_sh1_1_5)
    prob_sh1_2_5s.append(prb_sh1_2_5)
    prob_sh2_1_5s.append(prb_sh2_1_5)
    prob_sh2_2_5s.append(prb_sh2_2_5)
    prob_12s.append(prb_12)
    prob_00s.append(prb_00)


def ht_indp_aggregator():
    valid_games_H_indp = 0
    count_2_5_H_indp = 0
    count_3_5_H_indp = 0
    count_sh1_1_5_H_indp = 0
    count_sh1_2_5_H_indp = 0
    count_12_H_indp = 0
    count_HW_H_indp = 0
    count_00_H_indp = 0

    date_ = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
    if len(date_) > 0:
        home_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
        away_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
        home_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:first-child')
        away_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:last-child')
        for k in range(DSCRM_H_A):
            try:
                if YEAR <= int(date_[k].text.split('.')[-1].strip()) < 90:
                    valid_games_H_indp += 1
                    if (int(home_score[k].text) > int(away_score[k].text)) and (home_x[k].text == home_teamx):
                        count_HW_H_indp += 1
                    if (int(away_score[k].text) > int(home_score[k].text)) and (away_x[k].text == home_teamx):
                        count_HW_H_indp += 1
                    if int(home_score[k].text) == int(away_score[k].text):
                        count_HW_H_indp += 0
                    if (int(home_score[k].text) + int(away_score[k].text)) >= 0 and (home_x[k].text == home_teamx) and int(home_score[k].text) >= 0:
                        count_00_H_indp += 1
                    if (int(home_score[k].text) + int(away_score[k].text)) >= 0 and (away_x[k].text == home_teamx) and int(away_score[k].text) >= 0:
                        count_00_H_indp += 1
                    if (int(home_score[k].text) + int(away_score[k].text)) >= 3 and (home_x[k].text == home_teamx) and int(home_score[k].text) >= 2:
                        count_2_5_H_indp += 1
                    if (int(home_score[k].text) + int(away_score[k].text)) >= 3 and (away_x[k].text == home_teamx) and int(away_score[k].text) >= 2:
                        count_2_5_H_indp += 1
                    if (int(home_score[k].text) + int(away_score[k].text)) >= 4 and (home_x[k].text == home_teamx) and int(home_score[k].text) >= 3:
                        count_3_5_H_indp += 1
                    if (int(home_score[k].text) + int(away_score[k].text)) >= 4 and (away_x[k].text == home_teamx) and int(away_score[k].text) >= 3:
                        count_3_5_H_indp += 1
                    if ((int(home_score[k].text) + 1.5) > int(away_score[k].text)) and (home_x[k].text == home_teamx):
                        count_sh1_1_5_H_indp += 1
                    if ((int(away_score[k].text) + 1.5) > int(home_score[k].text)) and (away_x[k].text == home_teamx):
                        count_sh1_1_5_H_indp += 1
                    if ((int(home_score[k].text) + 2.5) > int(away_score[k].text)) and (home_x[k].text == home_teamx):
                        count_sh1_2_5_H_indp += 1
                    if ((int(away_score[k].text) + 2.5) > int(home_score[k].text)) and (away_x[k].text == home_teamx):
                        count_sh1_2_5_H_indp += 1
                    if int(home_score[k].text) != int(away_score[k].text) and int(home_score[k].text) >= 1 and (home_x[k].text == home_teamx):
                        count_12_H_indp += 1
                    if int(away_score[k].text) != int(home_score[k].text) and int(away_score[k].text) >= 1 and (away_x[k].text == home_teamx):
                        count_12_H_indp += 1
                else:
                    print(f"Date Error at Home1 : {date_[k].text}")
                    valid_games_H_indp += 1
            except ValueError:
                print(f"Value Error at Home1 : {date_[k].text} | {home_x[k].text} vs {away_x[k].text}")
                print(f"Score1H - {home_score[k].text} : {away_score[k].text}")
                valid_games_H_indp += 1
            except IndexError:
                valid_games_H_indp += 1
    else:
        valid_games_H_indp = DSCRM_H_A

    return [valid_games_H_indp, count_HW_H_indp, count_2_5_H_indp, count_3_5_H_indp, count_sh1_1_5_H_indp, count_sh1_2_5_H_indp, count_12_H_indp, count_00_H_indp]


def ht_indp_prob_calc(ht_probz):
    prob_HW_H_indp = float(ht_probz[1] / ht_probz[0])
    prob_AW_H_indp = 1 - prob_HW_H_indp
    prob_2_5_H_indp = float(ht_probz[2] / ht_probz[0])
    prob_3_5_H_indp = float(ht_probz[3] / ht_probz[0])
    prob_sh1_1_5_H_indp = float(ht_probz[4] / ht_probz[0])
    prob_sh1_2_5_H_indp = float(ht_probz[5] / ht_probz[0])
    prob_sh2_1_5_H_indp = 1 - prob_sh1_1_5_H_indp
    prob_sh2_2_5_H_indp = 1 - prob_sh1_2_5_H_indp
    prob_12_H_indp = float(ht_probz[6] / ht_probz[0])
    prob_00_H_indp = float(ht_probz[7] / ht_probz[0])

    ht_indp_probs = [prob_HW_H_indp, prob_AW_H_indp, prob_2_5_H_indp, prob_3_5_H_indp, prob_sh1_1_5_H_indp,
                     prob_sh1_2_5_H_indp, prob_sh2_1_5_H_indp, prob_sh2_2_5_H_indp, prob_12_H_indp, prob_00_H_indp]

    probs_HT_INDP = []
    for prob in ht_indp_probs:
        if prob == 1.0:
            prob -= 0.01
        elif prob == 0:
            prob += 0.01
        probs_HT_INDP.append(prob)

    return [probs_HT_INDP[0], probs_HT_INDP[1], probs_HT_INDP[2], probs_HT_INDP[3], probs_HT_INDP[4], probs_HT_INDP[5],
            probs_HT_INDP[6], probs_HT_INDP[7], probs_HT_INDP[8], probs_HT_INDP[9]]


def ht_indp_appender(prb_HW_H_indp, prb_AW_H_indp, prb_2_5_H_indp, prb_3_5_H_indp, prb_sh1_1_5_H_indp,
                     prb_sh1_2_5_H_indp, prb_sh2_1_5_H_indp, prb_sh2_2_5_H_indp, prb_12_H_indp, prb_00_H_indp):
    prob_HW_H_indps.append(prb_HW_H_indp)
    prob_AW_H_indps.append(prb_AW_H_indp)
    prob_2_5_H_indps.append(prb_2_5_H_indp)
    prob_3_5_H_indps.append(prb_3_5_H_indp)
    prob_sh1_1_5_H_indps.append(prb_sh1_1_5_H_indp)
    prob_sh1_2_5_H_indps.append(prb_sh1_2_5_H_indp)
    prob_sh2_1_5_H_indps.append(prb_sh2_1_5_H_indp)
    prob_sh2_2_5_H_indps.append(prb_sh2_2_5_H_indp)
    prob_12_H_indps.append(prb_12_H_indp)
    prob_00_H_indps.append(prb_00_H_indp)


def at_indp_aggregator():
    valid_games_A_indp = 0
    count_00_A_indp = 0
    count_2_5_A_indp = 0
    count_3_5_A_indp = 0
    count_sh2_1_5_A_indp = 0
    count_sh2_2_5_A_indp = 0
    count_12_A_indp = 0
    count_AW_A_indp = 0
    date__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
    if len(date__) > 0:
        home_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__homeParticipant .h2h__participantInner')
        away_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__awayParticipant .h2h__participantInner')
        home_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:first-child')
        away_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:last-child')
        for n in range(DSCRM_H_A):
            try:
                if YEAR <= int(date__[n].text.split('.')[-1].strip()) < 90:
                    valid_games_A_indp += 1
                    if (int(home_score[n].text) > int(away_score[n].text)) and (home_x[n].text == away_teamx):
                        count_AW_A_indp += 1
                    if (int(away_score[n].text) > int(home_score[n].text)) and (away_x[n].text == away_teamx):
                        count_AW_A_indp += 1
                    if int(home_score[n].text) == int(away_score[n].text):
                        count_AW_A_indp += 0
                    if (int(home_score[n].text) + int(away_score[n].text)) >= 0 and (home_x[n].text == away_teamx) and int(home_score[n].text) >= 0:
                        count_00_A_indp += 1
                    if (int(home_score[n].text) + int(away_score[n].text)) >= 0 and (away_x[n].text == away_teamx) and int(away_score[n].text) >= 0:
                        count_00_A_indp += 1
                    if (int(home_score[n].text) + int(away_score[n].text)) >= 3 and (home_x[n].text == away_teamx) and int(home_score[n].text) >= 2:
                        count_2_5_A_indp += 1
                    if (int(home_score[n].text) + int(away_score[n].text)) >= 3 and (away_x[n].text == away_teamx) and int(away_score[n].text) >= 2:
                        count_2_5_A_indp += 1
                    if (int(home_score[n].text) + int(away_score[n].text)) >= 4 and (home_x[n].text == away_teamx) and int(home_score[n].text) >= 3:
                        count_3_5_A_indp += 1
                    if (int(home_score[n].text) + int(away_score[n].text)) >= 4 and (away_x[n].text == away_teamx) and int(away_score[n].text) >= 3:
                        count_3_5_A_indp += 1
                    if ((int(home_score[n].text) + 1.5) > int(away_score[n].text)) and (home_x[n].text == away_teamx):
                        count_sh2_1_5_A_indp += 1
                    if ((int(away_score[n].text) + 1.5) > int(home_score[n].text)) and (away_x[n].text == away_teamx):
                        count_sh2_1_5_A_indp += 1
                    if ((int(home_score[n].text) + 2.5) > int(away_score[n].text)) and (home_x[n].text == away_teamx):
                        count_sh2_2_5_A_indp += 1
                    if ((int(away_score[n].text) + 2.5) > int(home_score[n].text)) and (away_x[n].text == away_teamx):
                        count_sh2_2_5_A_indp += 1
                    if int(home_score[n].text) != int(away_score[n].text) and int(home_score[n].text) >= 1 and (home_x[n].text == away_teamx):
                        count_12_A_indp += 1
                    if int(away_score[n].text) != int(home_score[n].text) and int(away_score[n].text) >= 1 and (away_x[n].text == away_teamx):
                        count_12_A_indp += 1
                else:
                    print(f"Date Error at Away1: {date__[n].text}")
                    valid_games_A_indp += 1
            except ValueError:
                print(f"Error at Away1: {date__[n].text} | {home_x[n].text} vs {away_x[n].text}")
                print(f"Score1A - {home_score[n].text} : {away_score[n].text}")
                valid_games_A_indp += 1
            except IndexError:
                valid_games_A_indp += 1
    else:
        valid_games_A_indp = DSCRM_H_A

    return [valid_games_A_indp, count_AW_A_indp, count_2_5_A_indp, count_3_5_A_indp,
            count_sh2_1_5_A_indp, count_sh2_2_5_A_indp, count_12_A_indp, count_00_A_indp]


def at_indp_prob_calc(at_probz):
    prob_AW_A_indp = float(at_probz[1] / at_probz[0])
    prob_HW_A_indp = 1 - prob_AW_A_indp
    prob_2_5_A_indp = float(at_probz[2] / at_probz[0])
    prob_3_5_A_indp = float(at_probz[3] / at_probz[0])
    prob_sh2_1_5_A_indp = float(at_probz[4] / at_probz[0])
    prob_sh2_2_5_A_indp = float(at_probz[5] / at_probz[0])
    prob_sh1_1_5_A_indp = 1 - prob_sh2_1_5_A_indp
    prob_sh1_2_5_A_indp = 1 - prob_sh2_2_5_A_indp
    prob_12_A_indp = float(at_probz[6] / at_probz[0])
    prob_00_A_indp = float(at_probz[7] / at_probz[0])

    at_indp_probs = [prob_HW_A_indp, prob_AW_A_indp, prob_2_5_A_indp, prob_3_5_A_indp, prob_sh1_1_5_A_indp,
                     prob_sh1_2_5_A_indp, prob_sh2_1_5_A_indp, prob_sh2_2_5_A_indp, prob_12_A_indp, prob_00_A_indp]

    probs_AT_INDP = []
    for prob in at_indp_probs:
        if prob == 1.0:
            prob -= 0.01
        elif prob == 0:
            prob += 0.01
        probs_AT_INDP.append(prob)

    return [probs_AT_INDP[0], probs_AT_INDP[1], probs_AT_INDP[2], probs_AT_INDP[3], probs_AT_INDP[4], probs_AT_INDP[5],
            probs_AT_INDP[6], probs_AT_INDP[7], probs_AT_INDP[8], probs_AT_INDP[9]]


def at_indp_appender(prb_HW_A_indp, prb_AW_A_indp, prb_2_5_A_indp, prb_3_5_A_indp, prb_sh1_1_5_A_indp,
                     prb_sh1_2_5_A_indp, prb_sh2_1_5_A_indp, prb_sh2_2_5_A_indp, prb_12_A_indp, prb_00_A_indp):
    prob_HW_A_indps.append(prb_HW_A_indp)
    prob_AW_A_indps.append(prb_AW_A_indp)
    prob_2_5_A_indps.append(prb_2_5_A_indp)
    prob_3_5_A_indps.append(prb_3_5_A_indp)
    prob_sh1_1_5_A_indps.append(prb_sh1_1_5_A_indp)
    prob_sh1_2_5_A_indps.append(prb_sh1_2_5_A_indp)
    prob_sh2_1_5_A_indps.append(prb_sh2_1_5_A_indp)
    prob_sh2_2_5_A_indps.append(prb_sh2_2_5_A_indp)
    prob_12_A_indps.append(prb_12_A_indp)
    prob_00_A_indps.append(prb_00_A_indp)


def ht_g_diff_avg_aggregator():
    ht_diffs = []
    date_ = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
    if len(date_) > 0:
        home_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
        away_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
        home_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:first-child')
        away_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:last-child')
        for m in range(DSCRM_H_A):
            try:
                if YEAR <= int(date_[m].text.split('.')[-1].strip()) < 90:
                    if home_x[m].text == home_teamx:
                        ht_diff = int(home_score[m].text) - int(away_score[m].text)
                        ht_diffs.append(ht_diff)
                    if away_x[m].text == home_teamx:
                        ht_diff = int(away_score[m].text) - int(home_score[m].text)
                        ht_diffs.append(ht_diff)
                else:
                    ht_diffs.append(0)
            except (ValueError, IndexError):
                ht_diffs.append(0)
        try:
            hts_mean = stats.mean(ht_diffs)
            ht_g_diff_avgs.append(round(hts_mean, 2))
        except stats.StatisticsError:
            ht_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))
    else:
        ht_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))


def at_g_diff_avg_aggregator():
    at_diffs = []
    date__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
    if len(date__) > 0:
        home_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__homeParticipant .h2h__participantInner')
        away_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__awayParticipant .h2h__participantInner')
        home_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:first-child')
        away_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:last-child')
        for m in range(DSCRM_H_A):
            try:
                if YEAR <= int(date__[m].text.split('.')[-1].strip()) < 90:
                    if away_x[m].text == away_teamx:
                        at_diff = int(away_score[m].text) - int(home_score[m].text)
                        at_diffs.append(at_diff)
                    if home_x[m].text == away_teamx:
                        at_diff = int(home_score[m].text) - int(away_score[m].text)
                        at_diffs.append(at_diff)
                else:
                    at_diffs.append(0)
            except (ValueError, IndexError):
                at_diffs.append(0)
        try:
            ats_mean = stats.mean(at_diffs)
            at_g_diff_avgs.append(round(ats_mean, 2))
        except stats.StatisticsError:
            at_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))
    else:
        at_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))


def bt_g_diff_avg_aggregator():
    bth_diffs = []
    bta_diffs = []
    date___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__date')
    if len(date___) > 0:
        home_x = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
        away_x = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
        home_score = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__result span:first-child')
        away_score = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__result span:last-child')
        for m in range(DSCRM_BT):
            try:
                if YEAR <= int(date___[m].text.split('.')[-1].strip()) < 90:
                    if home_x[m].text == home_teamx:
                        bth_diff = int(home_score[m].text) - int(away_score[m].text)
                        bth_diffs.append(bth_diff)
                    if away_x[m].text == home_teamx:
                        bth_diff = int(away_score[m].text) - int(home_score[m].text)
                        bth_diffs.append(bth_diff)
                    if away_x[m].text == away_teamx:
                        bta_diff = int(away_score[m].text) - int(home_score[m].text)
                        bta_diffs.append(bta_diff)
                    if home_x[m].text == away_teamx:
                        bta_diff = int(home_score[m].text) - int(away_score[m].text)
                        bta_diffs.append(bta_diff)
                else:
                    bth_diffs.append(0)
                    bta_diffs.append(0)
            except (ValueError, IndexError):
                bth_diffs.append(0)
                bta_diffs.append(0)
        try:
            bths_mean = stats.mean(bth_diffs)
            btas_mean = stats.mean(bta_diffs)
            bth_g_diff_avgs.append(round(bths_mean, 2))
            bta_g_diff_avgs.append(round(btas_mean, 2))
        except stats.StatisticsError:
            bth_g_diff_avgs_x = round(rdm.uniform(-2, 2), 2)
            bta_g_diff_avgs_x = -1 * bth_g_diff_avgs_x
            bth_g_diff_avgs.append(bth_g_diff_avgs_x)
            bta_g_diff_avgs.append(bta_g_diff_avgs_x)
    else:
        bth_g_diff_avgs_x = round(rdm.uniform(-2, 2), 2)
        bta_g_diff_avgs_x = -1 * bth_g_diff_avgs_x
        bth_g_diff_avgs.append(bth_g_diff_avgs_x)
        bta_g_diff_avgs.append(bta_g_diff_avgs_x)


def ht_g_avg_aggregator():
    ht_scores = []
    date_ = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
    if len(date_) > 0:
        home_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
        away_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
        home_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:first-child')
        away_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:last-child')
        for m in range(DSCRM_H_A):
            try:
                if YEAR <= int(date_[m].text.split('.')[-1].strip()) < 90:
                    if home_x[m].text == home_teamx:
                        ht_scores.append(int(home_score[m].text))
                    if away_x[m].text == home_teamx:
                        ht_scores.append(int(away_score[m].text))
                else:
                    ht_scores.append(0)
            except (ValueError, IndexError):
                ht_scores.append(0)
        try:
            hts_mean = stats.mean(ht_scores)
            ht_g_avgs.append(round(hts_mean, 2))
        except stats.StatisticsError:
            ht_g_avgs.append(round(rdm.uniform(0, 2), 2))
    else:
        ht_g_avgs.append(round(rdm.uniform(0, 2), 2))


def at_g_avg_aggregator():
    at_scores = []
    date__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
    if len(date__) > 0:
        home_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__homeParticipant .h2h__participantInner')
        away_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__awayParticipant .h2h__participantInner')
        home_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:first-child')
        away_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:last-child')
        for m in range(DSCRM_H_A):
            try:
                if YEAR <= int(date__[m].text.split('.')[-1].strip()) < 90:
                    if away_x[m].text == away_teamx:
                        at_scores.append(int(away_score[m].text))
                    if home_x[m].text == away_teamx:
                        at_scores.append(int(home_score[m].text))
                else:
                    at_scores.append(0)
            except (ValueError, IndexError):
                at_scores.append(0)
        try:
            ats_mean = stats.mean(at_scores)
            at_g_avgs.append(round(ats_mean, 2))
        except stats.StatisticsError:
            at_g_avgs.append(round(rdm.uniform(0, 2), 2))
    else:
        at_g_avgs.append(round(rdm.uniform(0, 2), 2))


def bt_g_avg_aggregator():
    bth_scores = []
    bta_scores = []
    date___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__date')
    if len(date___) > 0:
        home_x = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
        away_x = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
        home_score = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__result span:first-child')
        away_score = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__result span:last-child')
        for m in range(DSCRM_BT):
            try:
                if YEAR <= int(date___[m].text.split('.')[-1].strip()) < 90:
                    if home_x[m].text == home_teamx:
                        bth_scores.append(int(home_score[m].text))
                    if away_x[m].text == home_teamx:
                        bth_scores.append(int(away_score[m].text))
                    if away_x[m].text == away_teamx:
                        bta_scores.append(int(away_score[m].text))
                    if home_x[m].text == away_teamx:
                        bta_scores.append(int(home_score[m].text))
                else:
                    bth_scores.append(0)
                    bta_scores.append(0)
            except (ValueError, IndexError):
                bth_scores.append(0)
                bta_scores.append(0)
        try:
            bths_mean = stats.mean(bth_scores)
            btas_mean = stats.mean(bta_scores)
            bth_g_avgs.append(round(bths_mean, 2))
            bta_g_avgs.append(round(btas_mean, 2))
        except stats.StatisticsError:
            bth_g_avgs.append(round(rdm.uniform(0, 2), 2))
            bta_g_avgs.append(round(rdm.uniform(0, 2), 2))
    else:
        bth_g_avgs.append(round(rdm.uniform(0, 2), 2))
        bta_g_avgs.append(round(rdm.uniform(0, 2), 2))


def home_counter():
    games_count_home = 0
    try:
        suby1 = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row')
        for n in range(len(suby1)):
            dattee = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
            try:
                if int(dattee[n].text.split('.')[-1].strip()) >= YEAR:
                    games_count_home += 1
            except ValueError:
                print(f"Error at Count Home: {dattee[n].text}")
                if n + 1 != len(suby1):
                    games_count_home += 1
        home_nums_matches_played.append(games_count_home)
    except ElementNotInteractableException:
        home_nums_matches_played.append(0)
    except NoSuchElementException:
        home_nums_matches_played.append(0)


def away_counter():
    games_count_away = 0
    try:
        suby2 = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row')
        for n in range(len(suby2)):
            dattte = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
            try:
                if int(dattte[n].text.split('.')[-1].strip()) >= YEAR:
                    games_count_away += 1
            except ValueError:
                print(f"Error at Count Away: {dattte[n].text}")
                if n + 1 != len(suby2):
                    games_count_away += 1
        away_nums_matches_played.append(games_count_away)
    except ElementNotInteractableException:
        away_nums_matches_played.append(0)
    except NoSuchElementException:
        away_nums_matches_played.append(0)


def show_more_matches():
    status = 1
    shows = driver.find_elements(By.CSS_SELECTOR, '[class="h2h__showMore showMore"]')
    if len(shows) != 0:
        try:
            if len(shows) == 3:
                shows[0].click()
                sleep(0.1)
                shows[1].click()
                sleep(0.1)
                shows[2].click()
            elif len(shows) == 2:
                shows[0].click()
                sleep(0.1)
                shows[1].click()
            else:
                show = driver.find_element(By.CSS_SELECTOR, '[class="h2h__showMore showMore"]')
                show.click()
        except ElementClickInterceptedException:
            try:
                pass
            except ElementClickInterceptedException:
                pass
        except NoSuchElementException:
            pass
    else:
        status = 0

    return status


def data_break_zeroes1(home_pos_, away_pos_, z, ent1):
    while True:
        prb_HW_ = rdm.random()
        prb_AW_ = 1 - prb_HW_
        prb_12_ = 0.99
        prb_sh1_2_5_ = rdm.random()
        if prb_sh1_2_5_ >= 0.99:
            while True:
                prb_sh1_1_5_ = rdm.random()
                if prb_sh1_2_5_ >= prb_sh1_1_5_:
                    while True:
                        prb_sh2_2_5_ = rdm.random()
                        if prb_sh2_2_5_ >= 0.99:
                            while True:
                                prb_sh2_1_5_ = rdm.random()
                                if prb_sh2_2_5_ >= prb_sh2_1_5_:
                                    while True:
                                        prb_00_ = rdm.random()
                                        if prb_00_ >= 0.99:
                                            while True:
                                                prb_2_5_ = rdm.random()
                                                if prb_00_ >= prb_2_5_:
                                                    while True:
                                                        prb_3_5_ = rdm.random()
                                                        if prb_2_5_ >= prb_3_5_ and prb_3_5_ <= 0.01:
                                                            h2h_appender(prb_HW=prb_HW_, prb_AW=prb_AW_, prb_2_5=prb_2_5_, prb_3_5=prb_3_5_, prb_sh1_1_5=prb_sh1_1_5_,
                                                                         prb_sh1_2_5=prb_sh1_2_5_, prb_sh2_1_5=prb_sh2_1_5_, prb_sh2_2_5=prb_sh2_2_5_, prb_12=prb_12_, prb_00=prb_00_)
                                                            break
                                                    break
                                            break
                                    break
                            break
                    break
            break

    while True:
        prb_HW_H_indp_ = rdm.random()
        prb_AW_H_indp_ = 1 - prb_HW_H_indp_
        prb_12_H_indp_ = 0.99
        prb_sh1_2_5_H_indp_ = rdm.random()
        if prb_sh1_2_5_H_indp_ >= 0.99:
            while True:
                prb_sh1_1_5_H_indp_ = rdm.random()
                if prb_sh1_2_5_H_indp_ >= prb_sh1_1_5_H_indp_:
                    while True:
                        prb_sh2_2_5_H_indp_ = rdm.random()
                        if prb_sh2_2_5_H_indp_ >= 0.99:
                            while True:
                                prb_sh2_1_5_H_indp_ = rdm.random()
                                if prb_sh2_2_5_H_indp_ >= prb_sh2_1_5_H_indp_:
                                    while True:
                                        prb_00_H_indp_ = rdm.random()
                                        if prb_00_H_indp_ >= 0.99:
                                            while True:
                                                prb_2_5_H_indp_ = rdm.random()
                                                if prb_00_H_indp_ >= prb_2_5_H_indp_:
                                                    while True:
                                                        prb_3_5_H_indp_ = rdm.random()
                                                        if prb_2_5_H_indp_ >= prb_3_5_H_indp_ and prb_3_5_H_indp_ <= 0.01:
                                                            ht_indp_appender(prb_HW_H_indp=prb_HW_H_indp_, prb_AW_H_indp=prb_AW_H_indp_, prb_2_5_H_indp=prb_2_5_H_indp_,
                                                                             prb_3_5_H_indp=prb_3_5_H_indp_, prb_sh1_1_5_H_indp=prb_sh1_1_5_H_indp_,
                                                                             prb_sh1_2_5_H_indp=prb_sh1_2_5_H_indp_, prb_sh2_1_5_H_indp=prb_sh2_1_5_H_indp_,
                                                                             prb_sh2_2_5_H_indp=prb_sh2_2_5_H_indp_, prb_12_H_indp=prb_12_H_indp_, prb_00_H_indp=prb_00_H_indp_)
                                                            break
                                                    break
                                            break
                                    break
                            break
                    break
            break

    while True:
        prb_HW_A_indp_ = rdm.random()
        prb_AW_A_indp_ = 1 - prb_HW_A_indp_
        prb_12_A_indp_ = 0.99
        prb_sh1_2_5_A_indp_ = rdm.random()
        if prb_sh1_2_5_A_indp_ >= 0.99:
            while True:
                prb_sh1_1_5_A_indp_ = rdm.random()
                if prb_sh1_2_5_A_indp_ >= prb_sh1_1_5_A_indp_:
                    while True:
                        prb_sh2_2_5_A_indp_ = rdm.random()
                        if prb_sh2_2_5_A_indp_ >= 0.99:
                            while True:
                                prb_sh2_1_5_A_indp_ = rdm.random()
                                if prb_sh2_2_5_A_indp_ >= prb_sh2_1_5_A_indp_:
                                    while True:
                                        prb_00_A_indp_ = rdm.random()
                                        if prb_00_A_indp_ >= 0.99:
                                            while True:
                                                prb_2_5_A_indp_ = rdm.random()
                                                if prb_00_A_indp_ >= prb_2_5_A_indp_:
                                                    while True:
                                                        prb_3_5_A_indp_ = rdm.random()
                                                        if prb_2_5_A_indp_ >= prb_3_5_A_indp_ and prb_3_5_A_indp_ <= 0.01:
                                                            at_indp_appender(prb_HW_A_indp=prb_HW_A_indp_, prb_AW_A_indp=prb_AW_A_indp_, prb_2_5_A_indp=prb_2_5_A_indp_,
                                                                             prb_3_5_A_indp=prb_3_5_A_indp_, prb_sh1_1_5_A_indp=prb_sh1_1_5_A_indp_,
                                                                             prb_sh1_2_5_A_indp=prb_sh1_2_5_A_indp_, prb_sh2_1_5_A_indp=prb_sh2_1_5_A_indp_,
                                                                             prb_sh2_2_5_A_indp=prb_sh2_2_5_A_indp_, prb_12_A_indp=prb_12_A_indp_, prb_00_A_indp=prb_00_A_indp_)
                                                            break
                                                    break
                                            break
                                    break
                            break
                    break
            break

    FORM_CONFIGS = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
    bth_g_diff_avgs_z = round(rdm.uniform(-2, 2), 2)
    bta_g_diff_avgs_z = -1 * bth_g_diff_avgs_z
    home_nums_matches_played_z = rdm.randint(0, 20)
    away_nums_matches_played_z = home_nums_matches_played_z

    while True:
        h_form_W_z = rdm.choice(FORM_CONFIGS)
        h_form_L_z = rdm.choice(FORM_CONFIGS)
        h_form_D_z = rdm.choice(FORM_CONFIGS)
        a_form_W_z = rdm.choice(FORM_CONFIGS)
        a_form_L_z = rdm.choice(FORM_CONFIGS)
        a_form_D_z = rdm.choice(FORM_CONFIGS)
        if (h_form_W_z + h_form_L_z) == 1.0 and (a_form_W_z + a_form_L_z) == 1.0 and (h_form_D_z + a_form_D_z) == 0.0:
            h_form_W.append(h_form_W_z)
            h_form_D.append(h_form_D_z)
            h_form_L.append(h_form_L_z)
            a_form_W.append(a_form_W_z)
            a_form_D.append(a_form_D_z)
            a_form_L.append(a_form_L_z)
            break

    ht_g_avgs.append(round(rdm.uniform(0, 2), 2))
    ht_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))
    at_g_avgs.append(round(rdm.uniform(0, 2), 2))
    at_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))
    bth_g_avgs.append(round(rdm.uniform(0, 2), 2))
    bta_g_avgs.append(round(rdm.uniform(0, 2), 2))
    bth_g_diff_avgs.append(bth_g_diff_avgs_z)
    bta_g_diff_avgs.append(bta_g_diff_avgs_z)

    if ent1 < 10:
        home_nums_matches_played.append(home_nums_matches_played_z)
        away_nums_matches_played.append(away_nums_matches_played_z)
    try:
        match_times.append(sub_m_t[z])
    except (IndexError, NoSuchElementException, StaleElementReferenceException):
        match_times.append("XX:XX")


def data_break_zeroes2(home_pos_, away_pos_, z):
    while True:
        prb_HW_ = rdm.random()
        prb_AW_ = 1 - prb_HW_
        prb_12_ = 0.99
        prb_sh1_2_5_ = rdm.random()
        if prb_sh1_2_5_ >= 0.99:
            while True:
                prb_sh1_1_5_ = rdm.random()
                if prb_sh1_2_5_ >= prb_sh1_1_5_:
                    while True:
                        prb_sh2_2_5_ = rdm.random()
                        if prb_sh2_2_5_ >= 0.99:
                            while True:
                                prb_sh2_1_5_ = rdm.random()
                                if prb_sh2_2_5_ >= prb_sh2_1_5_:
                                    while True:
                                        prb_00_ = rdm.random()
                                        if prb_00_ >= 0.99:
                                            while True:
                                                prb_2_5_ = rdm.random()
                                                if prb_00_ >= prb_2_5_:
                                                    while True:
                                                        prb_3_5_ = rdm.random()
                                                        if prb_2_5_ >= prb_3_5_ and prb_3_5_ <= 0.01:
                                                            h2h_appender(prb_HW=prb_HW_, prb_AW=prb_AW_, prb_2_5=prb_2_5_, prb_3_5=prb_3_5_, prb_sh1_1_5=prb_sh1_1_5_,
                                                                         prb_sh1_2_5=prb_sh1_2_5_, prb_sh2_1_5=prb_sh2_1_5_, prb_sh2_2_5=prb_sh2_2_5_, prb_12=prb_12_, prb_00=prb_00_)
                                                            break
                                                    break
                                            break
                                    break
                            break
                    break
            break

    while True:
        prb_HW_H_indp_ = rdm.random()
        prb_AW_H_indp_ = 1 - prb_HW_H_indp_
        prb_12_H_indp_ = 0.99
        prb_sh1_2_5_H_indp_ = rdm.random()
        if prb_sh1_2_5_H_indp_ >= 0.99:
            while True:
                prb_sh1_1_5_H_indp_ = rdm.random()
                if prb_sh1_2_5_H_indp_ >= prb_sh1_1_5_H_indp_:
                    while True:
                        prb_sh2_2_5_H_indp_ = rdm.random()
                        if prb_sh2_2_5_H_indp_ >= 0.99:
                            while True:
                                prb_sh2_1_5_H_indp_ = rdm.random()
                                if prb_sh2_2_5_H_indp_ >= prb_sh2_1_5_H_indp_:
                                    while True:
                                        prb_00_H_indp_ = rdm.random()
                                        if prb_00_H_indp_ >= 0.99:
                                            while True:
                                                prb_2_5_H_indp_ = rdm.random()
                                                if prb_00_H_indp_ >= prb_2_5_H_indp_:
                                                    while True:
                                                        prb_3_5_H_indp_ = rdm.random()
                                                        if prb_2_5_H_indp_ >= prb_3_5_H_indp_ and prb_3_5_H_indp_ <= 0.01:
                                                            ht_indp_appender(prb_HW_H_indp=prb_HW_H_indp_, prb_AW_H_indp=prb_AW_H_indp_, prb_2_5_H_indp=prb_2_5_H_indp_,
                                                                             prb_3_5_H_indp=prb_3_5_H_indp_, prb_sh1_1_5_H_indp=prb_sh1_1_5_H_indp_,
                                                                             prb_sh1_2_5_H_indp=prb_sh1_2_5_H_indp_, prb_sh2_1_5_H_indp=prb_sh2_1_5_H_indp_,
                                                                             prb_sh2_2_5_H_indp=prb_sh2_2_5_H_indp_, prb_12_H_indp=prb_12_H_indp_, prb_00_H_indp=prb_00_H_indp_)
                                                            break
                                                    break
                                            break
                                    break
                            break
                    break
            break

    while True:
        prb_HW_A_indp_ = rdm.random()
        prb_AW_A_indp_ = 1 - prb_HW_A_indp_
        prb_12_A_indp_ = 0.99
        prb_sh1_2_5_A_indp_ = rdm.random()
        if prb_sh1_2_5_A_indp_ >= 0.99:
            while True:
                prb_sh1_1_5_A_indp_ = rdm.random()
                if prb_sh1_2_5_A_indp_ >= prb_sh1_1_5_A_indp_:
                    while True:
                        prb_sh2_2_5_A_indp_ = rdm.random()
                        if prb_sh2_2_5_A_indp_ >= 0.99:
                            while True:
                                prb_sh2_1_5_A_indp_ = rdm.random()
                                if prb_sh2_2_5_A_indp_ >= prb_sh2_1_5_A_indp_:
                                    while True:
                                        prb_00_A_indp_ = rdm.random()
                                        if prb_00_A_indp_ >= 0.99:
                                            while True:
                                                prb_2_5_A_indp_ = rdm.random()
                                                if prb_00_A_indp_ >= prb_2_5_A_indp_:
                                                    while True:
                                                        prb_3_5_A_indp_ = rdm.random()
                                                        if prb_2_5_A_indp_ >= prb_3_5_A_indp_ and prb_3_5_A_indp_ <= 0.01:
                                                            at_indp_appender(prb_HW_A_indp=prb_HW_A_indp_, prb_AW_A_indp=prb_AW_A_indp_, prb_2_5_A_indp=prb_2_5_A_indp_,
                                                                             prb_3_5_A_indp=prb_3_5_A_indp_, prb_sh1_1_5_A_indp=prb_sh1_1_5_A_indp_,
                                                                             prb_sh1_2_5_A_indp=prb_sh1_2_5_A_indp_, prb_sh2_1_5_A_indp=prb_sh2_1_5_A_indp_,
                                                                             prb_sh2_2_5_A_indp=prb_sh2_2_5_A_indp_, prb_12_A_indp=prb_12_A_indp_, prb_00_A_indp=prb_00_A_indp_)
                                                            break
                                                    break
                                            break
                                    break
                            break
                    break
            break

    FORM_CONFIGS = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
    bth_g_diff_avgs_z = round(rdm.uniform(-2, 2), 2)
    bta_g_diff_avgs_z = -1 * bth_g_diff_avgs_z
    home_nums_matches_played_z = rdm.randint(0, 20)
    away_nums_matches_played_z = home_nums_matches_played_z

    while True:
        h_form_W_z = rdm.choice(FORM_CONFIGS)
        h_form_L_z = rdm.choice(FORM_CONFIGS)
        h_form_D_z = rdm.choice(FORM_CONFIGS)
        a_form_W_z = rdm.choice(FORM_CONFIGS)
        a_form_L_z = rdm.choice(FORM_CONFIGS)
        a_form_D_z = rdm.choice(FORM_CONFIGS)
        if (h_form_W_z + h_form_L_z) == 1.0 and (a_form_W_z + a_form_L_z) == 1.0 and (h_form_D_z + a_form_D_z) == 0.0:
            h_form_W.append(h_form_W_z)
            h_form_D.append(h_form_D_z)
            h_form_L.append(h_form_L_z)
            a_form_W.append(a_form_W_z)
            a_form_D.append(a_form_D_z)
            a_form_L.append(a_form_L_z)
            break

    ht_g_avgs.append(round(rdm.uniform(0, 2), 2))
    ht_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))
    at_g_avgs.append(round(rdm.uniform(0, 2), 2))
    at_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))
    bth_g_avgs.append(round(rdm.uniform(0, 2), 2))
    bta_g_avgs.append(round(rdm.uniform(0, 2), 2))
    bth_g_diff_avgs.append(bth_g_diff_avgs_z)
    bta_g_diff_avgs.append(bta_g_diff_avgs_z)
    home_nums_matches_played.append(home_nums_matches_played_z)
    away_nums_matches_played.append(away_nums_matches_played_z)
    try:
        match_times.append(sub_m_t[z])
    except (IndexError, NoSuchElementException, StaleElementReferenceException):
        match_times.append("XX:XX")
    append_zeroes(home_pos=home_pos_, away_pos=away_pos_)


def home_form_checker(home_teamk):
    def h_f_zero():
        FORM_CONFIGS = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
        while True:
            h_form_W_v = rdm.choice(FORM_CONFIGS)
            h_form_L_v = rdm.choice(FORM_CONFIGS)
            h_form_D_v = rdm.choice(FORM_CONFIGS)
            if (h_form_W_v + h_form_L_v) == 1.0 and h_form_D_v == 0.0:
                h_form_W.append(h_form_W_v)
                h_form_D.append(h_form_D_v)
                h_form_L.append(h_form_L_v)
                break

    count_HW_form = 0
    count_HD_form = 0
    try:
        subx1 = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row')
        if len(subx1) >= FORM_COUNT:
            dssc = 0
            datte = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
            homme_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
            awway_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
            homme_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:first-child')
            awway_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:last-child')
            for k in range(FORM_COUNT):
                try:
                    if int(datte[k].text.split('.')[-1].strip()) >= YEAR:
                        if (int(homme_score[k].text) > int(awway_score[k].text)) and (str(homme_x[k].text) == str(home_teamk)):
                            count_HW_form += 1
                        if (int(awway_score[k].text) > int(homme_score[k].text)) and (str(awway_x[k].text) == str(home_teamk)):
                            count_HW_form += 1
                        if int(homme_score[k].text) == int(awway_score[k].text):
                            count_HD_form += 1
                        dssc += 1
                    else:
                        print(f"Home Form Year Unaccepted: {int(datte[k].text.split('.')[-1].strip())}")
                        dssc += 1
                except ValueError:
                    print(f"Value Error at FORM Home : {datte[k].text} | {homme_x[k].text} vs {awway_x[k].text}")
                    print(f"ScoreH - {homme_score[k].text} : {awway_score[k].text}")
                    count_HD_form += 1
                    dssc += 1
            if dssc >= FORM_COUNT:
                try:
                    H_form_W = float(count_HW_form / dssc)
                    H_form_D = float(count_HD_form / dssc)
                    H_form_L = float(1 - (H_form_W + H_form_D))
                    h_form_W.append(round(H_form_W, 1))
                    h_form_D.append(round(H_form_D, 1))
                    h_form_L.append(round(H_form_L, 1))
                except ZeroDivisionError:
                    h_f_zero()
            else:
                h_f_zero()
        else:
            h_f_zero()
    except ElementNotInteractableException:
        h_f_zero()


def away_form_checker(away_teamk):
    def a_f_zero():
        FORM_CONFIGS = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
        while True:
            a_form_W_v = rdm.choice(FORM_CONFIGS)
            a_form_L_v = rdm.choice(FORM_CONFIGS)
            a_form_D_v = rdm.choice(FORM_CONFIGS)
            if (a_form_W_v + a_form_L_v) == 1.0 and a_form_D_v == 0.0:
                a_form_W.append(a_form_W_v)
                a_form_D.append(a_form_D_v)
                a_form_L.append(a_form_L_v)
                break

    count_AW_form = 0
    count_AD_form = 0
    try:
        subx2 = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row')
        if len(subx2) >= FORM_COUNT:
            dssc = 0
            datte = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
            homme_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__homeParticipant .h2h__participantInner')
            awway_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__awayParticipant .h2h__participantInner')
            homme_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:first-child')
            awway_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:last-child')
            for n in range(FORM_COUNT):
                try:
                    if int(datte[n].text.split('.')[-1].strip()) >= YEAR:
                        if (int(homme_score[n].text) > int(awway_score[n].text)) and (str(homme_x[n].text) == str(away_teamk)):
                            count_AW_form += 1
                        if (int(awway_score[n].text) > int(homme_score[n].text)) and (str(awway_x[n].text) == str(away_teamk)):
                            count_AW_form += 1
                        if int(homme_score[n].text) == int(awway_score[n].text):
                            count_AD_form += 1
                        dssc += 1
                    else:
                        print(f"Away Form Year Unaccepted: {int(datte[n].text.split('.')[-1].strip())}")
                        dssc += 1
                except ValueError:
                    print(f"Error at FORM Away: {datte[n].text} | {homme_x[n].text} vs {awway_x[n].text}")
                    print(f"ScoreA - {homme_score[n].text} : {awway_score[n].text}")
                    count_AD_form += 1
                    dssc += 1
            if dssc >= FORM_COUNT:
                try:
                    A_form_W = float(count_AW_form / dssc)
                    A_form_D = float(count_AD_form / dssc)
                    A_form_L = float(1 - (A_form_W + A_form_D))
                    a_form_W.append(round(A_form_W, 1))
                    a_form_D.append(round(A_form_D, 1))
                    a_form_L.append(round(A_form_L, 1))
                except ZeroDivisionError:
                    a_f_zero()
            else:
                a_f_zero()
        else:
            a_f_zero()
    except ElementNotInteractableException:
        a_f_zero()


def odds_checker():
    def zeroth_odds_break(home_aug_odd_o, away_aug_odd_o, CLEARANCE_o):
        if 0 < home_aug_odd_o < 1 and 0 < away_aug_odd_o < 1:
            _1HWS.append(home_aug_odd_o)
            _2AWS.append(away_aug_odd_o)
        else:
            home_aug_odd_o = rdm.random()
            away_aug_odd_o = 1 - home_aug_odd_o
            odds_diff = abs(home_aug_odd_o - away_aug_odd_o)
            if odds_diff < CLEARANCE_o:
                home_aug_odd_o = rdm.random() * rdm.random()
                away_aug_odd_o = 1 - home_aug_odd_o
                odds_diff = abs(home_aug_odd_o - away_aug_odd_o)
                if odds_diff < CLEARANCE_o:
                    home_aug_odd_o = math.sqrt(rdm.random() * rdm.random())
                    away_aug_odd_o = 1 - home_aug_odd_o
                    odds_diff = abs(home_aug_odd_o - away_aug_odd_o)
                    if odds_diff < CLEARANCE_o:
                        home_aug_odd_o = 0.5 * (rdm.random() + rdm.random())
                        away_aug_odd_o = 1 - home_aug_odd_o
                        odds_diff = abs(home_aug_odd_o - away_aug_odd_o)
                        if odds_diff < CLEARANCE_o:
                            home_aug_odd_o = math.sqrt(0.5 * (rdm.random() + rdm.random()))
                            away_aug_odd_o = 1 - home_aug_odd_o
            _1HWS.append(home_aug_odd_o)
            _2AWS.append(away_aug_odd_o)

    def odds_augment(odds_home, odds_away):
        CLEARANCE = 0.7
        CLEARANCE_ = 0.875
        while True:
            try:
                home_aug_odd = 1 / float(odds_home)
                away_aug_odd = 1 / float(odds_away)
                odds_diff = abs(home_aug_odd - away_aug_odd)
                if odds_diff < CLEARANCE:
                    home_aug_odd = (1 - (float(odds_home) / (float(odds_home) + float(odds_away)))) * rdm.random()
                    away_aug_odd = (1 - (float(odds_away) / (float(odds_home) + float(odds_away)))) * rdm.random()
                    odds_diff = abs(home_aug_odd - away_aug_odd)
                    if odds_diff < CLEARANCE:
                        home_aug_odd = math.sqrt((1 - (float(odds_home) / (float(odds_home) + float(odds_away)))) * rdm.random())
                        away_aug_odd = math.sqrt((1 - (float(odds_away) / (float(odds_home) + float(odds_away)))) * rdm.random())
                        odds_diff = abs(home_aug_odd - away_aug_odd)
                        if odds_diff < CLEARANCE:
                            home_aug_odd = 0.5 * ((1 - (float(odds_home) / (float(odds_home) + float(odds_away)))) + rdm.random())
                            away_aug_odd = 0.5 * ((1 - (float(odds_away) / (float(odds_home) + float(odds_away)))) + rdm.random())
                            odds_diff = abs(home_aug_odd - away_aug_odd)
                            if odds_diff < CLEARANCE:
                                home_aug_odd = math.sqrt(0.5 * ((1 - (float(odds_home) / (float(odds_home) + float(odds_away)))) + rdm.random()))
                                away_aug_odd = math.sqrt(0.5 * ((1 - (float(odds_away) / (float(odds_home) + float(odds_away)))) + rdm.random()))
                                odds_diff = abs(home_aug_odd - away_aug_odd)
                                if odds_diff < CLEARANCE:
                                    home_aug_odd = 1 - ((float(odds_home) / (float(odds_home) + float(odds_away))) * rdm.random())
                                    away_aug_odd = 1 - ((float(odds_away) / (float(odds_home) + float(odds_away))) * rdm.random())
                                    odds_diff = abs(home_aug_odd - away_aug_odd)
                                    if odds_diff < CLEARANCE:
                                        home_aug_odd = 1 - math.sqrt((float(odds_home) / (float(odds_home) + float(odds_away))) * rdm.random())
                                        away_aug_odd = 1 - math.sqrt((float(odds_away) / (float(odds_home) + float(odds_away))) * rdm.random())
                                        odds_diff = abs(home_aug_odd - away_aug_odd)
                                        if odds_diff < CLEARANCE:
                                            home_aug_odd = 1 - 0.5 * ((float(odds_home) / (float(odds_home) + float(odds_away))) + rdm.random())
                                            away_aug_odd = 1 - 0.5 * ((float(odds_away) / (float(odds_home) + float(odds_away))) + rdm.random())
                                            odds_diff = abs(home_aug_odd - away_aug_odd)
                                            if odds_diff < CLEARANCE:
                                                home_aug_odd = 1 - math.sqrt(0.5 * ((float(odds_home) / (float(odds_home) + float(odds_away))) + rdm.random()))
                                                away_aug_odd = 1 - math.sqrt(0.5 * ((float(odds_away) / (float(odds_home) + float(odds_away))) + rdm.random()))
                                                odds_diff = abs(home_aug_odd - away_aug_odd)
                                                if odds_diff < CLEARANCE:
                                                    zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE)
                                                    break
                                            else:
                                                zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE)
                                                break
                                        else:
                                            zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE)
                                            break
                                    else:
                                        zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE)
                                        break
                                else:
                                    zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE)
                                    break
                            else:
                                zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE)
                                break
                        else:
                            zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE)
                            break
                    else:
                        zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE)
                        break
                else:
                    zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE)
                    break
            except ZeroDivisionError:
                home_aug_odd = rdm.random()
                away_aug_odd = 1 - home_aug_odd
                odds_diff = abs(home_aug_odd - away_aug_odd)
                if odds_diff < CLEARANCE_:
                    home_aug_odd = rdm.random() * rdm.random()
                    away_aug_odd = 1 - home_aug_odd
                    odds_diff = abs(home_aug_odd - away_aug_odd)
                    if odds_diff < CLEARANCE_:
                        home_aug_odd = math.sqrt(rdm.random() * rdm.random())
                        away_aug_odd = 1 - home_aug_odd
                        odds_diff = abs(home_aug_odd - away_aug_odd)
                        if odds_diff < CLEARANCE_:
                            home_aug_odd = 0.5 * (rdm.random() + rdm.random())
                            away_aug_odd = 1 - home_aug_odd
                            odds_diff = abs(home_aug_odd - away_aug_odd)
                            if odds_diff < CLEARANCE_:
                                home_aug_odd = math.sqrt(0.5 * (rdm.random() + rdm.random()))
                                away_aug_odd = 1 - home_aug_odd
                                odds_diff = abs(home_aug_odd - away_aug_odd)
                                if odds_diff < CLEARANCE_:
                                    zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE_)
                                    break
                            else:
                                zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE_)
                                break
                        else:
                            zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE_)
                            break
                    else:
                        zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE_)
                        break
                else:
                    zeroth_odds_break(home_aug_odd_o=home_aug_odd, away_aug_odd_o=away_aug_odd, CLEARANCE_o=CLEARANCE_)
                    break
    try:
        driver.find_element(By.LINK_TEXT, "ODDS").click()
        try:
            _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
            _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
            odds_augment(odds_home=_1HW, odds_away=_2AW)
            _12S.append(0.9998)
        except (NoSuchElementException, IndexError):
            try:
                _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                odds_augment(odds_home=_1HW, odds_away=_2AW)
                _12S.append(0.9998)
            except (ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, IndexError):
                try:
                    driver.refresh()
                    sleep(0.5)
                    _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                    _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                    odds_augment(odds_home=_1HW, odds_away=_2AW)
                    _12S.append(0.9998)
                except (ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, IndexError, StaleElementReferenceException):
                    while True:
                        _1HW_ = rdm.random()
                        _2AW_ = rdm.random()
                        if (_1HW_ + _2AW_) <= 1:
                            _1HW = 1 / _1HW_
                            _2AW = 1 / _2AW_
                            odds_augment(odds_home=_1HW, odds_away=_2AW)
                            break
                    _12S.append(0.9998)

        try:
            try:
                driver.find_element(By.LINK_TEXT, "AH").click()
            except (ElementClickInterceptedException, ElementNotInteractableException):
                pass
            ahl = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds')
            for y in range(len(ahl)):
                try:
                    id_sh_1_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_sh_1_5 == "+1.5":
                        OVER_sh1_1_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_sh1_1_5_S.append(1 / float(OVER_sh1_1_5))
                        OVER_sh2_1_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                        OVER_sh2_1_5_S.append(1 / float(OVER_sh2_1_5))
                        break
                    if y == (len(ahl) - 1):
                        OVER_sh1_1_5_S.append(rdm.random())
                        OVER_sh2_1_5_S.append(rdm.random())
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_sh1_1_5_S.append(rdm.random())
                    OVER_sh2_1_5_S.append(rdm.random())
            while True:
                OVER_sh1_2_5 = rdm.random()
                OVER_sh2_2_5 = rdm.random()
                if OVER_sh1_2_5 >= 0.99 and OVER_sh2_2_5 >= 0.99:
                    OVER_sh1_2_5_S.append(OVER_sh1_2_5)
                    OVER_sh2_2_5_S.append(OVER_sh2_2_5)
                    break
        except (NoSuchElementException, IndexError,  StaleElementReferenceException,
                ElementClickInterceptedException, ElementNotInteractableException):
            while True:
                OVER_sh1_2_5 = rdm.random()
                OVER_sh2_2_5 = rdm.random()
                if OVER_sh1_2_5 >= 0.99 and OVER_sh2_2_5 >= 0.99:
                    OVER_sh1_2_5_S.append(OVER_sh1_2_5)
                    OVER_sh2_2_5_S.append(OVER_sh2_2_5)
                    while True:
                        OVER_sh1_1_5 = rdm.random()
                        OVER_sh2_1_5 = rdm.random()
                        if OVER_sh1_2_5 >= OVER_sh1_1_5 and OVER_sh2_2_5 >= OVER_sh2_1_5:
                            OVER_sh1_1_5_S.append(OVER_sh1_1_5)
                            OVER_sh2_1_5_S.append(OVER_sh2_1_5)
                            break
                    break

        while True:
            OVER_3_5 = rdm.random()
            if OVER_3_5 <= 0.01:
                OVER_3_5_S.append(OVER_3_5)
                while True:
                    OVER_00 = rdm.random()
                    if OVER_00 >= 0.99:
                        OVER_00_S.append(OVER_00)
                        while True:
                            OVER_2_5 = rdm.random()
                            if OVER_00 >= OVER_2_5 > OVER_3_5:
                                OVER_2_5_S.append(OVER_2_5)
                                break
                        break
                break
    except (NoSuchElementException, IndexError, ElementNotInteractableException,
            ElementClickInterceptedException, StaleElementReferenceException):
        while True:
            CLEARANCE__ = 0.875
            home_aug_odd_ = rdm.random()
            away_aug_odd_ = 1 - home_aug_odd_
            odds_diff_ = abs(home_aug_odd_ - away_aug_odd_)
            if odds_diff_ < CLEARANCE__:
                home_aug_odd_ = rdm.random() * rdm.random()
                away_aug_odd_ = 1 - home_aug_odd_
                odds_diff_ = abs(home_aug_odd_ - away_aug_odd_)
                if odds_diff_ < CLEARANCE__:
                    home_aug_odd_ = math.sqrt(rdm.random() * rdm.random())
                    away_aug_odd_ = 1 - home_aug_odd_
                    odds_diff_ = abs(home_aug_odd_ - away_aug_odd_)
                    if odds_diff_ < CLEARANCE__:
                        home_aug_odd_ = 0.5 * (rdm.random() + rdm.random())
                        away_aug_odd_ = 1 - home_aug_odd_
                        odds_diff_ = abs(home_aug_odd_ - away_aug_odd_)
                        if odds_diff_ < CLEARANCE__:
                            home_aug_odd_ = math.sqrt(0.5 * (rdm.random() + rdm.random()))
                            away_aug_odd_ = 1 - home_aug_odd_
                            odds_diff_ = abs(home_aug_odd_ - away_aug_odd_)
                            if odds_diff_ < CLEARANCE__:
                                zeroth_odds_break(home_aug_odd_o=home_aug_odd_, away_aug_odd_o=away_aug_odd_, CLEARANCE_o=CLEARANCE__)
                                break
                        else:
                            zeroth_odds_break(home_aug_odd_o=home_aug_odd_, away_aug_odd_o=away_aug_odd_, CLEARANCE_o=CLEARANCE__)
                            break
                    else:
                        zeroth_odds_break(home_aug_odd_o=home_aug_odd_, away_aug_odd_o=away_aug_odd_, CLEARANCE_o=CLEARANCE__)
                        break
                else:
                    zeroth_odds_break(home_aug_odd_o=home_aug_odd_, away_aug_odd_o=away_aug_odd_, CLEARANCE_o=CLEARANCE__)
                    break
            else:
                zeroth_odds_break(home_aug_odd_o=home_aug_odd_, away_aug_odd_o=away_aug_odd_, CLEARANCE_o=CLEARANCE__)
                break

        while True:
            OVER_sh1_2_5 = rdm.random()
            OVER_sh2_2_5 = rdm.random()
            OVER_3_5 = rdm.random()
            _12_ = 0.9998
            if OVER_sh1_2_5 >= 0.99 and OVER_sh2_2_5 >= 0.99 and OVER_3_5 <= 0.01:
                OVER_sh1_2_5_S.append(OVER_sh1_2_5)
                OVER_sh2_2_5_S.append(OVER_sh2_2_5)
                OVER_3_5_S.append(OVER_3_5)
                _12S.append(_12_)
                while True:
                    OVER_sh1_1_5 = rdm.random()
                    OVER_sh2_1_5 = rdm.random()
                    if OVER_sh1_2_5 >= OVER_sh1_1_5 and OVER_sh2_2_5 >= OVER_sh2_1_5:
                        OVER_sh1_1_5_S.append(OVER_sh1_1_5)
                        OVER_sh2_1_5_S.append(OVER_sh2_1_5)
                        while True:
                            OVER_00 = rdm.random()
                            if OVER_00 >= 0.99:
                                OVER_00_S.append(OVER_00)
                                while True:
                                    OVER_2_5 = rdm.random()
                                    if OVER_00 >= OVER_2_5 > OVER_3_5:
                                        OVER_2_5_S.append(OVER_2_5)
                                        break
                                break
                        break
                break


def writer(w, A, B, C, data):
    data.write(f"{countries[w]}|{leagues[w]}|{home_teams[w]}|{away_teams[w]}|{home_positions[w]}|"
               f"{away_positions[w]}|{home_nums_matches_played[w]}|{away_nums_matches_played[w]}|{home_points[w]}|"
               f"{away_points[w]}|{h_form_W[w]}|{h_form_D[w]}|{h_form_L[w]}|{a_form_W[w]}|{a_form_D[w]}|{a_form_L[w]}|"
               f"{ht_g_avgs[w]}|{at_g_avgs[w]}|{bth_g_avgs[w]}|{bta_g_avgs[w]}|{ht_g_diff_avgs[w]}|{at_g_diff_avgs[w]}|{bth_g_diff_avgs[w]}|{bta_g_diff_avgs[w]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[w]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[w]}|"
               f"{OUTCOMES[2]}:-{bayesian_2_5_d[w]}|{OUTCOMES[3]}:-{bayesian_3_5_d[w]}|"
               f"{OUTCOMES[4]}:-{bayesian_sh1_1_5_d[w]}|{OUTCOMES[5]}:-{bayesian_sh1_2_5_d[w]}|"
               f"{OUTCOMES[6]}:-{bayesian_sh2_1_5_d[w]}|{OUTCOMES[7]}:-{bayesian_sh2_2_5_d[w]}|{OUTCOMES[8]}:-{bayesian_12_d[w]}|"
               f"{match_times[w]}|{sport}|{C}_{A}_{B}|{set_date_s_size()[0]}\n")


def writer1(y, F, G, H, J, data):
    data.write(f"{countries[y]}|{leagues[y]}|{home_teams[y]}|{away_teams[y]}|{home_positions[y]}|"
               f"{away_positions[y]}|{home_nums_matches_played[y]}|{away_nums_matches_played[y]}|{home_points[y]}|"
               f"{away_points[y]}|{h_form_W[y]}|{h_form_D[y]}|{h_form_L[y]}|{a_form_W[y]}|{a_form_D[y]}|{a_form_L[y]}|"
               f"{ht_g_avgs[y]}|{at_g_avgs[y]}|{bth_g_avgs[y]}|{bta_g_avgs[y]}|{ht_g_diff_avgs[y]}|{at_g_diff_avgs[y]}|{bth_g_diff_avgs[y]}|{bta_g_diff_avgs[y]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[y]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[y]}|"
               f"{OUTCOMES[2]}:-{bayesian_2_5_d[y]}|{OUTCOMES[3]}:-{bayesian_3_5_d[y]}|"
               f"{OUTCOMES[4]}:-{bayesian_sh1_1_5_d[y]}|{OUTCOMES[5]}:-{bayesian_sh1_2_5_d[y]}|"
               f"{OUTCOMES[6]}:-{bayesian_sh2_1_5_d[y]}|{OUTCOMES[7]}:-{bayesian_sh2_2_5_d[y]}|{OUTCOMES[8]}:-{bayesian_12_d[y]}|"
               f"{match_times[y]}|{sport}|{J}_{F}_{G}_{H}|{set_date_s_size()[0]}\n")


def writer2(z, K, L, M, N, P, data):
    data.write(f"{countries[z]}|{leagues[z]}|{home_teams[z]}|{away_teams[z]}|{home_positions[z]}|"
               f"{away_positions[z]}|{home_nums_matches_played[z]}|{away_nums_matches_played[z]}|{home_points[z]}|"
               f"{away_points[z]}|{h_form_W[z]}|{h_form_D[z]}|{h_form_L[z]}|{a_form_W[z]}|{a_form_D[z]}|{a_form_L[z]}|"
               f"{ht_g_avgs[z]}|{at_g_avgs[z]}|{bth_g_avgs[z]}|{bta_g_avgs[z]}|{ht_g_diff_avgs[z]}|{at_g_diff_avgs[z]}|{bth_g_diff_avgs[z]}|{bta_g_diff_avgs[z]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[z]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[z]}|"
               f"{OUTCOMES[2]}:-{bayesian_2_5_d[z]}|{OUTCOMES[3]}:-{bayesian_3_5_d[z]}|"
               f"{OUTCOMES[4]}:-{bayesian_sh1_1_5_d[z]}|{OUTCOMES[5]}:-{bayesian_sh1_2_5_d[z]}|"
               f"{OUTCOMES[6]}:-{bayesian_sh2_1_5_d[z]}|{OUTCOMES[7]}:-{bayesian_sh2_2_5_d[z]}|{OUTCOMES[8]}:-{bayesian_12_d[z]}|"
               f"{match_times[z]}|{sport}|{P}_{K}_{L}_{M}_{N}|{set_date_s_size()[0]}\n")


def baye_appender(baye_HW, baye_AW, baye_2_5, baye_3_5, baye_sh1_1_5, baye_sh1_2_5, baye_sh2_1_5,
                  baye_sh2_2_5, baye_12, baye_00):
    bayesian_home_Win_d.append(round((float(baye_HW)), 4))
    bayesian_away_Win_d.append(round((float(baye_AW)), 4))
    bayesian_2_5_d.append(round((float(baye_2_5)), 4))
    bayesian_3_5_d.append(round((float(baye_3_5)), 4))
    bayesian_sh1_1_5_d.append(round((float(baye_sh1_1_5)), 4))
    bayesian_sh1_2_5_d.append(round((float(baye_sh1_2_5)), 4))
    bayesian_sh2_1_5_d.append(round((float(baye_sh2_1_5)), 4))
    bayesian_sh2_2_5_d.append(round((float(baye_sh2_2_5)), 4))
    bayesian_12_d.append(round((float(baye_12)), 4))
    bayesian_00_d.append(round((float(baye_00)), 4))


def writer_alt_xlr_(w, A, B, C, data):
    data.write(f"{countries[w]}|{leagues[w]}|{home_teams[w]}|{away_teams[w]}|{home_positions[w]}|"
               f"{away_positions[w]}|{home_nums_matches_played[w]}|{away_nums_matches_played[w]}|{home_points[w]}|"
               f"{away_points[w]}|{h_form_W[w]}|{h_form_D[w]}|{h_form_L[w]}|{a_form_W[w]}|{a_form_D[w]}|{a_form_L[w]}|"
               f"{ht_g_avgs[w]}|{at_g_avgs[w]}|{bth_g_avgs[w]}|{bta_g_avgs[w]}|{ht_g_diff_avgs[w]}|{at_g_diff_avgs[w]}|{bth_g_diff_avgs[w]}|{bta_g_diff_avgs[w]}|"
               f"{OUTCOMES_ALT_XLR[0]}:-{bayesian_home_Win_d[w]}|{OUTCOMES_ALT_XLR[1]}:-{bayesian_away_Win_d[w]}|"
               f"{OUTCOMES_ALT_XLR[2]}:-{bayesian_12_d[w]}|"
               f"{match_times[w]}|{sport}|{C}_{A}_{B}|{set_date_s_size()[0]}\n")


def writer_alt_xlr_1(y, F, G, H, J, data):
    data.write(f"{countries[y]}|{leagues[y]}|{home_teams[y]}|{away_teams[y]}|{home_positions[y]}|"
               f"{away_positions[y]}|{home_nums_matches_played[y]}|{away_nums_matches_played[y]}|{home_points[y]}|"
               f"{away_points[y]}|{h_form_W[y]}|{h_form_D[y]}|{h_form_L[y]}|{a_form_W[y]}|{a_form_D[y]}|{a_form_L[y]}|"
               f"{ht_g_avgs[y]}|{at_g_avgs[y]}|{bth_g_avgs[y]}|{bta_g_avgs[y]}|{ht_g_diff_avgs[y]}|{at_g_diff_avgs[y]}|{bth_g_diff_avgs[y]}|{bta_g_diff_avgs[y]}|"
               f"{OUTCOMES_ALT_XLR[0]}:-{bayesian_home_Win_d[y]}|{OUTCOMES_ALT_XLR[1]}:-{bayesian_away_Win_d[y]}|"
               f"{OUTCOMES_ALT_XLR[2]}:-{bayesian_12_d[y]}|"
               f"{match_times[y]}|{sport}|{J}_{F}_{G}_{H}|{set_date_s_size()[0]}\n")


def writer_alt_xlr_2(z, K, L, M, N, P, data):
    data.write(f"{countries[z]}|{leagues[z]}|{home_teams[z]}|{away_teams[z]}|{home_positions[z]}|"
               f"{away_positions[z]}|{home_nums_matches_played[z]}|{away_nums_matches_played[z]}|{home_points[z]}|"
               f"{away_points[z]}|{h_form_W[z]}|{h_form_D[z]}|{h_form_L[z]}|{a_form_W[z]}|{a_form_D[z]}|{a_form_L[z]}|"
               f"{ht_g_avgs[z]}|{at_g_avgs[z]}|{bth_g_avgs[z]}|{bta_g_avgs[z]}|{ht_g_diff_avgs[z]}|{at_g_diff_avgs[z]}|{bth_g_diff_avgs[z]}|{bta_g_diff_avgs[z]}|"
               f"{OUTCOMES_ALT_XLR[0]}:-{bayesian_home_Win_d[z]}|{OUTCOMES_ALT_XLR[1]}:-{bayesian_away_Win_d[z]}|"
               f"{OUTCOMES_ALT_XLR[2]}:-{bayesian_12_d[z]}|"
               f"{match_times[z]}|{sport}|{P}_{K}_{L}_{M}_{N}|{set_date_s_size()[0]}\n")


def baye_appender_alt_xlr_(baye_HW, baye_AW, baye_12):
    bayesian_home_Win_d.append(round((float(baye_HW)), 4))
    bayesian_away_Win_d.append(round((float(baye_AW)), 4))
    bayesian_12_d.append(round((float(baye_12)), 4))


def scheduler():
    driver.get(SPORT_)
    if date_time != tmrw_date:
        try:
            cookie_click1()
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
            try:
                driver.get(SPORT_)
                sleep(1.5)
                cookie_click1()
            except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
                cookie_click1()
            except UnexpectedAlertPresentException:
                alert_handler()
    try:
        driver.find_element(By.CSS_SELECTOR, ".filters__group .filters__tab:last-child").click()
    except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
        try:
            driver.get(SPORT_)
            cookie_click()
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
            cookie_click()
        except UnexpectedAlertPresentException:
            alert_handler1()
    except UnexpectedAlertPresentException:
        alert_handler1()
    calender_day = int(driver.find_element(By.ID, 'calendarMenu').text.split("/")[0])
    selected_day = int(tmrw_date.split("-")[0])
    if calender_day > selected_day:
        driver.find_element(By.CSS_SELECTOR, '[title="Previous day"]').click()
    elif calender_day < selected_day:
        driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()
    else:
        pass


def total_aggregator():
    def h2h_zero():
        print("h2h_zero")
        while True:
            prb_HW_ = rdm.random()
            prb_AW_ = 1 - prb_HW_
            prb_12_ = 0.99
            prb_sh1_2_5_ = rdm.random()
            if prb_sh1_2_5_ >= 0.99:
                while True:
                    prb_sh1_1_5_ = rdm.random()
                    if prb_sh1_2_5_ >= prb_sh1_1_5_:
                        while True:
                            prb_sh2_2_5_ = rdm.random()
                            if prb_sh2_2_5_ >= 0.99:
                                while True:
                                    prb_sh2_1_5_ = rdm.random()
                                    if prb_sh2_2_5_ >= prb_sh2_1_5_:
                                        while True:
                                            prb_00_ = rdm.random()
                                            if prb_00_ >= 0.99:
                                                while True:
                                                    prb_2_5_ = rdm.random()
                                                    if prb_00_ >= prb_2_5_:
                                                        while True:
                                                            prb_3_5_ = rdm.random()
                                                            if prb_2_5_ >= prb_3_5_ and prb_3_5_ <= 0.01:
                                                                h2h_appender(prb_HW=prb_HW_, prb_AW=prb_AW_, prb_2_5=prb_2_5_, prb_3_5=prb_3_5_, prb_sh1_1_5=prb_sh1_1_5_,
                                                                             prb_sh1_2_5=prb_sh1_2_5_, prb_sh2_1_5=prb_sh2_1_5_, prb_sh2_2_5=prb_sh2_2_5_, prb_12=prb_12_, prb_00=prb_00_)
                                                                break
                                                        break
                                                break
                                        break
                                break
                        break
                break

    def ht_indp_zero():
        print("ht_indp_zero")
        while True:
            prb_HW_H_indp_ = rdm.random()
            prb_AW_H_indp_ = 1 - prb_HW_H_indp_
            prb_12_H_indp_ = 0.99
            prb_sh1_2_5_H_indp_ = rdm.random()
            if prb_sh1_2_5_H_indp_ >= 0.99:
                while True:
                    prb_sh1_1_5_H_indp_ = rdm.random()
                    if prb_sh1_2_5_H_indp_ >= prb_sh1_1_5_H_indp_:
                        while True:
                            prb_sh2_2_5_H_indp_ = rdm.random()
                            if prb_sh2_2_5_H_indp_ >= 0.99:
                                while True:
                                    prb_sh2_1_5_H_indp_ = rdm.random()
                                    if prb_sh2_2_5_H_indp_ >= prb_sh2_1_5_H_indp_:
                                        while True:
                                            prb_00_H_indp_ = rdm.random()
                                            if prb_00_H_indp_ >= 0.99:
                                                while True:
                                                    prb_2_5_H_indp_ = rdm.random()
                                                    if prb_00_H_indp_ >= prb_2_5_H_indp_:
                                                        while True:
                                                            prb_3_5_H_indp_ = rdm.random()
                                                            if prb_2_5_H_indp_ >= prb_3_5_H_indp_ and prb_3_5_H_indp_ <= 0.01:
                                                                ht_indp_appender(prb_HW_H_indp=prb_HW_H_indp_, prb_AW_H_indp=prb_AW_H_indp_, prb_2_5_H_indp=prb_2_5_H_indp_,
                                                                                 prb_3_5_H_indp=prb_3_5_H_indp_, prb_sh1_1_5_H_indp=prb_sh1_1_5_H_indp_,
                                                                                 prb_sh1_2_5_H_indp=prb_sh1_2_5_H_indp_, prb_sh2_1_5_H_indp=prb_sh2_1_5_H_indp_,
                                                                                 prb_sh2_2_5_H_indp=prb_sh2_2_5_H_indp_, prb_12_H_indp=prb_12_H_indp_, prb_00_H_indp=prb_00_H_indp_)
                                                                break
                                                        break
                                                break
                                        break
                                break
                        break
                break

    def at_indp_zero():
        print("at_indp_zero")
        while True:
            prb_HW_A_indp_ = rdm.random()
            prb_AW_A_indp_ = 1 - prb_HW_A_indp_
            prb_12_A_indp_ = 0.99
            prb_sh1_2_5_A_indp_ = rdm.random()
            if prb_sh1_2_5_A_indp_ >= 0.99:
                while True:
                    prb_sh1_1_5_A_indp_ = rdm.random()
                    if prb_sh1_2_5_A_indp_ >= prb_sh1_1_5_A_indp_:
                        while True:
                            prb_sh2_2_5_A_indp_ = rdm.random()
                            if prb_sh2_2_5_A_indp_ >= 0.99:
                                while True:
                                    prb_sh2_1_5_A_indp_ = rdm.random()
                                    if prb_sh2_2_5_A_indp_ >= prb_sh2_1_5_A_indp_:
                                        while True:
                                            prb_00_A_indp_ = rdm.random()
                                            if prb_00_A_indp_ >= 0.99:
                                                while True:
                                                    prb_2_5_A_indp_ = rdm.random()
                                                    if prb_00_A_indp_ >= prb_2_5_A_indp_:
                                                        while True:
                                                            prb_3_5_A_indp_ = rdm.random()
                                                            if prb_2_5_A_indp_ >= prb_3_5_A_indp_ and prb_3_5_A_indp_ <= 0.01:
                                                                at_indp_appender(prb_HW_A_indp=prb_HW_A_indp_, prb_AW_A_indp=prb_AW_A_indp_, prb_2_5_A_indp=prb_2_5_A_indp_,
                                                                                 prb_3_5_A_indp=prb_3_5_A_indp_, prb_sh1_1_5_A_indp=prb_sh1_1_5_A_indp_,
                                                                                 prb_sh1_2_5_A_indp=prb_sh1_2_5_A_indp_, prb_sh2_1_5_A_indp=prb_sh2_1_5_A_indp_,
                                                                                 prb_sh2_2_5_A_indp=prb_sh2_2_5_A_indp_, prb_12_A_indp=prb_12_A_indp_, prb_00_A_indp=prb_00_A_indp_)
                                                                break
                                                        break
                                                break
                                        break
                                break
                        break
                break

    try:
        sub1 = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row')
        if len(sub1) < DSCRM_H_A:
            ht_indp_zero()
            ht_g_avgs.append(round(rdm.uniform(0, 2), 2))
            ht_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))
        else:
            ht_probs = ht_indp_aggregator()
            ht_g_avg_aggregator()
            ht_g_diff_avg_aggregator()
            if ht_probs[0] >= DSCRM_H_A:
                try:
                    ht_indp_values = ht_indp_prob_calc(ht_probs)
                    ht_indp_appender(prb_HW_H_indp=ht_indp_values[0], prb_AW_H_indp=ht_indp_values[1],
                                     prb_2_5_H_indp=ht_indp_values[2], prb_3_5_H_indp=ht_indp_values[3],
                                     prb_sh1_1_5_H_indp=ht_indp_values[4],
                                     prb_sh1_2_5_H_indp=ht_indp_values[5], prb_sh2_1_5_H_indp=ht_indp_values[6],
                                     prb_sh2_2_5_H_indp=ht_indp_values[7], prb_12_H_indp=ht_indp_values[8], prb_00_H_indp=ht_indp_values[9])
                except ZeroDivisionError:
                    ht_indp_zero()
            else:
                ht_indp_zero()
    except ElementNotInteractableException:
        ht_indp_zero()
    try:
        sub2 = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row')
        if len(sub2) < DSCRM_H_A:
            at_indp_zero()
            at_g_avgs.append(round(rdm.uniform(0, 2)))
            at_g_diff_avgs.append(round(rdm.uniform(-2, 2), 2))
        else:
            at_probs = at_indp_aggregator()
            at_g_avg_aggregator()
            at_g_diff_avg_aggregator()
            if at_probs[0] >= DSCRM_H_A:
                try:
                    at_indp_values = at_indp_prob_calc(at_probs)
                    at_indp_appender(prb_HW_A_indp=at_indp_values[0], prb_AW_A_indp=at_indp_values[1],
                                     prb_2_5_A_indp=at_indp_values[2], prb_3_5_A_indp=at_indp_values[3],
                                     prb_sh1_1_5_A_indp=at_indp_values[4],
                                     prb_sh1_2_5_A_indp=at_indp_values[5], prb_sh2_1_5_A_indp=at_indp_values[6],
                                     prb_sh2_2_5_A_indp=at_indp_values[7], prb_12_A_indp=at_indp_values[8], prb_00_A_indp=at_indp_values[9])
                except ZeroDivisionError:
                    at_indp_zero()
            else:
                at_indp_zero()
    except ElementNotInteractableException:
        at_indp_zero()
    try:
        sub3 = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row')
        if len(sub3) < DSCRM_BT:
            h2h_zero()
            bth_g_diff_avgs_x = round(rdm.uniform(-2, 2), 2)
            bta_g_diff_avgs_x = -1 * bth_g_diff_avgs_x
            bth_g_avgs.append(round(rdm.uniform(0, 2), 2))
            bta_g_avgs.append(round(rdm.uniform(0, 2), 2))
            bth_g_diff_avgs.append(bth_g_diff_avgs_x)
            bta_g_diff_avgs.append(bta_g_diff_avgs_x)
        else:
            h2h_probs = h2h_aggregator()
            bt_g_avg_aggregator()
            bt_g_diff_avg_aggregator()
            if h2h_probs[0] >= DSCRM_BT:
                try:
                    h2h_values = h2h_prob_calc(h2h_probs)
                    h2h_appender(prb_HW=h2h_values[0], prb_AW=h2h_values[1], prb_2_5=h2h_values[2], prb_3_5=h2h_values[3],
                                 prb_sh1_1_5=h2h_values[4], prb_sh1_2_5=h2h_values[5],
                                 prb_sh2_1_5=h2h_values[6], prb_sh2_2_5=h2h_values[7], prb_12=h2h_values[8], prb_00=h2h_values[9])
                except ZeroDivisionError:
                    h2h_zero()
            else:
                h2h_zero()
    except ElementNotInteractableException:
        h2h_zero()


def print_all_data():
    print(f"Countries: {len(countries)}, Leagues: {len(leagues)}, Home Teams: {len(home_teams)}, "
          f"Home Positions: {len(home_positions)}, Home Points: {len(home_points)}, "
          f"Home No Matches Played: {len(home_nums_matches_played)}, Away Teams: {len(away_teams)}, "
          f"Away Positions: {len(away_positions)}, Away Points: {len(away_points)}, "
          f"Away No Matches Played: {len(away_nums_matches_played)}, Match Times: {len(match_times)} "
          f"Home W Form: {len(h_form_W)}, Home D Form: {len(h_form_D)}, Home L Form: {len(h_form_L)}, "
          f"Away W Form: {len(a_form_W)}, Away D Form: {len(a_form_D)}, Away L Form: {len(a_form_L)}"
          f"Prob GGs: {len(prob_2_5s)}, Prob 3_5s: {len(prob_3_5s)}, Prob sh1_1_5s: {len(prob_sh1_1_5s)},"
          f"Prob 12s: {len(prob_12s)}, Prob HWs: {len(prob_HWs)}, Prob AWs: {len(prob_AWs)}, "
          f"Prob GG_H_indps: {len(prob_2_5_H_indps)}, Prob 3_5_H_indps: {len(prob_3_5_H_indps)}, "
          f"Prob sh1_1_5_H_indps: {len(prob_sh1_1_5_H_indps)}, Prob 12_H_indps: {len(prob_12_H_indps)},"
          f"Prob HW_H_indps: {len(prob_HW_H_indps)}, Prob AW_H_indps: {len(prob_AW_H_indps)}, "
          f"Prob GG_A_indps: {len(prob_2_5_A_indps)}, Prob 3_5_A_indps: {len(prob_3_5_A_indps)}, "
          f"Prob sh1_1_5_A_indps: {len(prob_sh1_1_5_A_indps)}, Prob 12_A_indps: {len(prob_12_A_indps)}, "
          f"Prob HW_A_indps: {len(prob_HW_A_indps)}, Prob AW_A_indps: {len(prob_AW_A_indps)}, "
          f"Odds _1HWS: {len(_1HWS)}, Odds _2AWS: {len(_2AWS)}, Odds OVER_3_5_S: {len(OVER_3_5_S)}, "
          f"Odds OVER_sh1_1_5_S: {len(OVER_sh1_1_5_S)}, Odds _12S: {len(_12S)}"
          f"Bayesian Home Win: {len(bayesian_home_Win_d)}, Bayesian Away Win: {len(bayesian_away_Win_d)}, "
          f"Bayesian GG: {len(bayesian_2_5_d)}, Bayesian 3.5: {len(bayesian_3_5_d)}, "
          f"Bayesian bayesian_sh1_1_5: {len(bayesian_sh1_1_5_d)}, Bayesian 12: {len(bayesian_12_d) }")
    print(f"HTGAVG: {ht_g_avgs}")
    print(f"ATGAVG: {at_g_avgs}")
    print(f"HTGAVG: {len(ht_g_avgs)}")
    print(f"ATGAVG: {len(at_g_avgs)}")
    print(f"BTHGAVG: {bth_g_avgs}")
    print(f"BTAGAVG: {bta_g_avgs}")
    print(f"BTHGAVG: {len(bth_g_avgs)}")
    print(f"BTAGAVG: {len(bta_g_avgs)}")
    print(f"HTSCDIFF: {ht_g_diff_avgs}")
    print(f"ATSCDIFF: {at_g_diff_avgs}")
    print(f"HTSCDIFF: {len(ht_g_diff_avgs)}")
    print(f"ATSCDIFF: {len(at_g_diff_avgs)}")
    print(f"BTHSCDIFF: {bth_g_diff_avgs}")
    print(f"BTASCDIFF: {bta_g_diff_avgs}")
    print(f"BTHSCDIFF: {len(bth_g_diff_avgs)}")
    print(f"BTASCDIFF: {len(bta_g_diff_avgs)}")


OVER_00_S = []
OVER_2_5_S = []
OVER_3_5_S = []
OVER_sh1_1_5_S = []
OVER_sh1_2_5_S = []
OVER_sh2_1_5_S = []
OVER_sh2_2_5_S = []
_12S = []
_1HWS = []
_2AWS = []
a_form_D = []
a_form_L = []
a_form_W = []
at_g_avgs = []
at_g_diff_avgs = []
away_nums_matches_played = []
away_points = []
away_positions = []
away_teams = []
away_z_prob = []
bta_g_avgs = []
bta_g_diff_avgs = []
bth_g_avgs = []
bth_g_diff_avgs = []
countries = []
diff_z_prob = []
h_form_D = []
h_form_L = []
h_form_W = []
home_nums_matches_played = []
home_points = []
home_positions = []
home_teams = []
home_z_prob = []
ht_g_avgs = []
ht_g_diff_avgs = []
leagues = []
match_times = []
prob_12_A_indps = []
prob_12_H_indps = []
prob_12s = []
prob_2_5_A_indps = []
prob_2_5_H_indps = []
prob_2_5s = []
prob_3_5_A_indps = []
prob_3_5_H_indps = []
prob_3_5s = []
prob_AW_A_indps = []
prob_AW_H_indps = []
prob_AWs = []
prob_HW_A_indps = []
prob_HW_H_indps = []
prob_HWs = []
prob_sh1_1_5_A_indps = []
prob_sh1_1_5_H_indps = []
prob_sh1_1_5s = []
prob_sh1_2_5_A_indps = []
prob_sh1_2_5_H_indps = []
prob_sh1_2_5s = []
prob_sh2_1_5_A_indps = []
prob_sh2_1_5_H_indps = []
prob_sh2_1_5s = []
prob_sh2_2_5_A_indps = []
prob_sh2_2_5_H_indps = []
prob_sh2_2_5s = []
prob_00_A_indps = []
prob_00_H_indps = []
prob_00s = []

# if date_time != tmrw_date:
try:
    hidden_matches = driver.find_elements(By.CSS_SELECTOR, '[class="event__info"]')
    print(len(hidden_matches))
    for hidden_m in hidden_matches:
        try:
            hidden_m.click()
        except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException, IndexError) as e:
            print(f"Skip A-{hidden_matches.index(hidden_m)}")
            try:
                hidden_matchez = driver.find_elements(By.CSS_SELECTOR, '[class="event__info"]')
                hidden_matchez[0].click()
                print(f"Click C-{hidden_matches.index(hidden_m)}")
            except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException, IndexError) as e:
                print(f"Skip B-{hidden_matches.index(hidden_m)}")
                break
except NoSuchElementException:
    print("No Hidden Matches")

driver.execute_script("window.scrollTo(0, 0);")
sleep(0.5)


divs = driver.find_elements(By.CSS_SELECTOR, f'.{sport} .event__match--scheduled')
print(len(divs))

try:
    sub_m_t = []
    match_timez = driver.find_elements(By.CLASS_NAME, 'event__time')
    for m_t in range(len(match_timez)):
        sub_m_t.append(match_timez[m_t].text.split('\n')[0])
except StaleElementReferenceException:
    sub_m_t = []
    driver.refresh()
    sleep(0.5)
    scheduler()
    match_timez = driver.find_elements(By.CLASS_NAME, 'event__time')
    for m_t in range(len(match_timez)):
        sub_m_t.append(match_timez[m_t].text.split('\n')[0])
except UnexpectedAlertPresentException:
    try:
        alertz = driver.switch_to.alert
        alertz.accept()
        driver.switch_to.default_content()
    except NoAlertPresentException:
        pass
    sub_m_t = []
    driver.refresh()
    sleep(0.5)
    scheduler()
    match_timez = driver.find_elements(By.CLASS_NAME, 'event__time')
    for m_t in range(len(match_timez)):
        sub_m_t.append(match_timez[m_t].text.split('\n')[0])
print(f"Length of Match lists: {len(sub_m_t)}")

for i in range(len(sub_m_t)):
    try:
        divs[i].click()
    except (IndexError, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException):
        scheduler()
        try:
            divs = driver.find_elements(By.CSS_SELECTOR, f'.{sport} .event__match--scheduled')
            divs[i].click()
        except (IndexError, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException):
            scheduler()
            try:
                divs = driver.find_elements(By.CSS_SELECTOR, f'.{sport} .event__match--scheduled')
                divs[i].click()
            except (IndexError, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException):
                traceback.print_exc()
                winsound.Beep(2500, 10000)
                break

    print(f"{sport}:- {i + 1}/{len(sub_m_t)}")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    try:
        home_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__home  .participant__participantName a').text
        away_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__away  .participant__participantName a').text
    except (IndexError, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException):
        try:
            home_teamy = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[0].text
            home_teamz = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[1].text
            home_teamx = f"{home_teamy}/{home_teamz}"
            away_teamy = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[0].text
            away_teamz = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[1].text
            away_teamx = f"{away_teamy}/{away_teamz}"
        except (IndexError, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException):
            try:
                driver.refresh()
                winsound.Beep(2500, 10000)
                sleep(1.5)
                home_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__home  .participant__participantName a').text
                away_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__away  .participant__participantName a').text
            except (IndexError, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException):
                try:
                    home_teamy = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[0].text
                    home_teamz = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[1].text
                    home_teamx = f"{home_teamy}/{home_teamz}"
                    away_teamy = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[0].text
                    away_teamz = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[1].text
                    away_teamx = f"{away_teamy}/{away_teamz}"
                except (IndexError, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException):
                    driver.close()
                    driver.switch_to.window(window_before)
                    traceback.print_exc()
                    break

    try:
        driver.find_element(By.LINK_TEXT, "STANDINGS").click()
        rank = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")
        if len(rank) != 2:
            raise NoSuchElementException("Length of participants exceeded")
        try:
            fir_ent = int(driver.find_elements(By.CSS_SELECTOR, '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[0].text.strip())
        except IndexError:
            try:
                driver.refresh()
                sleep(1.5)
                fir_ent = int(driver.find_elements(By.CSS_SELECTOR, '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[0].text.strip())
            except IndexError:
                fir_ent = 0
        selected_teams_names = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected  .tableCellParticipant__name")
        try:
            pts_pos_mp()
            current_ht_pts = home_points[i]
            current_at_pts = away_points[i]
            z_scorer(htpts=current_ht_pts, atpts=current_at_pts)
        except (IndexError, StaleElementReferenceException):
            try:
                driver.close()
                driver.switch_to.window(window_before)
                divs[i].click()
                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                driver.find_element(By.LINK_TEXT, "STANDINGS").click()
                sleep(5)
                selected_teams_names = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected  .tableCellParticipant__name")
                pts_pos_mp()
                current_ht_pts = home_points[i]
                current_at_pts = away_points[i]
                z_scorer(htpts=current_ht_pts, atpts=current_at_pts)
            except (IndexError, StaleElementReferenceException):
                raise NoSuchElementException("Table Error")
        team_data()
        odds_checker()
        driver.find_element(By.LINK_TEXT, "H2H").click()
        status_ = None
        for p in range(INDP_MATCH_SAMPLE):
            status_ = show_more_matches()
        if status_ != 0:
            home_form_checker(home_teamk=home_teamx)
            away_form_checker(away_teamk=away_teamx)
            if fir_ent < 10:
                home_counter()
                away_counter()
            total_aggregator()
            driver.close()
            driver.switch_to.window(window_before)
            try:
                match_times.append(sub_m_t[i])
            except (IndexError, NoSuchElementException, StaleElementReferenceException):
                match_times.append("XX:XX")
                traceback.print_exc()
        else:
            data_break_zeroes1(home_pos_=home_positions[i], away_pos_=away_positions[i], z=i, ent1=fir_ent)
            driver.close()
            driver.switch_to.window(window_before)

    except NoSuchElementException:
        try:
            try:
                home_t_rank = int(driver.find_element(By.CSS_SELECTOR, '.duelParticipant .duelParticipant__home .participant__participantRank').text.split(': ')[1].split('.')[0])
                home_positions.append(home_t_rank)
            except NoSuchElementException:
                home_positions.append((rdm.randint(2000, 4000)))
            try:
                away_t_rank = int(driver.find_element(By.CSS_SELECTOR, '.duelParticipant .duelParticipant__away .participant__participantRank').text.split(': ')[1].split('.')[0])
                away_positions.append(away_t_rank)
            except NoSuchElementException:
                away_positions.append((rdm.randint(2000, 4000)))
            team_data()
            odds_checker()
            driver.find_element(By.LINK_TEXT, "H2H").click()
            status_ = None
            for p in range(INDP_MATCH_SAMPLE):
                status_ = show_more_matches()
            if status_ != 0:
                home_form_checker(home_teamk=home_teamx)
                away_form_checker(away_teamk=away_teamx)
                home_counter()
                away_counter()
                total_aggregator()
                driver.close()
                driver.switch_to.window(window_before)
                try:
                    match_times.append(sub_m_t[i])
                except (IndexError, NoSuchElementException, StaleElementReferenceException):
                    match_times.append("XX:XX")
                    traceback.print_exc()
                current_ht_pos = home_positions[i]
                current_at_pos = away_positions[i]
                append_zeroes(home_pos=current_ht_pos, away_pos=current_at_pos)

            else:
                data_break_zeroes2(home_pos_=home_positions[i], away_pos_=away_positions[i], z=i)
                driver.close()
                driver.switch_to.window(window_before)

        except (TimeoutException, IndexError, StaleElementReferenceException,
                NoSuchWindowException, WebDriverException) as e:
            print("Error Hold 1", e)
            traceback.print_exc()
            driver.close()
            driver.switch_to.window(window_before)
            break
        except InvalidSessionIdException:
            driver.get(SPORT_)
            print("Invalid1")
            break
        except UnexpectedAlertPresentException:
            try:
                alertz = driver.switch_to.alert
                alertz.accept()
                driver.switch_to.default_content()
                print("Alert4")
                break
            except NoAlertPresentException:
                print("No Alert4")
                break

    except (TimeoutException, IndexError, StaleElementReferenceException,
            NoSuchWindowException, WebDriverException) as e:
        print("Error Hold 2", e)
        driver.close()
        driver.switch_to.window(window_before)
        break
    except InvalidSessionIdException:
        driver.get(SPORT_)
        print("Invalid2")
        break
    except UnexpectedAlertPresentException:
        try:
            alertz = driver.switch_to.alert
            alertz.accept()
            driver.switch_to.default_content()
            print("Alert5")
            break
        except NoAlertPresentException:
            print("No Alert5")
            break

    if i % 5 == 0:
        with open(f"../LISTS - SPORTS DATA/SPORTS_DATA_LIST_{sport}.txt", mode="w") as file:
            try:
                file.write(f"countries = {countries}\nleagues = {leagues}\nhome_teams = {home_teams}\n"
                           f"home_positions = {home_positions}\nhome_points = {home_points}\n"
                           f"home_nums_matches_played = {home_nums_matches_played}\naway_teams = {away_teams}\n"
                           f"away_positions = {away_positions}\naway_points = {away_points}\n"
                           f"away_nums_matches_played = {away_nums_matches_played}\nmatch_times = {match_times}\n"
                           f"h_form_W = {h_form_W}\nh_form_D = {h_form_D}\nh_form_L = {h_form_L}\n"
                           f"a_form_W = {a_form_W}\na_form_D = {a_form_D}\na_form_L = {a_form_L}\n"
                           f"prob_00s = {prob_00s}\nprob_2_5s = {prob_2_5s}\nprob_3_5s = {prob_3_5s}\n"
                           f"prob_sh1_1_5s = {prob_sh1_1_5s}\nprob_sh1_2_5s = {prob_sh1_2_5s}\n"
                           f"prob_sh2_1_5s = {prob_sh2_1_5s}\nprob_sh2_2_5s = {prob_sh2_2_5s}\n"
                           f"prob_12s = {prob_12s}\nprob_HWs = {prob_HWs}\nprob_AWs = {prob_AWs}\n"
                           f"prob_00_H_indps = {prob_00_H_indps}\nprob_2_5_H_indps = {prob_2_5_H_indps}\nprob_3_5_H_indps = {prob_3_5_H_indps}\n"
                           f"prob_sh1_1_5_H_indps = {prob_sh1_1_5_H_indps}\nprob_sh1_2_5_H_indps = {prob_sh1_2_5_H_indps}\n"
                           f"prob_sh2_1_5_H_indps = {prob_sh2_1_5_H_indps}\nprob_sh2_2_5_H_indps = {prob_sh2_2_5_H_indps}\n"
                           f"prob_12_H_indps = {prob_12_H_indps}\n"
                           f"prob_HW_H_indps = {prob_HW_H_indps}\nprob_AW_H_indps = {prob_AW_H_indps}\n"
                           f"prob_00_A_indps = {prob_00_A_indps}\nprob_2_5_A_indps = {prob_2_5_A_indps}\nprob_3_5_A_indps = {prob_3_5_A_indps}\n"
                           f"prob_sh1_1_5_A_indps = {prob_sh1_1_5_A_indps}\nprob_sh1_2_5_A_indps = {prob_sh1_2_5_A_indps}\n"
                           f"prob_sh2_1_5_A_indps = {prob_sh2_1_5_A_indps}\nprob_sh2_2_5_A_indps = {prob_sh2_2_5_A_indps}\n"
                           f"prob_12_A_indps = {prob_12_A_indps}\n"
                           f"prob_HW_A_indps = {prob_HW_A_indps}\nprob_AW_A_indps = {prob_AW_A_indps}\n"
                           f"home_z_prob = {home_z_prob}\naway_z_prob = {away_z_prob}\ndiff_z_prob = {diff_z_prob}\n"
                           f"sport = '{sport}_{i}'\n_1HWS = {_1HWS}\n_2AWS = {_2AWS}\nOVER_2_5_S = {OVER_2_5_S}\n"
                           f"OVER_00_S = {OVER_00_S}\nOVER_3_5_S = {OVER_3_5_S}\n"
                           f"OVER_sh1_1_5_S = {OVER_sh1_1_5_S}\nOVER_sh1_2_5_S = {OVER_sh1_2_5_S}\n"
                           f"OVER_sh2_1_5_S = {OVER_sh2_1_5_S}\nOVER_sh2_2_5_S = {OVER_sh2_2_5_S}\n"
                           f"_12S = {_12S}\nmatch_date = '{set_date_s_size()[0]}'\n"
                           f"ht_g_diff_avgs = {ht_g_diff_avgs}\nat_g_diff_avgs = {at_g_diff_avgs}\nbth_g_diff_avgs = {bth_g_diff_avgs}\nbta_g_diff_avgs = {bta_g_diff_avgs}\n"
                           f"ht_g_avgs = {ht_g_avgs}\nat_g_avgs = {at_g_avgs}\nbth_g_avgs = {bth_g_avgs}\nbta_g_avgs = {bta_g_avgs}")
            except UnicodeError:
                pass
            except IndexError:
                continue

baye_home_Win_d = []
baye_away_Win_d = []
baye_12_d = []

for j in range(len(prob_HWs)):
    baye_12 = (prob_12s[j] * (prob_12_H_indps[j] * prob_12_A_indps[j])) / ((prob_12s[j] * (prob_12_H_indps[j] * prob_12_A_indps[j])) + ((1 - (prob_12_H_indps[j] * prob_12_A_indps[j])) * (1 - prob_12s[j])))
    baye_12_d.append(baye_12)
    baye_away_Win = (prob_AWs[j] * (prob_HW_A_indps[j] * prob_AW_A_indps[j])) / ((prob_AWs[j] * (prob_HW_A_indps[j] * prob_AW_A_indps[j])) + ((1 - (prob_HW_A_indps[j] * prob_AW_A_indps[j])) * (1 - prob_AWs[j])))
    baye_away_Win_d.append(baye_away_Win)
    baye_home_Win = (prob_HWs[j] * (prob_HW_H_indps[j] * prob_AW_H_indps[j])) / ((prob_HWs[j] * (prob_HW_H_indps[j] * prob_AW_H_indps[j])) + ((1 - (prob_HW_H_indps[j] * prob_AW_H_indps[j])) * (1 - prob_HWs[j])))
    baye_home_Win_d.append(baye_home_Win)


if len(home_teams) > 0:
    with open(f"../LISTS - SPORTS DATA/SPORTS_DATA_LIST_{sport}.txt", mode="w") as file:
        try:
            file.write(f"countries = {countries}\nleagues = {leagues}\nhome_teams = {home_teams}\n"
                       f"home_positions = {home_positions}\nhome_points = {home_points}\n"
                       f"home_nums_matches_played = {home_nums_matches_played}\naway_teams = {away_teams}\n"
                       f"away_positions = {away_positions}\naway_points = {away_points}\n"
                       f"away_nums_matches_played = {away_nums_matches_played}\nmatch_times = {match_times}\n"
                       f"h_form_W = {h_form_W}\nh_form_D = {h_form_D}\nh_form_L = {h_form_L}\n"
                       f"a_form_W = {a_form_W}\na_form_D = {a_form_D}\na_form_L = {a_form_L}\n"
                       f"prob_00s = {prob_00s}\nprob_2_5s = {prob_2_5s}\nprob_3_5s = {prob_3_5s}\n"
                       f"prob_sh1_1_5s = {prob_sh1_1_5s}\nprob_sh1_2_5s = {prob_sh1_2_5s}\n"
                       f"prob_sh2_1_5s = {prob_sh2_1_5s}\nprob_sh2_2_5s = {prob_sh2_2_5s}\n"
                       f"prob_12s = {prob_12s}\nprob_HWs = {prob_HWs}\nprob_AWs = {prob_AWs}\n"
                       f"prob_00_H_indps = {prob_00_H_indps}\nprob_2_5_H_indps = {prob_2_5_H_indps}\nprob_3_5_H_indps = {prob_3_5_H_indps}\n"
                       f"prob_sh1_1_5_H_indps = {prob_sh1_1_5_H_indps}\nprob_sh1_2_5_H_indps = {prob_sh1_2_5_H_indps}\n"
                       f"prob_sh2_1_5_H_indps = {prob_sh2_1_5_H_indps}\nprob_sh2_2_5_H_indps = {prob_sh2_2_5_H_indps}\n"
                       f"prob_12_H_indps = {prob_12_H_indps}\n"
                       f"prob_HW_H_indps = {prob_HW_H_indps}\nprob_AW_H_indps = {prob_AW_H_indps}\n"
                       f"prob_00_A_indps = {prob_00_A_indps}\nprob_2_5_A_indps = {prob_2_5_A_indps}\nprob_3_5_A_indps = {prob_3_5_A_indps}\n"
                       f"prob_sh1_1_5_A_indps = {prob_sh1_1_5_A_indps}\nprob_sh1_2_5_A_indps = {prob_sh1_2_5_A_indps}\n"
                       f"prob_sh2_1_5_A_indps = {prob_sh2_1_5_A_indps}\nprob_sh2_2_5_A_indps = {prob_sh2_2_5_A_indps}\n"
                       f"prob_12_A_indps = {prob_12_A_indps}\n"
                       f"prob_HW_A_indps = {prob_HW_A_indps}\nprob_AW_A_indps = {prob_AW_A_indps}\n"
                       f"home_z_prob = {home_z_prob}\naway_z_prob = {away_z_prob}\ndiff_z_prob = {diff_z_prob}\n"
                       f"sport = '{sport}'\n_1HWS = {_1HWS}\n_2AWS = {_2AWS}\nOVER_2_5_S = {OVER_2_5_S}\n"
                       f"OVER_00_S = {OVER_00_S}\nOVER_3_5_S = {OVER_3_5_S}\n"
                       f"OVER_sh1_1_5_S = {OVER_sh1_1_5_S}\nOVER_sh1_2_5_S = {OVER_sh1_2_5_S}\n"
                       f"OVER_sh2_1_5_S = {OVER_sh2_1_5_S}\nOVER_sh2_2_5_S = {OVER_sh2_2_5_S}\n"
                       f"_12S = {_12S}\nmatch_date = '{set_date_s_size()[0]}'\n"
                       f"ht_g_diff_avgs = {ht_g_diff_avgs}\nat_g_diff_avgs = {at_g_diff_avgs}\nbth_g_diff_avgs = {bth_g_diff_avgs}\nbta_g_diff_avgs = {bta_g_diff_avgs}\n"
                       f"ht_g_avgs = {ht_g_avgs}\nat_g_avgs = {at_g_avgs}\nbth_g_avgs = {bth_g_avgs}\nbta_g_avgs = {bta_g_avgs}")
        except UnicodeError:
            pass
        except IndexError:
            pass

    for CONFINTVL in CONFINTVLS:
        for COMBINER in COMBINERS[:4]:
            Z = COMBINER
            for COMB in COMB_PROB_METRICS1:
                X, Y = COMB
                bayesian_home_Win_d = []
                bayesian_away_Win_d = []
                bayesian_2_5_d = []
                bayesian_3_5_d = []
                bayesian_sh1_1_5_d = []
                bayesian_sh1_2_5_d = []
                bayesian_sh2_1_5_d = []
                bayesian_sh2_2_5_d = []
                bayesian_12_d = []
                bayesian_00_d = []

                for q in range(len(home_teams)):
                    try:
                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_2_5 = 0.5 * (rdm.random() + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                            bayesian_3_5 = 0.5 * (rdm.random() + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                            bayesian_sh1_1_5 = 0.5 * (rdm.random() + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                            bayesian_sh1_2_5 = 0.5 * (rdm.random() + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                            bayesian_sh2_1_5 = 0.5 * (rdm.random() + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                            bayesian_sh2_2_5 = 0.5 * (rdm.random() + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                            bayesian_12 = 0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            bayesian_00 = 0.5 * (rdm.random() + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_2_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                            bayesian_3_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                            bayesian_sh1_1_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                            bayesian_sh1_2_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                            bayesian_sh2_1_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                            bayesian_sh2_2_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            bayesian_00 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_2_5 = 0.5 * (OVER_2_5_S[q] + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                            bayesian_3_5 = 0.5 * (OVER_3_5_S[q] + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                            bayesian_sh1_1_5 = 0.5 * (OVER_sh1_1_5_S[q] + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                            bayesian_sh1_2_5 = 0.5 * (OVER_sh1_2_5_S[q] + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                            bayesian_sh2_1_5 = 0.5 * (OVER_sh2_1_5_S[q] + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                            bayesian_sh2_2_5 = 0.5 * (OVER_sh2_2_5_S[q] + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                            bayesian_12 = 0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            bayesian_00 = 0.5 * (OVER_00_S[q] + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + rdm.random())
                            bayesian_2_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + rdm.random())
                            bayesian_3_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + rdm.random())
                            bayesian_sh1_1_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + rdm.random())
                            bayesian_sh1_2_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + rdm.random())
                            bayesian_sh2_1_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + rdm.random())
                            bayesian_sh2_2_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + rdm.random())
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random())
                            bayesian_00 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (_2AWS[q] + rdm.random())
                            bayesian_2_5 = 0.5 * (OVER_2_5_S[q] + rdm.random())
                            bayesian_3_5 = 0.5 * (OVER_3_5_S[q] + rdm.random())
                            bayesian_sh1_1_5 = 0.5 * (OVER_sh1_1_5_S[q] + rdm.random())
                            bayesian_sh1_2_5 = 0.5 * (OVER_sh1_2_5_S[q] + rdm.random())
                            bayesian_sh2_1_5 = 0.5 * (OVER_sh2_1_5_S[q] + rdm.random())
                            bayesian_sh2_2_5 = 0.5 * (OVER_sh2_2_5_S[q] + rdm.random())
                            bayesian_12 = 0.5 * (_12S[q] + rdm.random())
                            bayesian_00 = 0.5 * (OVER_00_S[q] + rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + _1HWS[q])
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + _2AWS[q])
                            bayesian_2_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + OVER_2_5_S[q])
                            bayesian_3_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + OVER_3_5_S[q])
                            bayesian_sh1_1_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + OVER_sh1_1_5_S[q])
                            bayesian_sh1_2_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + OVER_sh1_2_5_S[q])
                            bayesian_sh2_1_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + OVER_sh2_1_5_S[q])
                            bayesian_sh2_2_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + OVER_sh2_2_5_S[q])
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q])
                            bayesian_00 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + OVER_00_S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[1]:
                            bayesian_home_Win = rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_2_5 = rdm.random() * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))
                            bayesian_3_5 = rdm.random() * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))
                            bayesian_sh1_1_5 = rdm.random() * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))
                            bayesian_sh1_2_5 = rdm.random() * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))
                            bayesian_sh2_1_5 = rdm.random() * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))
                            bayesian_sh2_2_5 = rdm.random() * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))
                            bayesian_12 = rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            bayesian_00 = rdm.random() * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))
                            bayesian_3_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))
                            bayesian_sh1_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))
                            bayesian_sh1_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))
                            bayesian_sh2_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))
                            bayesian_sh2_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            bayesian_00 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_2_5 = OVER_2_5_S[q] * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))
                            bayesian_3_5 = OVER_3_5_S[q] * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))
                            bayesian_sh1_1_5 = OVER_sh1_1_5_S[q] * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))
                            bayesian_sh1_2_5 = OVER_sh1_2_5_S[q] * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))
                            bayesian_sh2_1_5 = OVER_sh2_1_5_S[q] * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))
                            bayesian_sh2_2_5 = OVER_sh2_2_5_S[q] * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))
                            bayesian_12 = _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            bayesian_00 = OVER_00_S[q] * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random()
                            bayesian_away_Win = away_z_prob[q] * rdm.random()
                            bayesian_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * rdm.random()
                            bayesian_3_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * rdm.random()
                            bayesian_sh1_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * rdm.random()
                            bayesian_sh1_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * rdm.random()
                            bayesian_sh2_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * rdm.random()
                            bayesian_sh2_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * rdm.random()
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random()
                            bayesian_00 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * rdm.random()
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * rdm.random()
                            bayesian_away_Win = _2AWS[q] * rdm.random()
                            bayesian_2_5 = OVER_2_5_S[q] * rdm.random()
                            bayesian_3_5 = OVER_3_5_S[q] * rdm.random()
                            bayesian_sh1_1_5 = OVER_sh1_1_5_S[q] * rdm.random()
                            bayesian_sh1_2_5 = OVER_sh1_2_5_S[q] * rdm.random()
                            bayesian_sh2_1_5 = OVER_sh2_1_5_S[q] * rdm.random()
                            bayesian_sh2_2_5 = OVER_sh2_2_5_S[q] * rdm.random()
                            bayesian_12 = _12S[q] * rdm.random()
                            bayesian_00 = OVER_00_S[q] * rdm.random()
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * _1HWS[q]
                            bayesian_away_Win = away_z_prob[q] * _2AWS[q]
                            bayesian_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * OVER_2_5_S[q]
                            bayesian_3_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * OVER_3_5_S[q]
                            bayesian_sh1_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * OVER_sh1_1_5_S[q]
                            bayesian_sh1_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * OVER_sh1_2_5_S[q]
                            bayesian_sh2_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * OVER_sh2_1_5_S[q]
                            bayesian_sh2_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * OVER_sh2_2_5_S[q]
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q]
                            bayesian_00 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * OVER_00_S[q]
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_2_5 = math.sqrt(0.5 * (rdm.random() + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))))
                            bayesian_3_5 = math.sqrt(0.5 * (rdm.random() + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))))
                            bayesian_sh1_1_5 = math.sqrt(0.5 * (rdm.random() + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))))
                            bayesian_sh1_2_5 = math.sqrt(0.5 * (rdm.random() + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))))
                            bayesian_sh2_1_5 = math.sqrt(0.5 * (rdm.random() + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))))
                            bayesian_sh2_2_5 = math.sqrt(0.5 * (rdm.random() + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            bayesian_00 = math.sqrt(0.5 * (rdm.random() + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_2_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))))
                            bayesian_3_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))))
                            bayesian_sh1_1_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))))
                            bayesian_sh1_2_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))))
                            bayesian_sh2_1_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))))
                            bayesian_sh2_2_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            bayesian_00 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_2_5 = math.sqrt(0.5 * (OVER_2_5_S[q] + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))))
                            bayesian_3_5 = math.sqrt(0.5 * (OVER_3_5_S[q] + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))))
                            bayesian_sh1_1_5 = math.sqrt(0.5 * (OVER_sh1_1_5_S[q] + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))))
                            bayesian_sh1_2_5 = math.sqrt(0.5 * (OVER_sh1_2_5_S[q] + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))))
                            bayesian_sh2_1_5 = math.sqrt(0.5 * (OVER_sh2_1_5_S[q] + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))))
                            bayesian_sh2_2_5 = math.sqrt(0.5 * (OVER_sh2_2_5_S[q] + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            bayesian_00 = math.sqrt(0.5 * (OVER_00_S[q] + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + rdm.random()))
                            bayesian_2_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + rdm.random()))
                            bayesian_3_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + rdm.random()))
                            bayesian_sh1_1_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + rdm.random()))
                            bayesian_sh1_2_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + rdm.random()))
                            bayesian_sh2_1_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + rdm.random()))
                            bayesian_sh2_2_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random()))
                            bayesian_00 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + rdm.random()))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + rdm.random()))
                            bayesian_2_5 = math.sqrt(0.5 * (OVER_2_5_S[q] + rdm.random()))
                            bayesian_3_5 = math.sqrt(0.5 * (OVER_3_5_S[q] + rdm.random()))
                            bayesian_sh1_1_5 = math.sqrt(0.5 * (OVER_sh1_1_5_S[q] + rdm.random()))
                            bayesian_sh1_2_5 = math.sqrt(0.5 * (OVER_sh1_2_5_S[q] + rdm.random()))
                            bayesian_sh2_1_5 = math.sqrt(0.5 * (OVER_sh2_1_5_S[q] + rdm.random()))
                            bayesian_sh2_2_5 = math.sqrt(0.5 * (OVER_sh2_2_5_S[q] + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + rdm.random()))
                            bayesian_00 = math.sqrt(0.5 * (OVER_00_S[q] + rdm.random()))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + _1HWS[q]))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + _2AWS[q]))
                            bayesian_2_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + OVER_2_5_S[q]))
                            bayesian_3_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + OVER_3_5_S[q]))
                            bayesian_sh1_1_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + OVER_sh1_1_5_S[q]))
                            bayesian_sh1_2_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + OVER_sh1_2_5_S[q]))
                            bayesian_sh2_1_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + OVER_sh2_1_5_S[q]))
                            bayesian_sh2_2_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + OVER_sh2_2_5_S[q]))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q]))
                            bayesian_00 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + OVER_00_S[q]))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_2_5 = math.sqrt(rdm.random() * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                            bayesian_3_5 = math.sqrt(rdm.random() * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                            bayesian_sh1_1_5 = math.sqrt(rdm.random() * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                            bayesian_sh1_2_5 = math.sqrt(rdm.random() * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                            bayesian_sh2_1_5 = math.sqrt(rdm.random() * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                            bayesian_sh2_2_5 = math.sqrt(rdm.random() * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                            bayesian_12 = math.sqrt(rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            bayesian_00 = math.sqrt(rdm.random() * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_2_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                            bayesian_3_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                            bayesian_sh1_1_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                            bayesian_sh1_2_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                            bayesian_sh2_1_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                            bayesian_sh2_2_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            bayesian_00 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(_2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_2_5 = math.sqrt(OVER_2_5_S[q] * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                            bayesian_3_5 = math.sqrt(OVER_3_5_S[q] * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                            bayesian_sh1_1_5 = math.sqrt(OVER_sh1_1_5_S[q] * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                            bayesian_sh1_2_5 = math.sqrt(OVER_sh1_2_5_S[q] * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                            bayesian_sh2_1_5 = math.sqrt(OVER_sh2_1_5_S[q] * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                            bayesian_sh2_2_5 = math.sqrt(OVER_sh2_2_5_S[q] * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                            bayesian_12 = math.sqrt(_12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            bayesian_00 = math.sqrt(OVER_00_S[q] * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * rdm.random())
                            bayesian_2_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * rdm.random())
                            bayesian_3_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * rdm.random())
                            bayesian_sh1_1_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * rdm.random())
                            bayesian_sh1_2_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * rdm.random())
                            bayesian_sh2_1_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * rdm.random())
                            bayesian_sh2_2_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * rdm.random())
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random())
                            bayesian_00 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(_2AWS[q] * rdm.random())
                            bayesian_2_5 = math.sqrt(OVER_2_5_S[q] * rdm.random())
                            bayesian_3_5 = math.sqrt(OVER_3_5_S[q] * rdm.random())
                            bayesian_sh1_1_5 = math.sqrt(OVER_sh1_1_5_S[q] * rdm.random())
                            bayesian_sh1_2_5 = math.sqrt(OVER_sh1_2_5_S[q] * rdm.random())
                            bayesian_sh2_1_5 = math.sqrt(OVER_sh2_1_5_S[q] * rdm.random())
                            bayesian_sh2_2_5 = math.sqrt(OVER_sh2_2_5_S[q] * rdm.random())
                            bayesian_12 = math.sqrt(_12S[q] * rdm.random())
                            bayesian_00 = math.sqrt(OVER_00_S[q] * rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * _1HWS[q])
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * _2AWS[q])
                            bayesian_2_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * OVER_2_5_S[q])
                            bayesian_3_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * OVER_3_5_S[q])
                            bayesian_sh1_1_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * OVER_sh1_1_5_S[q])
                            bayesian_sh1_2_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * OVER_sh1_2_5_S[q])
                            bayesian_sh2_1_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * OVER_sh2_1_5_S[q])
                            bayesian_sh2_2_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * OVER_sh2_2_5_S[q])
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q])
                            bayesian_00 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * OVER_00_S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    except IndexError:
                        traceback.print_exc()
                        continue

                for q in range(len(bayesian_home_Win_d)):
                    if q == 0:
                        for i in range(11):
                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                           f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|BAYESIAN {OUTCOMES[0]}|"
                                           f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                           f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                           f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                    try:
                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if h_form_D[q] == 0 and a_form_D[q] == 0:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if h_form_D[q] == 0 or a_form_D[q] == 0:
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    except UnicodeError:
                        pass
                    except IndexError:
                        continue
                    except OSError:
                        pass
                for i in range(11):
                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                        file.write("\n\n\n\n\n")

        for PROB in PROB_METRICS:
            X = PROB
            Y = "ANALYSIS"
            Z = "STANDARD"
            bayesian_home_Win_d = []
            bayesian_away_Win_d = []
            bayesian_2_5_d = []
            bayesian_3_5_d = []
            bayesian_sh1_1_5_d = []
            bayesian_sh1_2_5_d = []
            bayesian_sh2_1_5_d = []
            bayesian_sh2_2_5_d = []
            bayesian_12_d = []
            bayesian_00_d = []

            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS[0]:
                        bayesian_home_Win = (prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))
                        bayesian_away_Win = (prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))
                        bayesian_2_5 = (prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))
                        bayesian_3_5 = (prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))
                        bayesian_sh1_1_5 = (prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))
                        bayesian_sh1_2_5 = (prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))
                        bayesian_sh2_1_5 = (prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))
                        bayesian_sh2_2_5 = (prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))
                        bayesian_12 = (prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))
                        bayesian_00 = (prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    if X == PROB_METRICS[1]:
                        prob_matches_home_W_against_EO = rdm.random()
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_2_5 = rdm.random()
                        prob_2_5_indp_home = rdm.random()
                        prob_2_5_indp_away = rdm.random()
                        bayesian_2_5 = (prob_2_5 * (prob_2_5_indp_home * prob_2_5_indp_away)) / ((prob_2_5 * (prob_2_5_indp_home * prob_2_5_indp_away)) + ((1 - (prob_2_5_indp_home * prob_2_5_indp_away)) * (1 - prob_2_5)))
                        prob_3_5 = rdm.random()
                        prob_3_5_indp_home = rdm.random()
                        prob_3_5_indp_away = rdm.random()
                        bayesian_3_5 = (prob_3_5 * (prob_3_5_indp_home * prob_3_5_indp_away)) / ((prob_3_5 * (prob_3_5_indp_home * prob_3_5_indp_away)) + ((1 - (prob_3_5_indp_home * prob_3_5_indp_away)) * (1 - prob_3_5)))
                        prob_sh1_1_5 = rdm.random()
                        prob_sh1_1_5_indp_home = rdm.random()
                        prob_sh1_1_5_indp_away = rdm.random()
                        bayesian_sh1_1_5 = (prob_sh1_1_5 * (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) / ((prob_sh1_1_5 * (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) + ((1 - (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) * (1 - prob_sh1_1_5)))
                        prob_sh1_2_5 = rdm.random()
                        prob_sh1_2_5_indp_home = rdm.random()
                        prob_sh1_2_5_indp_away = rdm.random()
                        bayesian_sh1_2_5 = (prob_sh1_2_5 * (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) / ((prob_sh1_2_5 * (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) + ((1 - (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) * (1 - prob_sh1_2_5)))
                        prob_sh2_1_5 = rdm.random()
                        prob_sh2_1_5_indp_home = rdm.random()
                        prob_sh2_1_5_indp_away = rdm.random()
                        bayesian_sh2_1_5 = (prob_sh2_1_5 * (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) / ((prob_sh2_1_5 * (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) + ((1 - (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) * (1 - prob_sh2_1_5)))
                        prob_sh2_2_5 = rdm.random()
                        prob_sh2_2_5_indp_home = rdm.random()
                        prob_sh2_2_5_indp_away = rdm.random()
                        bayesian_sh2_2_5 = (prob_sh2_2_5 * (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) / ((prob_sh2_2_5 * (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) + ((1 - (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) * (1 - prob_sh2_2_5)))
                        prob_12 = rdm.random()
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        prob_00 = rdm.random()
                        prob_00_indp_home = rdm.random()
                        prob_00_indp_away = rdm.random()
                        bayesian_00 = (prob_00 * (prob_00_indp_home * prob_00_indp_away)) / ((prob_00 * (prob_00_indp_home * prob_00_indp_away)) + ((1 - (prob_00_indp_home * prob_00_indp_away)) * (1 - prob_00)))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    if X == PROB_METRICS[2]:
                        bayesian_home_Win = home_z_prob[q]
                        bayesian_away_Win = away_z_prob[q]
                        bayesian_2_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))
                        bayesian_3_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))
                        bayesian_sh1_1_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))
                        bayesian_sh1_2_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))
                        bayesian_sh2_1_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))
                        bayesian_sh2_2_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        bayesian_00 = math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    if X == PROB_METRICS[3]:
                        bayesian_home_Win = _1HWS[q]
                        bayesian_away_Win = _2AWS[q]
                        bayesian_2_5 = OVER_2_5_S[q]
                        bayesian_3_5 = OVER_3_5_S[q]
                        bayesian_sh1_1_5 = OVER_sh1_1_5_S[q]
                        bayesian_sh1_2_5 = OVER_sh1_2_5_S[q]
                        bayesian_sh2_1_5 = OVER_sh2_1_5_S[q]
                        bayesian_sh2_2_5 = OVER_sh2_2_5_S[q]
                        bayesian_12 = _12S[q]
                        bayesian_00 = OVER_00_S[q]
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    if X == PROB_METRICS[4]:
                        bayesian_home_Win = home_z_prob[q] * diff_z_prob[q]
                        bayesian_away_Win = away_z_prob[q] * diff_z_prob[q]
                        bayesian_2_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q])) * diff_z_prob[q]
                        bayesian_3_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q])) * diff_z_prob[q]
                        bayesian_sh1_1_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q])) * diff_z_prob[q]
                        bayesian_sh1_2_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q])) * diff_z_prob[q]
                        bayesian_sh2_1_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q])) * diff_z_prob[q]
                        bayesian_sh2_2_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q])) * diff_z_prob[q]
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])) * diff_z_prob[q]
                        bayesian_00 = math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q])) * diff_z_prob[q]
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                except IndexError:
                    traceback.print_exc()
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|BAYESIAN {OUTCOMES[0]}|"
                                       f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                       f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                       f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                        if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                        if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                        if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                        if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                except UnicodeError:
                    pass
                except IndexError:
                    continue
                except OSError:
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                    file.write("\n\n\n\n\n")

        for COMB in COMB_PROB_METRICS2:
            X, Y = COMB
            Z = "COMBINATE"
            bayesian_home_Win_d = []
            bayesian_away_Win_d = []
            bayesian_2_5_d = []
            bayesian_3_5_d = []
            bayesian_sh1_1_5_d = []
            bayesian_sh1_2_5_d = []
            bayesian_sh2_1_5_d = []
            bayesian_sh2_2_5_d = []
            bayesian_12_d = []
            bayesian_00_d = []

            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[1]:
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_HWs[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_HWs[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_HWs[q])))
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_AWs[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_AWs[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_AWs[q])))
                        prob_2_5_indp_home = rdm.random()
                        prob_2_5_indp_away = rdm.random()
                        bayesian_2_5 = (prob_2_5s[q] * (prob_2_5_indp_home * prob_2_5_indp_away)) / ((prob_2_5s[q] * (prob_2_5_indp_home * prob_2_5_indp_away)) + ((1 - (prob_2_5_indp_home * prob_2_5_indp_away)) * (1 - prob_2_5s[q])))
                        prob_3_5_indp_home = rdm.random()
                        prob_3_5_indp_away = rdm.random()
                        bayesian_3_5 = (prob_3_5s[q] * (prob_3_5_indp_home * prob_3_5_indp_away)) / ((prob_3_5s[q] * (prob_3_5_indp_home * prob_3_5_indp_away)) + ((1 - (prob_3_5_indp_home * prob_3_5_indp_away)) * (1 - prob_3_5s[q])))
                        prob_sh1_1_5_indp_home = rdm.random()
                        prob_sh1_1_5_indp_away = rdm.random()
                        bayesian_sh1_1_5 = (prob_sh1_1_5s[q] * (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) + ((1 - (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) * (1 - prob_sh1_1_5s[q])))
                        prob_sh1_2_5_indp_home = rdm.random()
                        prob_sh1_2_5_indp_away = rdm.random()
                        bayesian_sh1_2_5 = (prob_sh1_2_5s[q] * (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) + ((1 - (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) * (1 - prob_sh1_2_5s[q])))
                        prob_sh2_1_5_indp_home = rdm.random()
                        prob_sh2_1_5_indp_away = rdm.random()
                        bayesian_sh2_1_5 = (prob_sh2_1_5s[q] * (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) + ((1 - (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) * (1 - prob_sh2_1_5s[q])))
                        prob_sh2_2_5_indp_home = rdm.random()
                        prob_sh2_2_5_indp_away = rdm.random()
                        bayesian_sh2_2_5 = (prob_sh2_2_5s[q] * (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) + ((1 - (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) * (1 - prob_sh2_2_5s[q])))
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12s[q])))
                        prob_00_indp_home = rdm.random()
                        prob_00_indp_away = rdm.random()
                        bayesian_00 = (prob_00s[q] * (prob_00_indp_home * prob_00_indp_away)) / ((prob_00s[q] * (prob_00_indp_home * prob_00_indp_away)) + ((1 - (prob_00_indp_home * prob_00_indp_away)) * (1 - prob_00s[q])))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[2]:
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - home_z_prob[q])))
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - away_z_prob[q])))
                        prob_2_5_indp_home = rdm.random()
                        prob_2_5_indp_away = rdm.random()
                        bayesian_2_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * (prob_2_5_indp_home * prob_2_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * (prob_2_5_indp_home * prob_2_5_indp_away)) + ((1 - (prob_2_5_indp_home * prob_2_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q])))))))
                        prob_3_5_indp_home = rdm.random()
                        prob_3_5_indp_away = rdm.random()
                        bayesian_3_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * (prob_3_5_indp_home * prob_3_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * (prob_3_5_indp_home * prob_3_5_indp_away)) + ((1 - (prob_3_5_indp_home * prob_3_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q])))))))
                        prob_sh1_1_5_indp_home = rdm.random()
                        prob_sh1_1_5_indp_away = rdm.random()
                        bayesian_sh1_1_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) + ((1 - (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q])))))))
                        prob_sh1_2_5_indp_home = rdm.random()
                        prob_sh1_2_5_indp_away = rdm.random()
                        bayesian_sh1_2_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) + ((1 - (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q])))))))
                        prob_sh2_1_5_indp_home = rdm.random()
                        prob_sh2_1_5_indp_away = rdm.random()
                        bayesian_sh2_1_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) + ((1 - (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q])))))))
                        prob_sh2_2_5_indp_home = rdm.random()
                        prob_sh2_2_5_indp_away = rdm.random()
                        bayesian_sh2_2_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) + ((1 - (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q])))))))
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])))))))
                        prob_00_indp_home = rdm.random()
                        prob_00_indp_away = rdm.random()
                        bayesian_00 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * (prob_00_indp_home * prob_00_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * (prob_00_indp_home * prob_00_indp_away)) + ((1 - (prob_00_indp_home * prob_00_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q])))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[3]:
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - _1HWS[q])))
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - _2AWS[q])))
                        prob_2_5_indp_home = rdm.random()
                        prob_2_5_indp_away = rdm.random()
                        bayesian_2_5 = (OVER_2_5_S[q] * (prob_2_5_indp_home * prob_2_5_indp_away)) / ((OVER_2_5_S[q] * (prob_2_5_indp_home * prob_2_5_indp_away)) + ((1 - (prob_2_5_indp_home * prob_2_5_indp_away)) * (1 - OVER_2_5_S[q])))
                        prob_3_5_indp_home = rdm.random()
                        prob_3_5_indp_away = rdm.random()
                        bayesian_3_5 = (OVER_3_5_S[q] * (prob_3_5_indp_home * prob_3_5_indp_away)) / ((OVER_3_5_S[q] * (prob_3_5_indp_home * prob_3_5_indp_away)) + ((1 - (prob_3_5_indp_home * prob_3_5_indp_away)) * (1 - OVER_3_5_S[q])))
                        prob_sh1_1_5_indp_home = rdm.random()
                        prob_sh1_1_5_indp_away = rdm.random()
                        bayesian_sh1_1_5 = (OVER_sh1_1_5_S[q] * (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) / ((OVER_sh1_1_5_S[q] * (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) + ((1 - (prob_sh1_1_5_indp_home * prob_sh1_1_5_indp_away)) * (1 - OVER_sh1_1_5_S[q])))
                        prob_sh1_2_5_indp_home = rdm.random()
                        prob_sh1_2_5_indp_away = rdm.random()
                        bayesian_sh1_2_5 = (OVER_sh1_2_5_S[q] * (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) / ((OVER_sh1_2_5_S[q] * (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) + ((1 - (prob_sh1_2_5_indp_home * prob_sh1_2_5_indp_away)) * (1 - OVER_sh1_2_5_S[q])))
                        prob_sh2_1_5_indp_home = rdm.random()
                        prob_sh2_1_5_indp_away = rdm.random()
                        bayesian_sh2_1_5 = (OVER_sh2_1_5_S[q] * (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) / ((OVER_sh2_1_5_S[q] * (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) + ((1 - (prob_sh2_1_5_indp_home * prob_sh2_1_5_indp_away)) * (1 - OVER_sh2_1_5_S[q])))
                        prob_sh2_2_5_indp_home = rdm.random()
                        prob_sh2_2_5_indp_away = rdm.random()
                        bayesian_sh2_2_5 = (OVER_sh2_2_5_S[q] * (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) / ((OVER_sh2_2_5_S[q] * (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) + ((1 - (prob_sh2_2_5_indp_home * prob_sh2_2_5_indp_away)) * (1 - OVER_sh2_2_5_S[q])))
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (_12S[q] * (prob_12_indp_home * prob_12_indp_away)) / ((_12S[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - _12S[q])))
                        prob_00_indp_home = rdm.random()
                        prob_00_indp_away = rdm.random()
                        bayesian_00 = (OVER_00_S[q] * (prob_00_indp_home * prob_00_indp_away)) / ((OVER_00_S[q] * (prob_00_indp_home * prob_00_indp_away)) + ((1 - (prob_00_indp_home * prob_00_indp_away)) * (1 - OVER_00_S[q])))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0]:
                        prob_matches_home_W_against_EO = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_matches_away_W_against_EO)))
                        prob_2_5 = rdm.random()
                        bayesian_2_5 = ((prob_2_5 * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5 * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5))))
                        prob_3_5 = rdm.random()
                        bayesian_3_5 = ((prob_3_5 * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5 * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5))))
                        prob_sh1_1_5 = rdm.random()
                        bayesian_sh1_1_5 = ((prob_sh1_1_5 * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5 * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5))))
                        prob_sh1_2_5 = rdm.random()
                        bayesian_sh1_2_5 = ((prob_sh1_2_5 * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5 * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5))))
                        prob_sh2_1_5 = rdm.random()
                        bayesian_sh2_1_5 = ((prob_sh2_1_5 * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5 * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5))))
                        prob_sh2_2_5 = rdm.random()
                        bayesian_sh2_2_5 = ((prob_sh2_2_5 * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5 * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5))))
                        prob_12 = rdm.random()
                        bayesian_12 = ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12))))
                        prob_00 = rdm.random()
                        bayesian_00 = ((prob_00 * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00 * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[2]:
                        bayesian_home_Win = (home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - home_z_prob[q])))
                        bayesian_away_Win = (away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - away_z_prob[q])))
                        bayesian_2_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))))))
                        bayesian_3_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))))))
                        bayesian_sh1_1_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))))))
                        bayesian_sh1_2_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))))))
                        bayesian_sh2_1_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))))))
                        bayesian_sh2_2_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))))))
                        bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))))))
                        bayesian_00 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * (prob_00_H_indps[q] * prob_00_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[3]:
                        bayesian_home_Win = (_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - _1HWS[q])))
                        bayesian_away_Win = (_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - _2AWS[q])))
                        bayesian_2_5 = (OVER_2_5_S[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((OVER_2_5_S[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - OVER_2_5_S[q])))
                        bayesian_3_5 = (OVER_3_5_S[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((OVER_3_5_S[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - OVER_3_5_S[q])))
                        bayesian_sh1_1_5 = (OVER_sh1_1_5_S[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((OVER_sh1_1_5_S[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - OVER_sh1_1_5_S[q])))
                        bayesian_sh1_2_5 = (OVER_sh1_2_5_S[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((OVER_sh1_2_5_S[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - OVER_sh1_2_5_S[q])))
                        bayesian_sh2_1_5 = (OVER_sh2_1_5_S[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((OVER_sh2_1_5_S[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - OVER_sh2_1_5_S[q])))
                        bayesian_sh2_2_5 = (OVER_sh2_2_5_S[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((OVER_sh2_2_5_S[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - OVER_sh2_2_5_S[q])))
                        bayesian_12 = (_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - _12S[q])))
                        bayesian_00 = (OVER_00_S[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((OVER_00_S[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - OVER_00_S[q])))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)
                except IndexError:
                    traceback.print_exc()
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|BAYESIAN {OUTCOMES[0]}|"
                                       f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                       f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                       f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                        if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                        if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                        if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                        if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                except UnicodeError:
                    pass
                except IndexError:
                    traceback.print_exc()
                    continue
                except OSError:
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                    file.write("\n\n\n\n\n")

        for COMBINER in COMBINERS:
            Z = COMBINER
            if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[6] and Z != COMBINERS[7]:
                for COMB in COMB_PROB_METRICS3:
                    W, X, Y = COMB
                    bayesian_home_Win_d = []
                    bayesian_away_Win_d = []
                    bayesian_2_5_d = []
                    bayesian_3_5_d = []
                    bayesian_sh1_1_5_d = []
                    bayesian_sh1_2_5_d = []
                    bayesian_sh2_1_5_d = []
                    bayesian_sh2_2_5_d = []
                    bayesian_12_d = []
                    bayesian_00_d = []

                    for q in range(len(home_teams)):
                        try:
                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_2_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + rdm.random() + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                                bayesian_3_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + rdm.random() + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                                bayesian_sh1_1_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + rdm.random() + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                                bayesian_sh1_2_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + rdm.random() + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                                bayesian_sh2_1_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + rdm.random() + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                                bayesian_sh2_2_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + rdm.random() + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                bayesian_00 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + rdm.random() + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * rdm.random() * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))
                                bayesian_3_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * rdm.random() * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))
                                bayesian_sh1_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * rdm.random() * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))
                                bayesian_sh1_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * rdm.random() * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))
                                bayesian_sh2_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * rdm.random() * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))
                                bayesian_sh2_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * rdm.random() * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                bayesian_00 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * rdm.random() * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + rdm.random() + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))))
                                bayesian_3_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + rdm.random() + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))))
                                bayesian_sh1_1_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + rdm.random() + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))))
                                bayesian_sh1_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + rdm.random() + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))))
                                bayesian_sh2_1_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + rdm.random() + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))))
                                bayesian_sh2_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + rdm.random() + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                bayesian_00 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + rdm.random() + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + rdm.random() + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))))
                                bayesian_3_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + rdm.random() + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))))
                                bayesian_sh1_1_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + rdm.random() + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))))
                                bayesian_sh1_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + rdm.random() + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))))
                                bayesian_sh2_1_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + rdm.random() + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))))
                                bayesian_sh2_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + rdm.random() + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                bayesian_00 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + rdm.random() + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_2_5 = (1 / 3) * (OVER_2_5_S[q] + rdm.random() + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                                bayesian_3_5 = (1 / 3) * (OVER_3_5_S[q] + rdm.random() + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                                bayesian_sh1_1_5 = (1 / 3) * (OVER_sh1_1_5_S[q] + rdm.random() + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                                bayesian_sh1_2_5 = (1 / 3) * (OVER_sh1_2_5_S[q] + rdm.random() + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                                bayesian_sh2_1_5 = (1 / 3) * (OVER_sh2_1_5_S[q] + rdm.random() + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                                bayesian_sh2_2_5 = (1 / 3) * (OVER_sh2_2_5_S[q] + rdm.random() + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                                bayesian_12 = (1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                bayesian_00 = (1 / 3) * (OVER_00_S[q] + rdm.random() + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = _1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = _2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_2_5 = OVER_2_5_S[q] * rdm.random() * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))
                                bayesian_3_5 = OVER_3_5_S[q] * rdm.random() * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))
                                bayesian_sh1_1_5 = OVER_sh1_1_5_S[q] * rdm.random() * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))
                                bayesian_sh1_2_5 = OVER_sh1_2_5_S[q] * rdm.random() * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))
                                bayesian_sh2_1_5 = OVER_sh2_1_5_S[q] * rdm.random() * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))
                                bayesian_sh2_2_5 = OVER_sh2_2_5_S[q] * rdm.random() * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))
                                bayesian_12 = _12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                bayesian_00 = OVER_00_S[q] * rdm.random() * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_2_5 = np.cbrt((1 / 3) * (OVER_2_5_S[q] + rdm.random() + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))))
                                bayesian_3_5 = np.cbrt((1 / 3) * (OVER_3_5_S[q] + rdm.random() + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))))
                                bayesian_sh1_1_5 = np.cbrt((1 / 3) * (OVER_sh1_1_5_S[q] + rdm.random() + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))))
                                bayesian_sh1_2_5 = np.cbrt((1 / 3) * (OVER_sh1_2_5_S[q] + rdm.random() + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))))
                                bayesian_sh2_1_5 = np.cbrt((1 / 3) * (OVER_sh2_1_5_S[q] + rdm.random() + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))))
                                bayesian_sh2_2_5 = np.cbrt((1 / 3) * (OVER_sh2_2_5_S[q] + rdm.random() + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                bayesian_00 = np.cbrt((1 / 3) * (OVER_00_S[q] + rdm.random() + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(_1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(_2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_2_5 = np.cbrt(OVER_2_5_S[q] * rdm.random() * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                                bayesian_3_5 = np.cbrt(OVER_3_5_S[q] * rdm.random() * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                                bayesian_sh1_1_5 = np.cbrt(OVER_sh1_1_5_S[q] * rdm.random() * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                                bayesian_sh1_2_5 = np.cbrt(OVER_sh1_2_5_S[q] * rdm.random() * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                                bayesian_sh2_1_5 = np.cbrt(OVER_sh2_1_5_S[q] * rdm.random() * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                                bayesian_sh2_2_5 = np.cbrt(OVER_sh2_2_5_S[q] * rdm.random() * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                                bayesian_12 = np.cbrt(_12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                bayesian_00 = np.cbrt(OVER_00_S[q] * rdm.random() * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_2_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + OVER_2_5_S[q] + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                                bayesian_3_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + OVER_3_5_S[q] + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                                bayesian_sh1_1_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + OVER_sh1_1_5_S[q] + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                                bayesian_sh1_2_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + OVER_sh1_2_5_S[q] + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                                bayesian_sh2_1_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + OVER_sh2_1_5_S[q] + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                                bayesian_sh2_2_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + OVER_sh2_2_5_S[q] + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                bayesian_00 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + OVER_00_S[q] + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * OVER_2_5_S[q] * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))
                                bayesian_3_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * OVER_3_5_S[q] * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))
                                bayesian_sh1_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * OVER_sh1_1_5_S[q] * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))
                                bayesian_sh1_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * OVER_sh1_2_5_S[q] * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))
                                bayesian_sh2_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * OVER_sh2_1_5_S[q] * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))
                                bayesian_sh2_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * OVER_sh2_2_5_S[q] * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                bayesian_00 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * OVER_00_S[q] * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + OVER_2_5_S[q] + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))))
                                bayesian_3_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + OVER_3_5_S[q] + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))))
                                bayesian_sh1_1_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + OVER_sh1_1_5_S[q] + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))))
                                bayesian_sh1_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + OVER_sh1_2_5_S[q] + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))))
                                bayesian_sh2_1_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + OVER_sh2_1_5_S[q] + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))))
                                bayesian_sh2_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + OVER_sh2_2_5_S[q] + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                bayesian_00 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + OVER_00_S[q] + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_2_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * OVER_2_5_S[q] * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                                bayesian_3_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * OVER_3_5_S[q] * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                                bayesian_sh1_1_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * OVER_sh1_1_5_S[q] * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                                bayesian_sh1_2_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * OVER_sh1_2_5_S[q] * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                                bayesian_sh2_1_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * OVER_sh2_1_5_S[q] * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                                bayesian_sh2_2_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * OVER_sh2_2_5_S[q] * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                bayesian_00 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * OVER_00_S[q] * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q])
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q])
                                bayesian_2_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + rdm.random() + OVER_2_5_S[q])
                                bayesian_3_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + rdm.random() + OVER_3_5_S[q])
                                bayesian_sh1_1_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + rdm.random() + OVER_sh1_1_5_S[q])
                                bayesian_sh1_2_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + rdm.random() + OVER_sh1_2_5_S[q])
                                bayesian_sh2_1_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + rdm.random() + OVER_sh2_1_5_S[q])
                                bayesian_sh2_2_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + rdm.random() + OVER_sh2_2_5_S[q])
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q])
                                bayesian_00 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + rdm.random() + OVER_00_S[q])
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q]
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q]
                                bayesian_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * rdm.random() * OVER_2_5_S[q]
                                bayesian_3_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * rdm.random() * OVER_3_5_S[q]
                                bayesian_sh1_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * rdm.random() * OVER_sh1_1_5_S[q]
                                bayesian_sh1_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * rdm.random() * OVER_sh1_2_5_S[q]
                                bayesian_sh2_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * rdm.random() * OVER_sh2_1_5_S[q]
                                bayesian_sh2_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * rdm.random() * OVER_sh2_2_5_S[q]
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q]
                                bayesian_00 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * rdm.random() * OVER_00_S[q]
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q]))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q]))
                                bayesian_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + rdm.random() + OVER_2_5_S[q]))
                                bayesian_3_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + rdm.random() + OVER_3_5_S[q]))
                                bayesian_sh1_1_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + rdm.random() + OVER_sh1_1_5_S[q]))
                                bayesian_sh1_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + rdm.random() + OVER_sh1_2_5_S[q]))
                                bayesian_sh2_1_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + rdm.random() + OVER_sh2_1_5_S[q]))
                                bayesian_sh2_2_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + rdm.random() + OVER_sh2_2_5_S[q]))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q]))
                                bayesian_00 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + rdm.random() + OVER_00_S[q]))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * rdm.random() * _1HWS[q])
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * rdm.random() * _2AWS[q])
                                bayesian_2_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * rdm.random() * OVER_2_5_S[q])
                                bayesian_3_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * rdm.random() * OVER_3_5_S[q])
                                bayesian_sh1_1_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * rdm.random() * OVER_sh1_1_5_S[q])
                                bayesian_sh1_2_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * rdm.random() * OVER_sh1_2_5_S[q])
                                bayesian_sh2_1_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * rdm.random() * OVER_sh2_1_5_S[q])
                                bayesian_sh2_2_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * rdm.random() * OVER_sh2_2_5_S[q])
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q])
                                bayesian_00 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * rdm.random() * OVER_00_S[q])
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        except IndexError:
                            traceback.print_exc()
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|BAYESIAN {OUTCOMES[0]}|"
                                               f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                               f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                               f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                    if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                    if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                    if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                    if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                    if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                    if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                    if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[0] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        except UnicodeError:
                            pass
                        except IndexError:
                            continue
                        except OSError:
                            pass
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                            file.write("\n\n\n\n\n")

        for COMBINER in COMBINERS:
            Z = COMBINER
            if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[4] and Z != COMBINERS[5]:
                for COMB in COMB_PROB_METRICS4:
                    V, W, X, Y = COMB
                    bayesian_home_Win_d = []
                    bayesian_away_Win_d = []
                    bayesian_2_5_d = []
                    bayesian_3_5_d = []
                    bayesian_sh1_1_5_d = []
                    bayesian_sh1_2_5_d = []
                    bayesian_sh2_1_5_d = []
                    bayesian_sh2_2_5_d = []
                    bayesian_12_d = []
                    bayesian_00_d = []

                    for q in range(len(home_teams)):
                        try:
                            if Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_2_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + rdm.random() + OVER_2_5_S[q] + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))
                                bayesian_3_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + rdm.random() + OVER_3_5_S[q] + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))
                                bayesian_sh1_1_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + rdm.random() + OVER_sh1_1_5_S[q] + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))
                                bayesian_sh1_2_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + rdm.random() + OVER_sh1_2_5_S[q] + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))
                                bayesian_sh2_1_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + rdm.random() + OVER_sh2_1_5_S[q] + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))
                                bayesian_sh2_2_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + rdm.random() + OVER_sh2_2_5_S[q] + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))
                                bayesian_12 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                bayesian_00 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + rdm.random() + OVER_00_S[q] + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * rdm.random() * OVER_2_5_S[q] * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))
                                bayesian_3_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * rdm.random() * OVER_3_5_S[q] * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))
                                bayesian_sh1_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * rdm.random() * OVER_sh1_1_5_S[q] * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))
                                bayesian_sh1_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * rdm.random() * OVER_sh1_2_5_S[q] * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))
                                bayesian_sh2_1_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * rdm.random() * OVER_sh2_1_5_S[q] * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))
                                bayesian_sh2_2_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * rdm.random() * OVER_sh2_2_5_S[q] * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                bayesian_00 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * rdm.random() * OVER_00_S[q] * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if Z == COMBINERS[6]:
                                bayesian_home_Win = ((1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))) ** 0.25
                                bayesian_away_Win = ((1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))) ** 0.25
                                bayesian_2_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) + rdm.random() + OVER_2_5_S[q] + ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q])))))) ** 0.25
                                bayesian_3_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) + rdm.random() + OVER_3_5_S[q] + ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q])))))) ** 0.25
                                bayesian_sh1_1_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) + rdm.random() + OVER_sh1_1_5_S[q] + ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q])))))) ** 0.25
                                bayesian_sh1_2_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) + rdm.random() + OVER_sh1_2_5_S[q] + ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q])))))) ** 0.25
                                bayesian_sh2_1_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) + rdm.random() + OVER_sh2_1_5_S[q] + ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q])))))) ** 0.25
                                bayesian_sh2_2_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) + rdm.random() + OVER_sh2_2_5_S[q] + ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q])))))) ** 0.25
                                bayesian_12 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))) ** 0.25
                                bayesian_00 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) + rdm.random() + OVER_00_S[q] + ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q])))))) ** 0.25
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                            if Z == COMBINERS[7]:
                                bayesian_home_Win = (home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))) ** 0.25
                                bayesian_away_Win = (away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))) ** 0.25
                                bayesian_2_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_2_5s[q]))) * rdm.random() * OVER_2_5_S[q] * ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) / ((prob_2_5s[q] * (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) + ((1 - (prob_2_5_H_indps[q] * prob_2_5_A_indps[q])) * (1 - prob_2_5s[q]))))) ** 0.25
                                bayesian_3_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_3_5s[q]))) * rdm.random() * OVER_3_5_S[q] * ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) / ((prob_3_5s[q] * (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) + ((1 - (prob_3_5_H_indps[q] * prob_3_5_A_indps[q])) * (1 - prob_3_5s[q]))))) ** 0.25
                                bayesian_sh1_1_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_1_5s[q]))) * rdm.random() * OVER_sh1_1_5_S[q] * ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) / ((prob_sh1_1_5s[q] * (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) + ((1 - (prob_sh1_1_5_H_indps[q] * prob_sh1_1_5_A_indps[q])) * (1 - prob_sh1_1_5s[q]))))) ** 0.25
                                bayesian_sh1_2_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_2_5s[q]))) * rdm.random() * OVER_sh1_2_5_S[q] * ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) / ((prob_sh1_2_5s[q] * (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) + ((1 - (prob_sh1_2_5_H_indps[q] * prob_sh1_2_5_A_indps[q])) * (1 - prob_sh1_2_5s[q]))))) ** 0.25
                                bayesian_sh2_1_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_1_5s[q]))) * rdm.random() * OVER_sh2_1_5_S[q] * ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) / ((prob_sh2_1_5s[q] * (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) + ((1 - (prob_sh2_1_5_H_indps[q] * prob_sh2_1_5_A_indps[q])) * (1 - prob_sh2_1_5s[q]))))) ** 0.25
                                bayesian_sh2_2_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_2_5s[q]))) * rdm.random() * OVER_sh2_2_5_S[q] * ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) / ((prob_sh2_2_5s[q] * (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) + ((1 - (prob_sh2_2_5_H_indps[q] * prob_sh2_2_5_A_indps[q])) * (1 - prob_sh2_2_5s[q]))))) ** 0.25
                                bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))) ** 0.25
                                bayesian_00 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_00s[q]))) * rdm.random() * OVER_00_S[q] * ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) / ((prob_00s[q] * (prob_00_H_indps[q] * prob_00_A_indps[q])) + ((1 - (prob_00_H_indps[q] * prob_00_A_indps[q])) * (1 - prob_00s[q]))))) ** 0.25
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_2_5=bayesian_2_5, baye_3_5=bayesian_3_5, baye_sh1_1_5=bayesian_sh1_1_5, baye_sh1_2_5=bayesian_sh1_2_5, baye_sh2_1_5=bayesian_sh2_1_5, baye_sh2_2_5=bayesian_sh2_2_5, baye_12=bayesian_12, baye_00=bayesian_00)

                        except IndexError:
                            traceback.print_exc()
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|BAYESIAN {OUTCOMES[0]}|"
                                               f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                               f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                               f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                        writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                        writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                        writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                        writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                        writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                        writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                            if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                        writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_2_5_d[q] > CONFINTVL or bayesian_sh1_1_5_d[q] > CONFINTVL or bayesian_sh2_1_5_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (bayesian_sh1_1_5_d[q] >= bayesian_sh2_1_5_d[q]) and (bayesian_sh1_2_5_d[q] >= bayesian_sh2_2_5_d[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((h_form_W[q] + h_form_D[q]) >= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (bayesian_sh2_1_5_d[q] >= bayesian_sh1_1_5_d[q]) and (bayesian_sh2_2_5_d[q] >= bayesian_sh1_2_5_d[q]) and (home_points[q] <= away_points[q]) and ((h_form_W[q] + h_form_D[q]) <= (a_form_W[q] + a_form_D[q])) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])))):
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if bayesian_3_5_d[q] <= bayesian_2_5_d[q] <= bayesian_00_d[q] and bayesian_3_5_d[q] <= (1 - (CONFINTVLS[-1])) and bayesian_sh1_2_5_d[q] >= bayesian_sh1_1_5_d[q] and bayesian_sh1_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and bayesian_sh2_2_5_d[q] >= bayesian_sh2_1_5_d[q] and bayesian_sh2_2_5_d[q] >= rdm.choice(CONFINTVLS[:2]) and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= rdm.choice(CONFINTVLS[:2]):
                                            if bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        except UnicodeError:
                            pass
                        except IndexError:
                            continue
                        except OSError:
                            pass
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                            file.write("\n\n\n\n\n")

    for CONFINTVL_ALT in CONFINTVLS_ALT:
        for COMBINER in COMBINERS[:4]:
            Z = COMBINER
            for COMB in COMB_PROB_METRICS1:
                X, Y = COMB
                bayesian_home_Win_d = []
                bayesian_away_Win_d = []
                bayesian_12_d = []

                for q in range(len(home_teams)):
                    try:
                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + rdm.random())
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random())
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (_2AWS[q] + rdm.random())
                            bayesian_12 = 0.5 * (_12S[q] + rdm.random())
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + _1HWS[q])
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + _2AWS[q])
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q])
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[1]:
                            bayesian_home_Win = rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random()
                            bayesian_away_Win = away_z_prob[q] * rdm.random()
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random()
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * rdm.random()
                            bayesian_away_Win = _2AWS[q] * rdm.random()
                            bayesian_12 = _12S[q] * rdm.random()
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * _1HWS[q]
                            bayesian_away_Win = away_z_prob[q] * _2AWS[q]
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q]
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random()))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + rdm.random()))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + _1HWS[q]))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + _2AWS[q]))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q]))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt(rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(_2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt(_12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * rdm.random())
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random())
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(_2AWS[q] * rdm.random())
                            bayesian_12 = math.sqrt(_12S[q] * rdm.random())
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * _1HWS[q])
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * _2AWS[q])
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q])
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    except IndexError:
                        continue

                for q in range(len(bayesian_home_Win_d)):
                    if q == 0:
                        for i in range(11):
                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                                file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_ALT}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                           f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                           f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                    try:
                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if h_form_D[q] == 0 and a_form_D[q] == 0:
                                    if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_0.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_0.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_1.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_1.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if ((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_2.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_2.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_W[q] > h_form_D[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_W[q] > a_form_D[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_3.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_3.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                if h_form_D[q] == 0 or a_form_D[q] == 0:
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_4.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_4.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_5.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_5.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_6.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_6.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_7.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_7.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                    if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_8.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_8.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_9.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_9.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_10.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_10.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    except UnicodeError:
                        pass
                    except IndexError:
                        continue
                    except OSError:
                        pass
                for i in range(11):
                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                        file.write("\n\n\n\n\n")

        for PROB in PROB_METRICS:
            X = PROB
            Y = "ANALYSIS"
            Z = "STANDARD"
            bayesian_home_Win_d = []
            bayesian_away_Win_d = []
            bayesian_12_d = []

            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS[0]:
                        bayesian_home_Win = (prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))
                        bayesian_away_Win = (prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))
                        bayesian_12 = (prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[1]:
                        prob_matches_home_W_against_EO = rdm.random()
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[2]:
                        bayesian_home_Win = home_z_prob[q]
                        bayesian_away_Win = away_z_prob[q]
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[3]:
                        bayesian_home_Win = _1HWS[q]
                        bayesian_away_Win = _2AWS[q]
                        bayesian_12 = _12S[q]
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[4]:
                        bayesian_home_Win = home_z_prob[q] * diff_z_prob[q]
                        bayesian_away_Win = away_z_prob[q] * diff_z_prob[q]
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])) * diff_z_prob[q]
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_ALT}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                       f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_0.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_0.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_1.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_1.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if ((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_2.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_2.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_W[q] > h_form_D[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_W[q] > a_form_D[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_3.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_3.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_4.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_4.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_5.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_5.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_6.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_6.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_7.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_7.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_8.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_8.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_9.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_9.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_10.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_10.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                except UnicodeError:
                    pass
                except IndexError:
                    continue
                except OSError:
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                    file.write("\n\n\n\n\n")

        for COMB in COMB_PROB_METRICS2:
            X, Y = COMB
            Z = "COMBINATE"
            bayesian_home_Win_d = []
            bayesian_away_Win_d = []
            bayesian_12_d = []

            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[1]:
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_HWs[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_HWs[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_HWs[q])))
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_AWs[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_AWs[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_AWs[q])))
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12s[q])))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[2]:
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - home_z_prob[q])))
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - away_z_prob[q])))
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])))))))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[3]:
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - _1HWS[q])))
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - _2AWS[q])))
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (_12S[q] * (prob_12_indp_home * prob_12_indp_away)) / ((_12S[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - _12S[q])))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0]:
                        prob_matches_home_W_against_EO = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        bayesian_12 = ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12))))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[2]:
                        bayesian_home_Win = (home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - home_z_prob[q])))
                        bayesian_away_Win = (away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - away_z_prob[q])))
                        bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))))))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[3]:
                        bayesian_home_Win = (_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - _1HWS[q])))
                        bayesian_away_Win = (_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - _2AWS[q])))
                        bayesian_12 = (_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - _12S[q])))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)
                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_ALT}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                       f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_0.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_0.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_1.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_1.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if ((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_2.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_2.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_W[q] > h_form_D[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_W[q] > a_form_D[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_3.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_3.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_4.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_4.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_5.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_5.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_6.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_6.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_7.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_7.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_8.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_8.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_9.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_9.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_10.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_10.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                except UnicodeError:
                    pass
                except IndexError:
                    continue
                except OSError:
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                    file.write("\n\n\n\n\n")

        for COMB in COMB_PROB_METRICS5:
            X, Y, W = COMB
            Z = "COMBINATE"
            bayesian_home_Win_d = []
            bayesian_away_Win_d = []
            bayesian_12_d = []
            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[1] and W == PROB_METRICS1[3]:
                        prob_matches_home_W_against_EO = rdm.random()
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = _1HWS[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = _12S[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[1] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = rdm.random()
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = home_z_prob[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = away_z_prob[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[3] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = rdm.random()
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = _1HWS[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = _12S[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[3]:
                        prob_matches_home_W_against_EO = baye_home_Win_d[q]
                        prob_matches_W_indp_home1 = _1HWS[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = baye_away_Win_d[q]
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = baye_12_d[q]
                        prob_12_indp_home = _12S[q]
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = baye_home_Win_d[q]
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = baye_away_Win_d[q]
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = baye_12_d[q]
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[3] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = baye_home_Win_d[q]
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = _1HWS[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = baye_away_Win_d[q]
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = baye_12_d[q]
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = _12S[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[2] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[1]:
                        prob_matches_home_W_against_EO = home_z_prob[q]
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = away_z_prob[q]
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[2] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[3]:
                        prob_matches_home_W_against_EO = home_z_prob[q]
                        prob_matches_W_indp_home1 = _1HWS[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = away_z_prob[q]
                        prob_matches_W_indp_home2 = _2AWS[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_home = _12S[q]
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[2] and Y == PROB_METRICS1[3] and W == PROB_METRICS1[1]:
                        prob_matches_home_W_against_EO = home_z_prob[q]
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = _1HWS[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = away_z_prob[q]
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = _12S[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[3] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[1]:
                        prob_matches_home_W_against_EO = _1HWS[q]
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = _2AWS[q]
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = _12S[q]
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[3] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = _1HWS[q]
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = _2AWS[q]
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = _12S[q]
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[3] and Y == PROB_METRICS1[2] and W == PROB_METRICS1[1]:
                        prob_matches_home_W_against_EO = _1HWS[q]
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = baye_home_Win_d[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = _2AWS[q]
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = baye_away_Win_d[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = _12S[q]
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = baye_12_d[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                except IndexError:
                    traceback.print_exc()
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_ALT}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                       f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_0.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_0.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_1.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_1.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if ((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)):
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_2.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                else:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_2.txt", mode="a") as file:
                                            writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_W[q] > h_form_D[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_W[q] > a_form_D[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_3.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                else:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_3.txt", mode="a") as file:
                                            writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_4.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_4.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)):
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_5.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                else:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_5.txt", mode="a") as file:
                                            writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_6.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_6.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_7.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_7.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_8.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_8.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_9.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_9.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                            if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_10.txt", mode="a") as file:
                                            writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_ALT and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_10.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                except UnicodeError:
                    traceback.print_exc()
                    pass
                except IndexError:
                    traceback.print_exc()
                    continue
                except OSError:
                    traceback.print_exc()
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_alt_{i}.txt", mode="a") as file:
                    file.write("\n\n\n\n\n")

        for COMBINER in COMBINERS:
            Z = COMBINER
            if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[6] and Z != COMBINERS[7]:
                for COMB in COMB_PROB_METRICS3:
                    W, X, Y = COMB
                    bayesian_home_Win_d = []
                    bayesian_away_Win_d = []
                    bayesian_12_d = []

                    for q in range(len(home_teams)):
                        try:
                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = _1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = _2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = _12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(_1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(_2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = np.cbrt(_12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q])
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q])
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q])
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q]
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q]
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q]
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q]))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q]))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q]))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * rdm.random() * _1HWS[q])
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * rdm.random() * _2AWS[q])
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q])
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        except IndexError:
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_ALT}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                               f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_0.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_0.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_1.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_1.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if ((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_2.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_2.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_W[q] > h_form_D[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_W[q] > a_form_D[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_3.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_3.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_4.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_4.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_5.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_5.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_6.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_6.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_7.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_7.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_8.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_8.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_9.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_9.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_10.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_ALT[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_10.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        except UnicodeError:
                            pass
                        except IndexError:
                            continue
                        except OSError:
                            pass
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                            file.write("\n\n\n\n\n")

        for COMBINER in COMBINERS:
            Z = COMBINER
            if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[4] and Z != COMBINERS[5]:
                for COMB in COMB_PROB_METRICS4:
                    V, W, X, Y = COMB
                    bayesian_home_Win_d = []
                    bayesian_away_Win_d = []
                    bayesian_12_d = []

                    for q in range(len(home_teams)):
                        try:
                            if Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[6]:
                                bayesian_home_Win = ((1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))) ** 0.25
                                bayesian_away_Win = ((1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))) ** 0.25
                                bayesian_12 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))) ** 0.25
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[7]:
                                bayesian_home_Win = (home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))) ** 0.25
                                bayesian_away_Win = (away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))) ** 0.25
                                bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))) ** 0.25
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        except IndexError:
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_ALT}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                               f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_0.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_1.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if ((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)):
                                        if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_2.txt", mode="a") as file:
                                                writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_W[q] > h_form_D[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_ALT and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_ALT and a_form_W[q] > a_form_D[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                        if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_3.txt", mode="a") as file:
                                                writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_4.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)):
                                        if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_5.txt", mode="a") as file:
                                                writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_6.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_7.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_8.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_ALT / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_9.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_ALT or bayesian_away_Win_d[q] > CONFINTVL_ALT:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_ALT) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_ALT and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_ALT and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_ALT:
                                    if ((home_positions[q] <= away_positions[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] >= FORM_VALUE_ALT and a_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q]))) or ((home_positions[q] >= away_positions[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] >= FORM_VALUE_ALT and h_form_W[q] <= (1 - FORM_VALUE_ALT)) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q]))):
                                        if (BAY_DIFF_ALT <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_ALT[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_10.txt", mode="a") as file:
                                                writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        except UnicodeError:
                            pass
                        except IndexError:
                            continue
                        except OSError:
                            pass
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_alt_{i}.txt", mode="a") as file:
                            file.write("\n\n\n\n\n")

    for CONFINTVL_XLR in CONFINTVLS_XLR:
        for COMBINER in COMBINERS[:4]:
            Z = COMBINER
            for COMB in COMB_PROB_METRICS1:
                X, Y = COMB
                bayesian_home_Win_d = []
                bayesian_away_Win_d = []
                bayesian_12_d = []

                for q in range(len(home_teams)):
                    try:
                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + rdm.random())
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random())
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (_2AWS[q] + rdm.random())
                            bayesian_12 = 0.5 * (_12S[q] + rdm.random())
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + _1HWS[q])
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + _2AWS[q])
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q])
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[1]:
                            bayesian_home_Win = rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random()
                            bayesian_away_Win = away_z_prob[q] * rdm.random()
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random()
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * rdm.random()
                            bayesian_away_Win = _2AWS[q] * rdm.random()
                            bayesian_12 = _12S[q] * rdm.random()
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * _1HWS[q]
                            bayesian_away_Win = away_z_prob[q] * _2AWS[q]
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q]
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random()))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + rdm.random()))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + _1HWS[q]))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + _2AWS[q]))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q]))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt(rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(_2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt(_12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * rdm.random())
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random())
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(_2AWS[q] * rdm.random())
                            bayesian_12 = math.sqrt(_12S[q] * rdm.random())
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * _1HWS[q])
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * _2AWS[q])
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q])
                            baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    except IndexError:
                        continue

                for q in range(len(bayesian_home_Win_d)):
                    if q == 0:
                        for i in range(11):
                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                                file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                           f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                           f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                    try:
                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if h_form_D[q] == 0 and a_form_D[q] == 0:
                                    if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if (((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q])) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q])) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q])):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if h_form_D[q] == 0 or a_form_D[q] == 0:
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                    if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                        writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    except UnicodeError:
                        pass
                    except IndexError:
                        continue
                    except OSError:
                        pass
                for i in range(11):
                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                        file.write("\n\n\n\n\n")

        for PROB in PROB_METRICS:
            X = PROB
            Y = "ANALYSIS"
            Z = "STANDARD"
            bayesian_home_Win_d = []
            bayesian_away_Win_d = []
            bayesian_12_d = []

            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS[0]:
                        bayesian_home_Win = (prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))
                        bayesian_away_Win = (prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))
                        bayesian_12 = (prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[1]:
                        prob_matches_home_W_against_EO = rdm.random()
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[2]:
                        bayesian_home_Win = home_z_prob[q]
                        bayesian_away_Win = away_z_prob[q]
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[3]:
                        bayesian_home_Win = _1HWS[q]
                        bayesian_away_Win = _2AWS[q]
                        bayesian_12 = _12S[q]
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[4]:
                        bayesian_home_Win = home_z_prob[q] * diff_z_prob[q]
                        bayesian_away_Win = away_z_prob[q] * diff_z_prob[q]
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])) * diff_z_prob[q]
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                       f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if ((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q])) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q])) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q])):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]))):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                except UnicodeError:
                    pass
                except IndexError:
                    continue
                except OSError:
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                    file.write("\n\n\n\n\n")

        for COMB in COMB_PROB_METRICS2:
            X, Y = COMB
            Z = "COMBINATE"
            bayesian_home_Win_d = []
            bayesian_away_Win_d = []
            bayesian_12_d = []

            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[1]:
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_HWs[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_HWs[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_HWs[q])))
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_AWs[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_AWs[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_AWs[q])))
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12s[q])))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[2]:
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - home_z_prob[q])))
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - away_z_prob[q])))
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])))))))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[3]:
                        prob_matches_W_indp_home1 = rdm.random()
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - _1HWS[q])))
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - _2AWS[q])))
                        prob_12_indp_home = rdm.random()
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (_12S[q] * (prob_12_indp_home * prob_12_indp_away)) / ((_12S[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - _12S[q])))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0]:
                        prob_matches_home_W_against_EO = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        bayesian_12 = ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12))))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[2]:
                        bayesian_home_Win = (home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - home_z_prob[q])))
                        bayesian_away_Win = (away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - away_z_prob[q])))
                        bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))))))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[3]:
                        bayesian_home_Win = (_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - _1HWS[q])))
                        bayesian_away_Win = (_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - _2AWS[q])))
                        bayesian_12 = (_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - _12S[q])))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)
                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                       f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if (((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF))):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q])) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q])) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]))):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                    writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                            writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                writer_alt_xlr_(w=q, A=X, B=Y, C=Z, data=file)

                except UnicodeError:
                    pass
                except IndexError:
                    continue
                except OSError:
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                    file.write("\n\n\n\n\n")

        for COMB in COMB_PROB_METRICS5:
            X, Y, W = COMB
            Z = "COMBINATE"
            bayesian_home_Win_d = []
            bayesian_away_Win_d = []
            bayesian_12_d = []
            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[1] and W == PROB_METRICS1[3]:
                        prob_matches_home_W_against_EO = rdm.random()
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = _1HWS[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = _12S[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[1] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = rdm.random()
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = home_z_prob[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = away_z_prob[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[0] and Y == PROB_METRICS1[3] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = rdm.random()
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = _1HWS[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = _12S[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[3]:
                        prob_matches_home_W_against_EO = baye_home_Win_d[q]
                        prob_matches_W_indp_home1 = _1HWS[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = baye_away_Win_d[q]
                        prob_matches_W_indp_home2 = rdm.random()
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = baye_12_d[q]
                        prob_12_indp_home = _12S[q]
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = baye_home_Win_d[q]
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = baye_away_Win_d[q]
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = baye_12_d[q]
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[3] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = baye_home_Win_d[q]
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = _1HWS[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = baye_away_Win_d[q]
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = baye_12_d[q]
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = _12S[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[2] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[1]:
                        prob_matches_home_W_against_EO = home_z_prob[q]
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = away_z_prob[q]
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[2] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[3]:
                        prob_matches_home_W_against_EO = home_z_prob[q]
                        prob_matches_W_indp_home1 = _1HWS[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = away_z_prob[q]
                        prob_matches_W_indp_home2 = _2AWS[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_home = _12S[q]
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[2] and Y == PROB_METRICS1[3] and W == PROB_METRICS1[1]:
                        prob_matches_home_W_against_EO = home_z_prob[q]
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = _1HWS[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = away_z_prob[q]
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = _2AWS[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = _12S[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[3] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[1]:
                        prob_matches_home_W_against_EO = _1HWS[q]
                        prob_matches_W_indp_home1 = baye_home_Win_d[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = _2AWS[q]
                        prob_matches_W_indp_home2 = baye_away_Win_d[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = _12S[q]
                        prob_12_indp_home = baye_12_d[q]
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[3] and Y == PROB_METRICS1[0] and W == PROB_METRICS1[2]:
                        prob_matches_home_W_against_EO = _1HWS[q]
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = _2AWS[q]
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = _12S[q]
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = rdm.random()
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[3] and Y == PROB_METRICS1[2] and W == PROB_METRICS1[1]:
                        prob_matches_home_W_against_EO = _1HWS[q]
                        prob_matches_W_indp_home1 = home_z_prob[q]
                        prob_matches_W_indp_away1 = baye_home_Win_d[q]
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = _2AWS[q]
                        prob_matches_W_indp_home2 = away_z_prob[q]
                        prob_matches_W_indp_away2 = baye_away_Win_d[q]
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = _12S[q]
                        prob_12_indp_home = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        prob_12_indp_away = baye_12_d[q]
                        bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                        baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                except IndexError:
                    traceback.print_exc()
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                       f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_0.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_0.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_1.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_1.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if (((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF))):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_2.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                else:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_2.txt", mode="a") as file:
                                            writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q])) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q])) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_3.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                else:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_3.txt", mode="a") as file:
                                            writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_4.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_4.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]))):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_5.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                else:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_5.txt", mode="a") as file:
                                            writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_6.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_6.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_7.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_7.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_8.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_8.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_9.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                    else:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_9.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                            if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                        with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_10.txt", mode="a") as file:
                                            writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_10.txt", mode="a") as file:
                                                writer_alt_xlr_1(y=q, F=X, G=Y, H=W, J=Z, data=file)

                except UnicodeError:
                    traceback.print_exc()
                    pass
                except IndexError:
                    traceback.print_exc()
                    continue
                except OSError:
                    traceback.print_exc()
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}_{W}/{Z}_{X}_{Y}_{W}_{sport}_xlr_{i}.txt", mode="a") as file:
                    file.write("\n\n\n\n\n")

        for COMBINER in COMBINERS:
            Z = COMBINER
            if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[6] and Z != COMBINERS[7]:
                for COMB in COMB_PROB_METRICS3:
                    W, X, Y = COMB
                    bayesian_home_Win_d = []
                    bayesian_away_Win_d = []
                    bayesian_12_d = []

                    for q in range(len(home_teams)):
                        try:
                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = _1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = _2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = _12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(_1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(_2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = np.cbrt(_12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q])
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q])
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q])
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q]
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q]
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q]
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q]))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q]))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q]))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * rdm.random() * _1HWS[q])
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * rdm.random() * _2AWS[q])
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q])
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        except IndexError:
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                               f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if ((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q])) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q])) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q])):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]))):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                            writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                    writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                        writer_alt_xlr_1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        except UnicodeError:
                            pass
                        except IndexError:
                            continue
                        except OSError:
                            pass
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                            file.write("\n\n\n\n\n")

        for COMBINER in COMBINERS:
            Z = COMBINER
            if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[4] and Z != COMBINERS[5]:
                for COMB in COMB_PROB_METRICS4:
                    V, W, X, Y = COMB
                    bayesian_home_Win_d = []
                    bayesian_away_Win_d = []
                    bayesian_12_d = []

                    for q in range(len(home_teams)):
                        try:
                            if Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[6]:
                                bayesian_home_Win = ((1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))) ** 0.25
                                bayesian_away_Win = ((1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))) ** 0.25
                                bayesian_12 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))) ** 0.25
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[7]:
                                bayesian_home_Win = (home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))) ** 0.25
                                bayesian_away_Win = (away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))) ** 0.25
                                bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))) ** 0.25
                                baye_appender_alt_xlr_(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        except IndexError:
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|HT_GDIFF|AT_GDIFF|BTH_GDIFF|BTA_GDIFF|"
                                               f"BAYESIAN {OUTCOMES_ALT_XLR[0]}|BAYESIAN {OUTCOMES_ALT_XLR[1]}|BAYESIAN {OUTCOMES_ALT_XLR[2]}|MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if ((home_positions[q] < away_positions[q]) and (home_points[q] > away_points[q]) and ((ht_g_avgs[q] > at_g_avgs[q]) and (bth_g_avgs[q] > bta_g_avgs[q]) and (ht_g_diff_avgs[q] > at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] > bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] > bayesian_away_Win_d[q]) and (abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF)) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q]) and (abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF)):
                                        if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((home_positions[q] <= away_positions[q]) and ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q])) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q])) and (home_points[q] <= away_points[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q])):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                        if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if ((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q]) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) or ((home_positions[q] > away_positions[q]) and (home_points[q] < away_points[q]) and ((ht_g_avgs[q] < at_g_avgs[q]) and (bth_g_avgs[q] < bta_g_avgs[q]) and (ht_g_diff_avgs[q] < at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] < bta_g_diff_avgs[q])) and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] < bayesian_away_Win_d[q]))):
                                        if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if (h_form_D[q] == 1.0 or a_form_D[q] == 1.0) or (h_form_W[q] == 1.0 or a_form_W[q] == 1.0):
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if (abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (0.5 * bayesian_12_d[q]) >= 0.5 * abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q])) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                    writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (abs(bth_g_diff_avgs[q]) > ABS_XLR) and abs(ht_g_avgs[q] - at_g_avgs[q]) > DG_AVG_XLR and abs(bth_g_avgs[q] - bta_g_avgs[q]) > DGB_AVG_XLR and abs(ht_g_diff_avgs[q] - at_g_diff_avgs[q]) > DG_DIF_XLR:
                                    if (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q]) and ((ht_g_avgs[q] >= at_g_avgs[q]) and (bth_g_avgs[q] >= bta_g_avgs[q]) and (ht_g_diff_avgs[q] >= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] >= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q]) and ((ht_g_avgs[q] <= at_g_avgs[q]) and (bth_g_avgs[q] <= bta_g_avgs[q]) and (ht_g_diff_avgs[q] <= at_g_diff_avgs[q]) and (bth_g_diff_avgs[q] <= bta_g_diff_avgs[q])) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if (BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q]) and (bayesian_12_d[q] >= CONFINTVLS_XLR[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                writer_alt_xlr_2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        except UnicodeError:
                            pass
                        except IndexError:
                            continue
                        except OSError:
                            pass
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                            file.write("\n\n\n\n\n")

    print_all_data()

driver.quit()

end_time = time.time()
print(f"run speed: {end_time - start_time}s")
