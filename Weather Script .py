from pathlib import Path
import platform
import time
import os

# This block gets the filename and uses it in the program.
# It doesn't matter were the file is located or what the filename is or will be.
filePath = str(Path(__file__).absolute())
fileExtention = filePath[len(filePath) - 3:]
directoryPath = str(os.path.dirname(os.path.abspath(__file__)))

name = filePath[(len(directoryPath) + 1):-len(fileExtention)] + '\n'


def sys_clear(name=None):
    ''' Clears terminal screen for diffrent OS's
    and takes a argument to print a string before clearing terminal screen'''

    if 'linux' or 'darwin' in platform.platform().lower():
        os.system('clear')
    elif 'windows' in platform.platform().lower():
        os.system('cls')
    else:
        # !!! Try to make a code that sends a message to your twitter. Just because you can.
        print("Sorry, Your OS is not known to me yet.")

    if name == None:
        []
    else:
        print(name)


sys_clear(name)

# localWeather arg might be for data that we'll get from the API outside of the class


class WeatherBaloon(object):
    def __init__(self, localWeather):
        self.localWeather = localWeather

    @staticmethod
    def menu():
        sys_clear(name)
        try:
            ''' Class WeatherBaloon menu. The number of methodes this class has'''
            print('Menu')

            answer = int(input('''
1. Check your current local weahter.
2. Convert Fahrenheit to Celsius or vice versa.
3. Quit

:> '''))

            while True:
                if answer == 1:
                    # WeatherBaloon.get_localweahter()
                    print('TEST FACE')
                    input('\nPress ENTEr to continue')
                elif answer == 2:
                    WeatherBaloon.get_tConv()
                elif answer == 3:
                    WeatherBaloon.quit()
                    break
                else:
                    WeatherBaloon.menu()
        except:
            WeatherBaloon.quit()

    @classmethod
    def get_localweahter(cls):
        ''' Get's local weather data from OpenWeather's API '''
        pass

    @staticmethod
    def get_tConv():
        try:
            while True:
                try:
                    sys_clear(name)
                    answer = int(input('''
1. Fahrenheit --> Celsius
2. Celsius --> Fahrenheit

:> '''))

                    if answer == 1:
                        answer = '°F'
                    elif answer == 2:
                        answer = '°C'
                except ValueError:
                    print('Keyboard err9r')
                    sys_clear(name)
                    continue

                sys_clear(name)

                temp = int(input(f"\nHow much {answer}?\n\n:> "))

                sys_clear(name)

                if answer == '°F':
                    degree = int(round((temp - 32) * 5 / 9))

                    print(f"\n{temp}°F is {degree}°C\n")
                else:
                    degree = int(round((9 * temp) / 5 + 32))
                    print(f"\n{temp}°C is {degree}°F.\n")

                time.sleep(5)
                sys_clear(name)

                answer = input('\nContinue?: (Y/N)\n\n:> ')
                if answer.lower() in ('y', 'yes', 'ok', 'oke', 'okee', 'sure', 'cool'):
                    WeatherBaloon.menu()
                else:
                    sys_clear(name)
                    print('the else')
                    WeatherBaloon.quit()
                    break
        except KeyboardInterrupt:
            sys_clear(name)
            print('keyin')
            WeatherBaloon.quit()

    @staticmethod
    def quit():
        sys_clear(name)
        print('\nGoodbye\n')


WeatherBaloon.menu()
