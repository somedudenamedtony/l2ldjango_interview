import datetime

from django.test import TestCase

from l2l.templatetags.l2l_extras import l2l_dt


class L2LDTFilterTestCase(TestCase):
    # test valid string conversion
    def test_valid_datetime_string(self):
        input_str = "2023-08-24T15:30:00"
        expected_output = "2023-08-24 15:30:00"
        output = l2l_dt(input_str)
        self.assertEqual(output, expected_output)

    # test valid datetime conversion
    def test_valid_datetime_object(self):
        input_dt = datetime.datetime(2023, 8, 24, 15, 30, 0)
        expected_output = "2023-08-24 15:30:00"
        output = l2l_dt(input_dt)
        self.assertEqual(output, expected_output)

    def test_invalid_input_type(self):
        # Int instead of datetime or string
        with self.assertRaises(ValueError):
            l2l_dt(123)

        # Incorrect format
        with self.assertRaises(ValueError):
            l2l_dt("2023-08-24")

    # Correct format but not ISO format
    def test_invalid_datetime_string(self):
        with self.assertRaises(ValueError):
            l2l_dt("2023-08-24 15:30:00")