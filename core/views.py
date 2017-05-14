import tweepy
from tweepy import OAuthHandler
from instaLooter import InstaLooter
from django.shortcuts import render
import pdb
import requests

from .forms import SearchForm


def index(request):
    """
    Main view
    """

    return render(request, 'base.html')


def search(request):
    if request.method == 'POST':
        form = SearchForm()
        if form.is_valid():
            search = form.cleaned_data.get('search')
            try:
                text = twitter(search)
            except:
                text = instagram(search)

    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form, 'text': text})


def twitter(request):
    consumer_key = 'bJbCKR9bnywpupwE20x16glPk'
    consumer_secret = 'bstcGDbEZVAmOdeQGVwo9GQpfR6x7vFIqsV3ggfUA4mKwCweQ1'
    access_token = '1198023481-nm5bdPvTV5j4qY5svmYjgGarPrPNMwEuGRRJCRH'
    access_secret = 'KuaSE62266vSm8EYlyOiOi4iOvaCssv7gclCW12eolglY'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    user = api.get_user(search(search))
    return (api.me().name)
    return (api.me().description)


def instagram(request):
    k = 0
    username = search(search)

    looter = InstaLooter(profile=username)

    for media in looter.medias():
        text = looter.get_post_info(media['code'])['edge_media_to_caption']['edges'][0]['node']['text'].split('#')[0]
        hashtags = looter.get_post_info(media['code'])['edge_media_to_caption']['edges'][0]['node']['text'].split('#')[
                   1:]
        picture = looter.get_post_info(media['code'])['display_src']
        k += 1
        if k > 2:
            break
        return ("{}\n".format(text))
        return ("{}\n".format(hashtags))
        return ("{}\n".format(picture))


def tensor():
    pass
