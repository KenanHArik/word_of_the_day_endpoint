import requests
from bs4 import BeautifulSoup

url = "https://www.dictionary.com/e/word-of-the-day/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# at the time of writing this code....
# the word of the day is the first h1 tag without a class name
h1 = soup.find_all('h1', class_='')
wotd = h1[0].text

# the word of the day pronunciation is the second div tag without a class name
div = soup.find_all('div', class_='')
div_text = div[1].text
after_bracket = div_text.split('[')[-1]
pron = after_bracket.split(']')[0]
wotd_p = f"[{pron}]"

# the part of speech is second p tag, and the definition is the third p tag
p = soup.find_all('p', class_='')
prt_of_speech = p[1].text.strip('\n').strip(' ')
definition = p[2].text.strip('\n').strip(' ')

print(f"Today's word of the day is: {wotd}, pronounced {wotd_p}, part of speech: {prt_of_speech}, defined as: {definition}")

