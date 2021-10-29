import unittest

from code.bot import add_user_record, user_list


def validate_user_list(users) -> str:
    """
    Helper method to validate the user list matches
    :param users: a sample dictionary of user: [records]
    :type: dict
    :return: True if user list matches
    :rtype: bool
    """
    # assert exact number of users
    if len(user_list) != len(users):
        return f'Length does not match. ' \
               f'Expected {len(users)} users' \
               f'Found {len(user_list)}'

    for user in users:
        # for each user, if it is not present in the user list
        if user not in user_list:
            return f'user {user} not found in user_list'

        # assert same number of records per user
        if len(user_list[user]) != len(users[user]):
            return f'user {user} number of records does not match.' \
                   f'Expected {len(users[user])} records. ' \
                   f'Found {len(user_list[user])}'

        # assert the record is right
        if user_list[user] != users[user]:
            return f"{user} record should be: {users[user]}, found {user_list[user]}"

    # if everything matches
    return ""


class TestAddUserRecord(unittest.TestCase):
    """
    Tests the addUserrecord method
    """

    def setUp(self) -> None:
        user_list = {}

    def test_add_user_record_one(self):
        """
        tests adding one record for one user
        :return:
        """
        assert len(user_list) == 0
        # adding one user
        users = {"1": ["TestRecordOne"]}
        for user in users:
            # for each record to add
            for record in users[user]:
                add_user_record(user, record)
        # validating the list
        message = validate_user_list(users)
        if message != "":
            assert False, message

    def test_add_user_record_multiple_record(self):
        """
        tests adding multiple records for one user
        :return:
        """
        assert len(user_list) == 0
        # adding one user, but multiple records
        users = {"1": ["TestRecordOne", "TestRecordTwo"]}
        for user in users:
            # for each record to add
            for record in users[user]:
                add_user_record(user, record)

        # validating the list
        message = validate_user_list(users)
        if message != "":
            assert False, message

    def test_add_user_record_multiple_user(self):
        """
        tests adding one record for multiple users
        :return:
        """

        assert len(user_list) == 0
        # adding all users
        users = {"1": ["TestRecordOne"], "2": ["TestRecordTwo"]}

        for user in users:
            # for each record to add
            for record in users[user]:
                add_user_record(user, record)

        # validating the list
        message = validate_user_list(users)
        if message != "":
            assert False, message

    def test_add_user_record_multiple_userrecord(self):
        """
        tests adding multiple records for multiple users
        :return:
        """
        assert len(user_list) == 0
        # adding all users
        users = {"1": ["TestRecordOne", "TestRecordThree"],
                 "2": ["TestRecordTwo", "TestRecordFour"]}

        for user in users:
            # for each record to add
            for record in users[user]:
                add_user_record(user, record)

        # validating the list
        message = validate_user_list(users)
        if message != "":
            assert False, message


if __name__ == '__main__':
    unittest.main()
