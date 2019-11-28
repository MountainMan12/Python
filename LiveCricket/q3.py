#Python Program to monitor cricket score 
#Author: Pawan Verma (2018211004)

import requests
import sys
import re
from bs4 import BeautifulSoup
from playsound import playsound as ps

def score_tracker(r, w, o, q):
    new_scores = live_cricket_status()
    if(new_scores[0] - r == 1):
        print('Just a single')
        r = r + 1
        print('Live Score '+ str(q) + ':' + str(r) + '\\' + str(new_scores[1]))
        print('Overs:', new_scores[2])
        ps('boundary.mp3')
    elif(new_scores[0] - r == 4):
        print('A Boundary!!!')
        ps('boundary.mp3')
        r = r + 4
        print('Live Score '+ str(q) + ':' + str(r) + '\\' + str(new_scores[1]))
        print('Overs:', new_scores[2])
    elif(new_scores[0] - r == 6):
        print('it\'s a six')
        ps('sixer.mp3')
        r = r + 6
        print('Live Score '+ str(q) + ':' + str(r) + '\\' + str(new_scores[1]))
        print('Overs:', new_scores[2])
    elif(new_scores[1] - w == 1):
        print('A wicket has fallen')
        ps('wicket.mp3')
        print('Live Score '+ str(q) + ':' + str(new_scores[0]) + '\\' + str(new_scores[1]))
        print('Overs:', new_scores[2])
    elif(new_scores[0] - r == 0 or new_scores[2] - o == 0):
        r = r
        o = o
    score_tracker(r,w,o,q)

def display_initial_score(x,y,z,t):
    print('Live Score '+ str(t) + ':' + str(x) + '\\' + str(y))
    print('Overs:', z)
    if(y != str('all out')):
        score_tracker(x,y,z,t)

def live_cricket_status():
    r = requests.get(URL)
    s = BeautifulSoup(r.content ,'html5lib')
    
    live_match = s.find('div', attrs={"cb-lv-scrs-col cb-text-live"})
    if(live_match):
        if(str('won') in live_match.text):
            match_status = s.find('div', attrs={"cb-lv-scrs-col text-black"}).text
            print(match_status)
            sys.exit
    
    if(live_match):
        score_card = s.find('a', attrs={"cb-lv-scrs-well cb-lv-scrs-well-live"}).text
        if(str('   ') in score_card):
            score_card = score_card.replace('   ',"")
    
        bat_team = re.search(r'(?<=^)\w+',score_card).group()
        runs = int(re.search(r'(?<= )\w+', score_card).group())
        if(str('all out') in score_card):
            wickets = str('all out')
        else:
            wickets = int(re.search(r'(?<=\/)\w+', score_card).group())
        overs = float(re.search(r'(?<=\()\w+.?.?', score_card).group())

        if(live_match.text == str('Innings Break')):
            print('Runs needed for opposition to win:', runs+1)

        return runs,wickets,overs,bat_team

URL = "https://www.cricbuzz.com/cricket-match/live-scores"
r = requests.get(URL)

s = BeautifulSoup(r.content ,'html5lib')
live_match = s.find('div', attrs={"cb-lv-scrs-col cb-text-live"})
if(not live_match):
    match_status = s.find('div', attrs={"cb-lv-scrs-col cb-text-complete"}).text
    print('There are no live matches going on')
    print("The latest cricket news is: ", match_status)
    sys.exit
if(live_match):
    if(str('Break') not in live_match and str('opt') not in live_match and str('need') not in live_match):
        print('Live match is in progress')
        match_name = s.find('a', attrs={"text-hvr-underline text-bold"}).text
        print(match_name)
        print(live_match.text)
        out = live_cricket_status()
        display_initial_score(out[0],out[1],out[2],out[3])








