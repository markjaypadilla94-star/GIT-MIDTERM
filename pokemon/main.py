import random
import requests

pokemon_list = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee"]
answer = random.choice(pokemon_list)

url = "https://pokeapi.co/api/v2/pokemon/" + answer
response = requests.get(url)

if response.status_code == 200:
   data = response.json()

   height = data["height"] * 10
   weight = data["weight"] / 10

   print("POKEMON GUESSING GAME")
   print("Guess the Pokemon!")
   print("Height:", height, "cm")
   print("Weight:", weight, "kg")
   print("You have 3 attempts.")

   for attempt in range(3):
       guess = input("Enter Pokemon name: ")
       if guess == answer:
           print("Correct! You win!")
           break
       else:
           print("Wrong guess!")
   else :
       print("Game Over!")
       print("Pokemon was :", answer)

else:
    print("Could not get the pokemon")