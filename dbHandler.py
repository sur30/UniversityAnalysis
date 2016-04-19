import MySQLdb
import os
import MySQLdb
import os
import datetime
import dbHandler

def entertweetDetails(rows):
    con = MySQLdb.connect(host='173.194.240.156', user='root', passwd='root', db='nfl') 
    cur = con.cursor() 
    #print rows
    que='INSERT INTO  final_tweet_details1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    #print que
    
    cur.executemany(que,rows)
    #res =cur.executemany("INSERT INTO  subject_detail_filter values(%s,%s,%s,%s)",rows)
    call_id = cur.lastrowid
    con.commit()
    con.close()
def addssubject_details(sub):
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='fir')
    cur = con.cursor()
    cur.execute("INSERT INTO  subject_detail_filter values(%s,%s,%s,%s)")
    con.commit()
    con.close()

def getsubject():
    con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='fir')
    cur = con.cursor()
    #print ('INSERT INTO ucla_student_details_2012_linkedin(CCID,First name,Last name,Location,profil count,positions count,profile links) values ("%s","%s","%s","%s","%s","%s","%s")'%tuple(profile))
    #INSERT INTO ucla_student_details_2012_linkedin(CCID,FirstName,LastName,Location,ProfileCount,positionscount,links) values ("12","ac","cd","12","ac","cd","gdfg")
    cur.execute('SELECT * from subject_detail')
    c = [] 
    for row in cur.fetchall():
        c.append(row)
    return c

    con.commit()
    con.close()
def getsubject1(uid1):
    
    try:
        con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='fir')
        cur = con.cursor()
        que='SELECT * from subject_detail_filter where uid in %s'
        
        #print "uid = ",uid1
        #print ('INSERT INTO ucla_student_details_2012_linkedin(CCID,First name,Last name,Location,profil count,positions count,profile links) values ("%s","%s","%s","%s","%s","%s","%s")'%tuple(profile))
        #INSERT INTO ucla_student_details_2012_linkedin(CCID,FirstName,LastName,Location,ProfileCount,positionscount,links) values ("12","ac","cd","12","ac","cd","gdfg")
        if len(uid1) ==1:
            cur.execute('select uid,GROUP_CONCAT(subject_term SEPARATOR "|") from subject_detail_filter where uid = %s group by uid',(uid1,))
        else:
            cur.execute('select uid,GROUP_CONCAT(subject_term SEPARATOR "|") from subject_detail_filter where uid in '+str(tuple(uid1))+' group by uid')
        #cur.execute(que,(uid1,))
        c = [] 
        for row in cur.fetchall():
            c.append(row)
        #if len(c) == 0:
            #c= ["no data"]
        print "subject_detail_filter",c,"for uid",uid1
        con.commit()
        con.close()
        return c
    except Exception, e:
        raise e
        
   

def getsubject2(uid1):
    try:
        
        #print uid1
        con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir')
        cur = con.cursor()
        que='SELECT * from subject_detail where uid in '+str(tuple(uid1))
        #print que
        #print uid1[0]
        #print ('INSERT INTO ucla_student_details_2012_linkedin(CCID,First name,Last name,Location,profil count,positions count,profile links) values ("%s","%s","%s","%s","%s","%s","%s")'%tuple(profile))
        #INSERT INTO ucla_student_details_2012_linkedin(CCID,FirstName,LastName,Location,ProfileCount,positionscount,links) values ("12","ac","cd","12","ac","cd","gdfg")
        
        cur.execute(que)
        c = [] 
        for row in cur.fetchall():
            c.append(row)
        con.commit()
        con.close()
        #print c
        return c



        
    except Exception, e:
        raise e
def getInputdata(si,rows):
    con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir') 
    cur = con.cursor() 
    #print rows
    #que='SELECT * from input_data limit %d',(ei)
    #que='SELECT * from input_data limit %d offset %d',(si,rows)
    #print que
    
    cur.execute('SELECT * from input_data limit %s offset %s',(rows,si))
    #res =cur.executemany("INSERT INTO  subject_detail_filter values(%s,%s,%s,%s)",rows)
    #cur.execute(que)
    c = [] 
    for row in cur.fetchall():
        c.append(row)
    con.commit()
    con.close()
    #print c
    return c

def getuid(lname):
    con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir')
    cur = con.cursor()
    #print ('INSERT INTO ucla_student_details_2012_linkedin(CCID,First name,Last name,Location,profil count,positions count,profile links) values ("%s","%s","%s","%s","%s","%s","%s")'%tuple(profile))
    #INSERT INTO ucla_student_details_2012_linkedin(CCID,FirstName,LastName,Location,ProfileCount,positionscount,links) values ("12","ac","cd","12","ac","cd","gdfg")
    cur.execute('select uid,lname,fname from general_detail_filter where lname=%s ',(lname,))
    c = [] 
    for row in cur.fetchall():
        c.append(row)
    
    return c
    con.commit()
    con.close()

def enterMasterDetails(rows):
    con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir') 
    cur = con.cursor() 
    #print rows
    que='INSERT INTO  subject_detail_filter values(%s,%s,%s,%s)'
    #print que
    
    cur.executemany(que,rows)
    #res =cur.executemany("INSERT INTO  subject_detail_filter values(%s,%s,%s,%s)",rows)
    call_id = cur.lastrowid
    con.commit()
    con.close()
def enterSubjectDetails(rows):
    con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir') 
    cur = con.cursor() 
    #print rows
    que='INSERT INTO  subject_detail_filter values(%s,%s,%s,%s)'
    #print que
    
    cur.executemany(que,rows)
    #res =cur.executemany("INSERT INTO  subject_detail_filter values(%s,%s,%s,%s)",rows)
    call_id = cur.lastrowid
    con.commit()
    con.close()
def insert_output(rows):
    con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir') 
    cur = con.cursor() 
    #print rows
    que='INSERT INTO  output_result_new_lnf (input_id,Proquest_id,lname_match,fname_match,Match_on_code,Match_on_keyword)values(%s,%s,%s,%s,%s,%s)'
    #print que
    
    cur.execute(que,rows)
    #res =cur.executemany("INSERT INTO  subject_detail_filter values(%s,%s,%s,%s)",rows)
    call_id = cur.lastrowid
    con.commit()
    con.close()
def insert_tid(rows):
    con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='nfl') 
    cur = con.cursor() 
    #print rows
    que='INSERT INTO  tweet_ids (kid,keyword,tid) values (%s,%s,%s)'
    #print que
    
    cur.execute(que,rows)
    #res =cur.executemany("INSERT INTO  subject_detail_filter values(%s,%s,%s,%s)",rows)
    call_id = cur.lastrowid
    con.commit()
    con.close()
def get_output(input_id):
    try:
        
        #print uid1
        i_id =[input_id]
        con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir')
        cur = con.cursor()
        #que='SELECT * from output_result_new where input_id = '+input_id[0]
        que='SELECT * from output_result_new_lnf_3 where input_id = %s order by year,level'
        
        cur.execute(que,i_id)
        c = [] 
        for row in cur.fetchall():
            c.append(row)
            #print row
        con.commit()
        con.close()
        #print c
        return c
    except Exception, e:
        raise e
def update_output(status,rid):
    try:
        
        #print uid1
        con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir')
        cur = con.cursor()
        que='update output_result_new_lnf_3 set status= %s where id =%s '
        #cur.execute('update output_result_new set status= %s where id =%s',(status,rid))
    
        
        cur.execute(que,(status,rid))
        #print que
        
        con.commit()
        con.close()
        
    except Exception, e:
        raise e

def get_level(input_id):
    try:
        
        #print uid1
        i_id =[input_id]
        con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir')
        cur = con.cursor()
        #que='SELECT * from output_result_new where input_id = '+input_id[0]
        que='SELECT distinct(level) from output_result_new_lnf_3 where input_id = %s order by level '
        
        cur.execute(que,(i_id[0],))
        c = [] 
        for row in cur.fetchall():
            c.append(row[0])
            #print row
        con.commit()
        con.close()
        #print "level",c
        return c
    except Exception, e:
        raise e
def count_level(input_id):
    try:
        
        i_id =[input_id]
        con = MySQLdb.connect(host='localhost', user='root', passwd='root', db='fir')
        cur = con.cursor()
        #que='SELECT * from output_result_new where input_id = '+input_id[0]
        que='SELECT count(distinct(level)) from output_result_new_lnf_3 where input_id = %s'
        
        cur.execute(que,(input_id,))
        call_id = cur.fetchone()
        c = call_id[0]
        #for row in cur.fetchall():
         #   c.append(row)
          #  print row
        con.commit()
        con.close()
        #print "count of ",c
        return c
    except Exception, e:
        raise e
  
#if __name__ == "__main__":
    #insert_tid(["1","1","1"])
    #print "main"
    #get_level(['10009'])
    #count_level('10009')
    #update_output("1","1")
    #output = get_output('10009')
    #print output
#     insert_output(['1000','AAI7425088','lname','fname','1','0'])
#     enterMasterDetails(['16','AAI7425088','AAI7424816','AAI7425088'])
     #getsubject1(['AAI3449611','AAI3452334'])
     #getsubject1(['AAI1308229','AAI1311031'])
