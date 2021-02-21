import httpx, uvicorn
from fastapi import FastAPI
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/word_of_the_day")
async def wotd():
    url = "https://www.dictionary.com/e/word-of-the-day/"
    page = httpx.get(url)
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
    return {"word": wotd,
    "pronunciation" : wotd_p,
    "partOfSpeech": prt_of_speech,
    "definition": definition}


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        # host="127.0.0.1",
        port=80,
        reload=False,
        debug=False,
    )