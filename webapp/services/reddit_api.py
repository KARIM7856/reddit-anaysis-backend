
import requests

client_id = "r0eMiLhGOJvRGd0K2SzPLQ"
secret = "4FT0u0GzDlWqSLdXD_-xf68nYqFcEA"

HEADERS = {'User-Agent': 'Python3:jupyter-notebook'}




response = requests.post("https://www.reddit.com/api/v1/access_token", auth=(client_id, secret), data={'grant_type': 'client_credentials'},
                         headers=HEADERS)

access_token = response.json()['access_token']

def get_threads(subreddit):

    response = requests.get('https://oauth.reddit.com/r/{}'.format(subreddit),
                            headers={'Authorization': 'Bearer {}'.format(access_token), 'User-Agent': 'Python3:jupyter-notebook'})
    json = response.json()
    n_threads = json['data']['dist']
    threads = []
    for i in range(2):

        threads.append(json['data']['children'][i]['data'])

    return threads


def get_thread_comments(subreddit, thread_id):
    response_thread = requests.get('https://oauth.reddit.com/r/{}/comments/{}'.format(subreddit, thread_id), headers={'Authorization': 'Bearer {}'.format(access_token),
                                                                                                                      'User-Agent': 'Python3:jupyter-notebook'})
    texts = []
    json = response_thread.json()

    print("dflksdjkds -------> ", json)

    return {
        'post': json[0]['data']['children'][0]['data']['selftext'],
        'comments': get_comment_replies(json[1]['data']['children'])
    }


def get_all_threads_comments(subreddit, threads):
    texts = []
    print('threads: ---------> ', threads)
    for thr in threads:
        texts.append(get_thread_comments(subreddit, thr['id']))

    return texts


def get_comment_replies(comment):
    # print(comment_replies)
    texts = []
    for i in comment:
        if i['kind'] == 'more':
            continue
        texts.append(i['data']['body'])
        if i['data']['replies'] != '':
            texts = texts + \
                get_comment_replies(i['data']['replies']['data']['children'])

    return texts
