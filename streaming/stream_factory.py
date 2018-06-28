from const import SUPPORTED_STREAMS
from streaming_json_file import JsonFileReader


class StreamFactory(object):

    @staticmethod
    def load_stream(stream_name):

        ext = stream_name.split('.')[-1]

        if SUPPORTED_STREAMS.get(ext):

            if ext == 'json':
                return JsonFileReader(stream_name).stream_data()
            else:
                raise Exception('Extension ' + ext + 'is not part of available streams. Please raise this to Product.')
