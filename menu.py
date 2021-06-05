from data import Data
from utils import Image

class Menu:
    def __init__(self, canvas):
        self.canvas = canvas

    def createMenu(self):

        menuItems = Data.getSchedule().games
        x = 0 
        y = 0
        buttonWidth = 960
        buttonHeight = 100

        for item in menuItems:
            sequentialId = item.sequentialId
            #print(sequentialId)

            #image = Image.open(os.path.join(currentDirectory, 'images/exposure-compensation-up.png'))
		    #evUpImage = ImageTk.PhotoImage(image)
		    #evUpButton = ttk.Button(root, compound=tk.CENTER, image=evUpImage, command=lambda: Buttons.handler(buttonDictionary, 'evUp'))
		    #evUpButton['style'] = 'default.TButton'
		    #evUpButton.place(x=borderLeft+(buttonWidth*6),y=0,width=buttonWidth,height=buttonHeight)


            gameId = item.gameId  
            print(item.link)
            print(item.away.name)
            awayLogo = Image.WebImageToBase64(item.away.logo)
            print(item.away.wins)
            print(item.away.losses)
            print(item.home.name)
            homeLogo = Image.WebImageToBase64(item.home.logo)
            print(item.home.wins)
            print(item.home.losses)
            print(item.time + ' ' + str(item.timezone))
            print('\n----------\n')

            # Set position of next button...
            if (x + buttonWidth) == buttonWidth:
                x = x * 2
            else:
                x = 0
            y = y + buttonHeight