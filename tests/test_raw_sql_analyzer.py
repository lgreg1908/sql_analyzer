# import unittest
# from pathlib import Path
# import sys
# from queries import sql_queries
# from results import results


# path_to_append: Path = Path.cwd().resolve().parent
# sys.path.append(str(path_to_append))

# from sql_analyzer.raw_sql_analyzer import RawSQLAnalyzer

# class TestRawSQLAnalyzer(unittest.TestCase):
#     def setUp(self):
#         self.queries = sql_queries
#         self.results = results
#         self.invalid_query = ''
        
#     def test_perform_full_analysis(self):
#         for idx, query in enumerate(self.queries):
#             with self.subTest(query_number=idx+1, query=query):
#                 analyzer = RawSQLAnalyzer(query)
#                 results = analyzer.perform_full_analysis()
#                 self.assertEqual(results, self.results[idx])

#     def test_init_exception(self):
#         with self.assertRaises(ValueError):
#             RawSQLAnalyzer(1908)

#     def test_analyze_count_functions_exception(self):
#         analyzer = RawSQLAnalyzer(self.invalid_query)
#         with self.assertRaises(Exception) as context:
#             analyzer.analyze_count_functions()

#     def test_analyze_count_where_exception(self):
#         analyzer = RawSQLAnalyzer(self.invalid_query)
#         with self.assertRaises(Exception):
#             analyzer.analyze_count_where()

#     def test_analyze_count_subqueries_and_depth_exception(self):
#         analyzer = RawSQLAnalyzer(self.invalid_query)
#         with self.assertRaises(Exception):
#             analyzer.analyze_count_subqueries_and_depth()

#     def test_analyze_analyze_get_statement_type_exception(self):
#         analyzer = RawSQLAnalyzer(self.invalid_query)
#         with self.assertRaises(Exception):
#             analyzer.analyze_get_statement_type()
    
#     def test_analyze_count_joins_exception(self):
#         analyzer = RawSQLAnalyzer(self.invalid_query)
#         with self.assertRaises(Exception):
#             analyzer.analyze_count_joins()


# if __name__ == '__main__':
#     unittest.main()
import unittest
from pathlib import Path
import sys
from queries import sql_queries
from results import results

# Append the parent directory of the current working directory to the system path
path_to_append: Path = Path.cwd().resolve().parent
sys.path.append(str(path_to_append))

from sql_analyzer.raw_sql_analyzer import RawSQLAnalyzer

class TestRawSQLAnalyzer(unittest.TestCase):
    """
    The TestRawSQLAnalyzer class contains a series of unit tests for the RawSQLAnalyzer class.
    It tests various scenarios including normal operations, error handling, and exception raising.
    """

    def setUp(self):
        """
        setUp is called before each test method to set up any objects or data needed for the tests.
        It initializes a set of SQL queries and expected results to be used in the tests.
        """
        self.queries = sql_queries
        self.results = results
        self.invalid_query = ''  # Invalid query for testing exception handling
        
    def test_perform_full_analysis(self):
        """
        Tests the 'perform_full_analysis' method of RawSQLAnalyzer.
        It verifies that the method returns the correct analysis results for a series of test queries.
        """
        for idx, query in enumerate(self.queries):
            with self.subTest(query_number=idx+1, query=query):
                analyzer = RawSQLAnalyzer(query)
                results = analyzer.perform_full_analysis()
                self.assertEqual(results, self.results[idx])

    def test_init_exception(self):
        """
        Tests that initializing RawSQLAnalyzer with a non-string query raises a ValueError.
        """
        with self.assertRaises(ValueError):
            RawSQLAnalyzer(1908)

    def test_analyze_count_functions_exception(self):
        """
        Tests that the 'analyze_count_functions' method raises an exception when called with an invalid query.
        """
        analyzer = RawSQLAnalyzer(self.invalid_query)
        with self.assertRaises(Exception) as context:
            analyzer.analyze_count_functions()

    def test_analyze_count_where_exception(self):
        """
        Tests that the 'analyze_count_where' method raises an exception when called with an invalid query.
        """
        analyzer = RawSQLAnalyzer(self.invalid_query)
        with self.assertRaises(Exception):
            analyzer.analyze_count_where()

    def test_analyze_count_subqueries_and_depth_exception(self):
        """
        Tests that the 'analyze_count_subqueries_and_depth' method raises an exception when called with an invalid query.
        """
        analyzer = RawSQLAnalyzer(self.invalid_query)
        with self.assertRaises(Exception):
            analyzer.analyze_count_subqueries_and_depth()

    def test_analyze_analyze_get_statement_type_exception(self):
        """
        Tests that the 'analyze_get_statement_type' method raises an exception when called with an invalid query.
        """
        analyzer = RawSQLAnalyzer(self.invalid_query)
        with self.assertRaises(Exception):
            analyzer.analyze_get_statement_type()
    
    def test_analyze_count_joins_exception(self):
        """
        Tests that the 'analyze_count_joins' method raises an exception when called with an invalid query.
        """
        analyzer = RawSQLAnalyzer(self.invalid_query)
        with self.assertRaises(Exception):
            analyzer.analyze_count_joins()

if __name__ == '__main__':
    unittest.main()
