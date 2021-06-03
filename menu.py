from data import Data

class Menu:
    
    def createMenu(scheduleUrl, favoriteTeam):
        menuItems = Data.getDaysSchedule(scheduleUrl, favoriteTeam).games
        #TODO: BUILD MENU WITH DAYS SCHEDULE