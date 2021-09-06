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


## Example deployment using Linux Alpine (3.13 at the time of writing) LXC container from recent installed to deployed python service

These commands are all written assuming root permission. Make sure you already have the latest updates before starting with `apk update && apk upgrade`

### Instal Python and pip

```
apk add --no-cache python3 py3-pip
```

### Instal git

```
apk add --no-cache git
```

### Clone this repository

```
git clone https://github.com/KenanHArik/word_of_the_day_endpoint.git
```

### Update and upgrade all packages

```
apk update && apk upgrade
```

### Install necessary Python packages using pip

```
pip3 install -r ./word_of_the_day_endpoint/requirements.txt
```

### Copy the wotd service file over to /etc/init.d, and update permissions

```
cp /root/word_of_the_day_endpoint/wotd /etc/init.d
chmod +x /etc/init.d/wotd
```

### Start the service, and allow it to start at boot time

```
/etc/init.d/wotd start
rc-update add wotd boot
```

If all went well, you should be able to reach the endpoint at the machine's IP address, at address xxx.xxx.xxx.xxx/word_of_the_day

similarly, with FastAPI - you should also see docs present at xxx.xxx.xxx.xxx/docs.

### If you ever need to check to make sure the service is running, you can do so with

```
rc-status -a
```
