import requests
import re
from bs4 import BeautifulSoup

class DoveletConfig():
  def __init__(self):
    # dovlet url
    self.BASE_URL = 'http://119.201.123.184'

    # user url
    self.LOGIN_URL = 'login.php'
    self.PROFILE_URL = 'status.php'

    # problem url
    self.PROBLEM_TEXT_URL = ''
    self.PROBLEM_SUBMIT_URL = '30stair/post.php'

    # stair url
    self.STAIR_URL = '30stair/index.php'

    self.STAIR_TABLES_TAG = 'table'
    self.STAIR_TABLES_ATTRS = {'width':'900'}
    
    self.STAIR_TAG = 'tr'
    self.STAIR_ATTRS = {'bgcolor':'white'}

    self.CORRECT_CHECK = '/img/check1.gif'
    self.IS_DOCUMENT = '/img/document.gif'
    
class Dovelet():
  def __init__(self):
    self.config = DoveletConfig()
  
  def make_url(self, url, query):
    url = self.config.BASE_URL + '/' + url

    # add query
    keys = query.keys()
    if keys:
      url += '?'
      for key in keys:
        url += (str(key)+ '=' + str(query[key]) + '&')
      
      # remove &
      url = url[:-1]
    
    return url
    
  def login(self, id, passwd):
    """
      :param str id: User Id
      :param str passwd: User password

      :return: (login success, cookies)
    """
    url = self.make_url(self.config.LOGIN_URL, {})
    
    r = requests.post(url, data = {
      'id': id,
      'passwd': passwd
    })
  
    # cookiejar to dict
    cookies = dict(zip(r.cookies.keys(), r.cookies.values()))
    success = cookies != {}

    return success, cookies

  def profile(self, cookies):
    url = self.make_url(self.config.PROFILE_URL, {})

    r = requests.get(url, cookies=cookies)

    # TODO: parse html
    html = r.text
    
    return html
  
  def problem_text(self, title, cookies):
    # set prblem text url and make request
    self.config.PROBLEM_TEXT_URL = ('30stair/' + title + '/' + title + '.php')
    url = self.make_url(self.config.PROBLEM_TEXT_URL, {
      'pname': title
    })
    self.config.PROBLEM_TEXT_URL = ''

    r = requests.get(url, cookies=cookies)

    # TODO: parse html
    html = r.text
    
    return html

  def problem_submit(self, title, language, source, cookies):
    url = self.make_url(self.config.PROBLEM_SUBMIT_URL, {
      'pname': title
    })

    r = requests.post(url, data={
      'select': language,
      'src': source
    }, cookies=cookies)

    # TODO: parse html
    html = r.text
    
    return html

  def stair(self, stair_num, cookies):
    # request content
    # returns all stair if other than 3n-2 is given
    url = self.make_url(self.config.STAIR_URL, {
      'select': 2
    })
    
    r = requests.get(url, cookies=cookies)

    soup = BeautifulSoup(r.text, "html.parser")
  
    # idx >= 1 && idx <=30
    idx = max(min(stair_num-1, 29), 0)
    stair_table = soup.find_all(self.config.STAIR_TABLES_TAG, attrs=self.config.STAIR_TABLES_ATTRS)[idx]


    stair_rows = stair_table.find_all(self.config.STAIR_TAG, attrs=self.config.STAIR_ATTRS, recursive=False)[1:]

    # parse problems
    stair = []
    for stair_row in stair_rows:
      row = stair_row.find_all('td', recursive=False)
      
      if row[0].a:
        solved = False if row[0].a.img['src'] != self.config.CORRECT_CHECK else True
      else:
        solved = None
      
      if row[0].img:
        is_document = (row[0].img['src'] == self.config.IS_DOCUMENT)
      else:
        is_document = False

      title = re.sub('\n*\s', '', row[1].text)
      full_link = self.config.BASE_URL+row[1].a['href']
      correct_rate = re.sub('\n*\s', '', row[2].text)
      published_date = re.sub('\n*\s', '', row[4].text)

      problem = { 'is_document': is_document, 'solved': solved, 'title': title, 'full_link': full_link, 'correct_rate': correct_rate, 'published_date': published_date }
      stair.append(problem)

    return stair