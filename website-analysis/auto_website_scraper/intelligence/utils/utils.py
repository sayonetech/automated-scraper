import re,psycopg2
from urlparse import urlparse
from bs4 import BeautifulSoup




def url_validation(image_url):
    """
    Different cases of image url validation
    :param url:  String
    :return: Boolean
    """
    FLAG = True

    #CASE 1
    if 'blank' in image_url:
        FLAG = False

    # CASE 2   # future

    return FLAG

def apply_schema_to_url(url):
    """
    Applies schema to urls fed.
    :param url: String
    :return: String
    """
    if not urlparse(url).scheme:
        #Applied default scheme if no scheme found
        return urlparse(url)._replace(scheme='http').geturl()
    return url

def remove_urls(next_urls):
    """
    Remove unwanted urls from url list.
    :param next_urls:
    :return: url_list
    """
    url_list = []
    unwanted = ['/','#1','#2','#3','#4','#5','#','.','./','../','..','#c','#a','#k','#j','#h','#o','#n','#m','#l','#b','#g','#f','#e','#d','#z','#y','#x']
    next_urls = list((set(next_urls).difference(unwanted)))
    for url in next_urls:
        pattern = re.compile('pdf|jpg|png|gif|pdf|jpeg|JPG|PNG|GIF|PDF|JPEG|PDF|tel:|javascript|lxml.etree|http://maps.google.de|https://www.facebook.com|mailto:|https://www.linkedin.com|https://plus.google.com|https://twitter.com|/dachs|wordpress')
        if pattern.match(url):
            next_urls.remove(url)
    for url in next_urls:
        replace_pattern1 = re.compile('./')
        if replace_pattern1.match(url):
            url = url.replace('./','')
            url_list.append(url)
        replace_pattern2 = re.compile('../')
        if replace_pattern2.match(url):
            url = url.replace('../','')
            url_list.append(url)
        url_list.append(url)
    return url_list

def make_up_url(url, domain):
    """
    Make up url in to format.
    :param url: String
    :return: String
    """
    url_object = urlparse(url)
    if (not(url_object.scheme) or not(url_object.netloc)) and url_object.path:
        if re.search('(/.+?/)', url_object.path):
            return domain+url_object.path
        elif '.' in  url_object.path:
            return domain+'/'+url_object.path
        else:
            return domain+url_object.path
    return url

def parse_site_variable(url):
    """
    Parse site variable for each site.l
    :param url: String
    :return: String
    """
    variable = re.search(r'\.(.+?)\.', url)
    name = None
    if variable:
        name = variable.group(1)
        variable = variable.group(1).replace('-','_')
    else:
        variable = re.search(r'\/\/(.+?)\.', url)
        if variable:
            name = variable.group(1)
            variable = variable.group(1).replace('-','_')

    return variable, name




def get_text(page_source):
     """
     :param page_source:
     :return: the Text content in the page source
     """
     soup = BeautifulSoup(page_source, 'html.parser')
     texts = soup.findAll(text=True)
     [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
     visible_text = soup.getText()
     return visible_text