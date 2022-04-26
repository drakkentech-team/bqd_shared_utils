import unittest


def run_unittests(test_filename):
    """
    Use this method to discover unittests at specified path, and run them
    :param path:
    :return: TestResult
    """
    import unittest
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(test_filename)

    runner = unittest.TextTestRunner()
    return runner.run(suite)


class MyTestCase(unittest.TestCase):
    def test_all_filter_sql_docs(self):
        test_file = "tests.filter_docs.test_filter_sql_docs"

        test_result = run_unittests(test_file)
        self.assertTrue(test_result.wasSuccessful(), "Some tests failed")
        
    def test_all_staging_coding(self):
        test_file = "tests.ftp.test_staging"

        test_result = run_unittests(test_file)
        self.assertTrue(test_result.wasSuccessful(), "Some tests failed")


if __name__ == "__main__":
    unittest.main()
