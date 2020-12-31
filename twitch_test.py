import unittest
from twitch import *
from dao import *
from unittest.mock import Mock, patch


class SuperTwitchTestCase(unittest.TestCase):
    """
    unit test for SuperTwitchTestCase
    """

    def setUp(self):
        self.SuperTwitch = SuperTwitch('')

    def testInsufficientArgs(self):
        self.assertIsNotNone(self.SuperTwitch)

    def tearDown(self):
        self.SuperTwitch = None


class TwitchTestCase(unittest.TestCase):
    """
    unit test Case for TwitchTestCase
    """
    def setUp(self):
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

    def test_creatchannel(self):
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')

        # create channel
        parse_createchannel = sub_parsers.add_parser('createchannel')
        parse_createchannel.add_argument('name')
        parse_createchannel.add_argument('id', type=int)
        parse_args = arg_parse.parse_args(['createchannel', 'hhhh', '1000'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.creatchannel()
        self.assertIsNone(tmp)

    @patch("dao.ChannelDao.createtable")
    def test_creatchannel_exception(self, mock_createtable):
        mock_createtable.side_effect = Exception
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')

        # create channel
        parse_createchannel = sub_parsers.add_parser('createchannel')
        parse_createchannel.add_argument('name')
        parse_createchannel.add_argument('id', type=int)
        parse_args = arg_parse.parse_args(['createchannel', 'hhhh', '1000'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.creatchannel()
        self.assertFalse(tmp)

    def test_parsetopspam(self):
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_parsetopspam = sub_parsers.add_parser('parsetopspam')
        parse_parsetopspam.add_argument('file')
        parse_args = arg_parse.parse_args(['parsetopspam', 'league.json'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.parsetopspam()
        self.assertIsNone(tmp)

    @patch("dao.ParseTopSpamDao.createtable")
    def test_parsetopspamexc_exception(self, mock_createtable):
        mock_createtable.side_effect = Exception
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_parsetopspam = sub_parsers.add_parser('parsetopspam')
        parse_parsetopspam.add_argument('file')
        parse_args = arg_parse.parse_args(['parsetopspam', 'league.json'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.parsetopspam()
        self.assertFalse(tmp)

    def test_gettopspam(self):
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_gettopspam = sub_parsers.add_parser('gettopspam')
        parse_gettopspam.add_argument("channel_id")
        parse_gettopspam.add_argument("stream_id")
        parse_args = arg_parse.parse_args(['gettopspam', '137512364', '451603129'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.gettopspam()
        self.assertIsNone(tmp)

    @patch("dao.GetTopSpamDao.selectvalues")
    def test_gettopspam_exception(self, mock_selectvalues):
        mock_selectvalues.side_effect = Exception
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_gettopspam = sub_parsers.add_parser('gettopspam')
        parse_gettopspam.add_argument("channel_id")
        parse_gettopspam.add_argument("stream_id")
        parse_args = arg_parse.parse_args(['gettopspam', '137512364', '451603129'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.gettopspam()
        self.assertFalse(tmp)

    @patch("dao.GetTopSpamDao.selectvalues")
    def test_gettopspam_sqlite_error(self, mock_selectvalues):
        mock_selectvalues.side_effect = sqlite3.Error
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_gettopspam = sub_parsers.add_parser('gettopspam')
        parse_gettopspam.add_argument("channel_id")
        parse_gettopspam.add_argument("stream_id")
        parse_args = arg_parse.parse_args(['gettopspam', '137512364', '451603129'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.gettopspam()
        self.assertFalse(tmp)

    def test_gettopspam2(self):
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_gettopspam2 = sub_parsers.add_parser('gettopspam2')
        parse_gettopspam2.add_argument("channel_id")
        parse_gettopspam2.add_argument("stream_id")
        parse_args = arg_parse.parse_args(['gettopspam2', '137512364', '451603129'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.gettopspam2()
        self.assertIsNone(tmp)

    @patch("dao.GetTopSpamDao2.selectvalues")
    def test_gettopspam2_exception(self, mock_selectvalues):
        mock_selectvalues.side_effect = Exception
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_gettopspam2 = sub_parsers.add_parser('gettopspam2')
        parse_gettopspam2.add_argument("channel_id")
        parse_gettopspam2.add_argument("stream_id")
        parse_args = arg_parse.parse_args(['gettopspam2', '137512364', '451603129'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.gettopspam2()
        self.assertFalse(tmp)

    @patch("dao.GetTopSpamDao2.selectvalues")
    def test_gettopspam2_sqlite_error(self, mock_selectvalues):
        mock_selectvalues.side_effect = sqlite3.Error
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_gettopspam2 = sub_parsers.add_parser('gettopspam2')
        parse_gettopspam2.add_argument("channel_id")
        parse_gettopspam2.add_argument("stream_id")
        parse_args = arg_parse.parse_args(['gettopspam2', '137512364', '451603129'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.gettopspam2()
        self.assertFalse(tmp)

    def test_storechatlog(self):
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_storechatlog = sub_parsers.add_parser("storechatlog")
        parse_storechatlog.add_argument('file')
        parse_args = arg_parse.parse_args(['storechatlog', 'shdvsnyxl.json'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.storechatlog()
        self.assertIsNone(tmp)

    @patch("dao.ChatlogDao.createtable")
    def test_storechatlog_exception(self, mock_createtable):
        mock_createtable.side_effect = Exception
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_storechatlog = sub_parsers.add_parser("storechatlog")
        parse_storechatlog.add_argument('file')
        parse_args = arg_parse.parse_args(['storechatlog', 'shdvsnyxl.json'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.storechatlog()
        self.assertFalse(tmp)

    @patch("dao.ChatlogDao.createtable")
    def test_storechatlog_sqlite_error(self, mock_createtable):
        mock_createtable.side_effect = sqlite3.Error
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_storechatlog = sub_parsers.add_parser("storechatlog")
        parse_storechatlog.add_argument('file')
        parse_args = arg_parse.parse_args(['storechatlog', 'shdvsnyxl.json'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.storechatlog()
        self.assertFalse(tmp)

    def test_viewership(self):
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_gettopspam = sub_parsers.add_parser('viewership')
        parse_gettopspam.add_argument("channel_id")
        parse_gettopspam.add_argument("stream_id")
        parse_args = arg_parse.parse_args(['viewership', '137512364', '451603129'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.viewership()
        self.assertIsNone(tmp)

    @patch("dao.ViewershipDAO.selectvalues")
    def test_viewership_exception(self, mock_selectvalues):
        mock_selectvalues.side_effect = Exception
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_gettopspam = sub_parsers.add_parser('viewership')
        parse_gettopspam.add_argument("channel_id")
        parse_gettopspam.add_argument("stream_id")
        parse_args = arg_parse.parse_args(['viewership', '137512364', '451603129'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.viewership()
        self.assertFalse(tmp)

    @patch("dao.ViewershipDAO.selectvalues")
    def test_viewership_sqlite_error(self, mock_selectvalues):
        mock_selectvalues.side_effect = sqlite3.Error
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_gettopspam = sub_parsers.add_parser('viewership')
        parse_gettopspam.add_argument("channel_id")
        parse_gettopspam.add_argument("stream_id")
        parse_args = arg_parse.parse_args(['viewership', '137512364', '451603129'])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.viewership()
        self.assertFalse(tmp)

    def test_querychatlog(self):
        arg_parse = argparse.ArgumentParser(description='Parse Twitch chatlogs')
        sub_parsers = arg_parse.add_subparsers(dest='sub')
        parse_querychatlog = sub_parsers.add_parser("querychatlog")
        parse_querychatlog.add_argument("filters", nargs="+")
        parse_args = arg_parse.parse_args(['querychatlog', "stream_id eq 451603129", "user eq Moobot"])
        self.twitch = Twitch(parse_args)
        tmp = self.twitch.querychatlog()
        self.assertIsNone(tmp)


class ParseTestCase(unittest.TestCase):
    """
    unit test for ParseTestCase
    """
    def setUp(self):
        self.parse = Parse()

    def test_createparse(self):
        tmp = self.parse.createparse('test')
        self.assertIsNotNone(tmp)

    def tearDown(self):
        self.parse = None


if __name__ =="__main__":
    unittest.main(exit=False)
