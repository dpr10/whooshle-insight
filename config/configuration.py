from PyQt4.QtCore import QDir
from os.path import exists


class Configuration:

    PDF_DOCUMENT = 'PDF'
    HTML_DOCUMENT = 'HTML'
    CHM_DOCUMENT = 'CHM'
    EPUB_DOCUMENT = 'EPUB'

    CONFIG_OPTION_ENABLED = '1'
    CONFIG_OPTION_DISABLED = '0'

    ROUTES_CONFIG_FILE = 'routes.ini'
    ROUTES_CONFIG_FILE_HEADER = '[routes]'

    INDEXING_CONFIG_FILE = 'indexing.ini'
    INDEXING_CONFIG_FILE_HEADER = '[indexing]'
    INDEXING_CONFIG_PATH = 'INDEX_PATH'

    APPS_CONFIG_FILE = 'apps.ini'
    APPS_CONFIG_FILE_HEADER = '[apps]'

    INDEXED_DOCUMENTS_CONFIG_FILE = 'indexed_documents.ini'
    INDEXED_DOCUMENTS_CONFIG_FILE_HEADER = '[indexed documents]'

    @staticmethod
    def _read_options(config_file, config_file_header):
        options = {}

        if exists(config_file):
            indexing_config_file = open(config_file, 'r')

            if indexing_config_file.readline().strip() == config_file_header:
                config_line = indexing_config_file.readline().strip()

                while config_line != '':
                    current_options = config_line.split('=')
                    options[current_options[0]] = current_options[1]

                    config_line = indexing_config_file.readline().strip()

        return options

    @staticmethod
    def _write_options(config_file, config_file_header, options):
        indexing_config_file = open(config_file, 'w')

        indexing_config_file.write('%s\n' % config_file_header)

        for key in options:
            indexing_config_file.write('%s=%s\n' % (key, options[key]))

        indexing_config_file.close()

    @staticmethod
    def routes():
        routes_list = []

        if exists(Configuration.ROUTES_CONFIG_FILE):
            routes_config_file = open(Configuration.ROUTES_CONFIG_FILE, 'r')

            if routes_config_file.readline().strip() == Configuration.ROUTES_CONFIG_FILE_HEADER:
                route = routes_config_file.readline().strip()

                while route != '':
                    routes_list.append(route)
                    route = routes_config_file.readline().strip()

            routes_config_file.close()

        return routes_list

    @staticmethod
    def set_routes(routes):
        routes_file = open(Configuration.ROUTES_CONFIG_FILE, 'w')

        routes_file.write(
            '%s\n' % Configuration.ROUTES_CONFIG_FILE_HEADER
        )

        for route in routes:
            routes_file.write('%s\n' % route)

        routes_file.close()

    @staticmethod
    def index_path():
        options = Configuration._read_options(
            config_file=Configuration.INDEXING_CONFIG_FILE,
            config_file_header=Configuration.INDEXING_CONFIG_FILE_HEADER
        )

        if Configuration.INDEXING_CONFIG_PATH in options:
            return QDir.fromNativeSeparators(options[Configuration.INDEXING_CONFIG_PATH])

        return QDir.fromNativeSeparators('%s/%s' % (QDir.homePath(), 'index_db'))

    @staticmethod
    def set_index_path(path):
        options = Configuration._read_options(
            config_file=Configuration.INDEXING_CONFIG_FILE,
            config_file_header=Configuration.INDEXING_CONFIG_FILE_HEADER
        )

        options[Configuration.INDEXING_CONFIG_PATH] = path

        Configuration._write_options(
            config_file=Configuration.INDEXING_CONFIG_FILE,
            config_file_header=Configuration.INDEXING_CONFIG_FILE_HEADER,
            options=options
        )

    @staticmethod
    def index_document(document_type):
        options = Configuration._read_options(
            config_file=Configuration.INDEXING_CONFIG_FILE,
            config_file_header=Configuration.INDEXING_CONFIG_FILE_HEADER
        )

        if document_type in options:
            if options[document_type] == Configuration.CONFIG_OPTION_ENABLED:
                return True

            if options[document_type] == Configuration.CONFIG_OPTION_DISABLED:
                return False

        return True

    @staticmethod
    def set_index_document(document_type, value):
        options = Configuration._read_options(
            config_file=Configuration.INDEXING_CONFIG_FILE,
            config_file_header=Configuration.INDEXING_CONFIG_FILE_HEADER
        )

        options[document_type] = value

        Configuration._write_options(
            config_file=Configuration.INDEXING_CONFIG_FILE,
            config_file_header=Configuration.INDEXING_CONFIG_FILE_HEADER,
            options=options
        )

    @staticmethod
    def indexed_documents():
        documents_list = []

        if exists(Configuration.INDEXED_DOCUMENTS_CONFIG_FILE):
            indexed_documents_file = open(
                Configuration.INDEXED_DOCUMENTS_CONFIG_FILE, 'r'
            )

            if indexed_documents_file.readline().strip() == Configuration.INDEXED_DOCUMENTS_CONFIG_FILE_HEADER:
                document = indexed_documents_file.readline().strip()

                while document != '':
                    documents_list.append(document)
                    document = indexed_documents_file.readline().strip()

            indexed_documents_file.close()

        return documents_list

    @staticmethod
    def set_indexed_documents(documents):
        indexed_documents_file = open(
            Configuration.INDEXED_DOCUMENTS_CONFIG_FILE, 'w'
        )

        indexed_documents_file.write(
            '%s\n' % Configuration.INDEXED_DOCUMENTS_CONFIG_FILE_HEADER
        )

        for document in documents:
            indexed_documents_file.write('%s\n' % document)

        indexed_documents_file.close()

    @staticmethod
    def app_route(document_type):
        options = Configuration._read_options(
            config_file=Configuration.APPS_CONFIG_FILE,
            config_file_header=Configuration.APPS_CONFIG_FILE_HEADER
        )

        if document_type in options:
            return options[document_type]

        return ''

    @staticmethod
    def set_app_route(document_type, route):
        options = Configuration._read_options(
            config_file=Configuration.APPS_CONFIG_FILE,
            config_file_header=Configuration.APPS_CONFIG_FILE_HEADER
        )

        options[document_type] = route

        Configuration._write_options(
            config_file=Configuration.APPS_CONFIG_FILE,
            config_file_header=Configuration.APPS_CONFIG_FILE_HEADER,
            options=options
        )
