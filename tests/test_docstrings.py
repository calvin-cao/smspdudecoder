import doctest
import unittest

def load_tests(loader, tests, pattern):
    tests.addTests(doctest.DocTestSuite('smspdu.codecs'))
    tests.addTests(doctest.DocTestSuite('smspdu.pdu_elements'))
    return tests
