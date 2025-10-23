import requests

def get_joke():
    url="http://www.official-joke-api.appspot.com/random_joke"
    response=requests.get(url)

    if response.status_code==200:
        print(f"Full json response is {response.json()}🤖🤖")
        joke_data=response.json()
        return f"{joke_data["setup"]} - {joke_data["punchline"]} "
    else:
        return "not able to get joke"

def main():
    print("Welcome to joke genarator😊😊")
    while True:
        user_input=input("Press enter for new joke , press q or type quit for exiting/quitting 👍👍").strip().lower() #Strip for removing unwanted spaces and lower for converting to small letters
        if user_input in("q" , "quit"):
            print("Thanks for joining , BYE...✌️✌️")
            break
        joke=get_joke()
        print(joke)
