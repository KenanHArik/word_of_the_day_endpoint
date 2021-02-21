# Word of the Day Endpoint

Thank you for visiting!

It is surprising that after searching for a bit through the webs, I could not find a good "Word of the Day" endpoint to tie into a display we are making to hang in our house..... so I made one. Perhaps the code can be useful so long as you want have the ability to host it.

All of the code is contained in app.py. If you run

```
python app.py
```

You will launch a FastAPI endpoint on your local machine, which can be accessed. When accessed with a get request, it will grab the latest word of the day from dictionary.com, and provide it back to you as a JSON object.

The day of writing this, the example response was:


```
{"word":"pharaonic","pronunciation":"[ fair-ey-on-ik, far-  ]","partOfSpeech":"adjective","definition":"impressively or overwhelmingly large, luxurious, etc."}
```

Hopefully this is useful to some 👍

