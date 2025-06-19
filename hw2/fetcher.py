from newspaper import Article

def fetch_article(url: str, language: str = 'ru') -> tuple[str, str]:
    """
    Скачивает и парсит статью.
    Возвращает (title, text).
    """
    article = Article(url, language=language)
    article.download()
    article.parse()
    return article.title, article.text

if __name__ == "__main__":
    t, txt = fetch_article("https://пример.сайт/новость")
    print(t)
    print(txt[:200])
