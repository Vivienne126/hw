import requests
url="https://uselessfacts.jsph.pl/random.json?language=en"

def facts():
    response=requests.get(url)
    if response.status_code==200:
        fact=response.json()
        print(f"The fact is: 🤷‍♀️🤷‍♀️🤷‍♀️ DID YOU KNOW!! {fact["text"]}")
    else:
        print("ERROR INCOMING!!! ❌❌❌ FAILED , FAILED to FETCH the DATA...🫨🫨🫨")

while True:
    user_input=input("PRESS!!! ENTER for a NEW FACT...✔️✔️✔️ or PRESS!!! Q or QUIT or BYE to quit👋👋")
    if user_input.lower()== in ["q" or "quit" or "bye"]:
        print("GoodBYE nice to see you...")
        break
    facts()