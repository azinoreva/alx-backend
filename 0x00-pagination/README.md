 Pagination Project
 Project Overview

This project focuses on implementing pagination techniques in backend development to efficiently manage large datasets. You will learn to paginate data using basic parameters, implement hypermedia-driven pagination, and ensure that pagination remains robust even when items are deleted from the dataset.

Files

1. **`0-simple_helper_function.py`**: Contains the `index_range` function, which calculates and returns the start and end indexes for pagination based on given page and page size parameters.

2. **`1-simple_pagination.py`**: Implements the `Server` class to manage a dataset of popular baby names. The class includes a method, `get_page`, that returns a specific page of data based on pagination parameters.

3. **`2-hypermedia_pagination.py`**: Extends the `Server` class by adding a `get_hyper` method, which provides hypermedia-driven pagination. This method returns additional metadata, such as next and previous pages, along with the paginated data. 

Each file progressively builds on the concepts of pagination to provide a comprehensive understanding of managing data in backend systems.
