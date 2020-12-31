"""
Python file for SuperTwitch and Twitch class.
"""
from logging.handlers import RotatingFileHandler
from abc import abstractmethod
from dao import *


class SuperTwitch:
    """
    Class for twitch log management.
        1. Creates a channal registration
        2. Parses chat log file.
            - Top spam parser
            - Chat log recorder
        3. Querying stored data.
            - Get top spam.
            - Query chat log.
    """
    def __init__(self, parse_args):
        """
        Initialization for twitch log management.
        """
        self.parse_args = parse_args

    @abstractmethod
    def creatchannel(self):
        """
        Function for creating channel.
        """

    @abstractmethod
    def parsetopspam(self):
        """
        Function for parsing top spam.
        """

    @abstractmethod
    def gettopspam(self):
        """
        Function for geting top spam.
        """

    @abstractmethod
    def storechatlog(self):
        """
        Function for storing chat log.
        """

    @abstractmethod
    def querychatlog(self):
        """
        Function for querying chat log.
        """


class Twitch(SuperTwitch):
    """
    Class for twitch log management.
        1. Creates a channal registration
        2. Parses chat log file.
            - Top spam parser
            - Chat log recorder
        3. Querying stored data.
            - Get top spam.
            - Query chat log.
    """
    def __init__(self, parse_args):
        """
        Initialization for twitch log management.
        """
        SuperTwitch.__init__(self, parse_args)
        self.parse_args = parse_args
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        handler = RotatingFileHandler('test.log', maxBytes=100000, backupCount=100)
        self.log.addHandler(handler)

    def creatchannel(self):
        """
        Function for creating channel.
        """
        # connecting
        channeldao = ChannelDao('twitch.db')
        try:
            channeldao.createtable()
            channeldao.insertvalues(self.parse_args.id, self.parse_args.name)
        except sqlite3.Error as e:
            self.log.error("Database error: %s" % e)
        except Exception as e:
            self.log.error("Exception in _query: %s" % e)
            return False
        finally:
            # print channel id and channel name
            channeldao.commitconnection()
            for result in channeldao.selectvalues(self.parse_args.id):
                self.log.info(result)
                print(result)
            channeldao.closeconnection()

    def parsetopspam(self):
        """
        Function for parsing top spam.
        """
        counts = {}
        u_counts = {}

        # open file
        with open(self.parse_args.file) as file:

            # load json style
            json_style = json.load(file)
            comments = json_style['comments']

            file_comments = comments[0]
            channel_id = file_comments["channel_id"]
            stream_id = file_comments["content_id"]

            # loop
            for comment in comments:
                user = comment["commenter"]["display_name"]
                body = comment["message"]["body"]
                count = counts.get(body, 0)
                counts[body] = count + 1
                ucount = u_counts.get(body, set())
                ucount.add(user)
                u_counts[body] = ucount

        # connecting
        parsetopspam_dao = ParseTopSpamDao('twitch.db')
        count = 0
        try:
            parsetopspam_dao.pragma()
            parsetopspam_dao.createtable()
            parsetopspam_dao.deletetable(channel_id, stream_id)
            parsetopspam_dao.commitconnection()

            # sort
            s_counts = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)

            for i, (key_var, var) in enumerate(s_counts):
                u_count_len = len(u_counts[key_var])

                # should probably parameterize "10"
                if var > 10:
                    count += 1
                    parsetopspam_dao.insertvalues(channel_id, stream_id, key_var, var, u_count_len)
        except sqlite3.Error as e:
            self.log.error("Database error: %s" % e)
        except Exception as e:
            self.log.error("Exception in _query: %s" % e)
            return False
        finally:
            parsetopspam_dao.commitconnection()
            parsetopspam_dao.closeconnection()

            # log result
            self.log.info("inserted {} top spam records for stream {} on channel {}".format(count,
                                                                                            stream_id, channel_id))
            print("inserted {} top spam records for stream {} on channel {}".format(count, stream_id, channel_id))

    def gettopspam(self):
        """
        Function for geting top spam.
        """
        # connecting
        gettopspam_dao = GetTopSpamDao('twitch.db')
        out = []
        try:
            # find corresponding spam text, occurrences and user count for the channel asked
            for result in gettopspam_dao.selectvalues(self.parse_args.stream_id, self.parse_args.channel_id):
                out.append({"spam_text": result[2], "occurrences": result[3], "user_count": result[4]})
        except sqlite3.Error as e:
            self.log.error("Database error: %s" % e)
            return False
        except Exception as e:
            self.log.error("Exception in _query: %s" % e)
            return False
        finally:
            gettopspam_dao.closeconnection()

            # log the result
            self.log.info(json.dumps(out, sort_keys=True))
            print(json.dumps(out, sort_keys=True))

    def gettopspam2(self):
        """
        Function for geting top spam.
        """
        # connecting
        gettopspam_dao2 = GetTopSpamDao2('twitch.db')
        out = []
        try:
            # find corresponding spam text, occurrences and user count for the channel asked
            for result in gettopspam_dao2.selectvalues(self.parse_args.stream_id, self.parse_args.channel_id):
                out.append({"spam_text": result[1], "occurrences": result[0], "user_count": result[2]})
        except sqlite3.Error as e:
            self.log.error("Database error: %s" % e)
            return False
        except Exception as e:
            self.log.error("Exception in _query: %s" % e)
            return False
        finally:
            gettopspam_dao2.closeconnection()

            # log the result
            self.log.info(json.dumps(out, sort_keys=True))
            print(json.dumps(out, sort_keys=True))

    def storechatlog(self):
        """
        Function for storing chat log.
        """
        # open the file
        with open(self.parse_args.file) as file:

            # load json style
            json_style = json.load(file)
            comments = json_style['comments']

            file_comments = comments[0]
            channel_id = file_comments["channel_id"]
            stream_id = file_comments["content_id"]

            # connecting
            chatlogdao = ChatlogDao('twitch.db')
            try:
                chatlogdao.createtable()
                chatlogdao.deletvalues(channel_id, stream_id)
            except sqlite3.Error as e:
                self.log.error("Database error: %s" % e)
                return False
            except Exception as e:
                self.log.error("Exception in _query: %s" % e)
                return False
            finally:
                # loop and insert values to chat_log
                for comment in comments:
                    acc = [channel_id, stream_id, comment["message"]["body"], comment["commenter"]["display_name"],
                           comment["created_at"], comment["content_offset_seconds"]]
                    chatlogdao.updatevalues(acc)
                chatlogdao.commitconnection()
                chatlogdao.closeconnection()

                # log the result
                self.log.info("inserted {} records to chat log for stream {} "
                              "on channel {}".format(len(comments), stream_id, channel_id))
                print("inserted {} records to chat log for stream {} "
                      "on channel {}".format(len(comments), stream_id, channel_id))

    def viewership(self):
        """
        Function for viewership.
        """
        channel_id = self.parse_args.channel_id
        stream_id = self.parse_args.stream_id

        # connecting
        viewership_dao = ViewershipDAO('twitch.db')
        texts = []
        users = []
        offsets = []
        chat_times = []
        try:
            # get the value from chat_log
            for result in viewership_dao.selectvalues(stream_id, channel_id):
                texts.extend([result[2]])
                users.extend([result[3]])
                offsets.extend([result[5]])
                chat_times.extend([result[4]])
        except sqlite3.Error as e:
            self.log.error("Database error: %s" % e)
            return False
        except Exception as e:
            self.log.error("Exception in _query: %s" % e)
            return False
        finally:
            viewership_dao.closeconnection()

        # find starttime, max offset
        starttime = 0
        max_offset = 0
        if len(chat_times) > 0:
            starttime = min(chat_times)
        if len(offsets) > 0:
            max_offset = max(offsets) / 60

        # wrap data that get from cgat_log to a list for helper function
        lists = [texts, offsets, users]
        per_minute = self.viewershiphelper(max_offset, lists)

        # log the result
        count = 0
        per_minute_str = '['
        while count < len(per_minute)-1:
            per_minute_str += per_minute[count]
            per_minute_str += ", "
            count += 1
        if len(per_minute) > 0:
            per_minute_str += per_minute[len(per_minute)-1]
        per_minute_str += "]"
        self.log.info("[{{\"channel_id\": {}, \"stream_id\": {}, \"starttime\": {}, "
                      "\"per_minute\": {}}}] ".format(channel_id, stream_id, starttime, per_minute_str))
        print("[{{\"channel_id\": {}, \"stream_id\": {}, \"starttime\": {}, "
              "\"per_minute\": {}}}] ".format(channel_id, stream_id, starttime, per_minute_str))

    def viewershiphelper(self, max_offset, lists):
        """
        helper function for viewership.
        :param max_offset: the maximum offset in the channel.
        :type max_offset: int
        :param lists: include all the texts, offsets and users in the channel.
        :type lists: list of list
        :return: return the per_minute object.
        :rtype: list
        """
        # get data from parameter
        texts = lists[0]
        offsets = lists[1]
        users = lists[2]
        per_minute = []
        offset = 0

        # loop to find information needed for every minute
        while offset < max_offset:
            viewers = 0
            viewerlist = []
            messages = 0
            acc = 0
            while acc < len(texts):
                if offset*60 <= offsets[acc] <= (offset+1)*60:
                    name = users[acc]
                    messages += 1
                    if name not in viewerlist:
                        viewerlist.extend([name])
                        viewers += 1
                acc += 1

            per_minute += ["{\"offset\": " + str(offset+1) + ", \"viewers\": " + str(viewers)
                           + ", \"messages\": " + str(messages) + "}"]
            offset += 1
        return per_minute

    def querychatlog(self):
        """
        Function for querying chat log.
        """
        # find data needed
        query = "select * from chat_log "
        if len(self.parse_args.filters) > 0:
            query += "where "
        for file in self.parse_args.filters:
            pos = file.index(' ')
            pos_from_tail = file.rindex(' ')
            column = file[0:pos]
            value = file[pos_from_tail + 1:]
            operation = file[pos + 1:pos_from_tail]

            # use helper function to determine operations
            query += self.queryupdatefragment(operation, value, column)

        if len(self.parse_args.filters) > 0:
            query = query[:-4]

        query += " order by chat_time"

        # use helper function to log result
        self.descriptionhelper(query)

    def queryupdatefragment(self, operation, value, column):
        """
        helper function for querying chat log. Easy to add or delete operations.
        """
        fragment = column
        str_cols = ['text', 'user']
        helper_map = {"eq": " = ", "gt": " > ", "lt": " < ", "gteq": " >= ", "lteq": " <= ", "like": " like "}
        if operation in helper_map:
            fragment += helper_map[operation]
        if column in str_cols:
            fragment += "'" + value + "' AND "
        else:
            fragment += value + ' AND '

        return fragment

    def descriptionhelper(self, query):
        """
        helper function for querying chat log.
        """
        connection = sqlite3.connect('twitch.db')
        cursor = connection.cursor()
        out = []
        rows = cursor.execute(query)
        names = []
        for description in cursor.description:
            names.append(description[0])
        for result in rows:
            json_style = {}
            for i, name in enumerate(names):
                json_style[name] = result[i]
            out.append(json_style)
        connection.close()
        self.log.info(json.dumps(out, sort_keys=True))
        print(json.dumps(out, sort_keys=True))


class Parse:
    """
    Class for creating parse.
    """
    def __init__(self):
        self.parse = 0

    def createparse(self, str):
        """
        Helper function for creating parse.
        """
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')

        # create channel
        parse_createchannel = sub_parsers.add_parser('createchannel')
        parse_createchannel.add_argument('name')
        parse_createchannel.add_argument('id', type=int)

        # parse top spam
        parse_parsetopspam = sub_parsers.add_parser('parsetopspam')
        parse_parsetopspam.add_argument('file')

        # get top spam
        parse_gettopspam = sub_parsers.add_parser('gettopspam')
        parse_gettopspam.add_argument("channel_id")
        parse_gettopspam.add_argument("stream_id")

        # get top spam2
        parse_gettopspam = sub_parsers.add_parser('gettopspam2')
        parse_gettopspam.add_argument("channel_id")
        parse_gettopspam.add_argument("stream_id")

        # viewership
        parse_gettopspam = sub_parsers.add_parser('viewership')
        parse_gettopspam.add_argument("channel_id")
        parse_gettopspam.add_argument("stream_id")

        # store chat log
        parse_storechatlog = sub_parsers.add_parser("storechatlog")
        parse_storechatlog.add_argument('file')

        # query chat log
        parse_querychatlog = sub_parsers.add_parser("querychatlog")
        parse_querychatlog.add_argument("filters", nargs="+")

        if str == 'test':
            parseargs = arg_parse.parse_args(['createchannel', 'hhhh', '1000'])
        else:
            parseargs = arg_parse.parse_args()
        return parseargs


if __name__ == "__main__":
    parse = Parse()
    parseargs = parse.createparse('')
    twitch = Twitch(parseargs)

    acc = {"createchannel": twitch.creatchannel, "parsetopspam": twitch.parsetopspam, "gettopspam": twitch.gettopspam,
           "storechatlog": twitch.storechatlog, 'querychatlog': twitch.querychatlog, "gettopspam2": twitch.gettopspam2,
           "viewership": twitch.viewership}
    if parseargs.sub in acc:
        acc[parseargs.sub]()
