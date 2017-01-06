import re

from bs4 import BeautifulSoup
from ..utils.utils import get_text

class PhoneParser(object):
    """
    Every response passes through this logic until get a required data
    """

    def __init__(self, response):
        self.response = response

    def process_response(self, response):
        """
        Get phone number logic
        :param response:
        :return: List
        """

        visible_text = get_text(response.body) #convert response.body only to  text
        phone = self.parse_phone_numbers(visible_text)
        return phone

    def parse_phone_numbers(self, page):
        """
        Parse phone number
        :param page:
        :return: List
        """

        #under development
        numbers = list(set(re.findall(r'[\bPhone\b|\bTelefon\b|\bTelfax\b|\bTel\b|\bFax\b].?:?\s?[+\d]{3}[\s/()\d-]+', page)))

        phone = []
        final_phone=[]
        for number in numbers:

            num=re.findall(r'[+\d]{3}[\s/()\d-]+',number)[0]
            if re.findall(r'x',number):
              type='fax'
            else:
              type='telephone'

            final_phone.append({'phone_number':re.sub('\s+', '',num),'type':type})

        numbers = list(set(re.findall(r'[+\d]{3}[\s/()\d-]+', page)))
        numbers.sort(key = len)
        numbers=numbers[-5:-1]
        for number in numbers:
            flag=0
            add_number=re.sub('\s+', '',number)
            for entry in final_phone:
              if entry["phone_number"] == add_number:
                flag=1
                break
            if flag==0:
             final_phone.append({'phone_number':add_number,'type':'undefined'})
        phone_data=[]
        for num in final_phone:
          if len(num["phone_number"])>9:
            phone_data.append(num)

        return phone_data
