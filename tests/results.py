results = [
    {
        'query_type': 'SELECT',
        'joins': 0,
        'functions': 3,
        'where': 3,
        'subqueries_and_maxdepth': (4, 2),
        'tables': {'table1', 'table2', 'table3', 'table4', 'table5'}
    }
    ,
    {
        'query_type': 'SELECT',
        'joins': 1,
        'functions': 0,
        'where': 1,
        'subqueries_and_maxdepth': (2, 2),
        'tables': {'table1', 'table2', 'table6'}
    }
    ,
    {
        'query_type': 'SELECT',
        'joins': 0,
        'functions': 2,
        'where': 3,
        'subqueries_and_maxdepth': (3, 3),
        'tables': {'table1', 'table2', 'table3', 'table4'}
    }
    ,
    {
        'query_type': 'SELECT',
        'joins': 0,
        'functions': 1,
        'where': 3,
        'subqueries_and_maxdepth': (4, 2),
        'tables': {'table1', 'table2', 'table3', 'table4', 'table5'}
    }
    ,
    {
        'query_type': 'INSERT',
        'joins': 0,
        'functions': 1,
        'where': 0,
        'subqueries_and_maxdepth': (0, 0),
        'tables': {'orders'}
    }
    ,
    {
        'query_type': 'UPDATE',
        'joins': 0,
        'functions': 0,
        'where': 1,
        'subqueries_and_maxdepth': (0, 0),
        'tables': {'employees'}
    }
    ,
    {
        'query_type': 'SELECT',
        'joins': 1,
        'functions': 0,
        'where': 0,
        'subqueries_and_maxdepth': (0, 0),
        'tables': {'products', 'categories'}
    }
    ,        
    {
        'query_type': 'UPDATE',
        'joins': 0,
        'functions': 0,
        'where': 1,
        'subqueries_and_maxdepth': (0, 0),
        'tables': {'table3'}
    }
    ,
    {
        'query_type': 'DELETE',
        'joins': 0,
        'functions': 0,
        'where': 1,
        'subqueries_and_maxdepth': (0, 0),
        'tables': {'table4'}
    }
    ,
    {
        'query_type': 'SELECT',
        'joins': 3,
        'functions': 0,
        'where': 0,
        'subqueries_and_maxdepth': (0, 0),
        'tables': {'table1', 'table2', 'table3', 'table4'}
    }
    ,
    {
        'query_type': 'SELECT',
        'joins': 1,
        'functions': 0,
        'where': 1,
        'subqueries_and_maxdepth': (2, 2),
        'tables': {'table1', 'table2', 'table3'}
    }
    ,
    {
        'query_type': 'SELECT',
        'joins': 2,
        'functions': 0,
        'where': 0,
        'subqueries_and_maxdepth': (1, 1),
        'tables': {'table1', 'table2', 'table3'}
    }
    ,
    {
        'query_type': 'INSERT',
        'joins': 0,
        'functions': 1,
        'where': 1,
        'subqueries_and_maxdepth': (2, 1),
        'tables': {'table1', 'table2', 'table3'}
    }
    ,
    {
        'query_type': 'UPDATE',
        'joins': 0,
        'functions': 0,
        'where': 3,
        'subqueries_and_maxdepth': (2, 1),
        'tables': {'table1', 'table2', 'table3'}
    }
    ,
    {
        'query_type': 'DELETE',
        'joins': 1,
        'functions': 0,
        'where': 1,
        'subqueries_and_maxdepth': (0, 0),
        'tables': {'table1', 'table2'}
    }
    ,
        ]