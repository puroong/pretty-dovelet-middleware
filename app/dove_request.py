import requests
import re
from bs4 import BeautifulSoup
from app import app

class DoveRequest:
    def is_logged_in(self, cookies):
        cookies = set(cookies.keys())
        required_cookies = set(['PHPSESSID', 'member_id', 'member_sid', 'member_passwd'])

        if len(cookies ^ required_cookies) is 0:
            return True
        else:
            return False

    def login(self, id, passwd):
        r = requests.post(app.config['DOVELET_HOST']+'/login.php', data={'id': id, 'passwd': passwd})
        cookies = dict(zip(r.cookies.keys(), r.cookies.values()))

        if self.is_logged_in(cookies):
            return cookies
        else:
            return None

    #no auth
    def get_stair(self, stair_num):
        # TODO: cookies = # pass cookie
        # select numbers are 3n-2, but if other than these numbers is given, all problems are returned
        r = request.get(app.config['DOVELET_HOST']+'/30stair/index.php?select=2', cookies=cookies)

        soup = BeautifulSoup(r.text, "html.parser")

        stair_tables_tag = soup.find_all('table', attrs={'width': '900'})
        stair_table_tag = stair_tables_tag [stair_num-1]

        stair_tags = stair_table_tag.find_all('tr', attrs={'bgcolor': 'white'}, recursive=False)[1:]

        stair = []
        for stair_tag in stair_tags:
            row = stair_tag.find_all('td', recursive=False)

            solved = False if row[0].a is None else True
            title = re.sub('\n*\s', '', row[1].text)
            full_link = app.config['DOVELET_HOST']+row[1].a['href']
            correct_rate = re.sub('\n*\s', '', row[2].text)
            published_date = re.sub('\n*\s', '', row[4].text)

            problem = { 'solved': solved, 'title': title, 'full_link': full_link, 'correct_rate': correct_rate, 'published_date': published_date }
            stair.append(problem)

        return stair

    #no auth
    def get_problem(self, full_link):
        # TODO: cookies = # pass cookies
        r = requests.get(full_link)

        text = r.text.split('<hr>')[0]
        text += '</body>'

        soup = BeautifulSoup(text, "html.parser")

        return str(soup.body.prettify())

    #auth required
    def submit(self, title, language, src):
        # TODO: cookies =  pass cookies
        if self.is_logged_in(cookies):
            eng_title = title.split('/')[1]
            r = self.login_session.post(app.config['DOVELET_HOST']+'/30stair/post.php?pname='+eng_title, data={'select': language, 'src': src})

            text = re.sub(r'<div align=right>(.*)</div>', '', r.text, flags=re.DOTALL)
            soup = BeautifulSoup(text, "html.parser")

            return str(soup.body.prettify())
        # TODO: raise noautherror
        else:
            pass
    #auth required
    def profile(self):
        pass
