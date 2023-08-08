from bs4 import BeautifulSoup
import requests

def scraper(count):
    url = 'https://www.topjobs.lk/applicant/vacancybyfunctionalarea.jsp'

    html_content = requests.get(url)

    soup_content = BeautifulSoup(html_content.text, 'lxml')

    job_body = soup_content.find_all('tr')

    available_jobs = []
    for job in job_body:
        jobs = job.find_all('h2')
        if jobs != []:
            available_jobs.append(jobs[0].find('span').text)

    return (available_jobs[:count])

    # # Writes to a Text File
    # with open('Jobs Available.txt', 'w') as file_2_save:
    #     for available_job in available_jobs:
    #         file_2_save.write(available_job + "\n")