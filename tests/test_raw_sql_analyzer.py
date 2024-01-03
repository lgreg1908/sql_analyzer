import unittest
from pathlib import Path
import sys
from queries import sql_queries
from results import results


path_to_append: Path = Path.cwd().resolve().parent
sys.path.append(str(path_to_append))

from sql_analyzer.raw_sql_analyzer import RawSQLAnalyzer

class TestRawSQLAnalyzer(unittest.TestCase):
    def setUp(self):
        self.queries = sql_queries
        self.results = results
        
    def test_perform_full_analysis(self):
        for idx, query in enumerate(self.queries):
            with self.subTest(query_number=idx+1, query=query):
                analyzer = RawSQLAnalyzer(query)
                results = analyzer.perform_full_analysis()
                self.assertEqual(results, self.results[idx])

if __name__ == '__main__':
    unittest.main()