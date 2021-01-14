from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestSalary(TestCase):
    def setUp(self):
        self.sal = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, MockDbHelper):
        DbHelper = MockDbHelper()
        DbHelper.get_maximum_salary.return_value = 50000
        max_salary = DbHelper.get_maximum_salary()
        DbHelper.get_minimum_salary.return_value = 15000
        min_salary = DbHelper.get_minimum_salary()
        self.assertGreater(max_salary, min_salary)