
import os
import glob
import time
import re
#import dbHandler
import json
import csv
import sys, string, os, traceback
import urllib
#to compose json 

def date_list():
    
    lidList = []
    lidList = ['2013-09-01','2013-09-02','2013-09-03','2013-09-04','2013-09-05','2013-09-06','2013-09-07','2013-09-08','2013-09-09','2013-09-10','2013-09-11','2013-09-12','2013-09-13','2013-09-14','2013-09-15','2013-09-16','2013-09-17','2013-09-18','2013-09-19','2013-09-20','2013-09-21','2013-09-22','2013-09-23','2013-09-24','2013-09-25','2013-09-26','2013-09-27','2013-09-28','2013-09-29','2013-09-30','2013-10-01','2013-10-02','2013-10-03','2013-10-04','2013-10-05','2013-10-06','2013-10-07','2013-10-08','2013-10-09','2013-10-10','2013-10-11','2013-10-12','2013-10-13','2013-10-14','2013-10-15','2013-10-16','2013-10-17','2013-10-18','2013-10-19','2013-10-20','2013-10-21','2013-10-22','2013-10-23','2013-10-24','2013-10-25','2013-10-26','2013-10-27','2013-10-28','2013-10-29','2013-10-30','2013-10-31','2013-11-01','2013-11-02','2013-11-03','2013-11-04','2013-11-05','2013-11-06','2013-11-07','2013-11-08','2013-11-09','2013-11-10','2013-11-11','2013-11-12','2013-11-13','2013-11-14','2013-11-15','2013-11-16','2013-11-17','2013-11-18','2013-11-19','2013-11-20','2013-11-21','2013-11-22','2013-11-23','2013-11-24','2013-11-25','2013-11-26','2013-11-27','2013-11-28','2013-11-29','2013-11-30','2013-12-01','2013-12-02','2013-12-03','2013-12-04','2013-12-05','2013-12-06','2013-12-07','2013-12-08','2013-12-09','2013-12-10','2013-12-11','2013-12-12','2013-12-13','2013-12-14','2013-12-15','2013-12-16','2013-12-17','2013-12-18','2013-12-19','2013-12-20','2013-12-21','2013-12-22','2013-12-23','2013-12-24','2013-12-25','2013-12-26','2013-12-27','2013-12-28','2013-12-29','2013-12-30','2013-12-31','2014-01-01','2014-01-02','2014-01-03','2014-01-04','2014-01-05','2014-01-06','2014-01-07','2014-01-08','2014-01-09','2014-01-10','2014-01-11','2014-01-12','2014-01-13','2014-01-14','2014-01-15','2014-01-16','2014-01-17','2014-01-18','2014-01-19','2014-01-20','2014-01-21','2014-01-22','2014-01-23','2014-01-24','2014-01-25','2014-01-26','2014-01-27','2014-01-28','2014-01-29','2014-01-30','2014-01-31','2014-02-01','2014-02-02','2014-02-03','2014-02-04','2014-02-05','2014-02-06','2014-02-07','2014-02-08','2014-02-09','2014-02-10','2014-02-11']
    return lidList
def keyword_list():
    
    lidList = []
    lidList = ['2013-09-01','2013-09-02','2013-09-03','2013-09-04','2013-09-05','2013-09-06','2013-09-07','2013-09-08','2013-09-09','2013-09-10','2013-09-11','2013-09-12','2013-09-13','2013-09-14','2013-09-15','2013-09-16','2013-09-17','2013-09-18','2013-09-19','2013-09-20','2013-09-21','2013-09-22','2013-09-23','2013-09-24','2013-09-25','2013-09-26','2013-09-27','2013-09-28','2013-09-29','2013-09-30','2013-10-01','2013-10-02','2013-10-03','2013-10-04','2013-10-05','2013-10-06','2013-10-07','2013-10-08','2013-10-09','2013-10-10','2013-10-11','2013-10-12','2013-10-13','2013-10-14','2013-10-15','2013-10-16','2013-10-17','2013-10-18','2013-10-19','2013-10-20','2013-10-21','2013-10-22','2013-10-23','2013-10-24','2013-10-25','2013-10-26','2013-10-27','2013-10-28','2013-10-29','2013-10-30','2013-10-31','2013-11-01','2013-11-02','2013-11-03','2013-11-04','2013-11-05','2013-11-06','2013-11-07','2013-11-08','2013-11-09','2013-11-10','2013-11-11','2013-11-12','2013-11-13','2013-11-14','2013-11-15','2013-11-16','2013-11-17','2013-11-18','2013-11-19','2013-11-20','2013-11-21','2013-11-22','2013-11-23','2013-11-24','2013-11-25','2013-11-26','2013-11-27','2013-11-28','2013-11-29','2013-11-30','2013-12-01','2013-12-02','2013-12-03','2013-12-04','2013-12-05','2013-12-06','2013-12-07','2013-12-08','2013-12-09','2013-12-10','2013-12-11','2013-12-12','2013-12-13','2013-12-14','2013-12-15','2013-12-16','2013-12-17','2013-12-18','2013-12-19','2013-12-20','2013-12-21','2013-12-22','2013-12-23','2013-12-24','2013-12-25','2013-12-26','2013-12-27','2013-12-28','2013-12-29','2013-12-30','2013-12-31','2014-01-01','2014-01-02','2014-01-03','2014-01-04','2014-01-05','2014-01-06','2014-01-07','2014-01-08','2014-01-09','2014-01-10','2014-01-11','2014-01-12','2014-01-13','2014-01-14','2014-01-15','2014-01-16','2014-01-17','2014-01-18','2014-01-19','2014-01-20','2014-01-21','2014-01-22','2014-01-23','2014-01-24','2014-01-25','2014-01-26','2014-01-27','2014-01-28','2014-01-29','2014-01-30','2014-01-31','2014-02-01','2014-02-02','2014-02-03','2014-02-04','2014-02-05','2014-02-06','2014-02-07','2014-02-08','2014-02-09','2014-02-10',]
    return lidList
def check_file():
    filename=glob.glob("D:/tyler/code/json_dumps/lname_not_found/*.txt")
    #print filename
    lidList = []
    for f in filename:
        #print f[f.find('\\')+1:]
        lid = f[f.find('\\')+1:f.find('.txt')]
        #print lid   
        lidList.append(lid.strip())
    return lidList
def readfile(file_name_path):
    wk_book1 = file_name_path
    #wk_book1 = 'D:\\tyler\\code\\output\\output_result_new_2.csv'
    with open(wk_book1, 'rb') as f1:
        spamreader = csv.reader(f1.read().splitlines())
        data =[]
        for row1 in spamreader:
            data.append(row1)
    return data
def readfile1(tweet_id_list,s,e):
    
    
    print s,e 
    #print tweet_id_list[0]
    data = []
    for i1 in range(s,e):
        if len(tweet_id_list[i1]) > 3:
            data.append(tweet_id_list[i1][3])
        #break
    return data

def parser(tweet_json):
    #tweet = eval(tweet_json)
    
    tweet= tweet_json
    #print tweet
      #tweet = ast.literal_eval(tweetText)
    # print json.dumps(tweet)
    tweetList = []
    tweetText = 'None'
    tweetTime = 'None'
    tweetGeoType = 'None'
    tweetGeoCoord = 'None'
    tweetId = 'None'
    tweetLang = 'None'
    tweetUrls = 'None'
    tweetSource = 'None'
    tweetReplyToName = 'None'
    tweetReplyToId = 'None'
    tweetPlace = 'None'
    tweetstr_id = 'None'
    tweetCountry = 'None'
    tweetFullname = 'None'
    userId = 'None'
    userHandle = 'None'
    userVerified = 'None'
    userLocation = 'None'
    userDesc = 'None'
    userUrls = 'None'
    userName = 'None'
    # print tweet['text'].encode('utf-8')
    print "tweet id",tweet['id']
    outFile ="D:/tweet_details_official.csv"
    tweetText = tweet['text'].encode('utf-8')
    
    # if (tweetText in tweetList) or ('namo ' in tweetText.lower()):
    if (tweetText.lower() in tweetList):
        pass
    else:
        
        tweetList.append(tweetText.lower())
        tweetTime = tweet['created_at']
        if tweet['geo'] != None:
            tweetGeoType = tweet['geo']['type'].encode('utf-8')
            tweetGeoCoord = tweet['geo']['coordinates']
        tweetId = tweet['id']
        
        if tweet['lang'] != None:
            tweetLang = tweet['lang']
        # if tweet['entities']['urls'] != None:
        #     tweetUrls = tweet['entities']['urls']
        if tweet['source'] != None:
            tweetSource = tweet['source'].encode('utf-8')
        if tweet['retweeted'] != None:
            tweetRetweetStatus = tweet['retweeted']
        if tweet['in_reply_to_screen_name'] != None:
            tweetReplyToName = tweet['in_reply_to_screen_name'].encode('utf-8')
        if tweet['in_reply_to_user_id'] != None:
            tweetReplyToId = tweet['in_reply_to_user_id']
        if tweet['id_str'] != None:
            tweetstr_id = tweet['id_str']
        if tweet['place'] != None:
            if tweet['place']['country'] != None:
                tweetCountry = tweet['place']['country'].encode('utf-8')
            if tweet['place']['full_name'] != None:
                tweetFullname = tweet['place']['full_name'].encode('utf-8')

        # print tweetText,tweetTime,tweetGeoType,tweetGeoCoord,tweetId,tweetLang,tweetUrls,tweetSource,tweetReplyToName,tweetReplyToId

        #User Details
        userDet = tweet['user']
        userId = userDet['id']
        userHandle = userDet['screen_name'].encode('utf-8')
        if userDet['verified'] != None:
            userVerified = userDet['verified']
        if userDet['location'] != None:
            userLocation = userDet['location'].encode('utf-8')
        if userDet['description'] != None:
            userDesc = userDet['description'].encode('utf-8')
        if userDet['followers_count'] != None:
            userFollowers = userDet['followers_count']
        if userDet['name'] != None:
            userName = userDet['name'].encode('utf-8')
        # if userDet['entities']['description']['urls'] != None:
        #     userUrls = userDet['entities']['description']['urls']

        # print userId,userHandle,userVerified,userLocation,userDesc,userUrls
        with open(outFile, "ab+") as out:
            writer = csv.writer(out)
            writer.writerow([tweetId,tweetText,tweetTime,tweetGeoType,tweetGeoCoord,tweetLang,tweetSource, tweetRetweetStatus,tweetReplyToName,tweetReplyToId,userId,userName,userHandle,userVerified,userLocation,userDesc,userFollowers,tweetstr_id,tweetCountry,tweetFullname])
        
    return tweetId


'''
if __name__ == '__main__':
    print "in main"
    # tweet_json = '{"contributors": null, "truncated": false, "text": "Congratulations to the 7th Grade Eagles football team on their 48-22 victory over Corning.", "in_reply_to_status_id": null, "id": 375757388344594432, "favorite_count": 1, "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>", "retweeted": false, "coordinates": {"type": "Point", "coordinates": [-90.57921974, 36.41839403]}, "entities": {"symbols": [], "user_mentions": [], "hashtags": [], "urls": []}, "in_reply_to_screen_name": null, "id_str": "375757388344594432", "retweet_count": 2, "in_reply_to_user_id": null, "favorited": false, "user": {"follow_request_sent": false, "profile_use_background_image": true, "profile_text_color": "0F37FF", "default_profile_image": false, "id": 66168457, "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/518788673026801665/W2eDynO0.png", "verified": false, "profile_location": null, "profile_image_url_https": "https://pbs.twimg.com/profile_images/494109766256324608/svMhrVsb_normal.jpeg", "profile_sidebar_fill_color": "FF0F2F", "entities": {"description": {"urls": []}}, "followers_count": 302, "profile_sidebar_border_color": "000000", "id_str": "66168457", "profile_background_color": "000000", "listed_count": 1, "is_translation_enabled": false, "utc_offset": -21600, "statuses_count": 7482, "description": "Douglas MacArthur Jr. High School Keystone Coordinator, Football & Basketball Coach. #OTR #CycloneFB #CycloneBB #CycloneVB", "friends_count": 96, "location": "Jonesboro, AR", "profile_link_color": "000000", "profile_image_url": "http://pbs.twimg.com/profile_images/494109766256324608/svMhrVsb_normal.jpeg", "following": false, "geo_enabled": true, "profile_banner_url": "https://pbs.twimg.com/profile_banners/66168457/1412375810", "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/518788673026801665/W2eDynO0.png", "name": "Mack Skelton", "lang": "en", "profile_background_tile": true, "favourites_count": 69, "screen_name": "mackskelton", "notifications": false, "url": null, "created_at": "Sun Aug 16 18:52:37 +0000 2009", "contributors_enabled": false, "time_zone": "Central Time (US & Canada)", "protected": false, "default_profile": false, "is_translator": false}, "geo": {"type": "Point", "coordinates": [36.41839403, -90.57921974]}, "in_reply_to_user_id_str": null, "lang": "en", "created_at": "Thu Sep 05 23:08:37 +0000 2013", "in_reply_to_status_id_str": null, "place": {"country_code": "US", "url": "https://api.twitter.com/1.1/geo/id/ace366d376504c37.json", "country": "United States", "place_type": "city", "bounding_box": {"type": "Polygon", "coordinates": [[[-90.632958, 36.397983], [-90.568331, 36.397983], [-90.568331, 36.424749], [-90.632958, 36.424749]]]}, "contained_within": [], "full_name": "Corning, AR", "attributes": {}, "id": "ace366d376504c37", "name": "Corning"}}'
    #tweet_json = '{"contributors": null}'
    #tweet_json = '[{"source": "<a href=\'http://twitter.com/download/iphone\' rel=\'nofollow\'>Twitter for iPhone</a>"}]'
    tweet_json = """[{"source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>"}]"""
    # print tweet_json.find('{')
    #t = tweet_json
    t = tweet_json.replace('\\',"\\\\")
    print t
    t1 = json.loads(t)
    print t1

    #import ast 
    #dic = ast.literal_eval(t1)
    #print dic
    # print t,t1
    
    if (tweet_json["text"].find("null")):
        pass
    else:
        print "hi"
    #t ={}
    #t = dict(tweet_json)
    #print t
    #parser(t)
'''
    
