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
    #url = "https://en.wikipedia.org/wiki/Ocean"
    #print(get_wiki_page_existence(wiki_page_url=url))

    wiki_page_urls = [
        "https://en.wikipedia.org/wiki/Ocean",
        "https://en.wikipedia.org/wiki/Island",
        "https://en.wikipedia.org/wiki/this_page_does_not_exist",
        "https://en.wikipedia.org/wiki/Shark",
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in wiki_page_urls:
            futures.append(
                executor.submit(
                    get_wiki_page_existence, 
                    wiki_page_url=url                  
                )
            )
        for future in concurrent.futures.as_completed(futures):            
            print(future.result())            