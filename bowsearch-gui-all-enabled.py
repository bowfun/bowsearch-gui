from guizero import App, Text, TextBox, PushButton
import webbrowser
import time

def search_typed():
    #Google function
    googleurl = "https://www.google.com/search?q=" + str(search.value)
    print("Opening Google")
    webbrowser.open(googleurl)

    #DuckDuckGo function
    ddgurl = "https://duckduckgo.com/?q=" + str(search.value)
    print("Opening DuckDuckGo")
    webbrowser.open(ddgurl)

    #Bing function
    bingurl = "https://www.bing.com/search?q=" + str(search.value)
    print("Opening Bing")
    webbrowser.open(bingurl)

    #Disabled Search Engines
    #If you want to enable one, uncomment it.
    #If there are two hashtags (##), only remove one.

    #Whoogle
    #A privacy-respecting alternative to Google.
    whoogleurl = "https://whoogle.privacydev.net/search?q=" +str(search.value)
    print("Opening Whoogle (Manually Enabled)")
    webbrowser.open(whoogleurl)

    #Brave Search
    #Also a privacy-respecting search engine.
    braveurl = "https://search.brave.com/search?q=" + str(search.value)
    print("Opening Brave Search (Manually Enabled)")
    webbrowser.open(braveurl)

    #Search Encrypt
    #Encrypts your searches locally.
    seurl = "https://www.searchencrypt.com/search?q=" + str(search.value)
    print("Opening Search Encrypt (Manually Enabled)")
    webbrowser.open(seurl)
    
app = App(title="BowSearch v1 - Made by BowFun")
message = Text(app, text="BowSearch v1 - Made by BowFun")
message2 = Text(app, text="Welcome! This tool will search across multiple search engines.")
message3 = Text(app, text="This version has all search engines enabled.")
search = TextBox(app, text="", width=20, height=1)
button = PushButton(app, text="Search", command=search_typed)

app.display()