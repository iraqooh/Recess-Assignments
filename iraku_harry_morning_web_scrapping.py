# Web Scrapping

from bs4 import BeautifulSoup
import requests, time

url = 'https://iraqooh.github.io/irakuharry/'

response = requests.get(url)

html = BeautifulSoup(response.content, 'html.parser')

print(f'Page Heading: {html.find("h1").get_text()}\n')

########################################################################

# Assignment

from bs4 import BeautifulSoup
import requests, time, csv, json, os, re, threading, queue, pandas
import matplotlib.pyplot as plt

class HarrysWebScrapper:
    """
    This class contains functions for providing usage functionality to the Xeno-Cano database query API.

    Modules:
        It depends on built-in Python modules time, csv, json, os and re.

        It also depends on the following modules which may require installation:

            bs4 (Beautiful Soup 4): This is a third-party library used for web scraping and parsing HTML and XML documents.

            threading: This module provides support for multi-threading, allowing you to run multiple threads concurrently.

            queue: This module provides the Queue class for implementing thread-safe queues for inter-thread communication.

            pandas: This is a powerful third-party library used for data manipulation and analysis.

            matplotlib: This is a widely used third-party library for creating visualizations and plots.
    
     Author:
        Iraku Harry, Department of Networks, School of Computing and Informatics Technology,
        College of Computing and Information Sciences,
        Makerere University, Kampala
    """

    """
    The following are private level class fields to store frequently used literals.

    """
    __options = {
        "menu" : ("Search Database", "Database Structure", 
                  "Get Search Tips", "Analyse Data"),
        "save" : (".csv", ".json", "Both"),
        "data" : ("Use Current Data", "Download Another Set", 
                  "Load from My Computer"),
        "eda" : ("View Snapshot of Data", "Description", 
                 "Technical Information", "Frequency Distribution", 
                 "Duplicates", "Empty Cells", "Clean Data and Update File", 
                 "Analyze Feature", "Visualize Data", "Make Feature Predictions (under development)")
    }

    __urls = {
        "search" : "https://xeno-canto.org/help/search",
        "explore" : "https://xeno-canto.org/explore/api",
        "request" : "https://xeno-canto.org/api/2/recordings?query="
    }

    __filename = "database_fields_queries.txt"


    """
    The following class methods are accessors to facilitate access to the private class fields.
    
    """
    @classmethod
    def get_options(cls, option):
        return cls.__options.get(option)
    
    @classmethod
    def get_url(cls, page):
        return cls.__urls.get(page)
    
    @classmethod
    def get_visuals(cls):
        return cls.__visuals
    
    @classmethod
    def get_filename(cls):
        return cls.__filename

    @classmethod
    def animate_loading(cls):
        """
        Displays text animation.

        This method displays a string of five characters with ASCII values between
        160 and 300. It uses the backspace escape character to clear them and
        display updated characters to simulate a character animation.

        Parameters:
            None

        Returns:
            None

        Raises:
            None. The sleep function it uses raises a KeyboardInterrupt.
        """
        try:
            print('>', end='', flush=True)
            for i in range(160, 300):
                time.sleep(0.03)
                print(f'\b\b\b\b\b{chr(i)}{chr(i+1)}{chr(i+2)}{chr(i+3)}'+
                      f'{chr(i+4)}', end='')
            print()
        except KeyboardInterrupt:
            print("\nAnimation stopped.")
    
    @classmethod
    def display_menu(cls, options, title, exit_option=None):
        """
        Displays the list of options 'options' and an optional exit option 'exit_option',
        with a 'title'.

        """
        print(title)
        for number in range(len(options)):
            print(f'{number + 1}. {options[number]}')
        if exit_option: print(f'{len(options) + 1}. {exit_option}')

    @classmethod
    def get_user_input(cls, prompt='Enter option: ', data_type='string', 
                       range_input=None):
        """
        Provides a command line interface for getting user input, 
        performs local validation of the input and returns the input if
        validated or None. The 'range_input' specifies the allowed range
        of numerical options, when 'data_type' is set to 'int'.

        """
        user_input = input(prompt).strip()
        if user_input == '': raise ValueError(
                'Input cannot be whitespace. Please try again.')
        if data_type == 'string': return user_input
        elif data_type == 'int':
            if not user_input.isnumeric():
                print('Your input must be numeric.')
                return None
            user_input = int(user_input)
            if not user_input in range_input: raise ValueError(
                    f'Your input must be in the range {range_input.start}' + 
                    f' to {range_input.stop - 1}')
            return user_input
    
    @classmethod
    def make_request(cls, url, success_code, output='json'):
        """
        Connects to the internet API specified by 'url' and upon success,
        it preprocesses the Response into the data type specified by 'output'
        and returns it.

        It raises HTTPError in case the connection fails or 
        JSONDecodeError in case the Response cannot be converted to JSON.

        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            if response.status_code != success_code:
                raise requests.exceptions.HTTPError()
            if output == 'json':
                data = response.json()
                if not data: 
                    raise requests.exceptions.JSONDecodeError(
                        'JSON decode error.')
                return data
            elif output == 'soup':
                return BeautifulSoup(response.content, 'html.parser')
            elif output == 'raw':
                return response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while making the request: {e}")

    @classmethod
    def fetch_data(cls, self, url):
        """
        Initiates request to 'url' for data and uses multithreading to
        run the @make_request and @animate_loading methods. The data 
        returned by @make_request is extracted and stored in the 'self.data'
        instance field.

        """
        query = HarrysWebScrapper.get_user_input('Enter search query: ')
        def worker(param1, param2, param3, result_queue):
            print(f'Please wait while the data is fetched from the ' +
                  'internet.....', end='')
            result = cls.make_request(param1, param2, param3)
            result_queue.put(result)
        result_queue, threads = queue.Queue(), []
        threads.append(threading.Thread(target=worker, args=(
            url + query, 200, 'json', result_queue)))
        threads.append(threading.Thread(
            target=cls.animate_loading,
            args=())
        )
        threads[0].start()
        threads[1].start()
        threads[0].join()
        threads[1].join()
        data = result_queue.get()
        if data == None: 
            raise requests.exceptions.ContentDecodingError(
                'Failed to retrieve data. Check the url or internet connection.')
        self.data = data.get('recordings', [])
    
    @classmethod
    def save_file(cls, self):
        """
        Enquires if the user wants to save the data extracted by @fetch_data.
        If so, it requests the user to specify the file type and filenames
        before saving it locally.

        """
        status = False
        choice = cls.get_user_input('Would you like to save the data?' +
                                    ' Y/N ')
        print()
        if choice.lower() == 'y':
            cls.display_menu(cls.__options.get("save"), 'File types')
            filetype = cls.get_user_input('Select file type: ', 'int', 
                                          range(1, 4))
            filename = cls.get_user_input('Enter filename (without ' + 
                                          'extension): ')
            print()
            if re.search(r'.*(?=[\/:*?<>|]).*', filename): 
                raise ValueError('Error: Filenames cannot have a ' +
                                 '\\/:?<> or | character.')
            try:
                if filetype == 1 or filetype == 3:
                    with open(filename + cls.__options.get("save")[0], 
                              "w", newline="", encoding='utf-8') as file:
                        csvstream = csv.DictWriter(file, fieldnames=list(
                            self.data[0].keys()))
                        csvstream.writeheader()
                        csvstream.writerows(self.data)
                        status = True
                        print(f'File saved as {filename}.csv')
                        self.session_filename = filename + ".csv"
                if filetype == 2 or filetype == 3:
                    with open(filename + cls.__options.get("save")[1], 
                              "w", encoding='utf-8') as file:
                        json.dump(self.data, file, indent=2, 
                                  ensure_ascii=False)
                        status = True
                        print(f'File saved as {filename}.json')
                        self.session_filename = filename + ".json"
            except OSError as e:
                status = e
        return status

    def __init__(self):
        """
        Initializes the application with several instance variables.

        """
        self.data, self.headers, self.descriptions = [], [], []
        self.queries, self.advanced = [], []
        self.session_filename = None
        self.df = None

    def init(self):
        """
        Checks if application data is available in the working directory
        and loads it into the several available instance variables. If not
        found, it calls @fetch_all_fields, @fetch_search_queries to 
        make requests to the remote server. It then calls @save_all_data
        to store the updated instance variables to the working directory.

        """
        if os.path.exists(HarrysWebScrapper.__filename):
            print('Loading data from local storage...\n')
            try:
                with open(HarrysWebScrapper.__filename, "r") as file:
                    items = file.readlines()
                    self.headers = items[items.index('headers\n') + 
                                         1].rstrip('<=>\n').split("<=>")
                    self.descriptions = items[items.index(
                        'descriptions\n') + 1].rstrip('<=>\n').split(
                        "<=>") + items[items.index('descriptions\n') +
                                        2].rstrip('<=>').split("<=>")
                    self.descriptions = self.descriptions[:-1]
                    self.queries = items[items.index('queries\n') + 
                                         1].rstrip('<=>\n').split("<=>")
                    self.advanced = items[items.index(
                        'advanced\n') + 1].rstrip('<=>\n').split("<=>")
            except OSError as e:
                return e
        else:
            self.fetch_all_fields()
            self.fetch_search_queries()
            self.save_all_data()

    def fetch_all_fields(self):
        """
        Calls @make_request to fetch database information from the url referenced
        by the 'explore' key of the __urls class field.

        """
        soup = HarrysWebScrapper.make_request(HarrysWebScrapper.__urls.get("explore"), 200, 'soup')
        items = list(filter(
            lambda x: str(x).startswith('<p>The following'), 
            soup.find_all('p')))[0].find_next_sibling('ul').findChildren('li')
        for item in items:
            item = item.get_text()
            if item.startswith(' '):
                trunc = self.descriptions.pop() + item
                self.descriptions.append(trunc)
            else: self.descriptions.append(item)
        if not self.data:
            HarrysWebScrapper.fetch_data(self, 
                                         HarrysWebScrapper.__urls.get("request"))
        self.headers = list(self.data[0].keys())

    def fetch_search_queries(self):
        """
        Calls @make_request to fetch database search query categories from the url
        referenced by the 'search' key of the __urls class field.

        """
        soup = HarrysWebScrapper.make_request(
            HarrysWebScrapper.__urls.get("search"), 200, 'soup')
        h2_elements = soup.find_all('h2')[1:]
        for heading in h2_elements:
            self.queries.append(heading.get_text())
        h3_elements = soup.find_all('h3')
        for heading in h3_elements:
            self.advanced.append(heading.get_text())

    def save_technical(self, data, mode, tag):
        """
        Saves 'data' to the application file. The 'mode' takes the
        'w' value for column headers and 'a' for the rest of the data.
        It is thus called four times by the @save_all_data method.

        """
        with open(HarrysWebScrapper.__filename, mode, 
                  encoding='utf-8') as file:
            file.write(tag + '\n')
            for item in data:
                file.write(item + '<=>')
            file.write('\n')
    
    def save_all_data(self):
        """
        Calls the @save_technical method for each of the application data.

        """
        self.save_technical(self.headers, "w", "headers")
        self.save_technical(self.descriptions, "a", "descriptions")
        self.save_technical(self.queries, "a", "queries")
        self.save_technical(self.advanced, "a", "advanced")
        print('Data saved to local storage.')

    def filter_scrapped_content(self, elements, query):
        """
        Scraps content from the list of HTML elements in 'elements' by
        filtering the elements based on the innerHTML provided by 'query'.

        It returns the scrapped content to the calling context.

        """
        filter_elements = list(filter(lambda element : 
                                      query in str(element), elements))
        if filter_elements:
            target = filter_elements[0]
            text = ''
            siblings = target.find_next_siblings()
            for sibling in siblings:
                if not str(sibling).startswith(
                    '<h2>') and not str(sibling).startswith('<h3>'):
                    text += sibling.get_text().lstrip()
                else: break
            return '\n' + query + '\n' + text + '\n'
        return None
    
    def explore_search_queries(self):
        """
        Provides an command line interface for the user to browse the 
        syntaxes of search queries for the Xeno-Canto API.

        """
        while True:
            HarrysWebScrapper.display_menu(self.queries, "Search Queries",
                                            "Back to Main Menu")
            choice = HarrysWebScrapper.get_user_input(
                'Select query type: ', 'int', range(1, len(self.queries) 
                                                    + 2))
            if choice == len(self.queries) + 1:
                print()
                break
            if choice == None:
                print()
                continue
            soup = HarrysWebScrapper.make_request(
                HarrysWebScrapper.__urls.get("search"), 200, 'soup')
            elements = soup.find_all('h2') + soup.find_all('h3')
            if choice == 1 or choice == 3: 
                content = self.filter_scrapped_content(
                    elements, self.queries[choice - 1])
                print(content + '\n')
            elif choice == 2:
                while True:
                    HarrysWebScrapper.display_menu(self.advanced, 
                                                   "Advanced Queries", 
                                                   "Back to Search Queries")
                    choice = HarrysWebScrapper.get_user_input(
                        'Select advanced search query: ', 
                        'int', range(1, len(self.advanced) + 2)
                    )
                    if choice == len(self.advanced) + 1: break
                    content = self.filter_scrapped_content(
                        elements, self.advanced[choice - 1])
                    print(content)
    
    def select_dataset(self):
        """
        Enables the user to select a dataset for exploratory data analysis and
        other data science activities.

        """
        while True:
            HarrysWebScrapper.display_menu(HarrysWebScrapper.__options.get("data"), '\nData Sources')
            source = HarrysWebScrapper.get_user_input('Select the source for dataset: ', 'int', range(1, len(HarrysWebScrapper.__options.get("data")) + 1))
            if source == None: continue
            if source == 1:
                if not self.session_filename:
                    print('You don\'t have any datasets. Download and try again.')
                    continue
                if self.session_filename.endswith('.csv'):
                    self.df = pandas.read_csv(self.session_filename)
                elif self.session_filename.endswith('.json'):
                    self.df = pandas.read_json(self.session_filename)
            elif source == 2:
                HarrysWebScrapper.fetch_data(
                    self, HarrysWebScrapper.__urls.get("request"))
                self.df = pandas.DataFrame(self.data)
                filename = HarrysWebScrapper.get_user_input(
                    'Enter filename (CSV): ')
                self.session_filename = filename
            elif source == 3:
                filename = HarrysWebScrapper.get_user_input(
                    'Enter filename: ')
                try:
                    if filename.lower().endswith('.csv'):
                        self.df = pandas.read_csv(filename)
                    elif filename.lower().endswith(('.xls', '.xlsx')):
                        self.df = pandas.read_excel(filename)
                    elif filename.lower().endswith('.json'):
                        self.df = pandas.read_json(filename)
                    elif filename.lower().endswith(('.html', 'htm')):
                        self.df = pandas.read_html(filename)
                    else:
                        print('Unsupported file format.')
                        continue
                except FileNotFoundError as e:
                    print(e)
                    continue
                self.session_filename = filename
                self.headers = list(self.df.columns)
            break

    def clean_data(self):
        """
        Removes empty cells (with NaN values) and duplicate entries from the data.

        Disclaimer: This version does not enable the user to customize the cleaning process
        nor does it fix wrong data types and formats (it assumes they don't exist).

        """
        if self.df.duplicated().sum() > 0:
            self.df.drop_duplicates(inplace=True)
            print('Duplicates found and removed.')
        else: print('No duplicates found!')
        if self.df.isna().any().any():
            if not self.headers: self.init()
            for field in self.headers:
                if self.df[field].isna().sum() > 0:
                    if self.df[field].isna().sum() == len(self.df):
                        self.df.drop(columns=field, inplace=True)
                        self.headers.remove(field)
                        print(f'...empty cells dropped from {field}...')
                    else:
                        if str(self.df[field].dtype) in ['float64', 
                                                         'int64']:
                            self.df.loc[self.df[field].isna(), 
                                        field] = self.df[field].mean()
                            print(f'...empty cells in {field} have been' +
                                  ' set to the mean value...')
                        else:
                            self.df.loc[self.df[field].isna(), 
                                        field] = self.df[field].describe().top
                            print(f'...empty cells in {field} have been'+
                                  ' set to the most frequent value...')
        else: print('No empty cells found!')
        self.df.to_csv(self.session_filename, header=self.headers, 
                       mode="w", encoding='utf-8')
        print(f'Data successfully cleaned and saved to'+
              ' {self.session_filename}')

    def run_app(self):
        """
        Launches the main user interface of the application.

        """
        try:
            while True:
                HarrysWebScrapper.display_menu(
                    HarrysWebScrapper.__options.get("menu"), 
                    '\nMenu', 'Exit Application'
                )
                option = self.get_user_input(
                    'Select Functionality: ', 'int', 
                    range(1, len(HarrysWebScrapper.__options.get("menu")) + 2))
                if option == 1:
                    HarrysWebScrapper.fetch_data(
                        self, HarrysWebScrapper.__urls.get("request"))
                    if self.data: HarrysWebScrapper.save_file(self)
                elif option == 2:
                    self.init()
                    for col in self.descriptions:
                        print(col)
                elif option == 3:
                    self.init()
                    self.explore_search_queries()
                elif option == 4:
                    self.select_dataset()
                    while True:
                        try:
                            HarrysWebScrapper.display_menu(
                                HarrysWebScrapper.__options.get("eda"), 
                                '\nExploratory Data Analysis', 
                                'Back to Main Menu')
                            choice = HarrysWebScrapper.get_user_input(
                                'Select feature: ', 'int', 
                                range(1, len(HarrysWebScrapper.__options.get("eda")) + 2))
                            if choice == len(HarrysWebScrapper.__options.get("eda")) + 1: break
                            elif choice == 1:
                                print(self.df.head())
                            elif choice == 2:
                                print(self.df.describe())
                            elif choice == 3:
                                print(self.df.info())
                            elif choice == 4:
                                if not self.headers: self.init()
                                feature = HarrysWebScrapper.get_user_input('Enter feature: ')
                                if feature not in self.headers:
                                    print('The column name you provided is invalid. Check and try again.')
                                    continue
                                print(self.df[feature].value_counts())
                            elif choice == 5:
                                dup = self.df.duplicated().sum()
                                if dup > 0:
                                    print(f'There are {dup} duplicate entries in the data.')
                                else: print('Your data has no duplicate entries.')
                            elif choice == 6:
                                empty = self.df[self.df.isnull().any(axis=1)]
                                if empty.shape[0] > 0: print(empty)
                                else: print('Your data has no empty cells.')
                            elif choice == 7:
                                self.clean_data()
                            elif choice == 8:
                                if not self.headers: self.init()
                                choice = HarrysWebScrapper.get_user_input('Enter feature: ')
                                if choice not in self.headers:
                                    print('The column name you provided is invalid. Check and try again.')
                                    continue
                                print(self.df[choice].describe())
                            elif choice == 9:
                                numeric_columns = self.df.select_dtypes(include=['int64', 'float64']).columns
                                df_num = self.df.drop(columns=self.df.columns.difference(numeric_columns))
                                while True:
                                    HarrysWebScrapper.display_menu(
                                        numeric_columns, 
                                        '\nFeature Visualizations', 
                                        'Back to Data Analysis')
                                    feature = HarrysWebScrapper.get_user_input(
                                        'Select feature: ', 'int', 
                                        range(1, len(numeric_columns) + 2))
                                    if feature == len(numeric_columns) + 1: break
                                    else:
                                        plt.figure(figsize=(8, 6))
                                        plt.title(f'Density Plot for {numeric_columns[feature - 1]}')
                                        plt.xlabel('Value')
                                        plt.ylabel('Density')
                                        plt.hist(
                                            df_num[numeric_columns[feature - 1]], 
                                            density=True, bins=30, alpha=0.6, 
                                            color='blue', edgecolor='black'
                                        )
                                        plt.show()
                            elif choice == 10:
                                pass
                        except TypeError as e:
                            print('The data format cannot be manipulated.')
                            continue
                elif option == 5:
                    print('Good Bye...')
                    break
        except requests.exceptions.HTTPError as e:
            print(e)
        except requests.exceptions.ConnectionError as e:
            print('Your internet is disconnected.')

if __name__ == '__main__':
        print('Welcome to the Xeno-Cano Bird Database Explorer by Iraku Harry')
        app = HarrysWebScrapper()
        try:
            app.run_app()
        except requests.exceptions.ConnectionError as e:
            print(e)
        except requests.exceptions.HTTPError as e:
            print(e)
        except OSError as e:
            print(e)
        except TypeError as e:
            print(e)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt as e:
            print(e)