"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup
import re

def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html,features="html.parser")
        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})
        total_male_number = 0
        total_female_number = 0
        # to record the position of the  boy and the girl
        g = 0
        w = 0
        i = 0
        # every student info
        for tag in tags:
            number_info = tag.tbody.text.split()
            for line in number_info:
                # boy and girl number index
                w = 2 + 5 * i
                g = 4 + 5 * i
                if number_info[w].isalpha() or number_info[g].isalpha():
                    pass
                else:
                    w = 2 + 5 * i
                    g = 4 + 5 * i
                    male_number = number_info[w]
                    female_number = number_info[g]
                    i = i + 1
                    # remove , in the number
                    new_male_number = re.sub(",", "", male_number)
                    # to add the number
                    total_male_number += int(new_male_number)
                    new_female_number = re.sub(",", "", female_number)
                    total_female_number += int(new_female_number)

        print("Male Number:", total_male_number)
        print("Female Number:", total_female_number)


if __name__ == '__main__':
    main()
