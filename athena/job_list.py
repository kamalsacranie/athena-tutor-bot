from bs4 import BeautifulSoup
from datetime import datetime


class JobSoup(BeautifulSoup):

    def __init__(self, source):
        self.job_cards = self._get_job_list(source)
        self.job_dict_list = self._create_job_dict()

    def _get_job_list(self, source: str):
        job_screen_soup = BeautifulSoup(source, 'html.parser')
        job_cards = job_screen_soup.find_all('div', class_='card card-custom')
        return job_cards
    
    def _create_job_dict(self):
        
        job_dict_list = list()

        def get_title(card: str):
            container = card.findChildren('h3')[0]
            anchor = container.findChildren('a')[0]
            title = anchor.getText().replace('\n', '')
            link = anchor.get('href').replace('\n', '')
            return title.strip(), link.strip()

        def get_label(card, text: str):
            lable = card.findChildren('label', text=text)[0]
            rate = lable.findNext('div')
            return rate.getText().replace('\n', '').strip()
        
        def get_synopsis(card, class_):
            container = card.findChildren(
                'div',
                {'class': class_}
            )[0]
            synopsis_tag = container.findChildren('p')[0]
            return synopsis_tag.getText().replace('\n', '').strip()

        for card in self.job_cards:
            title, link = get_title(card)
            job_dict = {
                'title': title,
                'link': link,
                'rate': get_label(card, 'Pay Rate:'),
                'date-created': datetime.strptime(
                    get_label(card, 'Date Created:'), '%d/%m/%Y'
                ),
                'synopsis': get_synopsis(card, 'detail-long-item px-2 render-md'),
            }

            job_dict_list.append(job_dict)
        
        return job_dict_list
        
