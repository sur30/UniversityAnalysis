import requests
import datetime
import time
from bs4 import BeautifulSoup as bs
import support as S
#import dbHandler
import csv
import glob

#keywords_list = S.readfile('D:\\twitter\\pilot_keywords.csv')

#keywords_list = [['11','%23Redskins'],['31','%23dallascowboys'],['2','%23Giants'],['2','%23NewyorkGiants'],['2','%23nygiants'],['4','%23PhiladelphiaEagles'],['11','%23Redskins'],['11','%23WashingtonRedskins'],['31','%23dallascowboys'],['31','%23Cowboys']]
#keywords_list = [['4','%23Eagles']]
def payload(sp,ep):
    filepath = "./keyword5.csv"
    keywords_list = S.readfile(filepath)
    #keywords_list = [['0','Representative Steve Kestell']]
    
    
    #dates_list = ['2013-09-04','2013-09-05','2013-09-06','2013-09-07']
    #dates_list = ['2013-09-04','2013-09-05']
    #dates_list = S.date_list()
    filepath1 = "./date_range.csv"
    dates_list = S.readfile(filepath1)
    tweet_info = csv.writer(open("./tweet_ids_terri_remaining"+sp+"_"+ep+".csv",'ab+'))
    spoint  = int(sp)
    epoint  = int(ep)
    for k1 in range(spoint,epoint):
        print keywords_list[k1][1]
        #k2= keywords_list[k1][1].strip("@")
        k2 = keywords_list[k1][1]
        print k2

        for d1 in range(len(dates_list)):
            
            
            k4 = k2+"-"+dates_list[d1][0]
            #k2  = "\""+k2+"\""
            print k4
            start_date  = dates_list[d1][0]
            start_epoch = int((datetime.datetime.strptime(start_date, "%Y-%m-%d") - datetime.datetime(1970,1,1)).total_seconds())
            end_date    = dates_list[d1][1]
            end_epoch   = start_epoch - 5000
            #k2 = "Representative Steve Kestell "
            #q = "Eagles since:" + start_date + " until:" + end_date
            q = k2 +" since:" + start_date + " until:" + end_date

            
            print q
            scroll_cursor = "TWEET-t%s-t%s" % (start_epoch, end_epoch)
            scroll_cursor = ""

            has_more_items = True
            count = 0
            tweetHTML = ""
            totalTweets = 0

            while count < 300:

                falseCounter = 0
                #url = 'https://twitter.com/i/search/timeline?q=%s&src=typd&include_available_features=1&include_entities=1&last_note_ts=35&scroll_cursor=%s' % (q, scroll_cursor)
                url = 'https://twitter.com/i/search/timeline?f=realtime&q=%s&src=typd&include_available_features=1&include_entities=1&last_note_ts=35&scroll_cursor=%s' % (q, scroll_cursor)
                

                headers = {
                    "cookie": '''external_referer="sQr0xRwtlCwrmSiFmo9Ms3PWH0SmSUXaGIME+lo2c9Bx3f5tDT8nfQ==|1"; guest_id=v1%3A139954374768358805; auth_token=22566a46611f84d2d1879036ade92cf1a74524f3; secure_session=true; twll=l%3D1399543820; remember_checked=1; remember_checked_on=1; ad_partner=; lang=en; twid=u%3D2483484974%7C3ZOg8IXYJYQtGds69V4htE8n4hc%3D; ssExp4974=1399543821; pid="v3:1399543833876948256857997"; webn=2483484974; external_referer=sQr0xRwtlCwrmSiFmo9Ms3PWH0SmSUXaGIME%2Blo2c9Bx3f5tDT8nfQ%3D%3D%7C1; __utma=43838368.1948717281.1399543745.1399543745.1399543745.1; __utmb=43838368.15.10.1399543745; __utmc=43838368; __utmz=43838368.1399543745.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _twitter_sess=BAh7DjoMY3NyZl9pZCIlYWNiYWQ0MjY5MzRkN2EzOTgyOTFlNzFhYzE5MmU4%250AM2Y6CXVzZXJsKwcu%252BQaUOhhpbl9lbWFpbF92YWxpZGF0aW9uVDoHaWQiJWFj%250ANDcxOGYzZjYyNzcyZWQxNGViOGEzN2IyZThjYjlkOhFmaXJzdF9pbnZpdGVU%250AOhVpbl9uZXdfdXNlcl9mbG93VCIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxl%250Acjo6Rmxhc2g6OkZsYXNoSGFzaHsABjoKQHVzZWR7ADoQc3RheV9zZWN1cmVU%250AOg9jcmVhdGVkX2F0bCsIZtRO20UB--1f324b7ee6038b2af80f049ecb00c76ca2b61d6b'''
                }
                
                #print response 
                try:
                    r = requests.get(url, headers=headers)
                    response = r.json()
                    
                    has_more_items = response["has_more_items"]
                    scroll_cursor = response["scroll_cursor"]
                    focused_refresh_interval = response["focused_refresh_interval"]
                    
                    # Append New Tweets
                    tweetHTML += response["items_html"]

                    # Count the number of Tweets
                    soup = bs("<ol>" + response["items_html"].encode("utf-8") + "</ol>")
                    newTweets = len(soup.find("ol").find_all("li", recursive=False))
                    totalTweets += newTweets
                    #print l.get("data-item-id")
                    tid = soup.findAll("li")
                    for l in tid:
                        info = []
                        tid= l.get("data-item-id")
                        #print tid
                        if tid is None:
                            pass
                        else:
                            info.append(keywords_list[k1][0])
                            k3 = '@'+keywords_list[k1][1]
                            #print k3
                            info.append(k3)
                            info.append(start_date)
                            info.append(str(tid))
                            tweet_info.writerow(info)
                    #dbHandler.insert_tid(info)
                    
                    # Sleep if false returned for has_more_items
                    if not has_more_items:
                        falseCounter += 1

                        # End loop if count of tweets is 0
                        if newTweets == 0:
                            break

                    #print "%s. %s, %s, %s tweets\t\t%s total" % (count+1, scroll_cursor, has_more_items, newTweets, totalTweets)
                    count += 1

                except Exception, e:
                    pass
                    #raise e
                # break
            #print "<ol>" + tweetHTML.encode('utf-8') + "</ol>"
            print "filename",k4
            html_twitter =(open("./Dump/" +k4+'.html','wb+'))
            html_twitter.write(tweetHTML.encode('utf8','replace'))
            print "[%s requests] [%s tweets]" % (count, totalTweets)
            # break
            
if __name__ == '__main__':
    start_page = raw_input("Enter start index:")
    end_page = raw_input("Enter end index:")
    payload(start_page,end_page)