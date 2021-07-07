import unittest
from ss_t2 import *


class TestEnvelope (unittest.TestCase):

    def test_create_envelope(self):
        env = Envelope(1.25, 10)
        self.assertEqual(env.a, 1.25)
        self.assertEqual(env.b, 10)

    def test_not_fitting_ints(self):
        env1 = Envelope(2, 2)
        env2 = Envelope(1, 3)
        self.assertFalse(env1 < env2)
        self.assertFalse(env1 > env2)

    def test_not_fitting_with_floats(self):
        env1 = Envelope(2.2, 2)
        env2 = Envelope(1, 3.1)
        self.assertFalse(env1 < env2)
        self.assertFalse(env1 > env2)

    def test_first_inside_second(self):
        env1 = Envelope(2, 5)
        env2 = Envelope(10, 11)
        self.assertTrue(env1 < env2)
        self.assertFalse(env1 > env2)

    def test_errors(self):
        with self.assertRaises(TypeError):
            env1 = Envelope('221', 5)
            env2 = Envelope(10, 11)
            self.assertTrue(env1 < env2)


if __name__ == '__main__':
    unittest.main()
