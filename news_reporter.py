def speak(str):
    from win32com.client import Dispatch
    utter = Dispatch("SAPI.SpVoice")
    utter.Speak(str)
    pass

def news(link):
    import requests

    result = requests.get(url=link)
    dict = result.json()
    # print(dict["articles"][0]["title"])
    speak("Here are some Top Headlines for the day.")
    for i in range(5):
        print(dict["articles"][i]["title"])
        speak(dict["articles"][i]["title"])
    speak("That was all for today. See you later.")
def main():
    speak("Press 1, for international NEWS.")
    speak("Press 2, for national NEWS.")
    speak("Press 3, for sports NEWS.")
    speak("Press 4, for business NEWS.")

    x = int(input("Enter Here: "))
    if x == 1:
        linkee = "https://newsapi.org/v2/everything?q=keyword&apiKey=3f004b68a7124ee7a1e0a3e26f83c922"
        news(linkee)
    elif x == 2:
        speak("Plese Enter your country.")
        country = input("Enter your Country: ").lower()
        country = country[:2]
        linkee = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey=3f004b68a7124ee7a1e0a3e26f83c922"
        news(linkee)
    elif x == 3:
        speak("Plese Enter your country.")
        linkee = "https://newsapi.org/v2/everything?q=sports&apiKey=3f004b68a7124ee7a1e0a3e26f83c922"
        news(linkee)
    elif x == 4:
        linkee = "https://newsapi.org/v2/everything?q=business&apiKey=3f004b68a7124ee7a1e0a3e26f83c922"
        news(linkee)


if __name__ == '__main__':
    main()