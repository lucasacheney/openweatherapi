import  json, requests
import time
import os

def cont():
  cont_program = input('\nContinue?\n(y)es or (n)o:')
  if cont_program == 'y':
    if (os.name == 'posix'):
      os.system('clear')
    else:
      os.system('cls')
    repeat()
  elif cont_program == 'n':
    print("\nThank you for using the application!")
    time.sleep(2)
    if (os.name == 'posix'):
      os.system('clear')
    else:
      os.system('cls')
    quit()
  elif cont_program:
    cont()

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "479dbb188f1c7f9efcd641b06c174143"
    
def repeat():
  
  zip = input("Enter the zip code of the location that you wish to know the forecast for.\n#")
  print()

  url = f"{base_url}?zip={zip}&units=imperial&APPID={appid}"
  
  response = requests.get(url)
  unformated_data = response.json()

  try:
    valid_zip = unformated_data["main"]
  except:
    print("Enter a valid zip code.")
    print()
    time.sleep(2)
    repeat()

  temp = unformated_data["main"]["temp"]
  print(f"The current temperature is: {temp}°F")

  temp_min = unformated_data["main"]["temp_min"]
  print(f"The minimum temperature today is: {temp_min}°F")

  temp_max = unformated_data["main"]["temp_max"]
  print(f"The max temperature today is: {temp_max}°F")

  cont()

repeat()