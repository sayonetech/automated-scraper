from scrapy.http.response.html import HtmlResponse
from scrapy.exceptions import IgnoreRequest
from scrapy import log
import re

class FilterResponses(object):
    """Limit the HTTP response types that Scrapy dowloads."""

    @staticmethod
    def is_valid_response(type_whitelist, content_type_header):
        for type_regex in type_whitelist:
            if re.search(type_regex, content_type_header):
                return True
        return False


    def process_response(self, request, response, spider):
        """
        Only allow HTTP response types that that match the given list of 
        filtering regexs
        """
        # to specify on a per-spider basis
        # type_whitelist = getattr(spider, "response_type_whitelist", None)
        type_whitelist = (r'.pdf',r'.jpg',r'.png',r'.jpeg',r'.gif',r'.doc' )

        content_type_header = response.headers.get('content-type', None)
        if not content_type_header or not type_whitelist:
            return response

        for exe in type_whitelist:
          searchObj = re.search( exe,response.url, re.M|re.I)
          if searchObj:

              msg = "Ignoring request {}, content-type was not in whitelist".format(response.url)
              log.msg(msg, level=log.INFO)
              raise IgnoreRequest()

        return response
