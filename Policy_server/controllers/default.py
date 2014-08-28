# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

import os
import subprocess
import MySQLdb


machine = "localhost";
db_username="root";
db_password="hadoop";
def page():
    connection = MySQLdb.connect(host=machine,user=db_username,passwd=db_password)
    cur = connection.cursor()
    query = "show databases"
    cur.execute(query)
    databases = cur.fetchall()
    print databases
    dir1 = {}
    dat = []
    print dir1
    for (d,) in databases:
                dir1[d] = {}
                dat.append(d)
  #              cur = connection.cursor()
  #              query1 = "use "+d
  #              cur.execute(query1)

                connection1 = MySQLdb.connect(host=machine,user=db_username,passwd=db_password,db=d)
                cur = connection1.cursor()
                query2 = "show tables"
                cur.execute(query2)
                tables = cur.fetchall()
                for (t,) in tables:
                        dir1[d][t] = []
                        cur = connection1.cursor()
                        query = "desc `"+t +"`;";
                        print d
                        print query
                        cur.execute(query);
                        columns = cur.fetchall()
                        print dir1
                        for i in columns:
                                dir1[d][t].append(i[0])
    return dict(dir1=dir1,dat=dat)

import os.path
import json
from pprint import pprint
from os import listdir
from os.path import isfile, join

def nextpage():
        postvars = request.post_vars
        dir2 = {}
        database = postvars['dropbox']
        dir2[database] = {}
        temp = {}
        filename = postvars['Policy_name']
        print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        print filename
        postkeys = postvars.keys()
        L = []
        for i in postkeys:
                if i == "save" or i == "dropbox" or i == "policy_name":
                        continue;
                else:
                        p = i.split('$')
                        if (p[0] != database):
                                continue;
                        else:
                                temp[i] = postvars[i]
                                if (len(p) == 2):
                                      if (postvars[i] != ''):
                                              dir2[database][p[1]] = {}
                                              L.append(p[1])
                                """
                                l = len(p)
                                if (l == 2):
                                        if (postvars[i] == ''):
                                                continue;
                                        if p[1] in dir1[database].keys():
                                                 print "yeah"
                                        else:
                                                 dir1[database][p[1]] = {}
                                else if (l == 3):
                                        if p[1] in d
                                """
        connection = MySQLdb.connect(host=machine,user=db_username,passwd=db_password,db=database)
        for i in L:
                cur = connection.cursor()
                query = "desc "+ i+";"
                cur.execute(query);
                columns = cur.fetchall()
                for j in columns:
                        if (database+"$"+i+"$"+j[0] in temp.keys()):
                                if (postvars[database+"$"+i+"$"+j[0]+"$method"] == "mask" ):
                                        dir2[database][i][j[0]] = {"mask" : postvars[database+"$"+i+"$"+j[0]+"$info"]}
                                else:
                                        dir2[database][i][j[0]] = postvars[database+"$"+i+"$"+j[0]+"$method"]





        """
        for i in L:
                for k in dir1[database][i]:
                        if postvars[database+"$"+i+"$"+k] =

        """
        print dir2
        for i in dir2[database].keys():
                if dir2[database][i] == {}:

                         del dir2[database][i]
        print dir2
        fname = './applications/Policy_server/json_files/'+filename+'.json'
        if os.path.isfile(fname) == True:
                print "file exist"
        else:
                print "file does not exist"
                with open(fname,'w') as f:
                     json.dump(dir2, f,ensure_ascii=False)
                     f.write('\n')
        print "SAR IIIIII  RAN"
        mypath = './applications/Policy_server/json_files/'
        Afiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
        print Afiles
        Ffiles = []
        for i in Afiles:
                k = []
                k = i.split('.')
                Ffiles.append(k[0])
        return dict(Ffiles=Ffiles)




def json_html():
        postvars = request.get_vars;
        print postvars
        filename1 = postvars['fname']
        filename= ""
        filename=filename+"./applications/Policy_server/json_files/"
        filename=filename+filename1+".json"
        f = open(filename,'r')
        L = []
        L = f.readlines()
        print L
        f.close()
        return dict(L=L)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())
