from unittest import TestCase
from handlers import pulls


class TestPulls(TestCase):

    def setUp(self):
        """Init"""

    def test_acpt_state(self):
        self.assertEqual(pulls.get_pulls('accepted')[0]['labels'][0]['name'], 'accepted')

    def test_closed_state(self):
        self.assertEqual(pulls.get_pulls('closed')[0]['state'], 'closed')

    def tearDown(self):
        """Finish"""
