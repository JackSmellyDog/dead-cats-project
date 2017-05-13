import tweepy
from tweepy import OAuthHandler
from instaLooter import InstaLooter
import pdb


def twitter():
    consumer_key = 'bJbCKR9bnywpupwE20x16glPk'
    consumer_secret = 'bstcGDbEZVAmOdeQGVwo9GQpfR6x7vFIqsV3ggfUA4mKwCweQ1'
    access_token = '1198023481-nm5bdPvTV5j4qY5svmYjgGarPrPNMwEuGRRJCRH'
    access_secret = 'KuaSE62266vSm8EYlyOiOi4iOvaCssv7gclCW12eolglY'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    user = api.get_user(input("Please enter the twitter username: "))
    return (api.me().name)
    return (api.me().description)


def instagram():
    k = 0

    username = input("Input username: ")

    looter = InstaLooter(profile=username)

    for media in looter.medias():
        text = looter.get_post_info(media['code'])['edge_media_to_caption']['edges'][0]['node']['text'].split('#')[0]
        hashtags = looter.get_post_info(media['code'])['edge_media_to_caption']['edges'][0]['node']['text'].split('#')[
                   1:]
        k += 1
        if k > 2:
            break
        return ("{}\n".format(text))
        return ("{}\n".format(hashtags))


def tensor():
