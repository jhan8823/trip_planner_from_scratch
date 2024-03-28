import json
import os

import requests
from langchain.tools import tool

class SearchTools():
    @tool('Search the internet')
    def search_internet(query):
        """
        Useful to search the internet for information on a given query and return relevant results.
        """
        top_results_to_return = 4
        url = "https://google.serper.dev/search"
        payload=json.dumps({"q":query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # check if there is an organic key
        if 'organic' not in response.json():
            return "No results found."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_results_to_return]:
                try:
                    string.append('\n'.join([f"Title: {result['title']}", 
                                             f"Link: {result['url']}", 
                                             f"Snippet: {result['snippet']}",
                                             "\n -------------------"]))
                except KeyError:
                    next
            return '\n'.join(string)
        
