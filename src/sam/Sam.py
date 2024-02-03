import requests
from sam.utils import ConstructParams


class Scraper:
    """
    A class for interacting with the sam.gov API, facilitating search operations, retrieval of exclusion details, resources, results, and downloading resource files.

    For full documentation of this class, visit "https://github.com/Diego-Arrechea/sam-scraper".
    """

    def __init__(self):
        self.headers = {
            "authority": "sam.gov",
            "accept": "application/json, text/plain, */*",
            "accept-language": "es-ES,es;q=0.7",
            "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

    def search(self, sort="relevance", status="active", limit="9999999999"):
        """
        Performs a search on the sam.gov API using specified criteria.

        Parameters:
        - sort (str): Sorting criterion for the results ('relevance' by default).
        - status (str): Status of the results to search ('active' by default).
        - limit (str): Limit on the number of results to return ('9999999999' by default to attempt returning all possible results).

        Returns:
        - dict: A dictionary containing the search results.

        For full documentation of this method, visit "https://github.com/Diego-Arrechea/sam-scraper".
        """

        params = {
            "random": ConstructParams().time(),
            "index": "ei",
            "page": "0",
            "sort": ConstructParams().sort(sort),
            "size": ConstructParams().limit(limit),
            "mode": "search",
            "responseType": "json",
            "q": "construction",
            "qMode": "ALL",
            "is_active": ConstructParams().status(status),
        }

        response = requests.get(
            "https://sam.gov/api/prod/sgs/v1/search/",
            params=params,
            headers=self.headers,
        )
        return response.json()["_embedded"]["results"]

    def get_details(self, pirKey=None, pirValue=None, id=None):
        """
        Retrieves combined details of a record, including results and resources, based on ID or PIR criteria.

        Parameters:
        - pirKey (str): PIR key for exclusion search (optional).
        - pirValue (str): PIR value for exclusion search (optional).
        - id (str): ID of the record to get details (optional).

        Returns:
        - dict: A dictionary with combined details of the record.

        For full documentation of this method, visit "https://github.com/Diego-Arrechea/sam-scraper".
        """

        data = {}

        if id:
            data["result"] = self.__get_result(id)
            try:
                data["resources"] = self.__get_resources(id)
            except:
                data["resources"] = None

        if pirKey and pirValue:
            data["exclusion"] = self.__get_exclusion(pirKey, pirValue)

        return data

    def __get_exclusion(self, pirKey, pirValue):
        """
        Retrieves exclusion details based on specified PIR criteria.

        Parameters:
        - pirKey (str): PIR key for the search.
        - pirValue (str): Corresponding PIR value to the key.

        Returns:
        - dict: A dictionary containing the exclusion details.

        For full documentation of this method, visit "https://github.com/Diego-Arrechea/sam-scraper".
        """

        params = {
            "random": ConstructParams().time(),
            "pirKey": pirKey,
            "pirValue": pirValue,
        }

        response = requests.get(
            "https://sam.gov/api/prod/view-details/v2/api/exclusion",
            params=params,
            headers=self.headers,
        )
        return response.json()

    def __get_resources(self, main_id):
        """
        Retrieves resources associated with a main opportunity ID.

        Parameters:
        - main_id (str): Main ID of the opportunity for which to retrieve resources.

        Returns:
        - list: A list of resources associated with the opportunity.

        For full documentation of this method, visit "https://github.com/Diego-Arrechea/sam-scraper".
        """

        response = requests.get(
            "https://sam.gov/api/prod/opps/v3/opportunities/{main_id}/resources".format(
                main_id=main_id
            ),
            headers=self.headers,
        )
        return response.json()["_embedded"]["opportunityAttachmentList"][0][
            "attachments"
        ]

    def __get_result(self, main_id):
        """
        Retrieves the result of an opportunity based on its main ID.

        Parameters:
        - main_id (str): Main ID of the opportunity.

        Returns:
        - dict: A dictionary containing the result of the opportunity.

        For full documentation of this method, visit "https://github.com/Diego-Arrechea/sam-scraper".
        """

        response = requests.get(
            "https://sam.gov/api/prod/opps/v2/opportunities/{main_id}".format(
                main_id=main_id
            ),
            headers=self.headers,
        )
        return response.json()

    def download_resource(ID, name_file):
        """
        Downloads a resource file based on a specific ID and saves the file with the provided name.

        Parameters:
        - ID (str): ID of the resource file to download.
        - name_file (str): Name of the file under which to save the downloaded resource.

        Returns:
        - str: Message indicating the success of the download or an error message.

        For full documentation of this method, visit "https://github.com/Diego-Arrechea/sam-scraper".
        """

        respuesta = requests.get(
            "https://sam.gov/api/prod/opps/v3/opportunities/resources/files/{ID}/download?&token=".format(
                ID=ID
            )
        )
        if respuesta.status_code == 200:
            with open(name_file, "wb") as archivo:
                archivo.write(respuesta.content)
