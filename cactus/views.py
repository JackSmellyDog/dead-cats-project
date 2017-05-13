import tweepy, json
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

    #def process_or_store(tweet):
        #print(json.dumps(tweet))

    #for tweet in tweepy.Cursor(api.user_timeline).items():
        #process_or_store(tweet._json)

    #for status in tweepy.Cursor(api.home_timeline).items(10):
        #print(status.text)

    #for status in tweepy.Cursor(api.home_timeline).items(10):
        # Process a single status
        #process_or_store(status._json)

    #for friend in tweepy.Cursor(api.friends).items():
        #process_or_store(friend._json)

    #if __name__=="__main__":
    user = api.get_user(input("Please enter the twitter username: "))
    return (api.me().name)
    return (api.me().description)


def instagram():
    k = 0

    username = input("Input username: ")

    looter = InstaLooter(profile=username)

    # with open("outimagesfile.txt", "w") as output:
    # pdb.set_trace()
    for media in looter.medias():
        url = looter.get_post_info(media['code']['edge_media_to_caption'])
        k += 1
        if k > 2:
            break
            # else:
            # url = media['display_src']
            # k+=1
        # if k==3:
        # break output.write
        print("{}\n".format(url))
