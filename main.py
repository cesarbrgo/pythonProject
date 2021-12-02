# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    print("benvingut al conversor de temperatures")


print('selecciona una una opcio')
print('1-per convertir a farenheit')
print('2-per convertir a kelvin ')
print('qualsevol altre per sortir ')
opcio = int(input('selecciona la opcio: '))
temperatura = int(input('introdueix una temperatura: '))
match opcio:
    case 1:
        print('farenheit=', ((temperatura - 32) * 5 / 9))
    case 2:
        print('kelvin=', temperatura + 273)
    case _:
        print('adeu')

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
