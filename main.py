from bs4 import BeautifulSoup as bs 
import requests as rq
import time


def find_jobs():
    html_text = rq.get('https://www.adzuna.co.za/kwazulu-natal/junior-developer').text

    soup = bs(html_text, 'lxml')
    jobs = soup.find_all('div', class_= "a" )

    for index, job in enumerate(jobs):
            with open(f'job-posts/{index}.txt', 'w') as f:
                tit = job.find('h2').text
                comp = job.find('p', class_="as").text
                info = job.find('span', class_="at_tr").text
                link = job.h2.a['href']



                f.write(f"Company Name: {comp.strip()}")
                f.write('\n')
                f.write(f"Position: {tit.strip()}")
                f.write('\n')
                f.write(f"More Info: {info.strip()}")
                f.write('\n')
                f.write(f"Link: {link}")
                f.write('\n')
                print(f"Job Posts saved as: {index}")
                

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes to scrape again...')
        time.sleep(time_wait * 60)


