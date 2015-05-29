from os.path import exists
from os import mkdir

from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

from config.configuration import Configuration


class QueryManager:

    def __init__(self):
        if not exists(Configuration.index_path()):
            mkdir(Configuration.index_path())

            schema = Schema(
                title=TEXT(),
                author=TEXT(),
                content=TEXT(),
                url=ID(unique=True, stored=True)
            )

            create_in(dirname=Configuration.index_path(), schema=schema)

        self._index_database = open_dir(
            dirname=str(Configuration.index_path())
        )

    def serch(self, to_search, field='content'):
        """
        return the documents searched
        :param to_search: text to search
        :param field: field
        :return: documents finded
        """
        query = QueryParser(
            fieldname=field, schema=self._index_database.schema)
        query = query.parse(text=to_search)

        results = []

        with self._index_database.searcher() as searcher:
            searcher_results = searcher.search(query, limit=None)

            for result in searcher_results:
                results.append(result.fields())

        return results

    def search_page(self, to_search, page=1, field='content'):
        """
        return the number of page and the current page of results searched
        :param to_search: text to search
        :param page: current page
        :param field: field searched
        :return: documents finded
        """
        query = QueryParser(
            fieldname=field, schema=self._index_database.schema)
        query = query.parse(text=to_search)

        results = []

        with self._index_database.searcher() as searcher:
            searcher_results = searcher.search_page(query, page)

            yield searcher_results.pagecount

            for result in searcher_results:
                results.append(result.fields())

        yield results
