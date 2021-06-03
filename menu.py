from data import Data

class Menu:
    
    def createMenu():
        menuItems = Data.getSchedule().games
        
        for item in menuItems:
            sequentialId = item.sequentialId
            #print(sequentialId)
            gameId = item.gameId  
            print(item.link)
            print(item.away.name)
            print(item.away.logo)
            print(item.away.wins)
            print(item.away.losses)
            print(item.home.name)
            print(item.home.logo)
            print(item.home.wins)
            print(item.home.losses)
            print(item.time + ' ' + str(item.timezone))
            print('\n----------\n')
