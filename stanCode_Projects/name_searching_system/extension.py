"""
File: extension.py
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


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        items = soup.tbody.text
        item = items.split()
        male_val = []
        female_val = []
        for i in range(0, len(item), 5):
            rank = item[i]
            man_val = ''
            for ch in item[i+2]:
                if ch != ',':
                    man_val += ch
            woman_val = ''
            for ch in item[i + 4]:
                if ch != ',':
                    woman_val += ch
            if rank == '200':
                male_val.append(int(man_val))
                female_val.append(int(woman_val))
                break
            male_val.append(int(man_val))
            female_val.append(int(woman_val))
        print('Male Number:', sum(male_val))
        print('Female Number:', sum(female_val))

        ##################


if __name__ == '__main__':
    main()
