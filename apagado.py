import os
import subprocess

def shutdown_computer():
    if os.name == 'nt':  # Para sistemas Windows
        subprocess.call(['shutdown', '/s', '/t', '0'])
    elif os.name == 'posix':  # Para sistemas Linux o macOS
        subprocess.call(['shutdown', '-h', 'now'])
    else:
        print('Lo siento, este ejecutable solo es compatible con Windows, Linux y macOS.')

def main():
    print('¡Este ejecutable apagará tu computadora!')
    confirm = input('¿Estás seguro de que deseas continuar? (y/n): ')
    if confirm.lower() == 'y':
        shutdown_computer()
    else:
        print('Apagado cancelado.')

if __name__ == '__main__':
    main()