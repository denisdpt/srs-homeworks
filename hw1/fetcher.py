from newspaper import Article

def fetch_article_text(url: str, language: str = 'ru') -> str:
    # Скачиваем и парсит текст статьи по URL, а возвращаем чистый текст.
    article = Article(url, language=language)
    article.download()
    article.parse()
    return article.text

if __name__ == "__main__":
    test_url = "https://пример.сайт/новость"
    print(fetch_article_text(test_url)[:500])
