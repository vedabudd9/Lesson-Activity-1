import re, random
from colorama import Fore,init
init(autoreset=True)
destination= {
    "beaches" : ["Bali", "Maldives", "Phuket"]
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
        elif answer="no":
            print (Fore.RED + f"TravelBot: Let's try another.")
            recommened()
        else:
            print(Fore.RED+ "TravelBot: I'll suggest again.")
            recommended()
    else:print(Fore.RED+ "TravelBot: Sorry I don't think I have that type of destination.")
    show_help()
def packing_trip():
    print(Fore.CYAN + "TravelBot: Where to?")
    location= normalized_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN+"TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}.")
    print(Fore.Green + "- Pack versatile clothes.")
    print(Fore.GREEN + "-Bring charger/adapters.")
    print(Fore.GREEN + "-Check weather forecast.")
def tell_joke():
    print(Fore.YELLOW + f"TravelBot:{randon.choice(jokes)}")
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "-Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips(say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end. \n")
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name=imput(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you,{name}!")
    show_help()
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input= normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")
if_name_=="_main_":
  chat()
   