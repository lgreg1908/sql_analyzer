
# README for SQL Analysis Library

## Overview
This library provides a comprehensive solution for analyzing SQL queries. It includes two main modules, each with several functions to dissect and examine various aspects of SQL statements. 

### Features
- Search and extract specific tokens from SQL statements.
- Count and analyze subqueries, including depth calculation.
- Extract table names using regular expressions.
- Analyze a raw SQL query to extract details like query type, tables used, and columns involved.

## Modules

### Module 1: `utils`

#### Functions
1. `search_tokens`: Recursively searches tokens in a SQL statement based on a given condition.
2. `find_by_type`: Finds elements of a specific type in a SQL query.
3. `find_by_value`: Finds elements with a specific value in a SQL query.
4. `find_by_ttype_and_values`: Finds tokens of a specific token type and any of a list of values in a SQL query.
5. `count_subqueries_and_depth`: Recursively counts the number and depth of subqueries in a SQL query.
6. `extract_tables_with_regex`: Extracts table names from a given SQL query using regular expressions.

### Module 2: `RawSQLAnalyzer`

#### Class: `RawSQLAnalyzer`
Analyzes a raw SQL query to extract various details.

##### Methods
- `parsed_query`: Parses the raw SQL query.
- `analyze_count_functions`: Counts the number of SQL functions used in the query.
- `analyze_count_where`: Counts the number of 'WHERE' clauses in the query.
- `analyze_count_subqueries_and_depth`: Counts the number of subqueries and determines their maximum depth.
- `analyze_get_tables`: Extracts the names of the tables used in the SQL query.
- `analyze_get_statement_type`: Extracts the type of the SQL statement.
- `analyze_count_joins`: Counts JOIN clauses in a SQL query.
- `perform_full_analysis`: Performs a full analysis of the query.
