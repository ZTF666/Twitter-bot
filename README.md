# TweetBot

A small python bot that automates the process of login in twitter .
Send follow requests from the suggestions tab .
Follow people based on a given #Hashtag .
Likes tweets based on a given #Hashtag .


## THIS IS A WiP !!!!!!!!

```
Since this is still experimental , things my change or be a bit buggy .
Once fully finished , this section will be deleted.
```

## How to use

- **Install**

```python
pip install selenium
```

- **Download**


 💿 [ChromeDriver](http://chromedriver.chromium.org/) 💿 
```
👇👆
```
🦊🦎 [GeckoDriver](https://github.com/mozilla/geckodriver/releases) 🦎🦊

``` 
If you're using windows , you may want to put the .exe in the same folder as the script.
At least that's how i do it.
```

## Functionalities

```
Functionalities implemented so far :

LOGIN ✔️
FOllOW ✔️
LIKE TWEETS ✔️
SEARCH BY HASHTAG ✔️
UNFOLLOW ❌
RETWEET ❌


```

**Likes**
Tweaks & optimisation :

>  <p>You can optimise the scrolls to get more tweets this by changing the number . </p>
> <p>Line 50</p>

```python
 for i in range(1,3):
```
>  <p>You can optimise the number of likes by changing the number . </p>
>  <p>For testing purposes this only likes 4 posts </p>
> <p>Line 56</p>

```python
        for X in range(1,5):
```


**Follow**
Tweaks & optimisation :

>  <p>You can optimise the scrolls to get more profiles this by changing the number . </p>
> <p>Line 68</p>

```python
for i in range(1,5):
```

>  <p>You can optimise the number of follow requets by changing the number . </p>
>  <p>For testing purposes this only follows 8 people and stops </p>
> <p>Line 73</p>

```python
 for X in range(1,9):
```

>  <p> This link should be altered , put your own id instead of mine in the creds.py </p>
```python
        self.driver.get('https://twitter.com/i/connect_people?user_id=YOUR_PROFILE_ID_GOES_HERE')
```

**Credentials**

```
As any other file containing sensitive data, creds.py contains :
```

```python
login = 'PHONE_EMAIL_OR_USERNAME'
pwd = 'PASSWORD'
hashtag='YOUR HASHTAG HERE'
id='YOUR_TWITTER_ID
```

```
Make sure to change those before launching .
```

## LIMITATIONS :

```
The script bugs out from time to time depending on your internet speed .
This is not a perfect script , this have been made with basic knowledge .
The function SLEEP() , has high intervals because of my 3rd world internet , 💛 4mbps 💛 .
You should adapt it to your needs .
```

## Support

```
Any help improving this and adding more stuff is welcome ! .
```

## Contact me

```
you can contact me at ZTF666@protonmail.ch or via my portfolio
```

[Portfolio](https://ztfportfolio.web.app/)

## License

**🐤TweetBot** released under the [MIT](LICENSE) License.

```
Made with 💘 by a 👨‍💻 on a 💻 | 2020 | ZTF666

``` 