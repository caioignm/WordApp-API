from bs4 import BeautifulSoup
from bs4.element import Comment
import re
from urllib.request import urlopen, Request


class WordCount:
    def __init__(self, url, word):
        self.url = url if isinstance(url, list) else [url]
        self.word = word
    
    def _tag_visible(self, element):
        if element.parent.name in [
            'style', 
            'script', 
            'head', 
            'title', 
            'meta', 
            '[document]'
            ]:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def _text_from_html(self, body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self._tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)        
    
    def _list_words(self, url):
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = Request(url, headers=headers)
        html = urlopen(request).read()
        content = self._text_from_html(html)
        word_list = re.split(r'\s+', content)
        return word_list
    
    def count_words(self):
        response = []
        for url in self.url:
            response.append(
                {
                    "word": self.word,
                    "url": url,
                    "value": self._list_words(url).count(self.word)
                
                }
            )
        return response

