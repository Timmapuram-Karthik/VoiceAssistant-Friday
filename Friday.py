import datetime
import os
import webbrowser
import openai
import pyttsx3
import requests
import speech_recognition as sr
import wikipediaapi

import key

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for a female voice and 0 for a male voice

# Initialize the Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

# Initialize a chat history string for the AI chatbot
chatStr = ''


# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to recognize audio input
def audio_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 4000
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"user said {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand the query.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        return 'None'


# Function to open websites
def open_website(site_name):
    sites = {
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.org",
        "google": "https://www.google.com",
        "stackoverflow": "https://stackoverflow.com",
        "github": "https://www.github.com"
    }

    if site_name in sites:
        speak(f"Opening {site_name}")
        webbrowser.open(sites[site_name])
    else:
        speak(f"Sorry, I don't know how to open {site_name}")


# Function to open applications
def open_application(app_name):
    app_dict = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint"
    }

    if app_name in app_dict:
        try:
            os.system(app_dict[app_name])
            speak(f"Opening {app_name}")
        except Exception as e:
            print(f"Error opening {app_name}: {e}")
    else:
        try:
            os.system(f'start {app_name}')  # Add 'start' before the app_name
            speak(f"Opening {app_name}")
        except Exception as e:
            print(f"Error opening {app_name}: {e}")


# Function to get the current time
def get_current_time():
    strfTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"The Time is {strfTime}")
    speak(f"The Time is {strfTime}")


# Function to get weather information
def get_weather_info(area='chandragiri'):
    BaseURL = "http://api.weatherapi.com/v1"
    URL = f'{BaseURL}/current.json?key={key.weatherapi}&q={area}'
    response = requests.get(URL).json()
    weather_info = f'The weather of {area} is {response["current"]["temp_c"]} degree Celsius and {response["current"]["condition"]["text"]}'
    print(weather_info)
    speak(weather_info)


# Function to get news headlines
def get_news_headlines():
    URL = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={key.newsapi}"
    response = requests.get(URL).json()
    articles = response.get("articles", [])
    if articles:
        for i, article in enumerate(articles[:5]):  # Display the top 5 news articles
            title = article.get("title", "No Title")
            description = article.get("description", "No Description")
            print(f"News {i + 1}: {title}")
            print(f"Description: {description}\n")
            speak(f"News {i + 1}: {title}. {description}")
    else:
        print("No news articles found for the given query.")
        speak("No news articles found for the given query.")


# Function to get news information based on a query
def get_news_info(news_query):
    BaseURL = "https://newsapi.org/v2/everything?q="
    URL = f'{BaseURL}{news_query}&sortBy=popularity&apiKey{key.newsapi}'
    response = requests.get(URL).json()
    articles = response.get("articles", [])
    if articles:
        for i, article in enumerate(articles[:5]):  # Display the top 5 news articles
            title = article.get("title", "No Title")
            description = article.get("description", "No Description")
            print(f"News {i + 1}: {title}")
            print(f"Description: {description}\n")
            speak(f"News {i + 1}: {title}. {description}")
    else:
        print("No news articles found for the given query.")
        speak("No news articles found for the given query.")


# Function to get Wikipedia information
def get_wikipedia_info(query):
    page = wiki_wiki.page(query)
    if page.exists():
        summary = page.summary[:500]  # Limit summary to 500 characters
        print(summary)
        speak(summary)
    else:
        print("No Wikipedia information found for the given query.")
        speak("No Wikipedia information found for the given query.")


# Function to search the web
def search_on_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    speak(f"Searching the web for {query}")


# Function to handle date-related queries
def handle_date_query(query):
    if "tomorrow's date" in query:
        tomorrow_date = datetime.datetime.now() + datetime.timedelta(days=1)
        formatted_date = tomorrow_date.strftime("%A, %B %d, %Y")
        print(f"Tomorrow's date is {formatted_date}")
        speak(f"Tomorrow's date is {formatted_date}")
    elif "date for" in query or "day for" in query:
        parts = query.split("for")
        if len(parts) > 1:
            query_date = parts[1].strip()
            try:
                parsed_date = datetime.datetime.strptime(query_date, "%Y-%m-%d")
                formatted_date = parsed_date.strftime("%A, %B %d, %Y")
                print(f"The date for {query_date} is {formatted_date}")
                speak(f"The date for {query_date} is {formatted_date}")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                speak("Invalid date format. Please use YYYY-MM-DD.")
        else:
            print("Please specify a date in the query.")
            speak("Please specify a date in the query.")


# Function to fetch jokes
def jokes():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': key.jokesapi})
    if response.status_code == requests.codes.ok:
        import json
        jokes_data = json.loads(response.text)
        joke = jokes_data[0]["joke"]
        print(joke)
        speak(joke)
    else:
        print("Error:", response.status_code, response.text)


# Function to generate text using OpenAI's GPT-3
def write(query):
    openai.api_key = key.openaikey
    text = f"OpenAI response for Prompt: {query} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(query.split('write')[1:]).strip()}.txt", "w") as f:
        f.write(text)


# Function to perform a general chat or Wolfram Alpha query
def chat(query):
    try:
        global chatStr
        print(chatStr)
        openai.api_key = key.openaikey
        chatStr += f"User: {query}\n Friday: "
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        speak(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        speak("Sorry, I couldn't understand your query.")


# Function to exit the program
def exit_program():
    speak("Goodbye!")
    exit()


# Your code for the voice assistant starts here
if __name__ == '__main__':
    speak("Hello, I am Friday")

    while True:
        print("Listening...")
        text = audio_input().lower()
        if 'none' not in text:
            if "who created you" in text:
                answer = "I was created by Karthik."
                speak(answer)
            elif "what is your name" in text:
                answer = "My name is Friday."
                speak(answer)
            elif "how are you" in text:
                answer = "I'm just a computer program, so I don't have feelings, but thanks for asking!"
                speak(answer)
            elif "what is the meaning of life" in text:
                answer = "The meaning of life is a philosophical question that has been debated for centuries."
                speak(answer)
            elif 'joke' in text:
                jokes()
            elif "open" in text:
                site_name = text.split("open", 1)[1].strip()
                open_website(site_name)
            elif "open" in text:
                app_name = text.split("open", 1)[1].strip()
                open_application(app_name)
            elif "the time" in text:
                get_current_time()
            elif "weather" in text:
                if 'of' in text:
                    area = text.split("of", 1)[1].strip()
                    get_weather_info(area)
                else:
                    get_weather_info()
            elif "news about" in text or "news of" in text:
                if 'about' in text:
                    news_query = text.split("about", 1)[1].strip()
                elif 'of' in text:
                    news_query = text.split("of", 1)[1].strip()
                get_news_info(news_query)
            elif "headlines" in text or 'news' in text:
                news_headlines = text.split("headlines", 1)[1].strip()
                get_news_headlines()
            elif "wikipedia" in text:
                query = text.split("wikipedia", 1)[1].strip()
                get_wikipedia_info(query)
            elif "search" in text or 'search for' in text:
                if 'for' in text:
                    query = text.split("for", 1)[1].strip()
                else:
                    query = text.split("search", 1)[1].strip()
                search_on_web(query)
            elif "date" in text or "day" in text:
                handle_date_query(text)
            elif "goodbye" in text or "exit" in text:
                exit_program()
            elif "write" in text:
                write(text)
            else:
                chat(text)
