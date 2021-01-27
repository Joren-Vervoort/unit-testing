from typing import List, Dict

import pytest #pytest will be used to check the raised errors.
import unittest 
from unittest.mock import Mock #a Mock function will be used to test the connetion_to_db

class TestMock(unittest.TestCase):

    def test_mock(self):
        mocked_object = Mock()

class ConnectionDatabaseError(Exception):

    """Raised when the database connection fails."""

    def test_connect_to_db():

        """ Checks if the ConnectionDatabaseError is raised when the connection fails."""

        with pytest.raises(ConnectionDatabaseError) as exception_info:
            connect_to_db(connection_string)
            raise ConnectionDatabaseError
        expected_message = "Can't connect to the databse!"
        assert exception_info.match(expected_message)

class TestDbError(Exception):

    """Raised when a unit test tries to connect to the database."""

    def test_get_users_list_from_db():
        with pytest.raises(TestDbError) as exception_info:
            get_users_list_from_db(connection_string)
            raise TestDbError
        expected_message = "ERROR: YOU FORGOT TO MOCK connect_to_db"
        assert exception_info.match(expected_message)

def connect_to_db(connection_string: str):
    """
    Function that connects to the db.
    
    We will not give you access to the DB yet. So mock this function if you want to test it.

    TODO: add a unit test to verify that this function raises a ConnectionDatabaseError when a different connection string than 'test' is provided.
    TODO: add a unit test to verify that this function raises a TestDbError when a string 'test' is provided.
    """
    print("connection string: ", connection_string)
    if connection_string == "test":
        raise TestDbError("ERROR: YOU FORGOT TO MOCK connect_to_db")
    else:
        raise ConnectionDatabaseError("Can't connect to the databse!")


def get_users_list_from_db(connection_string: str) -> List[Dict[str, str]]:
    """
    Function that gets the list of users from the database and returns them as a list of dict.

    Each user is formatted like that: { 'username': 'jonh Doe', 'birthday': '02/12/1985', 'role': 'admin' }
    The unit test should return at least 20 users.
    The unit test should check that all the users have a username, a birthday and a role.
    """
    db = connect_to_db(connection_string)
    users = db.get_user()
    return users


def add(num_1: int, num_2: int, num_3: int) -> int:

    """
    Function that adds 3 given integers.
    """

    return num_1 + num_2 + num_3

def test_add(self):

    """
    A unit test that tests ALL THE INT between 1 and 200 in less than 10 coding lines.
    """
    
    with self.assertRaises(ValueError):
        for i in range(1,201):
            for j in range(1,201):
                for k in range(1,201):
                    test_result = add(i,j,k)
                    expected_result = sum(i,j,k)
                    self.assertEqual(test_result, expected_result)
    
