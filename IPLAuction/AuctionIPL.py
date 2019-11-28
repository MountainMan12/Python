#-------------IPL Auction--------------------
#Author: Pawan Verma (2018211004)

#Reading the player dataset
import pandas as pd
import numpy as np
import random
#path="D:\\SEMESTER 3\\SCE\\team_assignment2"

url = "https://web.iiit.ac.in/~tarpit.sahu/ipl_auctions_dataset.txt"
df = pd.read_csv(url, header = None, sep=':')
headers = ["Player_Name","Country","Attribute","Price"]

df.columns = headers
#df2 = df.drop_duplicates(subset="Player_Name", keep='first', inplace=False)
#Reading the config.txt file
#params = pd.read_csv("config.txt", header=None, nrows=5, sep=':')
#headers_params = ["Attribute","ll","ul"]
#params.columns = headers_params

teams = pd.read_csv("config.txt", skiprows=7,header=None, sep=':')
headers_teams = ["Team_name","Budget"]
teams.columns = headers_teams

team_names = list(teams["Team_name"])
df2 = df
'''Team Selection
Each team gets a limited budget of INR 1 crore and each team
can select no more than 18 players'''
random.seed(100)
for k in range(0,len(team_names)):
    budget = 10000000
    n = 18
    #Batsman
    bat = df2[(df2['Attribute'] == 'Batsman') & (df2['Country'] == 'India')].sample(n = np.random.randint(low = 5, high = 7, size = 1))
    df2 = df2.drop(bat.index) #This player will not be selected again
    n = n - len(bat)
    rem_budget = budget - bat['Price'].sum()
    #Bowlers
    bowl = df2[(df2['Attribute'] == 'Bowler') & (df2['Country'] == 'India')].sample(n = np.random.randint(low = 4, high = 6, size = 1))
    df2 = df2.drop(bowl.index)
    n = n - len(bowl)
    rem_budget = rem_budget - bowl['Price'].sum()
    #WicketKeeper
    wk = df2[(df2['Attribute'] == 'Wicket Keeper') & (df2['Country'] == 'India')].sample(n = np.random.randint(low = 1, high = 2, size = 1))
    df2 = df2.drop(wk.index)
    n = n - len(wk)
    rem_budget = rem_budget - wk['Price'].sum()
    #All rounder
    allr = df2[(df2['Attribute'] == 'All-Rounder') & (df2['Country'] == 'India')].sample(n = np.random.randint(low = 2, high = 4, size = 1))
    df2 = df2.drop(allr.index)
    n = n - len(allr)
    rem_budget = rem_budget - allr['Price'].sum()
    #Overseas
    osea = df2[(df2['Country'] != 'India')].sample(n = np.random.randint(low = 4, high = 7, size = 1))
    df2 = df2.drop(osea.index)
    n = n - len(osea)
    rem_budget = rem_budget - osea['Price'].sum()

    ipl_team = pd.concat([bat,bowl,wk,allr,osea])
    #Checking whether a team exceeded the alloted budget
    if(rem_budget < 0):
        print('IPL TEAM ' + str(i) + 'is exceeding budget')
        
    #Checking whether the size of the team does not exceed 18 players
    if (len(ipl_team) > 18):
        diff = len(ipl_team) - 18
        ind = list(ipl_team.index)
        for i in range(0, diff):
            drop_indices = random.choice(ind)
            ipl_team = ipl_team.drop(drop_indices)

    fn = team_names[k]+str('.txt')
    file1 = open(fn, "w")
    file1.write(team_names[k] + '\n' + '\n')
    for j in range(0, len(ipl_team)):
        file1.write('Player '+str(j+1)+'\n')
        file1.write('Name: '+str(list(ipl_team["Player_Name"])[j])+'\n')
        file1.write('Country: '+str(list(ipl_team["Country"])[j])+'\n')
        file1.write('Ability: '+str(list(ipl_team["Attribute"])[j])+'\n')
        file1.write('Fees: ' +str(list(ipl_team["Price"])[j])+'\n'+'\n'+'\n')

    file1.close()



