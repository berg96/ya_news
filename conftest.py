import pytest

from news.models import Comment, News


@pytest.fixture
def news():
    news = News.objects.create(
        title='Title',
        text='Text',
    )
    return news


@pytest.fixture
def id_for_news(news):
    return news.id,


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='IamGroot')


@pytest.fixture
def author_client(author, client):
    client.force_login(author)
    return client


@pytest.fixture
def comment(author, news):
    comment = Comment.objects.create(
        news = news,
        author = author,
        text = 'Text',
    )
    return comment
