import json
from urllib.parse import urlparse, unquote, parse_qs
import re
import os

def request(flow):
    pass


def response(flow):

    if 'mgets' in flow.request.url:
        # print(flow.response.text)
        with open('./data/mgets.txt', 'a', encoding='utf-8') as file:
            # file.write(flow.request.url)
            # file.write('\n')
            file.write(flow.response.text)
            file.write('\n')
            # file.write('\n')
            # file.write('\n')

    if 'getModuleHtml' in flow.request.url:
        # print(flow.response.text)
        with open('./data/getModuleHtml.txt', 'a', encoding='utf-8') as file:
            # file.write(flow.request.url)
            # file.write('\n')
            file.write(flow.response.text)
            file.write('\n')
            # file.write('\n')
            # file.write('\n')

