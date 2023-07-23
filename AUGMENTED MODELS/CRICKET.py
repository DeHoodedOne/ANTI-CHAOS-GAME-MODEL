import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException, ElementClickInterceptedException, UnexpectedAlertPresentException, \
    WebDriverException, NoSuchWindowException, TimeoutException, InvalidSessionIdException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FFService
import winsound
from time import sleep
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
BAY_DIFF_XLR = CRITERIA[3]
CONFINTVLS = CRITERIA[4]
CONFINTVLS_XLR = CRITERIA[7]
DSCRM_BT = CRITERIA[8]
DSCRM_H_A = CRITERIA[9]
FORM_COUNT = CRITERIA[10]
FORM_DIFF = CRITERIA[11]
FORM_VALUE = CRITERIA[12]
FORM_VALUE_XLR = CRITERIA[15]
INDP_MATCH_SAMPLE = CRITERIA[16]
NMP = CRITERIA[17]
POS_DIFF = CRITERIA[18]
POS_MARK = CRITERIA[19]
YEAR = CRITERIA[20]

METRICS = combinatorials()

PROB_METRICS = METRICS[0]
PROB_METRICS1 = METRICS[1]
COMBINERS = METRICS[2]
COMB_PROB_METRICS1 = METRICS[3]
COMB_PROB_METRICS2 = METRICS[4]
COMB_PROB_METRICS3 = METRICS[5]
COMB_PROB_METRICS4 = METRICS[6]

OUTCOMES = ["HW", "AW", "12"]

start_time = time.time()
SPORT_ = master_sport_list()[0][9]

ms_edge_path = CRITERIA[24][3]
options = EdgeOptions()
options.add_extension("_AdblockPlus.crx")
options.add_argument("start-maximized")
driver = webdriver.Edge(executable_path=ms_edge_path, options=options)

# firefox_path = CRITERIA[23][3]
# adblock = "_dablocker_ultimate.xpi"
# service = FFService(firefox_path)
# driver = webdriver.Firefox(service=service)
# driver.install_addon(adblock, temporary=True)
# driver.maximize_window()

# chrome_path = CRITERIA[21][3]
# service = Service(chrome_path)
# options = webdriver.ChromeOptions()
# options.add_extension("_AdblockPlus.crx")
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=service, options=options)

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
        except (IndexError, ValueError):
            try:
                home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[0].text.strip()
                home_points.append(float(home_t_point))
            except (IndexError, ValueError):
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
        except (IndexError, ValueError):
            try:
                away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[0].text.strip()
                away_points.append(float(away_t_point))
            except (IndexError, ValueError):
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
                    away_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[5].text.strip()
                    away_nums_matches_played.append(int(away_t_mp))
                except ValueError:
                    away_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[6].text.strip()
                    away_nums_matches_played.append(int(away_t_mp))
                except IndexError:
                    away_nums_matches_played.append(0)
            try:
                away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[1].text.strip()
                away_points.append(int(away_t_point))
            except (IndexError, ValueError):
                try:
                    away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[1].text.strip()
                    away_points.append(float(away_t_point))
                except (IndexError, ValueError):
                    away_points.append(0)
        else:
            try:
                home_t_position = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[1].text.split('.')[0].strip()
                home_positions.append(int(home_t_position))
            except IndexError:
                home_positions.append(0)
            if first_entry > 9:
                try:
                    home_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[5].text.strip()
                    home_nums_matches_played.append(int(home_t_mp))
                except ValueError:
                    home_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[6].text.strip()
                    home_nums_matches_played.append(int(home_t_mp))
                except IndexError:
                    home_nums_matches_played.append(0)
            try:
                home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[1].text.strip()
                home_points.append(int(home_t_point))
            except (IndexError, ValueError):
                try:
                    home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[1].text.strip()
                    home_points.append(float(home_t_point))
                except (IndexError, ValueError):
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
    teams_pts = driver.find_elements(By.CSS_SELECTOR, '.ui-table__row  .table__cell--points ')
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


def append_zeroes1():
    def zeroth_break(home_z_, away_z_, diff_z_, CLEARANCE_z):
        if 0 < home_z_ < 1 and 0 < away_z_ < 1:
            home_z_prob.append(home_z_)
            away_z_prob.append(away_z_)
            diff_z_prob.append(diff_z_)
        else:
            home_z_ = rdm.random()
            away_z_ = 1 - home_z_
            diff_z_ = abs(home_z_ - away_z_)
            if diff_z_ < CLEARANCE_z:
                home_z_ = rdm.random() * rdm.random()
                away_z_ = 1 - home_z_
                diff_z_ = abs(home_z_ - away_z_)
                if diff_z_ < CLEARANCE_z:
                    home_z_ = math.sqrt(rdm.random() * rdm.random())
                    away_z_ = 1 - home_z_
                    diff_z_ = abs(home_z_ - away_z_)
                    if diff_z_ < CLEARANCE_z:
                        home_z_ = 0.5 * (rdm.random() + rdm.random())
                        away_z_ = 1 - home_z_
                        diff_z_ = abs(home_z_ - away_z_)
                        if diff_z_ < CLEARANCE_z:
                            home_z_ = math.sqrt(0.5 * (rdm.random() + rdm.random()))
                            away_z_ = 1 - home_z_
                            diff_z_ = abs(home_z_ - away_z_)
            home_z_prob.append(home_z_)
            away_z_prob.append(away_z_)
            diff_z_prob.append(diff_z_)

    away_points.append(rdm.randint(0, 70))
    home_points.append(rdm.randint(0, 70))
    home_positions.append(rdm.randint(0, 20))
    away_positions.append(rdm.randint(0, 20))
    CLEARANCE_ = 0.875
    while True:
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
    count_12 = 0
    count_HW = 0
    count_AW = 0
    date___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__date')
    if len(date___) > 0:
        result = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__result')
        winner = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row [class="h2h__participantInner winner"]')
        for m in range(DSCRM_BT):
            try:
                if YEAR <= int(date___[m].text.split('.')[-1].strip()) < 90:
                    valid_games += 1
                    if "won" in result[m].text.split(" ") and (winner[m].text == home_teamx):
                        count_HW += 1
                    if "won" in result[m].text.split(" ") and (winner[m].text == away_teamx):
                        count_AW += 1
                    if ("drawn." or "tied." or "Draw" or ("No" and "Result.")) in result[m].text.split(" "):
                        count_HW += 0
                        count_AW += 0
                    if ("drawn." and "tied." and ("No" and "Result.")) not in result[m].text.split(" "):
                        count_12 += 1
                else:
                    print(f"Date Error at 1H2H: {date___[m].text}")
                    valid_games += 1
            except ValueError:
                print(f"Value Error at 1H2H")
                valid_games += 1
            except IndexError:
                valid_games += 1
    else:
        valid_games = DSCRM_BT

    return [valid_games, count_HW, count_AW, count_12]


def h2h_prob_calc(h2h_probz):
    prob_HW = float(h2h_probz[1] / h2h_probz[0])
    prob_AW = float(h2h_probz[2] / h2h_probz[0])
    prob_12i = float(h2h_probz[3] / h2h_probz[0])

    h2h_probs = [prob_HW, prob_AW, prob_12i]
    probs_H2H = []
    for prob in h2h_probs:
        if prob == 1.0:
            prob -= 0.01
        elif prob == 0:
            prob += 0.01
        probs_H2H.append(prob)
    return [probs_H2H[0], probs_H2H[1], probs_H2H[2]]


def h2h_appender(prb_HW, prb_AW, prb_12):
    prob_HWs.append(prb_HW)
    prob_AWs.append(prb_AW)
    prob_12s.append(prb_12)


def ht_indp_aggregator():
    valid_games_H_indp = 0
    count_12_H_indp = 0
    count_HW_H_indp = 0

    date_ = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
    if len(date_) > 0:
        h_icon = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__icon .formIcon')
        for k in range(DSCRM_H_A):
            try:
                if YEAR <= int(date_[k].text.split('.')[-1].strip()) < 90:
                    valid_games_H_indp += 1
                    if h_icon[k].text == "W":
                        count_HW_H_indp += 1
                    if h_icon[k].text == "D":
                        count_HW_H_indp += 0
                    if h_icon[k].text != "D":
                        count_12_H_indp += 1
                else:
                    print(f"Date Error at Home1 : {date_[k].text}")
                    valid_games_H_indp += 1
            except ValueError:
                print(f"Value Error at Home1")
                valid_games_H_indp += 1
            except IndexError:
                valid_games_H_indp += 1
    else:
        valid_games_H_indp = DSCRM_H_A

    return [valid_games_H_indp, count_HW_H_indp, count_12_H_indp]


def ht_indp_prob_calc(ht_probz):
    prob_HW_H_indp = float(ht_probz[1] / ht_probz[0])
    prob_AW_H_indp = 1 - prob_HW_H_indp
    prob_12_H_indp = float(ht_probz[2] / ht_probz[0])

    ht_indp_probs = [prob_HW_H_indp, prob_AW_H_indp, prob_12_H_indp]
    probs_HT_INDP = []
    for prob in ht_indp_probs:
        if prob == 1.0:
            prob -= 0.01
        elif prob == 0:
            prob += 0.01
        probs_HT_INDP.append(prob)

    return [probs_HT_INDP[0], probs_HT_INDP[1], probs_HT_INDP[2]]


def ht_indp_appender(prb_HW_H_indp, prb_AW_H_indp, prb_12_H_indp):
    prob_HW_H_indps.append(prb_HW_H_indp)
    prob_AW_H_indps.append(prb_AW_H_indp)
    prob_12_H_indps.append(prb_12_H_indp)


def at_indp_aggregator():
    valid_games_A_indp = 0
    count_12_A_indp = 0
    count_AW_A_indp = 0
    date__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
    if len(date__) > 0:
        a_icon = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__row .h2h__icon .formIcon')
        for n in range(DSCRM_H_A):
            try:
                if YEAR <= int(date__[n].text.split('.')[-1].strip()) < 90:
                    valid_games_A_indp += 1
                    if a_icon[n].text == "W":
                        count_AW_A_indp += 1
                    if a_icon[n].text == "D":
                        count_AW_A_indp += 0
                    if a_icon[n].text != "D":
                        count_12_A_indp += 1
                else:
                    print(f"Date Error at Away1: {date__[n].text}")
                    valid_games_A_indp += 1
            except ValueError:
                print(f"Error at Away1")
                valid_games_A_indp += 1
            except IndexError:
                valid_games_A_indp += 1
    else:
        valid_games_A_indp = DSCRM_H_A

    return [valid_games_A_indp, count_AW_A_indp, count_12_A_indp]


def at_indp_prob_calc(at_probz):
    prob_AW_A_indp = float(at_probz[1] / at_probz[0])
    prob_HW_A_indp = 1 - prob_AW_A_indp
    prob_12_A_indp = float(at_probz[2] / at_probz[0])

    at_indp_probs = [prob_HW_A_indp, prob_AW_A_indp, prob_12_A_indp]

    probs_AT_INDP = []
    for prob in at_indp_probs:
        if prob == 1.0:
            prob -= 0.01
        elif prob == 0:
            prob += 0.01
        probs_AT_INDP.append(prob)

    return [probs_AT_INDP[0], probs_AT_INDP[1], probs_AT_INDP[2]]


def at_indp_appender(prb_HW_A_indp, prb_AW_A_indp, prb_12_A_indp):
    prob_HW_A_indps.append(prb_HW_A_indp)
    prob_AW_A_indps.append(prb_AW_A_indp)
    prob_12_A_indps.append(prb_12_A_indp)


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


def data_break_zeroes1(z, ent1):
    print("data_break_zeroes1")
    prb_HW_ = rdm.random()
    prb_AW_ = 1 - prb_HW_
    prb_12_ = rdm.random()
    h2h_appender(prb_HW=prb_HW_, prb_AW=prb_AW_, prb_12=prb_12_)

    prb_HW_H_indp_ = rdm.random()
    prb_AW_H_indp_ = 1 - prb_HW_H_indp_
    prb_12_H_indp_ = rdm.choice(CONFINTVLS)
    ht_indp_appender(prb_HW_H_indp=prb_HW_H_indp_, prb_AW_H_indp=prb_AW_H_indp_, prb_12_H_indp=prb_12_H_indp_)

    prb_HW_A_indp_ = rdm.random()
    prb_AW_A_indp_ = 1 - prb_HW_A_indp_
    prb_12_A_indp_ = rdm.choice(CONFINTVLS)
    at_indp_appender(prb_HW_A_indp=prb_HW_A_indp_, prb_AW_A_indp=prb_AW_A_indp_, prb_12_A_indp=prb_12_A_indp_)

    FORM_CONFIGS = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
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
    if ent1 < 10:
        home_nums_matches_played.append(home_nums_matches_played_z)
        away_nums_matches_played.append(away_nums_matches_played_z)
    try:
        match_times.append(sub_m_t[z])
    except (IndexError, NoSuchElementException, StaleElementReferenceException):
        match_times.append("XX:XX")
    append_zeroes1()


def data_break_zeroes2(z):
    print("data_break_zeroes2")
    prb_HW_ = rdm.random()
    prb_AW_ = 1 - prb_HW_
    prb_12_ = rdm.random()
    h2h_appender(prb_HW=prb_HW_, prb_AW=prb_AW_, prb_12=prb_12_)

    prb_HW_H_indp_ = rdm.random()
    prb_AW_H_indp_ = 1 - prb_HW_H_indp_
    prb_12_H_indp_ = rdm.choice(CONFINTVLS)
    ht_indp_appender(prb_HW_H_indp=prb_HW_H_indp_, prb_AW_H_indp=prb_AW_H_indp_, prb_12_H_indp=prb_12_H_indp_)

    prb_HW_A_indp_ = rdm.random()
    prb_AW_A_indp_ = 1 - prb_HW_A_indp_
    prb_12_A_indp_ = rdm.choice(CONFINTVLS)
    at_indp_appender(prb_HW_A_indp=prb_HW_A_indp_, prb_AW_A_indp=prb_AW_A_indp_, prb_12_A_indp=prb_12_A_indp_)

    FORM_CONFIGS = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
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
    home_nums_matches_played.append(home_nums_matches_played_z)
    away_nums_matches_played.append(away_nums_matches_played_z)
    try:
        match_times.append(sub_m_t[z])
    except (IndexError, NoSuchElementException, StaleElementReferenceException):
        match_times.append("XX:XX")
    append_zeroes1()


def home_form_checker():
    def h_f_zero():
        FORM_CONFIGS = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
        while True:
            h_form_W_z = rdm.choice(FORM_CONFIGS)
            h_form_L_z = rdm.choice(FORM_CONFIGS)
            h_form_D_z = rdm.choice(FORM_CONFIGS)
            if (h_form_W_z + h_form_L_z) == 1.0 and h_form_D_z == 0.0:
                h_form_W.append(h_form_W_z)
                h_form_D.append(h_form_D_z)
                h_form_L.append(h_form_L_z)
                break

    count_HW_form = 0
    count_HD_form = 0
    try:
        subx1 = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row')
        if len(subx1) >= FORM_COUNT:
            dssc = 0
            datte = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
            form_icon = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__icon .formIcon')
            for k in range(FORM_COUNT):
                try:
                    if int(datte[k].text.split('.')[-1].strip()) >= YEAR:
                        if form_icon[k].text == "W":
                            count_HW_form += 1
                        if form_icon[k].text == "D":
                            count_HD_form += 1
                        dssc += 1
                    else:
                        print(f"Home Form Year Unaccepted: {int(datte[k].text.split('.')[-1].strip())}")
                        dssc += 1
                except ValueError:
                    print(f"Value Error at FORM Home")
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


def away_form_checker():
    def a_f_zero():
        FORM_CONFIGS = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
        while True:
            a_form_W_z = rdm.choice(FORM_CONFIGS)
            a_form_L_z = rdm.choice(FORM_CONFIGS)
            a_form_D_z = rdm.choice(FORM_CONFIGS)
            if (a_form_W_z + a_form_L_z) == 1.0 and a_form_D_z == 0.0:
                a_form_W.append(a_form_W_z)
                a_form_D.append(a_form_D_z)
                a_form_L.append(a_form_L_z)
                break

    count_AW_form = 0
    count_AD_form = 0
    try:
        subx2 = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row')
        if len(subx2) >= FORM_COUNT:
            dssc = 0
            datte = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
            form_icon = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__icon .formIcon')
            for n in range(FORM_COUNT):
                try:
                    if int(datte[n].text.split('.')[-1].strip()) >= YEAR:
                        if form_icon[n].text == "W":
                            count_AW_form += 1
                        if form_icon[n].text == "D":
                            count_AD_form += 1
                        dssc += 1
                    else:
                        print(f"Away Form Year Unaccepted: {int(datte[n].text.split('.')[-1].strip())}")
                        dssc += 1
                except ValueError:
                    print(f"Error at FORM Away")
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
            _12S.append(rdm.choice(CONFINTVLS))
        except (NoSuchElementException, IndexError):
            try:
                _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                odds_augment(odds_home=_1HW, odds_away=_2AW)
                _12S.append(rdm.choice(CONFINTVLS))
            except (ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, IndexError):
                try:
                    driver.refresh()
                    sleep(0.5)
                    _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                    _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                    odds_augment(odds_home=_1HW, odds_away=_2AW)
                    _12S.append(rdm.choice(CONFINTVLS))
                except (ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException, IndexError, StaleElementReferenceException):
                    while True:
                        _1HW_ = rdm.random()
                        _2AW_ = rdm.random()
                        if (_1HW_ + _2AW_) <= 1:
                            _1HW = 1 / _1HW_
                            _2AW = 1 / _2AW_
                            odds_augment(odds_home=_1HW, odds_away=_2AW)
                            break
                    _12S.append(rdm.choice(CONFINTVLS))
    except (NoSuchElementException, IndexError, ElementNotInteractableException,
            ElementClickInterceptedException, StaleElementReferenceException):
        _12S.append(rdm.choice(CONFINTVLS))
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


def writer(w, A, B, C, data):
    data.write(f"{countries[w]}|{leagues[w]}|{home_teams[w]}|{away_teams[w]}|{home_positions[w]}|"
               f"{away_positions[w]}|{home_nums_matches_played[w]}|{away_nums_matches_played[w]}|{home_points[w]}|"
               f"{away_points[w]}|{h_form_W[w]}|{h_form_D[w]}|{h_form_L[w]}|{a_form_W[w]}|{a_form_D[w]}|{a_form_L[w]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[w]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[w]}|{OUTCOMES[2]}:-{bayesian_12_d[w]}|"
               f"{match_times[w]}|{sport}|{C}_{A}_{B}|{set_date_s_size()[0]}\n")


def writer1(y, F, G, H, J, data):
    data.write(f"{countries[y]}|{leagues[y]}|{home_teams[y]}|{away_teams[y]}|{home_positions[y]}|"
               f"{away_positions[y]}|{home_nums_matches_played[y]}|{away_nums_matches_played[y]}|{home_points[y]}|"
               f"{away_points[y]}|{h_form_W[y]}|{h_form_D[y]}|{h_form_L[y]}|{a_form_W[y]}|{a_form_D[y]}|{a_form_L[y]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[y]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[y]}|{OUTCOMES[2]}:-{bayesian_12_d[y]}|"
               f"{match_times[y]}|{sport}|{J}_{F}_{G}_{H}|{set_date_s_size()[0]}\n")


def writer2(z, K, L, M, N, P, data):
    data.write(f"{countries[z]}|{leagues[z]}|{home_teams[z]}|{away_teams[z]}|{home_positions[z]}|"
               f"{away_positions[z]}|{home_nums_matches_played[z]}|{away_nums_matches_played[z]}|{home_points[z]}|"
               f"{away_points[z]}|{h_form_W[z]}|{h_form_D[z]}|{h_form_L[z]}|{a_form_W[z]}|{a_form_D[z]}|{a_form_L[z]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[z]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[z]}|{OUTCOMES[2]}:-{bayesian_12_d[z]}|"
               f"{match_times[z]}|{sport}|{P}_{K}_{L}_{M}_{N}|{set_date_s_size()[0]}\n")


def baye_appender(baye_HW, baye_AW, baye_12):
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
        except UnexpectedAlertPresentException:
            alert_handler1()
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
        prb_HW_ = rdm.random()
        prb_AW_ = 1 - prb_HW_
        prb_12_ = rdm.random()
        h2h_appender(prb_HW=prb_HW_, prb_AW=prb_AW_, prb_12=prb_12_)

    def ht_indp_zero():
        print("ht_indp_zero")
        prb_HW_H_indp_ = rdm.random()
        prb_AW_H_indp_ = 1 - prb_HW_H_indp_
        prb_12_H_indp_ = rdm.choice(CONFINTVLS)
        ht_indp_appender(prb_HW_H_indp=prb_HW_H_indp_, prb_AW_H_indp=prb_AW_H_indp_, prb_12_H_indp=prb_12_H_indp_)

    def at_indp_zero():
        print("at_indp_zero")
        prb_HW_A_indp_ = rdm.random()
        prb_AW_A_indp_ = 1 - prb_HW_A_indp_
        prb_12_A_indp_ = rdm.choice(CONFINTVLS)
        at_indp_appender(prb_HW_A_indp=prb_HW_A_indp_, prb_AW_A_indp=prb_AW_A_indp_, prb_12_A_indp=prb_12_A_indp_)

    try:
        sub1 = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row')
        if len(sub1) < DSCRM_H_A:
            ht_indp_zero()
        else:
            ht_probs = ht_indp_aggregator()
            if ht_probs[0] >= DSCRM_H_A:
                try:
                    ht_indp_values = ht_indp_prob_calc(ht_probs)
                    ht_indp_appender(prb_HW_H_indp=ht_indp_values[0], prb_AW_H_indp=ht_indp_values[1],
                                     prb_12_H_indp=ht_indp_values[2])
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
        else:
            at_probs = at_indp_aggregator()
            if at_probs[0] >= DSCRM_H_A:
                try:
                    at_indp_values = at_indp_prob_calc(at_probs)
                    at_indp_appender(prb_HW_A_indp=at_indp_values[0], prb_AW_A_indp=at_indp_values[1],
                                     prb_12_A_indp=at_indp_values[2])
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
        else:
            h2h_probs = h2h_aggregator()
            if h2h_probs[0] >= DSCRM_BT:
                try:
                    h2h_values = h2h_prob_calc(h2h_probs)
                    h2h_appender(prb_HW=h2h_values[0], prb_AW=h2h_values[1], prb_12=h2h_values[2])
                except ZeroDivisionError:
                    h2h_zero()
            else:
                h2h_zero()
    except ElementNotInteractableException:
        h2h_zero()


def print_all_data():
    print(f"Countries: {countries}")
    print(f"Leagues: {leagues}")
    print(f"Home Teams: {home_teams}")
    print(f"Home Positions: {home_positions}")
    print(f"Home Points: {home_points}")
    print(f"Home No Matches Played: {home_nums_matches_played}")
    print(f"Away Teams: {away_teams}")
    print(f"Away Positions: {away_positions}")
    print(f"Away Points: {away_points}")
    print(f"Away No Matches Played: {away_nums_matches_played}")
    print(f"Match Times: {match_times}")
    print(f"Home W Form: {h_form_W}")
    print(f"Home D Form: {h_form_D}")
    print(f"Home L Form: {h_form_L}")
    print(f"Away W Form: {a_form_W}")
    print(f"Away D Form: {a_form_D}")
    print(f"Away L Form: {a_form_L}")
    print(f"Prob 12s: {prob_12s}")
    print(f"Prob HWs: {prob_HWs}")
    print(f"Prob AWs: {prob_AWs}")
    print(f"Prob 12_A_indps: {prob_12_A_indps}")
    print(f"Prob HW_A_indps: {prob_HW_A_indps}")
    print(f"Prob AW_A_indps: {prob_AW_A_indps}")
    print(f"Bayesian Home Win: {bayesian_home_Win_d}")
    print(f"Bayesian Away Win: {bayesian_away_Win_d}")
    print(f"Bayesian 12: {bayesian_12_d}")
    print(f"Odds _1HWS: {_1HWS}")
    print(f"Odds _2AWS: {_2AWS}")
    print(f"Odds _12S: {_12S}")
    print(f"Countries: {len(countries)}, Leagues: {len(leagues)}, Home Teams: {len(home_teams)}, "
          f"Home Positions: {len(home_positions)}, Home Points: {len(home_points)}, "
          f"Home No Matches Played: {len(home_nums_matches_played)}, Away Teams: {len(away_teams)}, "
          f"Away Positions: {len(away_positions)}, Away Points: {len(away_points)}, "
          f"Away No Matches Played: {len(away_nums_matches_played)}, Match Times: {len(match_times)} "
          f"Home W Form: {len(h_form_W)}, Home D Form: {len(h_form_D)}, Home L Form: {len(h_form_L)}, "
          f"Away W Form: {len(a_form_W)}, Away D Form: {len(a_form_D)}, Away L Form: {len(a_form_L)}"
          f"Prob 12s: {len(prob_12s)}, Prob HWs: {len(prob_HWs)}, Prob AWs: {len(prob_AWs)}, Prob 12_H_indps: {len(prob_12_H_indps)},"
          f"Prob HW_H_indps: {len(prob_HW_H_indps)}, Prob AW_H_indps: {len(prob_AW_H_indps)}, Prob 12_A_indps: {len(prob_12_A_indps)}, "
          f"Prob HW_A_indps: {len(prob_HW_A_indps)}, Prob AW_A_indps: {len(prob_AW_A_indps)}, "
          f"Odds _1HWS: {len(_1HWS)}, Odds _2AWS: {len(_2AWS)}, Odds _12S: {len(_12S)}, "
          f"Bayesian Home Win: {len(bayesian_home_Win_d)}, Bayesian Away Win: {len(bayesian_away_Win_d)}, Bayesian 12: {len(bayesian_12_d) }")


countries = []
home_teams = []
away_teams = []
leagues = []
home_positions = []
away_positions = []
home_points = []
away_points = []
match_times = []
home_nums_matches_played = []
away_nums_matches_played = []
h_form_W = []
h_form_L = []
h_form_D = []
a_form_W = []
a_form_D = []
a_form_L = []
prob_12s = []
prob_HWs = []
prob_AWs = []
prob_12_H_indps = []
prob_HW_H_indps = []
prob_AW_H_indps = []
prob_12_A_indps = []
prob_HW_A_indps = []
prob_AW_A_indps = []
home_z_prob = []
away_z_prob = []
diff_z_prob = []
_1HWS = []
_2AWS = []
_12S = []

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
        print("Alert3")
    except NoAlertPresentException:
        print("No Alert3")
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
            driver.refresh()
            sleep(2)
            winsound.Beep(2500, 10000)
            driver.refresh()
            sleep(1)
            home_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__home  .participant__participantName a').text
            away_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__away  .participant__participantName a').text
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
                sleep(2)
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
            home_form_checker()
            away_form_checker()
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
            data_break_zeroes1(z=i, ent1=fir_ent)
            driver.close()
            driver.switch_to.window(window_before)

    except NoSuchElementException:
        try:
            team_data()
            odds_checker()
            driver.find_element(By.LINK_TEXT, "H2H").click()
            status_ = None
            for p in range(INDP_MATCH_SAMPLE):
                status_ = show_more_matches()
            if status_ != 0:
                home_form_checker()
                away_form_checker()
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
                append_zeroes1()
            else:
                data_break_zeroes2(z=i)
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
                           f"prob_12s = {prob_12s}\nprob_HWs = {prob_HWs}\nprob_AWs = {prob_AWs}\n"
                           f"prob_12_H_indps = {prob_12_H_indps}\n"
                           f"prob_HW_H_indps = {prob_HW_H_indps}\nprob_AW_H_indps = {prob_AW_H_indps}\n"
                           f"prob_12_A_indps = {prob_12_A_indps}\n"
                           f"prob_HW_A_indps = {prob_HW_A_indps}\nprob_AW_A_indps = {prob_AW_A_indps}\n"
                           f"home_z_prob = {home_z_prob}\naway_z_prob = {away_z_prob}\ndiff_z_prob = {diff_z_prob}\n"
                           f"sport = '{sport}_{i}'\n_1HWS = {_1HWS}\n_2AWS = {_2AWS}\n"
                           f"_12S = {_12S}\nmatch_date = '{set_date_s_size()[0]}'")
            except UnicodeError:
                pass
            except IndexError:
                continue

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
                       f"prob_12s = {prob_12s}\nprob_HWs = {prob_HWs}\nprob_AWs = {prob_AWs}\n"
                       f"prob_12_H_indps = {prob_12_H_indps}\n"
                       f"prob_HW_H_indps = {prob_HW_H_indps}\nprob_AW_H_indps = {prob_AW_H_indps}\n"
                       f"prob_12_A_indps = {prob_12_A_indps}\n"
                       f"prob_HW_A_indps = {prob_HW_A_indps}\nprob_AW_A_indps = {prob_AW_A_indps}\n"
                       f"home_z_prob = {home_z_prob}\naway_z_prob = {away_z_prob}\ndiff_z_prob = {diff_z_prob}\n"
                       f"sport = '{sport}'\n_1HWS = {_1HWS}\n_2AWS = {_2AWS}\n"
                       f"_12S = {_12S}\nmatch_date = '{set_date_s_size()[0]}'")
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
                bayesian_12_d = []

                for q in range(len(home_teams)):
                    try:
                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + rdm.random())
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (_2AWS[q] + rdm.random())
                            bayesian_12 = 0.5 * (_12S[q] + rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + _1HWS[q])
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + _2AWS[q])
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[1]:
                            bayesian_home_Win = rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random()
                            bayesian_away_Win = away_z_prob[q] * rdm.random()
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random()
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * rdm.random()
                            bayesian_away_Win = _2AWS[q] * rdm.random()
                            bayesian_12 = _12S[q] * rdm.random()
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * _1HWS[q]
                            bayesian_away_Win = away_z_prob[q] * _2AWS[q]
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q]
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random()))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + rdm.random()))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + _1HWS[q]))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + _2AWS[q]))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q]))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt(rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(_2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt(_12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * rdm.random())
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(_2AWS[q] * rdm.random())
                            bayesian_12 = math.sqrt(_12S[q] * rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * _1HWS[q])
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * _2AWS[q])
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    except IndexError:
                        continue

                for q in range(len(bayesian_home_Win_d)):
                    if q == 0:
                        for i in range(11):
                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                           f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                           f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                           f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                    try:
                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if h_form_D[q] == 0 and a_form_D[q] == 0:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                if h_form_D[q] == 0 or a_form_D[q] == 0:
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
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
            bayesian_12_d = []

            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS[0]:
                        bayesian_home_Win = (prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))
                        bayesian_away_Win = (prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))
                        bayesian_12 = (prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

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
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[2]:
                        bayesian_home_Win = home_z_prob[q]
                        bayesian_away_Win = away_z_prob[q]
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[3]:
                        bayesian_home_Win = _1HWS[q]
                        bayesian_away_Win = _2AWS[q]
                        bayesian_12 = _12S[q]
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[4]:
                        bayesian_home_Win = home_z_prob[q] * diff_z_prob[q]
                        bayesian_away_Win = away_z_prob[q] * diff_z_prob[q]
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])) * diff_z_prob[q]
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                       f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                       f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
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
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

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
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

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
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0]:
                        prob_matches_home_W_against_EO = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        bayesian_12 = ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[2]:
                        bayesian_home_Win = (home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - home_z_prob[q])))
                        bayesian_away_Win = (away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - away_z_prob[q])))
                        bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[3]:
                        bayesian_home_Win = (_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - _1HWS[q])))
                        bayesian_away_Win = (_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - _2AWS[q])))
                        bayesian_12 = (_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - _12S[q])))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)
                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                       f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                       f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                            if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
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
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = _1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = _2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = _12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(_1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(_2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = np.cbrt(_12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q])
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q])
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q])
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q]
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q]
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q]
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q]))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q]))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q]))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * rdm.random() * _1HWS[q])
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * rdm.random() * _2AWS[q])
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q])
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        except IndexError:
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                               f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                               f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
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
                    bayesian_12_d = []

                    for q in range(len(home_teams)):
                        try:
                            if Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[6]:
                                bayesian_home_Win = ((1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))) ** 0.25
                                bayesian_away_Win = ((1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))) ** 0.25
                                bayesian_12 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))) ** 0.25
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[7]:
                                bayesian_home_Win = (home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))) ** 0.25
                                bayesian_away_Win = (away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))) ** 0.25
                                bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))) ** 0.25
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        except IndexError:
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                               f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                               f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                        if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                        if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                        if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                            if ((BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q])) and (bayesian_12_d[q] >= CONFINTVLS[-1]):

                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL or bayesian_away_Win_d[q] > CONFINTVL:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (((home_positions[q] <= away_positions[q]) and (home_points[q] >= away_points[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q])) or ((home_positions[q] >= away_positions[q]) and (home_points[q] <= away_points[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]))):
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] >= FORM_VALUE and a_form_W[q] <= (1 - FORM_VALUE))) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] >= FORM_VALUE and h_form_W[q] <= (1 - FORM_VALUE))):
                                        if BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
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

    print_all_data()

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
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = 0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = 0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + rdm.random())
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (_1HWS[q] + rdm.random())
                            bayesian_away_Win = 0.5 * (_2AWS[q] + rdm.random())
                            bayesian_12 = 0.5 * (_12S[q] + rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = 0.5 * (home_z_prob[q] + _1HWS[q])
                            bayesian_away_Win = 0.5 * (away_z_prob[q] + _2AWS[q])
                            bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[1]:
                            bayesian_home_Win = rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_12 = _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random()
                            bayesian_away_Win = away_z_prob[q] * rdm.random()
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random()
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * rdm.random()
                            bayesian_away_Win = _2AWS[q] * rdm.random()
                            bayesian_12 = _12S[q] * rdm.random()
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * _1HWS[q]
                            bayesian_away_Win = away_z_prob[q] * _2AWS[q]
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q]
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random()))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + rdm.random()))
                            bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + rdm.random()))
                            bayesian_12 = math.sqrt(0.5 * (_12S[q] + rdm.random()))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                            bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + _1HWS[q]))
                            bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + _2AWS[q]))
                            bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q]))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt(rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = math.sqrt(_2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_12 = math.sqrt(_12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * rdm.random())
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(_1HWS[q] * rdm.random())
                            bayesian_away_Win = math.sqrt(_2AWS[q] * rdm.random())
                            bayesian_12 = math.sqrt(_12S[q] * rdm.random())
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                            bayesian_home_Win = math.sqrt(home_z_prob[q] * _1HWS[q])
                            bayesian_away_Win = math.sqrt(away_z_prob[q] * _2AWS[q])
                            bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    except IndexError:
                        continue

                for q in range(len(bayesian_home_Win_d)):
                    if q == 0:
                        for i in range(11):
                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                                file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                           f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                           f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                           f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                    try:
                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if h_form_D[q] == 0 and a_form_D[q] == 0:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                if h_form_D[q] == 0 or a_form_D[q] == 0:
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                        if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                                        else:
                                            if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

                        if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)

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
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

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
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[2]:
                        bayesian_home_Win = home_z_prob[q]
                        bayesian_away_Win = away_z_prob[q]
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[3]:
                        bayesian_home_Win = _1HWS[q]
                        bayesian_away_Win = _2AWS[q]
                        bayesian_12 = _12S[q]
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS[4]:
                        bayesian_home_Win = home_z_prob[q] * diff_z_prob[q]
                        bayesian_away_Win = away_z_prob[q] * diff_z_prob[q]
                        bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])) * diff_z_prob[q]
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                       f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                       f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                if X != PROB_METRICS[2] and X != PROB_METRICS[3] and X != PROB_METRICS[4]:
                                    if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

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
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

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
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

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
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0]:
                        prob_matches_home_W_against_EO = rdm.random()
                        bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_matches_home_W_against_EO)))
                        prob_matches_away_W_against_EO = rdm.random()
                        bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_matches_away_W_against_EO)))
                        prob_12 = rdm.random()
                        bayesian_12 = ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[2]:
                        bayesian_home_Win = (home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - home_z_prob[q])))
                        bayesian_away_Win = (away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - away_z_prob[q])))
                        bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                    if X == PROB_METRICS1[1] and Y == PROB_METRICS1[3]:
                        bayesian_home_Win = (_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - _1HWS[q])))
                        bayesian_away_Win = (_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - _2AWS[q])))
                        bayesian_12 = (_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - _12S[q])))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)
                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                       f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                       f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                            if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                        if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                            if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF_XLR and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                except UnicodeError:
                    pass
                except IndexError:
                    continue
                except OSError:
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
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
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = _1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = _2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = _12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(_1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(_2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = np.cbrt(_12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                                bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q])
                                bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q])
                                bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q])
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q]
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q]
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q]
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                                bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q]))
                                bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q]))
                                bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q]))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                                bayesian_home_Win = np.cbrt(home_z_prob[q] * rdm.random() * _1HWS[q])
                                bayesian_away_Win = np.cbrt(away_z_prob[q] * rdm.random() * _2AWS[q])
                                bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q])
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        except IndexError:
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                               f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                               f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                                if (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2):
                                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                        with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                            writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                            else:
                                                if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF_XLR / 2) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

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
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[1]:
                                bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                                bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                                bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[6]:
                                bayesian_home_Win = ((1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))) ** 0.25
                                bayesian_away_Win = ((1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))) ** 0.25
                                bayesian_12 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))) ** 0.25
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                            if Z == COMBINERS[7]:
                                bayesian_home_Win = (home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))) ** 0.25
                                bayesian_away_Win = (away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))) ** 0.25
                                bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))) ** 0.25
                                baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_12=bayesian_12)

                        except IndexError:
                            continue

                    for q in range(len(bayesian_home_Win_d)):
                        if q == 0:
                            for i in range(11):
                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                                    file.write(f"CONFIDENCE INTERVAL - {CONFINTVL_XLR}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                               f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|BAYESIAN {OUTCOMES[0]}|"
                                               f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|"
                                               f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                        try:
                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_D[q] == 0 and a_form_D[q] == 0:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_0.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_1.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]):
                                        if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_2.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_W[q] > a_form_D[q]) and (bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE_XLR and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE_XLR and h_form_W[q] > h_form_D[q]) and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q])):
                                    if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                        if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_3.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                    if h_form_D[q] == 0 or a_form_D[q] == 0:
                                        if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_4.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF and (bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]):
                                        if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_5.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_6.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_7.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_8.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                        if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                            if (BAY_DIFF_XLR / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:

                                                with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_9.txt", mode="a") as file:
                                                    writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                            if bayesian_home_Win_d[q] > CONFINTVL_XLR or bayesian_away_Win_d[q] > CONFINTVL_XLR:
                                if (home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP) and (h_form_W[q] >= FORM_VALUE_XLR or a_form_W[q] >= FORM_VALUE_XLR) and abs(h_form_W[q] - a_form_W[q]) >= FORM_DIFF:
                                    if ((bayesian_home_Win_d[q] >= bayesian_away_Win_d[q]) and (home_positions[q] <= away_positions[q]) and (h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] <= a_form_D[q])) or ((bayesian_home_Win_d[q] <= bayesian_away_Win_d[q]) and (home_positions[q] >= away_positions[q]) and (a_form_W[q] > h_form_W[q] and a_form_L[q] < h_form_L[q] and a_form_D[q] <= h_form_D[q])):
                                        if BAY_DIFF_XLR <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS_XLR[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_10.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        except UnicodeError:
                            pass
                        except IndexError:
                            continue
                        except OSError:
                            pass
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_xlr_{i}.txt", mode="a") as file:
                            file.write("\n\n\n\n\n")


driver.quit()

end_time = time.time()
print(f"run speed: {end_time - start_time}s")
