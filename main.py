from bs4 import BeautifulSoup
import urllib.request
from hcemail import Email
import pyfiglet
from colorama import Fore


font = pyfiglet.figlet_format('News Extractor and Email Sender', font = 'doh', width=200)
print(font)
print(Fore.MAGENTA + "-- The script automatically scrapes News on the front page of https://news.ycombinator.com/.")
print(Fore.WHITE + "-- It then sends the extracted News to a gmail address with clickable links.\n")

def get_data():
    # res = requests.get("https://news.ycombinator.com/").text
    print(Fore.MAGENTA + "Fetching News headlines...\n")
    res = urllib.request.urlopen("https://news.ycombinator.com/").read()
    soup = BeautifulSoup(res, 'lxml')

    titles = soup.find_all('span', class_='titleline')
    link = soup.select("span[class='titleline'] a")
    authors = soup.find_all('a', class_="hnuser")
    posted_times = soup.find_all('span', class_='age')
    comments = soup.select("span[class='subline'] a:nth-child(6)")
    
    print(Fore.MAGENTA, "News Headlines fetched and sent to email...\n")
    ready = Email()
    return ready.send_email(titles,link, authors, posted_times, comments)

    # for i in range(len(titles)):
    #     data = f"""{{
    #         "Title: ": {titles[i].text},
    #         "Author: ": {authors[i].text},
    #         "Posted: ": {posted_times[i].text},
    #         "Comment: ": {comments[i].text.replace("xa0", " ")}
    #     }}"""
    #     print(data)
    #     print("---"* 30)

    #     return \

if __name__ == "__main__":
    get_data()
    print("JOB DONE!".center(150))

    print(pyfiglet.figlet_format("Thanks,\nAjani", font='doh', width=400))