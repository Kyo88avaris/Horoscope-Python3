'''
Site:
https://astrostyle.com/horoscopes/daily/{}/   {} = sign

required external plugin:
requests
beautifulsoup4

'''
import re
import requests
from bs4 import BeautifulSoup


def get_date(horoscope_content):
    date = horoscope_content.find('h2').text
    date = date.split()
    date = date[:-1]

    return date

def horoscope(horoscope_content):
    h_text = horoscope_content.find('p').text

    return h_text

def main():

    h_sign = ('aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

    user_input = input("""Please select your Sign from below:  You can either designate the number or type the sign
    1. Aries (Mar 31 - Apr 19)
    2. Taurus (Apr 20 - May 20)
    3. Gemini (May 21 - June 20)
    4. Cancer (June 21 - July 22)
    5. Leo (July 23 - Aug 22)
    6. Virgo (Aug 23- Sep 22)
    7. Libra (Sep 23 - Oct 22)
    8. Scorpio (Oct 23 - Nov 21)
    9. Sagittarius (Nov 22- Dec 21)
    10. Capricorn (Dec 22 - Jan 19)
    11. Aquarius (Jan 20 - Feb 18)
    12. Pisces (Feb 19 - Mar 20)\n\nInput: """)

    val = False

    while not val:
        if user_input.lower() in h_sign:
            try:
                sign = int(user_input)
                if sign == 1:
                    sign = 'aries'
                elif sign == 2:
                    sign = 'taurus'
                elif sign == 3:
                    sign = 'gemini'
                elif sign == 4:
                    sign = 'cancer'
                elif sign == 5:
                    sign = 'leo'
                elif sign == 6:
                    sign = 'virgo'
                elif sign == 7:
                    sign = 'libra'
                elif sign == 8:
                    sign = 'scorpio'
                elif sign == 9:
                    sign = 'sagittarius'
                elif sign == 10:
                    sign = 'capricorn'
                elif sign == 11:
                    sign = 'aquarius'
                else:
                    sign = 'pisces'
                val = True
            except:
                sign = user_input
                val = True

    url = 'https://astrostyle.com/horoscopes/daily/{}/'.format(sign)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    horoscope_content = soup.find(class_='horoscope-content')

    date = get_date(horoscope_content)
    h_text = horoscope(horoscope_content)

    print("Today is: {}".format(" ".join(date)))
    print("Sign: {}\n".format(sign.capitalize()))
    print("Horoscope for the day\n\n {}".format(h_text))



if __name__ == '__main__':
    main()


