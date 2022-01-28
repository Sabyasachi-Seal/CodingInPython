command = ''
stopped = True
while True:
    command =  (input(">").lower())
    if command == 'start':
        if stopped == False:
            print('Car is already started....')
        elif stopped == True:
            print('Car Started...')
            stopped = False
    elif command== 'stop':
        if stopped == True:
            print('Car is already stopped.....')
        elif stopped == False:
            print('Car Stopped....')
            stopped = True
    elif command== 'quit':
        print('bye bye... meet ya soon')
        break
    elif command == 'help':
        print("""
Start -> Starts the car
Stop -> Stops the car
Quit -> Exit from the game
        """)
    else:
        print("""
Sorry , Command Unrecognised.
Type 'help' for instructions""")



