from typing import (List, Type, Callable, Tuple)
import logging
from sqlparse.sql import (Statement, TokenList, Token)
import re
logger = logging.getLogger(__name__)


def search_tokens(statement: Statement, condition: Callable[[TokenList], bool]) -> List:
    """
    Recursively searches tokens in a SQL statement based on a given condition.

    Args:
        statement (Statement): The parsed SQL statement.
        condition (Callable): A function that defines the condition to search for.

    Returns:
        List: A list of tokens that meet the search condition.
    """
    found_elements = []

    def search(tokens: TokenList):
        for token in tokens:
            if condition(token):
                found_elements.append(token)
            if token.is_group:
                search(token.tokens)

    search(statement.tokens)
    return found_elements

def find_by_type(statement: Statement, element_type: Type) -> List:
    """
    Finds elements of a specific type in a SQL query.

    Args:
        statement (Statement): The parsed SQL statement.
        element_type (Type): The type of element to find.

    Returns:
        List: A list of found elements of the specified type.
    """
    return search_tokens(statement, lambda token: isinstance(token, element_type))


def find_by_value(statement: Statement, value: str) -> List:
    """
    Finds elements with a specific value in a SQL query.

    Args:
        statement (Statement): The parsed SQL statement.
        value (str): The value to search for.

    Returns:
        List: A list of found elements with the specified value.
    """
    return search_tokens(statement, lambda token: token.value.upper() == value.upper())

def find_by_ttype_and_values(statement: Statement, ttype: Token, values: List[str]) -> List:
    """
    Finds tokens of a specific token type (ttype) and any of a list of values in a SQL query.

    Args:
        statement (Statement): The parsed SQL statement.
        ttype (TokenType): The token type to search for.
        values (List[str]): The list of values to search for.

    Returns:
        List: A list of tokens of the specified token type and any of the specified values.
    """
    values_lower = [value.lower() for value in values]
    return search_tokens(statement, lambda token: 
                         token.ttype is ttype and 
                         any(value in token.value.lower() for value in values_lower))

def count_subqueries_and_depth(statement: Statement, current_depth: int = 0) -> Tuple[int, int]:
    """
    Recursively counts the number and depth of subqueries in a SQL query.

    Args:
        tokens (TokenList): Tokens from a parsed SQL statement.
        current_depth (int): The current depth of nested subqueries.

    Returns:
        Tuple[int, int]: A tuple containing the total count of subqueries and the maximum depth.
    """
    try:
        subquery_count = 0
        max_depth = current_depth

        for token in statement:
            if token.is_group:
                is_subquery = any(sub_token.value.upper().startswith("SELECT") for sub_token in token.tokens)
                if is_subquery:
                    nested_count, nested_depth = count_subqueries_and_depth(token.tokens, current_depth + 1)
                    subquery_count += 1  # Count this as a subquery
                    subquery_count += nested_count  # Add nested subqueries count
                    max_depth = max(max_depth, nested_depth)
                else:
                    # Check nested tokens without incrementing depth
                    nested_count, nested_depth = count_subqueries_and_depth(token.tokens, current_depth)
                    subquery_count += nested_count
                    max_depth = max(max_depth, nested_depth)

        return subquery_count, max_depth
    except Exception as e:
        logger.error(f"Error in counting subqueries: {e}")
        raise


# def extract_tables_with_regex(query):
#     # Regex pattern to match table names in various SQL commands
#     pattern = (
#         r'\bFROM\s+([\w]+)|\bJOIN\s+([\w]+)|'          # Matches table names in SELECT, JOIN
#         r'\bINSERT\s+INTO\s+([\w]+)|'                  # Matches table names in INSERT INTO
#         r'\bUPDATE\s+([\w]+)\b|'                       # Matches table names in UPDATE
#         r'\bDELETE\s+FROM\s+([\w]+)'                   # Matches table names in DELETE
#     )

#     # Find all matches in the query
#     matches = re.findall(pattern, query, re.IGNORECASE)

#     # Process matches to extract table names
#     tables = set()
#     for match in matches:
#         # Each match is a tuple, but only one element in the tuple is the table name
#         table_name = [m for m in match if m][0]
#         tables.add(table_name)
#     return tables
def extract_tables_with_regex(query: str) -> set:
    """
    Extracts table names from a given SQL query.

    This function uses regular expressions to identify table names in different SQL commands 
    including SELECT, INSERT, UPDATE, DELETE, and various JOINs. It is designed to handle 
    nested queries, table names in different contexts, and to exclude common aliases, CTE names, 
    and SQL keywords.

    Args:
        query (str): The SQL query string from which table names are to be extracted.

    Returns:
        set: A set of unique table names found in the query.

    Raises:
        ValueError: If the query is not a valid string.
    """
    if not isinstance(query, str):
        raise ValueError("The query must be a string.")

    pattern = (
        r'\bFROM\s+(?:\(?([^\s,()]+)\)?)|'            # Matches table names in FROM, possibly within parentheses
        r'\bJOIN\s+(?:\(?([^\s,()]+)\)?)|'             # Matches table names in JOIN, possibly within parentheses
        r'\bINTO\s+(?:\(?([^\s,()]+)\)?)|'             # Matches table names in INSERT INTO, possibly within parentheses
        r'\bUPDATE\s+(?:\(?([^\s,()]+)\)?)\b|'         # Matches table names in UPDATE, possibly within parentheses
        r'\bDELETE\s+FROM\s+(?:\(?([^\s,()]+)\)?)'     # Matches table names in DELETE, possibly within parentheses
    )

    # Exclude patterns typically used for CTEs and their aliases
    exclude_patterns = ['as', 'on', 'using', 'with', 'cte', 'select']

    try:
        matches = re.findall(pattern, query, re.IGNORECASE)

        tables = set()
        for match in matches:
            for m in match:
                if m and m.lower() not in exclude_patterns:
                    tables.add(m)
        return tables
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred while extracting table names: {e}")
        return set()
# from google.cloud import bigquery

# def estimate_query_cost(query, client):
#     job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
#     query_job = client.query(query, job_config=job_config)

#     # Estimated cost
#     bytes_processed = query_job.total_bytes_processed
#     estimated_cost = calculate_cost(bytes_processed)
#     return estimated_cost

# def calculate_cost(bytes_processed):
#     # BigQuery charges per TB processed after the free quota.
#     # Calculate cost based on current pricing.
#     price_per_tb = 5  # example price in USD
#     tb_processed = bytes_processed / (1024 ** 4)
#     return tb_processed * price_per_tb
