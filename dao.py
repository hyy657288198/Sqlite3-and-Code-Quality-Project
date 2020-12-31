import json
import argparse
import sqlite3
import logging
class SuperDao:
    """
    Class for the access object super class of twitch.db.
        1. Creates a data base access
        2. Creates commit, close method for database.
    """
    def __init__(self, db):
        """
        Initialization for this data access object.
        Connect to database.
        """
        self.db = db
        self.connection = sqlite3.connect('twitch.db')
        self.cursor = self.connection.cursor()

    def commitconnection(self):
        """
        Commit method for the data base.
        """
        self.connection.commit()

    def closeconnection(self):
        """
        Close connection to the data base.
        """
        self.connection.close()


class ChannelDao(SuperDao):
    """
    Subclass for creating channel method.
    """
    def __init__(self, db):
        """
        Initialization for this data access object.
        Connect to database by calling superclass.
        """
        SuperDao.__init__(self, db)

    def createtable(self):
        """
        Function for creating table.
        """
        self.cursor.execute('''CREATE TABLE if not exists channels
                            (channel_id integer primary key, channel_name text)''')

    def insertvalues(self, parse_args_id, parse_args_name):
        """
        Function for inserting value.
        """
        self.cursor.execute("INSERT INTO CHANNELS VALUES ({},'{}')".format(parse_args_id, parse_args_name))

    def selectvalues(self, parse_args_id):
        """
        Function for selecting value.
        """
        return self.cursor.execute("select * from channels where channel_id = {}".format(parse_args_id))


class ParseTopSpamDao(SuperDao):
    """
    Subclass for parsing top spam method.
    """
    def __init__(self, db):
        """
        Initialization for this data access object.
        Connect to database by calling superclass.
        """
        SuperDao.__init__(self, db)

    def pragma(self):
        """
        Function for pragma.
        """
        self.cursor.execute('PRAGMA foreign_keys = ON;')

    def createtable(self):
        """
        Function for creating table.
        """
        self.cursor.execute('create table if not exists top_spam (channel_id integer NOT NULL, stream_id '
                            'integer NOT NULL, spam_text string, spam_occurrences integer, spam_user_count '
                            'integer, FOREIGN KEY(channel_id) REFERENCES channels(channel_id))')

    def insertvalues(self, channel_id, stream_id, key_var, var, u_count_len):
        """
        Function for inserting value.
        """
        self.cursor.execute('insert into top_spam values(?,?,?,?,?)',
                            (channel_id, stream_id, key_var, var, u_count_len))

    def deletetable(self, channel_id, stream_id):
        """
        Function for deleting table.
        """
        self.cursor.execute('delete from top_spam where channel_id = ? and stream_id = ?', (channel_id, stream_id))


class GetTopSpamDao(SuperDao):
    """
    Subclass for first geting top spam method.
    """
    def __init__(self, db):
        """
        Initialization for this data access object.
        Connect to database by calling superclass.
        """
        SuperDao.__init__(self, db)

    def selectvalues(self, stream_id, channel_id):
        """
        Function for selecting value.
        """
        return self.cursor.execute(("select * from top_spam where channel_id = {} and stream_id = " +
                                    stream_id + " order by spam_occurrences desc, spam_user_count desc"
                                                ", spam_text").format(channel_id))


class GetTopSpamDao2(SuperDao):
    """
    Subclass for second geting top spam method.
    """
    def __init__(self, db):
        """
        Initialization for this data access object.
        Connect to database by calling superclass.
        """
        SuperDao.__init__(self, db)

    def selectvalues(self, stream_id, channel_id):
        """
        Function for selecting value.
        """
        return self.cursor.execute(("select * from (select count(temp1) as ocurance, temp1, "
                                    "count(distinct temp2) as distinct_user from (select text as temp1, user "
                                    "as temp2 from chat_log where channel_id = {} and stream_id = {}) group "
                                    "by temp1) where ocurance > 10 order by ocurance desc, distinct_user desc, temp1").format(channel_id, stream_id))


class ViewershipDAO(SuperDao):
    """
    Subclass for viewership method.
    """
    def __init__(self, db):
        """
        Initialization for this data access object.
        Connect to database by calling superclass.
        """
        SuperDao.__init__(self, db)

    def selectvalues(self, stream_id, channel_id):
        """
        Function for selecting value.
        """
        return self.cursor.execute("select * from chat_log where channel_id = {} "
                                   "and stream_id = {}".format(channel_id, stream_id))


class ChatlogDao(SuperDao):
    """
    Subclass for storing chat log method.
    """
    def __init__(self, db):
        """
        Initialization for this data access object.
        Connect to database by calling superclass.
        """
        SuperDao.__init__(self, db)

    def createtable(self):
        """
        Function for creating table.
        """
        self.cursor.execute('create table if not exists chat_log (channel_id integer NOT NULL, stream_id '
                            'integer NOT NULL, text string, user string, chat_time datetime, offset int, '
                            'FOREIGN KEY(channel_id) REFERENCES channels(channel_id))')

    def insertvalues(self, parse_args_id, parse_args_name):
        """
        Function for inserting value.
        """
        self.cursor.execute("INSERT INTO CHANNELS VALUES ({},'{}')".format(parse_args_id, parse_args_name))

    def updatevalues(self, acc):
        """
        Function for undating value.
        """
        self.cursor.execute("insert into chat_log VALUES (?,?,?,?,?,?)", (acc[0], acc[1], acc[2],
                                                                          acc[3], acc[4], acc[5]))

    def deletvalues(self, channel_id, stream_id):
        """
        Function for deleting value.
        """
        self.cursor.execute('delete from chat_log where channel_id = ? and stream_id = ?', (channel_id, stream_id))
