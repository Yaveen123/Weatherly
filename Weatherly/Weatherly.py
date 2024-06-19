from gui_facade import *

finalfacade.ipdata()
program = [True, False]
while program[0]:
    question = finalfacade.standardscreen(False)
    if question[1] == True:
        importance = finalfacade.locationchangescreen([900, 620])
        finalfacade.locdata(importance[0])
    program = question
