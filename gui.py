from tkinter import *
from tkinter.ttk import *

from parse import *
 
root = Tk()
root.title("Chess To Excel")

usernameEntry = StringVar()
monthEntry = StringVar()
yearEntry = StringVar()

endMonthEntry = StringVar()
endYearEntry = StringVar()

def reset():
    resetDict()
    print("Tool reset")

def dev():
    getGames(True, "Masonrules9", "8", "2023")

# Grabs and print games from one month
def getGames(passedVar = False, username = '', month = '', year = '', endMonth = '', endYear = '', printOutput = True): 
    if passedVar == False:
        username = str(usernameEntry.get())
        month = str(monthEntry.get())
        year = str(yearEntry.get())
    try:
        response = get_player_games_by_month(username = username, year = year, month = month)
        games = response.json['games']

        if len(games) > 0:
            parseGames(games, username, month, year)
            if printOutput == True:
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
        print("No games found in time period")

    username = ''
    month = ''
    year = ''

def getMultiGames():
        username = str(usernameEntry.get())
        startMonth = str(monthEntry.get())
        startYear = str(yearEntry.get())

        endMonth = str(endMonthEntry.get())
        endYear = str(endYearEntry.get())

        if endMonth == '' or endYear == '':
            getGames(username = username, month = startMonth, year = startYear, passedVar = True, printOutput = True)
            print("\n\n")
        else:
            printOutput = False
            for month in range(int(startMonth), int(endMonth) + 1):
                if month == int(endMonth):
                    printOutput = True
                getGames(username = username, month = month, year = startYear, passedVar = True, printOutput = printOutput)
            print("\n\n")


     
     
name_label = Label(root, text = 'Username', font=('calibre',10, 'bold'))
name_entry = Entry(root,textvariable = usernameEntry, font=('calibre',10,'normal'))
  
month_label = Label(root, text = 'Month', font = ('calibre',10,'bold'))
month_entry=Entry(root, textvariable = monthEntry, font = ('calibre',10,'normal'))

year_label = Label(root, text = 'Year', font = ('calibre',10,'bold'))
year_entry=Entry(root, textvariable = yearEntry, font = ('calibre',10,'normal'))

end_month_label = Label(root, text = 'End month (opt)', font = ('calibre',10,'bold'))
end_month_entry=Entry(root, textvariable = endMonthEntry, font = ('calibre',10,'normal'))

end_year_label = Label(root, text = 'End year (opt)', font = ('calibre',10,'bold'))
end_year_entry=Entry(root, textvariable = endYearEntry, font = ('calibre',10,'normal'))
  
sub_btn=Button(root,text = 'Submit', command = getMultiGames)
dev_btn=Button(root,text = 'Dev', command = dev)
reset_btn=Button(root,text = 'Reset', command = reset)
  
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

month_label.grid(row=1,column=0)
month_entry.grid(row=1,column=1)

year_label.grid(row=2,column=0)
year_entry.grid(row=2,column=1)

end_month_label.grid(row=1,column=2)
end_month_entry.grid(row=1,column=3)

end_year_label.grid(row=2,column=2)
end_year_entry.grid(row=2,column=3)

reset_btn.grid(row=3,column=2)
sub_btn.grid(row=3,column=1)
dev_btn.grid(row=3,column=0)

root.mainloop()