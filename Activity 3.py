import re, random
from colorama import Fore,init
init(autoreset=True)
destination={
    "beaches": ["Bali", "Maldives", "Phuket"]
    "mountains" : ["Swiss Alps", "Rocky Moutains", "Himalayas"]
    "cities": ["Tokyo", "Paris", "New York"]
}
Joke = [
    "Why don't programmers like nature? Too many bugs!!!!!!!!!", "Why do travelers always feel warm? Because of all their hot spots!!!!!!!!!"
]
def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())
    def recommend():
        print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
        preference = input(Fore.YELLOW + "You: ")
        preference = normalize_input(preference)
    if preference in destinations:
        suggestion = random.choice(destination[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer=input(Fore.YELLOW + "You: ").lower()

        if answer="yes":
            print(Fore.GREEN + f"TravelBot: Awesone! Enjoy{suggestion}!")