from twython import Twython
import urllib2
import traceback
import csv
import urllib
import time
# import facebook
import sys
import urlparse
import datetime
from datetime import datetime
import multiprocessing
# import excelHelper
from multiprocessing import Pool
import subprocess
# import warnings
import requests
import dbHandler
# import threading
import json
import support as s
import datetime as dt
import parsing_support as ps
# from bs4 import BeautifulSoup as Soup
from time import gmtime, strftime
def getRateLimit(twitter,res):
    try:
        rateLimit = twitter.get_application_rate_limit_status(resources=res)
        print json.dumps(rateLimit)
    except Exception,e:
        print traceback.format_exc()

def getTweetData(twitter,tid_list1):
    try:
        #'376132654238019584, 376132654238019584'
        tweet_status = twitter.lookup_status(id = tid_list1)
        #print type(tweet_status)
        outputList = []
        for t1 in tweet_status:
            
            tinfoList =ps.parser(t1)
            tid = str(tinfoList[0])
            outputList.append(tinfoList)
            #print tid
            #userHandle = t['user']['screen_name'].encode('utf-8')
            #print userHandle
            #s.parser(t)
            #print t["source"]
            json_tid=  json.dumps(t1)
            
            f = open('D:/twitter/final_official_dumps/'+str(tid)+'.txt', 'w')
            f.write(str(json_tid))  
        return outputList
    except Exception,e:
        print traceback.format_exc()

def getUserTimeline(twitter, handle):
    user_timeline = twitter.get_user_timeline(screen_name = handle,count = 100)
    print json.dumps(user_timeline)



def getweets(twitter,keyword, count):
    # Issues - 1) Need to add a check to avoid duplicates when consecutive calls happen.
    print 'Getting tweets'
    maxid = None
    prevId = 0
    outFile = './dumps/tweetData' + keyword + '.csv'

    for i in range(count,600):
        try:
            if maxid:
                search_results = twitter.search(q = keyword,count = 100,max_id = str(int(maxid)-1), lang = 'en', include_rts = False) #include_rts not set to false so as to get all the tweets
            else:
                search_results = twitter.search(q = keyword,count = 100,max_id = maxid, lang = 'en', include_rts = False)
        
            # time.sleep(10)
     
            jsonSearch = json.dumps(search_results)        
            fileDump = './dumps/' + keyword + str(i) + '.txt'
            f = open(fileDump,'wb')
            f.write(jsonSearch) # python will convert \n to os.linesep
            f.close()
            # print search_results
            lenTweetData = len(search_results['statuses'])
            print lenTweetData
            
            # print search_results['statuses'][1]['text'].encode('utf8')
            # break
            if maxid == search_results['statuses'][-1]["id"]:
                break
            else:
                #parse JSON
                prevId = 0
                for tweet in search_results['statuses']:
                    if prevId != tweet['id']:
                        with open(outFile, "ab+") as out:
                            writer = csv.writer(out)
                            writer.writerow([keyword,tweet['text'].encode('utf8'),tweet['id']])
                        prevId = tweet['id']
            
            maxid = search_results['statuses'][-1]["id"]
            # print jsonSearch,'a'
            print 'Maxid - ',maxid
            if (i+1)%174 == 0:
                print 'sleeping'
                time.sleep(905)
                print 'And we are up again!!'
        except Exception,e:
            print traceback.format_exc(),'a'
            break
    return i

def getFollowers(twitter,screenName):
    print 'Getting Followers'
    followersData = csv.writer(open("followersData.csv", "ab+"))
    try:
        cursorVal = -1
        for i in range (600):
            followers = twitter.get_followers_ids(screen_name = screenName,count = 5000,cursor = cursorVal)
            time.sleep(10)
            # followers = twitter.get_followers_list(screen_name = screenName)  # Return a collection object(tweets and all) for the user following.
            jsonFollowers = json.dumps(followers)
            print jsonFollowers
            cursorVal = followers['next_cursor']
            followersList = followers['ids']
            print followersList
            for follow in followersList:
                followersData.writerow([screenName,str(follow)])
            print cursorVal,len(followers["ids"])
            if cursorVal == 0:
                break
            else:
                # parse JSON
                pass

    except Exception,e:
        print traceback.print_exc()
    return 1

def getFollowing(twitter,screenName):
    print 'Getting followings'
    followingData = csv.writer(open("followingData.csv", "ab+"))
    try:
        cursorVal = -1
        for i in range (600):
            following = twitter.get_friends_ids(screen_name = screenName,count = 5000,cursor = cursorVal)
            time.sleep(10)
            # followers = twitter.get_followers_list(screen_name = screenName)  # Return a collection object(tweets and all) for the user following.
            jsonFollowing = json.dumps(following)
            print jsonFollowing
            cursorVal = following['next_cursor']
            print cursorVal,len(following["ids"])
            followingList = following["ids"]
            print followingList
            for follow in followingList:
                followingData.writerow([screenName,str(follow)])
            if cursorVal == 0:
                break
            else:
                # parse json
                pass

    except Exception,e:
        print traceback.format_exc()
    return 1
    # following = twitter.get_friends_ids(screen_name = screenName,count = 5000)
    # jsonFollowing = json.dumps(following)
    # print jsonFollowing
    # return 1
# 
if __name__ == '__main__':
    try:
        #file_path = "D:\'twitter'\'twitter_tokens.csv"
        file_path = 'D:/twitter/_tokens.csv'
        #print file_path
        file_path1  = 'D:/twitter/official_handles/_ids_official_handles_final_0_32.csv'
        twee_id_list = s.readfile(file_path1)
        end = 14600
        start = 0
        t_token=s.readfile(file_path)
        dbList = []
        while(True):
            i =1
            s1 = strftime("%H:%M:%S",gmtime())
            for i in range(1,len(t_token)):
                tid_list =[]
            #print time.time()
            #for i in range(1,2):
                CONSUMER_TOKEN = t_token[i][2]
                CONSUMER_SECRET = t_token[i][3]
                Access_token = t_token[i][4]
                Access_token_secret = t_token[i][5]
                #print "ID"+t_token[i][1]
           
                twitter = Twython(CONSUMER_TOKEN, CONSUMER_SECRET, Access_token, Access_token_secret)
                count = 0
                #start = 1+end 
                for j in range(1,170):
                    start = end
                    end = start+ 100
                    #print start , end

                    tid_list = s.readfile1(twee_id_list,start,end)
                    
                    #print len(tid_list)
                    #print tid_list
                    #tid_list=[]
                    #break
                    outputList = getTweetData(twitter,tid_list)
                    if outputList:
                        dbList.extend(outputList)
                    if len(dbList) > 10000:
                        #Call db function
                        dbHandler.entertweetDetails(dbList)
                        dbList = []
                    #break
                #break
                #print 'finally'

            s2 = strftime("%H:%M:%S",gmtime())
            diff = dt.datetime.strptime(s2, '%H:%M:%S')-dt.datetime.strptime(s1, '%H:%M:%S')
            left = 900- diff.seconds
            if (left>0):
                time.sleep(left)
        if len(dbList) > 0:
            #Call db function
            dbHandler.entertweetDetails(dbList)
            dbList = []

    except Exception,e:
        print traceback.format_exc()
