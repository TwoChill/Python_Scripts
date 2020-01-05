# !!! I should probably use subprocesses instead of os.
import os

# Listdr will let you know everything that is in a directory.
from os.path import isfile, join
from os import listdir

from pathlib import Path
import time
import sys

import platform

usr_answer = [('Y', 'y', 'yes', 'Yes', 'YES', 'ok',
               'Ok', 'OK', 'sure', 'Sure', 'SURE')]

#######################################################################################################


def sys_clear():
    ''' Clears terminal screen for diffrent OS's '''

    if 'linux' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        print("Sorry, Your OS is not known to me yet.")

#######################################################################################################


sys_clear()

#######################################################################################################

# While loop check for installation Pyinstaller
while True:
    answer = input("\nIs Pyinstaller installed on your system? (Y/N) :> ")

    # Clears the terminal of previous outputs.
    time.sleep(1)
    sys_clear()

    if answer in usr_answer[0]:
        break
    else:
        answer = input('''\nInstall Pyinstaller now? (Y/N) :> ''')
        time.sleep(1)

        # Clears the terminal of previous outputs.
        sys.stdout.write("\n")
        sys_clear()

        if answer in usr_answer[0]:
            # Checking current Python version.
            version = sys.version[0]
            if int(version) <= 1:
                os.system(f'pip install pyinstaller')
                time.sleep(4)
                sys_clear()
                break
            else:
                os.system(f'pip{version} install pyinstaller')
                time.sleep(4)
                sys_clear()
                break
        else:
            answer = input('\nDo you want to exit this script? (Y/N) :> ')

            if answer in usr_answer[0]:
                time.sleep(3)
                sys_clear()
                print('\nExiting script!')
                time.sleep(1)
                quit()
            else:
                time.sleep(1)
                sys_clear()
                continue

#######################################################################################################

# Makes a string of this file's filepath.
filePath = str(Path(__file__).absolute())

# Gets the file extention as a string (via string slicing).
fileExtention = filePath[len(filePath) - 3:]

# Gets the directoryPath as a string.
directoryPath = str(os.path.dirname(os.path.abspath(__file__)))

#######################################################################################################


def run_Setup():
    # Lists all the files in the directory of this script.
    onlyFiles = [f for f in listdir(directoryPath)
                 if isfile(join(directoryPath, f))]

    # Lists only the .py files in the directory of this script.
    onlyFiles = [f for f in onlyFiles if fileExtention in f]

    # File names can't have whitespaces in them. This loop replaces them with a underscore.
    num = 0
    for fn in onlyFiles:
        if ' ' in onlyFiles[num]:
            onlyFiles[num] = onlyFiles[num].replace(' ', "_")

            # Makes sure all files end with '.py' (and not '_.py')
            if '_.py' in onlyFiles[num]:
                onlyFiles[num] = onlyFiles[num][:(
                    len(onlyFiles[num]) - 4)] + '.py'

            # Writes the underscore filenames to the file.
            os.rename(fn, onlyFiles[num])
            num += 1

    # This variable will hold the correct filepath to uses for py2exe.
    fileName = ''  # LEAVE EMPTY!

    # If the program detects more then one Python file to convert to EXE.
    if len(onlyFiles) > 2:
        num = len(onlyFiles)

        # Prints .py files to choose from.
        while True:
            print("\n\tI've detected", num,
                  "more files.\n\tWhich one do you want to use?\n\n")
            num = 1
            for fn in onlyFiles:

                # Replaces the '_' with whitespaces. Doesn't change the filename.
                fn = fn.replace('_', " ")

                if num < 10 and fileExtention == ".py":
                    print(str(num) + ". ", fn)
                elif num >= 10 and fileExtention == ".py":
                    print(str(num) + ".", fn)
                else:
                    num -= 1
                num += 1
            while True:
                try:
                    num = int(input('\n:> '))
                    if num > len(onlyFiles):
                        print(f"\n{num} is not a valid number")
                        continue
                    else:
                        break
                except ValueError as e:
                    print("\nThat's not a number at all!")
                    continue

            # Expect usr input to be greater then max_index of onlyPfile list.
            if num >= len(onlyFiles):
                num == len(onlyFiles)

            answer = input("\nTurn '" + str(onlyFiles[(num - 1)]
                                            ) + "' into a executable file? (Y/N) :> ")
            if answer in usr_answer[0]:
                sys_clear()
                fileName = onlyFiles[(num - 1)]
                # Execute Pyinstaller with parm; onefile.
                os.system(
                    f'pyinstaller {fileName[:-3]} -w {fileName} --onefile --onedir')
                time.sleep(1)
                break
            else:
                sys_clear()
                continue

    # If there are NO .py files next to this script.
    elif len(onlyFiles) == 0:
        sys.stdout.write(
            "\nThere are no files to use in this directory!\n\nEXITING THE SCRIPT!")
        time.sleep(5)
        quit(0)

    # If there is 1 .py file next to this script.
    else:
        fileName = onlyFiles[0]
        sys.stdout.write(f'\n{fileName} found!\n\nExecuting Pyinstaller!\n')

#######################################################################################################


# Run the function
run_Setup()


# Should delete the 'setup.py' file after 10 seconds (Assuming the py2exe process takes LESS the 10 seconds to finish)
time.sleep(4)

sys.stdout.write('\nSUCCESSFUL!\n\n')

time.sleep(10)

quit()
