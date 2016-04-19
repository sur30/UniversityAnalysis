import os
import glob
import time
import re
#import dbHandler
import json
import csv
import sys, string, os, traceback
import urllib
import dbHandler 
import parsing_support

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
    #print "tweet id",tweet['id']
    outFile ="D:/tweet_details_official.csv"
    output = []
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
        # output.append([tweetId,tweetText,tweetTime,tweetGeoType,tweetGeoCoord,tweetLang,tweetSource, tweetRetweetStatus,tweetReplyToName,tweetReplyToId,userId,userName,userHandle,userVerified,userLocation,userDesc,userFollowers,tweetstr_id,tweetCountry,tweetFullname])
        tweetinfolist = [tweetId,tweetText,tweetTime,tweetGeoType,str(tweetGeoCoord),tweetLang,tweetSource, tweetRetweetStatus,tweetReplyToName,tweetReplyToId,userId,userName,userHandle,userVerified,userLocation,userDesc,userFollowers,tweetstr_id,tweetCountry,tweetFullname]
        #return tweetinfolist
        # print userId,userHandle,userVerified,userLocation,userDesc,userUrls
    #     with open(outFile, "ab+") as out:
    #         writer = csv.writer(out)
    #         writer.writerow([tweetId,tweetText,tweetTime,tweetGeoType,tweetGeoCoord,tweetLang,tweetSource, tweetRetweetStatus,tweetReplyToName,tweetReplyToId,userId,userName,userHandle,userVerified,userLocation,userDesc,userFollowers,tweetstr_id,tweetCountry,tweetFullname])
        
    return tweetinfolist
