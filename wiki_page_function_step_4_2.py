import time
import requests
import concurrent.futures

def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exists"
    
    return wiki_page_url + " - " + page_status

if __name__ == "__main__":

    wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]

    print("Running threaded:")
    threaded_start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in wiki_page_urls:
            futures.append(executor.submit(get_wiki_page_existence, wiki_page_url=url))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print("Threaded time:", time.time() - threaded_start)

    """
    Running without threads:
https://en.wikipedia.org/wiki/0 - exists
https://en.wikipedia.org/wiki/1 - exists
https://en.wikipedia.org/wiki/2 - exists
https://en.wikipedia.org/wiki/3 - exists
https://en.wikipedia.org/wiki/4 - exists
https://en.wikipedia.org/wiki/5 - exists
https://en.wikipedia.org/wiki/6 - exists
https://en.wikipedia.org/wiki/7 - exists
https://en.wikipedia.org/wiki/8 - exists
https://en.wikipedia.org/wiki/9 - exists
https://en.wikipedia.org/wiki/10 - exists
https://en.wikipedia.org/wiki/11 - exists
https://en.wikipedia.org/wiki/12 - exists
https://en.wikipedia.org/wiki/13 - exists
https://en.wikipedia.org/wiki/14 - exists
https://en.wikipedia.org/wiki/15 - exists
https://en.wikipedia.org/wiki/16 - exists
https://en.wikipedia.org/wiki/17 - exists
https://en.wikipedia.org/wiki/18 - exists
https://en.wikipedia.org/wiki/19 - exists
https://en.wikipedia.org/wiki/20 - exists
https://en.wikipedia.org/wiki/21 - exists
https://en.wikipedia.org/wiki/22 - exists
https://en.wikipedia.org/wiki/23 - exists
https://en.wikipedia.org/wiki/24 - exists
https://en.wikipedia.org/wiki/25 - exists
https://en.wikipedia.org/wiki/26 - exists
https://en.wikipedia.org/wiki/27 - exists
https://en.wikipedia.org/wiki/28 - exists
https://en.wikipedia.org/wiki/29 - exists
https://en.wikipedia.org/wiki/30 - exists
https://en.wikipedia.org/wiki/31 - exists
https://en.wikipedia.org/wiki/32 - exists
https://en.wikipedia.org/wiki/33 - exists
https://en.wikipedia.org/wiki/34 - exists
https://en.wikipedia.org/wiki/35 - exists
https://en.wikipedia.org/wiki/36 - exists
https://en.wikipedia.org/wiki/37 - exists
https://en.wikipedia.org/wiki/38 - exists
https://en.wikipedia.org/wiki/39 - exists
https://en.wikipedia.org/wiki/40 - exists
https://en.wikipedia.org/wiki/41 - exists
https://en.wikipedia.org/wiki/42 - exists
https://en.wikipedia.org/wiki/43 - exists
https://en.wikipedia.org/wiki/44 - exists
https://en.wikipedia.org/wiki/45 - exists
https://en.wikipedia.org/wiki/46 - exists
https://en.wikipedia.org/wiki/47 - exists
https://en.wikipedia.org/wiki/48 - exists
https://en.wikipedia.org/wiki/49 - exists
Without threads time: 69.08397436141968
(venv) tvt@tvt:/media/tvt/WORK/for-projects/favtuts.com/github/python-threadpoolexecutor-demo$ python wiki_page_function_step_4_2.py 
Running threaded:
https://en.wikipedia.org/wiki/11 - exists
https://en.wikipedia.org/wiki/7 - exists
https://en.wikipedia.org/wiki/9 - exists
https://en.wikipedia.org/wiki/10 - exists
https://en.wikipedia.org/wiki/2 - exists
https://en.wikipedia.org/wiki/1 - exists
https://en.wikipedia.org/wiki/3 - exists
https://en.wikipedia.org/wiki/8 - exists
https://en.wikipedia.org/wiki/5 - exists
https://en.wikipedia.org/wiki/6 - exists
https://en.wikipedia.org/wiki/0 - exists
https://en.wikipedia.org/wiki/4 - exists
https://en.wikipedia.org/wiki/12 - exists
https://en.wikipedia.org/wiki/13 - exists
https://en.wikipedia.org/wiki/14 - exists
https://en.wikipedia.org/wiki/15 - exists
https://en.wikipedia.org/wiki/18 - exists
https://en.wikipedia.org/wiki/16 - exists
https://en.wikipedia.org/wiki/17 - exists
https://en.wikipedia.org/wiki/20 - exists
https://en.wikipedia.org/wiki/19 - exists
https://en.wikipedia.org/wiki/22 - exists
https://en.wikipedia.org/wiki/21 - exists
https://en.wikipedia.org/wiki/23 - exists
https://en.wikipedia.org/wiki/24 - exists
https://en.wikipedia.org/wiki/25 - exists
https://en.wikipedia.org/wiki/26 - exists
https://en.wikipedia.org/wiki/27 - exists
https://en.wikipedia.org/wiki/28 - exists
https://en.wikipedia.org/wiki/29 - exists
https://en.wikipedia.org/wiki/30 - exists
https://en.wikipedia.org/wiki/34 - exists
https://en.wikipedia.org/wiki/33 - exists
https://en.wikipedia.org/wiki/31 - exists
https://en.wikipedia.org/wiki/32 - exists
https://en.wikipedia.org/wiki/35 - exists
https://en.wikipedia.org/wiki/36 - exists
https://en.wikipedia.org/wiki/38 - exists
https://en.wikipedia.org/wiki/39 - exists
https://en.wikipedia.org/wiki/37 - exists
https://en.wikipedia.org/wiki/40 - exists
https://en.wikipedia.org/wiki/41 - exists
https://en.wikipedia.org/wiki/43 - exists
https://en.wikipedia.org/wiki/44 - exists
https://en.wikipedia.org/wiki/46 - exists
https://en.wikipedia.org/wiki/45 - exists
https://en.wikipedia.org/wiki/47 - exists
https://en.wikipedia.org/wiki/42 - exists
https://en.wikipedia.org/wiki/48 - exists
https://en.wikipedia.org/wiki/49 - exists
Threaded time: 51.25000739097595
"""