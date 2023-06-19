"""
File: extension_server.py
---------------------
This starts a server! Go to http://localhost:8000 to enjoy it. Currently
the server only serves up the HTML. It does not search. Implement code in
the "TODO" parts of this file to make it work.
"""

# This imports the SimpleServer library
import SimpleServer

# This imports the functions you defined in searchengine.py
from searchengine import create_index, search, textfiles_in_dir

# To get the json.dumps function.
import json


# the directory of files to search over
DIRECTORY = 'bbcnews'
# perhaps you want to limit to only 10 responses per search.
MAX_RESPONSES_PER_REQUEST = 10


class SearchServer:
    def __init__(self):
        """
        load the data that we need to run the search engine. This happens
        once when the server is first created.
        """
        self.html = open('extension_client.html').read()
        # : Your code here. Change this code to load any data you want to use!
        self.index = {}
        self.filetitles = {}
        self.textfiles_lst = textfiles_in_dir(DIRECTORY)
        self.create_ind = create_index(self.textfiles_lst, self.index, self.filetitles)

    # this is the server request callback function. You can't change its name or params!!!
    def handle_request(self, request):
        """
        This function gets called every time someone makes a request to our
        server. To handle a search, look for the query parameter with key "query"
        """
        # it is helpful to print out each request you receive!
        print(request)

        # if the command is empty, return the html for the search page
        if request.command == '':
            return self.html

        # if the command is search, the client wants you to perform a search!
        if request.command == 'search':
            # right now we respond to a search request with an empty string.
            # TODO: Your code here. change this code to return the string version 
            # of a list of dicts. Use json.dumps(collection) to turn a list into a string
            #print(query)
            find_query = request.params
            query_req = find_query['query']
            if query_req != '':
                search_result_lst = search(self.index, query_req)
                final_result = []
                for value in search_result_lst:
                    mid_value_dict = {}
                    mid_value_dict['title'] = self.filetitles[value]
                    final_result.append(mid_value_dict)
                final_result = json.dumps(final_result, indent=2)
                print('DEBUG RESULT')
                print(final_result)
                return final_result


def main():
    # Make an instance of your Server
    handler = SearchServer()

    # Start the server to handle internet requests at http://localhost:8000
    SimpleServer.run_server(handler, 8000)


if __name__ == '__main__':
    main()
