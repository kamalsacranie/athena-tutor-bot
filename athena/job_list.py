from typing import Any
from bs4 import BeautifulSoup
from datetime import datetime
from bs4.element import ResultSet, Tag


class JobSoup(BeautifulSoup):
    def __init__(self, source):
        self.job_cards = self._get_job_list(source)
        self.job_dict_list = self._create_job_dict()

    def _get_job_list(self, source: str) -> ResultSet[Any]:
        # Extracting all the job cards form our source
        job_screen_soup = BeautifulSoup(source, "html.parser")
        job_cards = job_screen_soup.find_all(
            "div", {"class": "card card-custom"}
        )
        return job_cards

    def _create_job_dict(self) -> list[dict[str, str]]:
        job_dict_list: list[dict[str, Any]] = list()

        # The following functions just get the relevant info
        def get_title(card: Tag) -> tuple[str, str]:
            container = card.findChildren("h3")[0]
            anchor = container.findChildren("a")[0]
            title = anchor.getText().replace("\n", "")
            link = anchor.get("href").replace("\n", "")
            return title.strip(), link.strip()

        def get_label(card: Tag, text: str) -> str:
            lable = card.findChildren("label", text=text)[0]
            rate = lable.findNext("div")
            return rate.getText().replace("\n", "").strip()

        def get_synopsis(card, element_class) -> str:
            container = card.findChildren("div", {"class": element_class})[0]
            synopsis_tag = container.findChildren("p")[0]
            return synopsis_tag.getText().replace("\n", "").strip()

        # Populates our job list
        for card in self.job_cards:
            print(type(card))
            title, link = get_title(card)
            job_dict = {
                "title": title,
                "link": link,
                "rate": get_label(card, "Pay Rate:"),
                "created_at": datetime.strptime(
                    get_label(card, "Date Created:"), "%d/%m/%Y"
                ),
                "synopsis": get_synopsis(
                    card, "detail-long-item px-2 render-md"
                ),
            }

            job_dict_list.append(job_dict)

        return job_dict_list
