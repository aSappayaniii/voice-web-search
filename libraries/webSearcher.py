import webbrowser

def googleSearch(query):
    search_url = f'https://www.google.com/search?q={query}'

    print("Searching...")

    webbrowser.open(search_url) # Opens a new tab
