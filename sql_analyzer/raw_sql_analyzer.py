import logging
from typing import (Tuple, Any, Dict, Set, List)
import inspect

import sqlparse
from sqlparse.tokens import Token as TokenType

from sql_analyzer import utils


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RawSQLAnalyzer:
    """
    This class analyzes a raw SQL query to extract various details such as the type of the query,
    the tables used, and the columns involved. It provides methods to count different SQL elements
    like functions, 'WHERE' clauses, subqueries, and to determine the depth of these subqueries.
    It also allows retrieving the names of tables used in the query. 

    Attributes:
        query (str): The raw SQL query string to be analyzed.
        _parsed_query (sqlparse.sql.Statement): The parsed form of the SQL query.
        _extracted_data (Dict[str, Any]): A dictionary to store extracted data from the query.
    """

    def __init__(self, query: str):
        """
        Initializes the RawSQLAnalyzer with a specific SQL query.

        Args:
            query (str): The raw SQL query string to be analyzed.
        """
        if not isinstance(query, str):
            raise ValueError("The query must be a string.")
        
        self.query = query
        self._parsed_query = None
        self._extracted_data: Dict[str, Any] = {}

    @property
    def parsed_query(self) -> sqlparse.sql.Statement:
        """
        Parses the raw SQL query and returns it as a sqlparse.sql.Statement object. 
        If the query is already parsed, it returns the cached version.

        Returns:
            sqlparse.sql.Statement: The parsed SQL query.
        """
        if not self._parsed_query:
            self._parsed_query = sqlparse.parse(self.query)[0] # Assume single statement
        return self._parsed_query
 
    def analyze_count_functions(self) -> int:
        """
        Counts the number of SQL functions used in the query.

        Returns:
            int: The number of functions found in the query.

        Raises:
            Exception: If there is an error in counting functions.
        """
        try:
            token_types: list = utils.find_by_type(self.parsed_query, sqlparse.sql.Function)
            self._extracted_data["functions"] = len(token_types)
            return self._extracted_data['functions']
        except Exception as e:
            logger.error(f"Failed to count functions: {e}")
            raise

    def analyze_count_where(self) -> int:
        """
        Counts the number of 'WHERE' clauses in the query.

        Returns:
            int: The number of 'WHERE' clauses found in the query.

        Raises:
            Exception: If there is an error in counting 'WHERE' clauses.
        """
        try:
            token_types: list = utils.find_by_type(self.parsed_query, sqlparse.sql.Where)
            self._extracted_data["where"] = len(token_types)
            return self._extracted_data['where']
        except Exception as e:
            logger.error(f"Failed to count functions: {e}")
            raise

    def analyze_count_subqueries_and_depth(self) -> Tuple[int, int]:
        """
        Counts the number of subqueries in the SQL query and determines the maximum depth
        of these subqueries.

        Returns:
            Tuple[int, int]: A tuple containing the number of subqueries and the maximum depth.

        Raises:
            Exception: If there is an error in counting subqueries and determining their depth.
        """
        try:
            n_queries, depth =  utils.count_subqueries_and_depth(self.parsed_query)
            self._extracted_data["subqueries_and_maxdepth"] = (n_queries, depth)
            return self._extracted_data["subqueries_and_maxdepth"]
        except Exception as e:
            logger.error(f"Failed to count subqueries: {e}")
            raise
        
    def analyze_get_tables(self) -> Set[str]:
        """
        Extracts the names of the tables used in the SQL query.

        Returns:
            Set[str]: A set containing the names of the tables found in the query.

        Raises:
            Exception: If there is an error in extracting table names.
        """
        try:
            tables = utils.extract_tables_with_regex(self.query)
            self._extracted_data["tables"] = tables
            return self._extracted_data["tables"]
        except Exception as e:
            logger.error(f"Failed to get tables: {e}")
            raise
    
    def analyze_get_statement_type(self) -> str:
        """
        Extracts the type of statement of the parsed query.

        Returns:
            str: A string containing the type of statement.

        Raises:
            Exception: If there is an error in extracting statement type.
        """
        try:
            self._extracted_data["query_type"] = self.parsed_query.get_type()
            return self._extracted_data["query_type"]
        except Exception as e:
            logger.error(f"Failed to extract query type: {e}")
            raise

    def analyze_count_joins(self) -> List:
        """
        Finds JOIN clauses in a SQL query.

        Args:
            statement (Statement): The parsed SQL statement.

        Returns:
            List: A list of JOIN clauses.
        """
        join_keywords = ["JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "CROSS JOIN"]
        try:
            joins: list = utils.find_by_ttype_and_values(self.parsed_query, TokenType.Keyword, join_keywords)
            self._extracted_data["joins"] = len(joins)
            return self._extracted_data['joins']
        except Exception as e:
            logger.error(f"Failed to count joins: {e}")
            raise
 
    def perform_full_analysis(self) -> Dict:
        """
        Performs a full analysis of the query by dynamically running all methods 
        that start with 'analyze'.

        Returns:
            Dict: A dictionary containing the results of the analysis.
        """
        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if name.startswith("analyze"):
                try:
                    method()  # Invoke the analysis method
                except Exception as e:
                    logger.error(f"Error running {name}: {e}")
        return self._extracted_data