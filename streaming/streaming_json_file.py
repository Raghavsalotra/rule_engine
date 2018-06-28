import json


class JsonFileReader(object):

    def __init__(self, abs_file_path):
        self.file_path = abs_file_path
        self._get_parsed_data()

    def _get_parsed_data(self):
        """
        load file and parse json
        :return: json converted to list of dictionaries
        """
        try:
            with open(self.file_path) as json_file:
                self.data = json.load(json_file)

        except IOError:
            raise Exception('Json File not present in path given.')

    def stream_data(self):

        for data in self.data:
            yield data


# TODO each streaming wrapper should have a abstract factory defined, to comply with methods each stream implementation
# TODO should provide. Because of time constraint this is not implemented yet.

# TODO As of now file is not read as lazily , i could not find a way to lazily load parsed json file.


# TODO I was thinking of lazy loading file with yield
