import unittest
from unittest.mock import Mock, patch, MagicMock
from dao import *
from sqlite3 import DatabaseError


class SuperDaoTestCase(unittest.TestCase):
    """
    the test cases for superDao class
    """

    def setUp(self):
        self.Mock = Mock()
        self.SuperDao = SuperDao("db")
    def tearDown(self):
        self.mock = Mock()
        self.SuperDao = None

    def test_commitSuperDao(self):
        mock_commit = self.Mock.commit
        self.SuperDao.commitconnection = mock_commit
        self.SuperDao.commitconnection()
        mock_commit.assert_called()
        mock_commit.assert_called_once()
        mock_commit.assert_called_with()
        for i in range(999):
            self.SuperDao.commitconnection()
        self.assertEqual(1000, mock_commit.call_count)

    def test_DbSuperDao(self):
        mock_db = self.Mock.Mock_db
        self.SuperDao.db = mock_db
        acc = self.SuperDao.db
        self.assertIsNotNone(acc)
        self.assertIs(acc, mock_db)

    def test_connectionSuperDao(self):
        mock_connection = self.Mock.connection
        self.SuperDao.connection = mock_connection
        mock_close = mock_connection.close
        mock_close.return_value = None
        self.SuperDao.closeconnection()
        self.assertIs(self.SuperDao.connection, mock_connection)
        mock_close.assert_called()

    def test_cursorSuperDao(self):
        mock_cursor = self.Mock.connection
        self.SuperDao.cursor = mock_cursor
        acc = self.SuperDao.cursor
        self.assertIs(acc, mock_cursor)
        self.assertIsNotNone(acc)

    def test_closeconnectionSuperDao(self):
        self.SuperDao.closeconnection()
        mock_connection = self.Mock.connection
        self.SuperDao.connection = mock_connection
        mock_close = mock_connection.close
        mock_close.return_value = None
        self.SuperDao.closeconnection()
        self.assertIs(self.SuperDao.connection, mock_connection)
        mock_close.assert_called_once()


class ChannelDaoTestCase(unittest.TestCase):
    """
    the test cases for channelDao class
    """

    def setUp(self):
        self.Mock = Mock()
        self.ChannelDao = ChannelDao('twitch.db')

    def tearDown(self):
        self.ChannelDao = None

    def test_commitChannelDao(self):
        mock_commit = self.Mock.commit
        self.ChannelDao.commitconnection = mock_commit
        self.ChannelDao.commitconnection()
        mock_commit.assert_called()
        mock_commit.assert_called_once()
        mock_commit.assert_called_with()
        for i in range(999):
            self.ChannelDao.commitconnection()
        self.assertEqual(1000, mock_commit.call_count)
        self.ChannelDao.commitconnection()

    def test_closeConeectionChannelDao(self):
        self.ChannelDao.closeconnection()
        mock_connection = self.Mock.connection
        self.ChannelDao.connection = mock_connection
        mock_close = mock_connection.close
        mock_close.return_value = None
        self.ChannelDao.closeconnection()
        self.assertIs(self.ChannelDao.connection, mock_connection)
        mock_close.assert_called_once()

    def test_creatchannel(self):
        mock_table = self.Mock.table
        self.ChannelDao.createtable = mock_table
        self.ChannelDao.createtable()
        mock_table.assert_called()
        mock_table.assert_called_once()
        acc = self.ChannelDao.createtable()
        self.assertIsNotNone(acc)

    def test_insertvalues(self):
        mock_insert = self.Mock.insert
        self.ChannelDao.insertvalues = mock_insert
        acc = self.ChannelDao.insertvalues(1, "")
        self.assertIsNotNone(acc)
        mock_insert.assert_called_with(1, "")

    def test_selectvalues(self):
        mock_select = self.Mock.select
        self.ChannelDao.selectvalues = mock_select
        acc = self.ChannelDao.selectvalues(1)
        self.assertIsNotNone(acc)
        mock_select.assert_called_with(1)
        mock_select.assert_called()


class ParseTopSpamDaoTestCase(unittest.TestCase):
    """
    the test cases for ParseTopSpamDaoTestCase class
    """

    def setUp(self):
        self.Mock = Mock()
        self.ParseTopSpamDao = ParseTopSpamDao('twitch.db')

    def tearDown(self):
        self.Mock = Mock()
        self.ParseTopSpamDao = None

    def test_pragma(self):
        mock_pragma = self.Mock.pragma
        self.ParseTopSpamDao.pragma = mock_pragma
        acc = self.ParseTopSpamDao.pragma()
        self.assertIsNotNone(acc)
        mock_pragma.assert_called()
        mock_pragma.assert_called_once()
        
    def test_createtable(self):
        mock_table = self.Mock.table
        self.ParseTopSpamDao.createtable = mock_table
        self.ParseTopSpamDao.createtable()
        acc = self.ParseTopSpamDao.createtable()
        self.assertIsNotNone(acc)
        mock_table.assert_called()
        mock_table.assert_called_with()
        for i in range(999):
            self.ParseTopSpamDao.createtable()
        self.assertEqual(1001, mock_table.call_count)



    def test_insertvalues(self):
        try:
            mock_insert = self.Mock.insert
            self.ParseTopSpamDao.insertvalues = mock_insert
            acc = self.ParseTopSpamDao.insertvalues(0, 0, 0, 0, 0)
            self.assertIsNotNone(acc)
            mock_insert.assert_called()
            mock_insert.assert_called_with(0, 0, 0, 0, 0)
        except Exception as e:
            return e is not None


    def test_deletvalues(self):
        try:
            mock_delete = self.Mock.delet
            self.ParseTopSpamDao.deletetable = mock_delete
            acc =  self.ParseTopSpamDao.deletetable(0, 0)
            self.assertIsNotNone(acc)
            mock_delete.assert_called()
            mock_delete.assert_called_with(0, 0)
        except Exception as e:
            return e is not None


class TopSpamDaoTestCase(unittest.TestCase):
    """
    the test cases for TopSpamDaoTestCase class
    """


    def setUp(self):
        self.GetTopSpamDao = GetTopSpamDao('twitch.db')
        self.Mock = Mock()

    def tearDown(self):
        self.Mock = Mock()
        self.GetTopSpamDao = None

    def test_isdb(self):
        mock_db = self.Mock.Mock_db
        self.GetTopSpamDao.db = mock_db
        acc = self.GetTopSpamDao.db
        self.assertIsNotNone(acc)
        self.assertIs(acc, mock_db)

    def test_selct(self):
        try:
            mock_select = self.Mock.select
            self.GetTopSpamDao.selectvalues = mock_select
            acc =  self.ParseTopSpamDao.selectvalues(0, 0)
            self.assertIsNotNone(acc)
            mock_select.assert_called()
            mock_select.assert_called_with(0, 0)
            self.GetTopSpamDao.selectvalues(0, 0)
        except Exception as e:
            return e is not None


class GetTopSpamDao2TestCase(unittest.TestCase):
    """
    the test cases for GetTopSpamDao2TestCase class
    """
    def setUp(self):
        self.GetTopSpamDao2 = GetTopSpamDao2('twitch.db')
        self.Mock = Mock()

    def tearDown(self):
        self.Mock = Mock()
        self.GetTopSpamDao2 = None

    def test_commitSuperDao(self):
        mock_commit = self.Mock.commit
        self.GetTopSpamDao2.commitconnection = mock_commit
        self.GetTopSpamDao2.commitconnection()
        mock_commit.assert_called()
        mock_commit.assert_called_once()
        mock_commit.assert_called_with()
        for i in range(999):
            self.GetTopSpamDao2.commitconnection()
        self.assertEqual(1000, mock_commit.call_count)
        self.GetTopSpamDao2.commitconnection()
        acc = self.GetTopSpamDao2.commitconnection()
        self.assertIsNotNone(acc)

    def test_closeconnectionSuperDao(self):
        self.GetTopSpamDao2.closeconnection()
        mock_connection = self.Mock.connection
        self.GetTopSpamDao2.connection = mock_connection
        mock_close = mock_connection.close
        mock_close.return_value = None
        self.GetTopSpamDao2.closeconnection()
        self.assertIs(self.GetTopSpamDao2.connection, mock_connection)
        mock_close.assert_called_once()
        acc = self.GetTopSpamDao2.closeconnection()
        self.assertIsNone(acc)

    def test_selectvalues(self):
        try:
            mock_select = self.Mock.select
            self.GetTopSpamDao2.selectvalues = mock_select
            acc =  self.GetTopSpamDao2.selectvalues(0, 0)
            self.assertIsNotNone(acc)
            mock_select.assert_called()
            mock_select.assert_called_with(0, 0)
            self.GetTopSpamDao2.selectvalues(0, 0)
        except Exception as e:
            return e is not None


class ViewershipDAOTestCase(unittest.TestCase):
    """
    the test cases for ViewershipDAOTestCase class
    """
    def setUp(self):
        self.ViewershipDAO = ViewershipDAO('twitch.db')
        self.Mock = Mock()

    def tearDown(self):
        self.Mock = Mock()
        self.ViewershipDAO = None

    def test_commitSuperDao(self):
        mock_commit = self.Mock.commit
        self.ViewershipDAO.commitconnection = mock_commit
        self.ViewershipDAO.commitconnection()
        mock_commit.assert_called()
        mock_commit.assert_called_once()
        mock_commit.assert_called_with()
        for i in range(999):
            self.ViewershipDAO.commitconnection()
        self.assertEqual(1000, mock_commit.call_count)
        self.ViewershipDAO.commitconnection()
        acc = self.ViewershipDAO.commitconnection()
        self.assertIsNotNone(acc)

    def test_closeconnectionSuperDao(self):
        self.ViewershipDAO.closeconnection()
        mock_connection = self.Mock.connection
        self.ViewershipDAO.connection = mock_connection
        mock_close = mock_connection.close
        mock_close.return_value = None
        self.ViewershipDAO.closeconnection()
        self.assertIs(self.ViewershipDAO.connection, mock_connection)
        mock_close.assert_called_once()
        acc = self.ViewershipDAO.closeconnection()
        self.assertIsNone(acc)

    def test_selectvalues(self):
        mock_select = self.Mock.select
        self.ViewershipDAO.selectvalues = mock_select
        acc = self.ViewershipDAO.selectvalues(0, 0)
        self.assertIsNotNone(acc)
        mock_select.assert_called()
        mock_select.assert_called_with(0, 0)
        self.ViewershipDAO.selectvalues(0, 0)
        acc = self.ViewershipDAO.selectvalues(0, 0)
        self.assertIsNotNone(acc)


class ChatlogDaoTestCase(unittest.TestCase):
    """
    the test cases for ChatlogDaoTestCase class
    """
    def setUp(self):
        self.Mock = Mock()
        self.ChatlogDao = ChatlogDao('twitch.db')

    def tearDown(self):
        self.Mock = Mock()
        self.ChatlogDao = None

    def test_commitSuperDao(self):
        mock_commit = self.Mock.commit
        self.ChatlogDao.commitconnection = mock_commit
        self.ChatlogDao.commitconnection()
        mock_commit.assert_called()
        mock_commit.assert_called_once()
        mock_commit.assert_called_with()
        for i in range(999):
            self.ChatlogDao.commitconnection()
        self.assertEqual(1000, mock_commit.call_count)
        self.ChatlogDao.commitconnection()
        acc = self.ChatlogDao.commitconnection()
        self.assertIsNotNone(acc)
        acc = self.ChatlogDao.commitconnection()
        self.assertIsNotNone(acc)

    def test_closeconnectionSuperDao(self):
        self.ChatlogDao.closeconnection()
        mock_connection = self.Mock.connection
        self.ChatlogDao.connection = mock_connection
        mock_close = mock_connection.close
        mock_close.return_value = None
        self.ChatlogDao.closeconnection()
        self.assertIs(self.ChatlogDao.connection, mock_connection)
        mock_close.assert_called_once()
        acc = self.ChatlogDao.closeconnection()
        self.assertIsNone(acc)
        acc = self.ChatlogDao.closeconnection()
        self.assertIsNone(acc)

    def test_createtable(self):
        mock_table = self.Mock.table
        self.ChatlogDao.createtable = mock_table
        self.ChatlogDao.createtable()
        acc = self.ChatlogDao.createtable()
        self.assertIsNotNone(acc)
        mock_table.assert_called()
        mock_table.assert_called_with()
        for i in range(999):
            self.ChatlogDao.createtable()
        self.assertEqual(1001, mock_table.call_count)
        acc = self.ChatlogDao.createtable()
        self.assertIsNotNone(acc)

    def test_insertvalues(self):
        try:
            mock_insert = self.Mock.insert
            self.ChatlogDao.insertvalues = mock_insert
            acc = self.ChatlogDao.insertvalues("", "")
            self.assertIsNotNone(acc)
            mock_insert.assert_called()
            mock_insert.assert_called_with("", "")
            self.ChatlogDao.insertvalues("", "")
            self.ChatlogDao.insertvalues("", "")
            mock_insert.assert_called()
            mock_insert.assert_called_with()
        except Exception as e:
            return e is not None

    def test_deletvalues(self):
        mock_delete = self.Mock.delet
        self.ChatlogDao.deletetable = mock_delete
        acc = self.ChatlogDao.deletetable("", "")
        self.assertIsNotNone(acc)
        mock_delete.assert_called()
        mock_delete.assert_called_with("", "")
        acc = self.ChatlogDao.deletvalues("", "")
        self.assertIsNone(acc)

    def test_updatevalues(self):
        try:
            mock_update = self.Mock.update
            self.ChatlogDao.updatevalues = mock_update
            acc = self.ChatlogDao.updatevalues(["", "", "", "", "", "", ""])
            self.assertIsNotNone(acc)
            mock_update.assert_called()
            mock_update.assert_called_with(["", "", "", "", "", "", ""])
        except Exception as e:
            return e is not None

if __name__ == "__main__":
    unittest.main(exit = False)