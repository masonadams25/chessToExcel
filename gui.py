from tkinter import *
from tkinter.ttk import *

from parse import *
 
root = Tk()
root.title("Chess To Excel")

usernameEntry = StringVar()
monthEntry = StringVar()
yearEntry = StringVar()

def dev():
    submit(True, "Masonrules9", "07", "2023")

def submit(passedVar = False, username = '', month = '', year = ''): 
    if passedVar == False:
        username = str(usernameEntry.get())
        month = str(monthEntry.get())
        year = str(yearEntry.get())

    try:
        response = get_player_games_by_month(username = username, year = year, month = month)
        games = response.json['games']

        if len(games) > 0:
            parseGames(games, username, month, year)
            writeToExcel(dailyGames)
            for day in dailyGames:
                print(str(dailyGames[day]['date']).ljust(6) + 
                    "- Avg rating: " + str(round(float(dailyGames[day]['avgRating']),2)).ljust(7) +
                    "- Rating: " + str(dailyGames[day]['rating']).ljust(5) +
                    "- Games: " + str(dailyGames[day]['totGames']).ljust(3) +
                    "- Wins: " + str(dailyGames[day]['wins']).ljust(3) +
                    "- Losses: " + str(dailyGames[day]['losses']).ljust(3) +
                    "- Win %: " + str(round(float(dailyGames[day]['winPercent']),2)).ljust(6) +
                    "- Avg acc: " + str(round(float(dailyGames[day]['avgAccuracy']),2)).ljust(7))
        else:
            print("No games found in time period")
    except:
        response = get_player_games_by_month(username = username, year = year, month = month)
        games = response.json['games']

        if len(games) > 0:
            parseGames(games, username, month, year)
            writeToExcel(dailyGames)
            for day in dailyGames:
                print(str(dailyGames[day]['date']).ljust(6) + 
                    "- Avg rating: " + str(round(float(dailyGames[day]['avgRating']),2)).ljust(7) +
                    "- Rating: " + str(dailyGames[day]['rating']).ljust(4) +
                    "- Games: " + str(dailyGames[day]['totGames']).ljust(3) +
                    "- Wins: " + str(dailyGames[day]['wins']).ljust(3) +
                    "- Losses: " + str(dailyGames[day]['losses']).ljust(3) +
                    "- Win %: " + str(round(float(dailyGames[day]['winPercent']),2)).ljust(6) +
                    "- Avg acc: " + str(round(float(dailyGames[day]['avgAccuracy']),2)).ljust(7))

    username = ''
    month = ''
    year = ''
     
     
name_label = Label(root, text = 'Username', font=('calibre',10, 'bold'))
name_entry = Entry(root,textvariable = usernameEntry, font=('calibre',10,'normal'))
  
month_label = Label(root, text = 'Month', font = ('calibre',10,'bold'))
month_entry=Entry(root, textvariable = monthEntry, font = ('calibre',10,'normal'))

year_label = Label(root, text = 'Year', font = ('calibre',10,'bold'))
year_entry=Entry(root, textvariable = yearEntry, font = ('calibre',10,'normal'))
  
sub_btn=Button(root,text = 'Submit', command = submit)
dev_btn=Button(root,text = 'Dev', command = dev)
  
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
month_label.grid(row=1,column=0)
month_entry.grid(row=1,column=1)
year_label.grid(row=2,column=0)
year_entry.grid(row=2,column=1)
sub_btn.grid(row=3,column=1)
dev_btn.grid(row=3,column=0)

root.mainloop()