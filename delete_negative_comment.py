import requests,urllib
from textblob import TextBlob
from constants import APP_ACCESS_TOKEN,BASE_URL
from textblob.sentiments import NaiveBayesAnalyzer
from get_post_id import get_post_id
from get_user_id import get_user_id
from plot import plot_pie_chart
# insta_username = "jyotithakur15111"

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()
    no_neg_comm = 0
    no_pos_comm = 0
    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    no_neg_comm += 1
                else:
                    no_pos_comm += 1
            plot_pie_chart(no_pos_comm,no_neg_comm)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'


