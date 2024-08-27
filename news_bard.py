class NewsBard:
    def __init__(self, news_data):
        self.data = news_data['results']
        self.lyrics = self.compose()

    def compose(self):
        lyrics = ""
        for item in self.data:
            lyrics += f"{item['title']}\n{item['description']}\n\n"
        return lyrics
