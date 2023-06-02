import requests,pyjokes,wikipedia
from bs4 import BeautifulSoup
from googletrans import Translator
from lab2 import amin

def ords():
    url = "https://gogo.mn/horoscope/western/today"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    ord = input("ymr ord: ")
    zurhai = soup.find("div", {"id": f"zodiac-switcher-mobile-{ord}"}).text.split("\n")
    zurhai = [element for element in zurhai if element != '']
    ordnud = soup.find_all("div", class_=f"zodiac-body-{ord}")[1].text.split("\n")
    ordnud = [element for element in ordnud if element != '']
    ordnud = [line.strip() for line in ordnud if line.strip()]

    print(zurhai,ordnud)

def weather():
    url = "https://ikon.mn/wetter"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    agaar = soup.find("div", class_="wfc").text.split("\n")
    agaar = [element for element in agaar if element != '']
    agaar = [line.strip() for line in agaar if line.strip()]
    agaar.insert(1,'Өдөр')
    agaar.insert(4,'Шөнө')
    agaar.insert(6,'Салхи')
    agaar.remove('|')
    print(agaar)

def tell_joke():
    joke = pyjokes.get_joke()
    translator = Translator()
    translation = translator.translate(f'{joke}', dest='MN').text
    print(translation)

def wikiped():
    wiki = input('hailtaa oruulna uu -> ')
    translator1 = Translator()
    translation1 = translator1.translate(f'{wiki}', dest='en').text
    info = wikipedia.summary(translation1)
    translator = Translator()
    translation = translator.translate(f'{info}', dest='MN').text
    print(translation)

def translate():
    print('mongol-angli eswel angli-mongol')    
    select = input('--> ')
    if select == 'angli-mongol':
        word = input('write word ')
        translator = Translator()
        translation = translator.translate(f'{word}', dest='MN').text
        print(translation)
    elif select == 'mongol-angli':
        word = input('үгээ бичнэ үү ')
        translator = Translator()
        translation = translator.translate(f'{word}', dest='en').text
        print(translation)
    else:
        print('уучлаарай та дээрх сонголтоос сонгоно дахин оролдоно уу')
        print('please try again choose another one')

def main():
    print('\nсайн байна уу. Би zurhai, tsag agaar, translate, onigoo, болон wikipedia гаас хайлт хийж өгч чадна')
    choose = input('та дээрх сонголтуудаас нэгийг сонгоно бичнэ үү - ')
    print(choose)
    if choose in 'zurhai':
        ords()
    elif choose in 'tsag agaar':
        weather()
    elif choose in 'translate':
        translate()
    elif choose in 'onigoo':
        tell_joke()
    elif choose in 'wikipedia':
        wikiped()
    elif choose in 'traffic':
        amin()

if __name__ == '__main__':
    main()