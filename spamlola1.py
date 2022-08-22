import pyautogui, webbrowser
from time import sleep

def main():
# phone, no space
  phone = '+56982449005'
# open whatsapp web, hit the chat box on the web 
  webbrowser.open(f'https://web.whatsapp.com/send?phone={+56982449005}') 
  sleep(10) # Text File, Hit with click on the web 
  with open('vacalola.txt','r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")



while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
