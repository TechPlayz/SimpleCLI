import pyfiglet as pf #ASCII ART
import os
print('Welcome to Basic Command Line Interface By TechPlayz')

while True:
    cmd = input('\nCommand: ')

    #COMMAND HANDLER
    try:
        args = cmd.upper().split() #argument handler

        #1. EXIT COMMAND
        if args[0] in ['EXIT','QUIT']:
            break

        #2. HELP COMMAND (READS FROM HELP.TXT)
        elif args[0] == 'HELP':
            try:
                f = open('help.txt', 'r')
                print(f.read())
                f.close()
            except:
                print('help.txt not found')
            
        #3. OUTPUT COMMAND
        elif args[0] == 'SAY':
            for x in args[1::]:
                print(x, end=' ')
        
        #4. COUNT COMMAND
        elif args[0] == 'COUNT':
            start = int(args[1])
            stop = int(args[2])
            for x in range(start, stop+1):
                print(x)

        #5. ASCII ART command
        elif args[0] == 'ASCII':
            asciiStr = ''
            for x in range(1,len(args)):
                asciiStr = asciiStr + args[x] + ' '
            print(pf.figlet_format(asciiStr))

        #6. CLEAR COMMAND
        elif args[0] in ['CLEAR', 'CLS']:
            os.system('cls')

        #7. ADD COMMAND
        elif args[0] in ['ADD', 'SUM']:
            addList = []
            for x in range(1, len(args)):
                addList.append(float(args[x]))
            print(sum(addList))

        #INVALID
        else:
            print('INVALID COMMAND, Type HELP for a list of commands')
    
    #exception if the argument list is empty
    except:
        pass