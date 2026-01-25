#You have specific interests (e.g., "Arch Linux News," "AI Research," "Bitcoin Price"). Instead of checking 10 websites, your script will generate a Daily Briefing Report.

'''Project ARchitecture
1: configuration layer(inputs) : sotore topic of interest in config.json

2.simulation engine(processing): for every topic in config.json a few "Fake" news headlines and a "confidence score, use nested dictionaries and the random module

3.The report Designer(Formatting): it creates a text file(e.g daily_report.txt) writes a header, lists the news by category, and adds a "summary" at the bottom(Total articles found: 12)

4.automated archive(output): save the reports as a .txt file, should automatically create a folder structure based on the data: Roports/2026/January/Briefing_25.txt'''

import json
import random
import os
from datetime import date


def read_json():
    with open("day_7/config.json", 'r')as f:
        topics = json.load(f)
    
    return topics

def create_dict(topics):
    headlines = [
    "Introduction to ",
    "History of ",
    "Applications of ",
    "Advantages of ", 
    "Limitations of ",
    "Future Scope of " 
    ]
    dict_list = []
    for topic in topics['title']:
         name = topic + "_dict"
         name = {
            "topic":topic,
            "headline": random.choice(headlines) + topic,
            "confidence": round(random.uniform(0.7, 1.0), 3)
            }
         dict_list.append(name)
    return dict_list

def create_report(dict_list):
        today = date.today()

        folder_path = f"/home/nawich/Reports/{today.strftime('%Y/%B')}"
        file_name = f"Briefing_{today.strftime('%d')}.txt"
        full_path = os.path.join(folder_path, file_name)

        os.makedirs(folder_path, exist_ok=True)

        with open(full_path, "w") as f:
            f.write(f"Daily News: {today} \n\n")
            for news in dict_list:
                 line = f"[{news['topic'].upper()}] {news['headline']}\n"
                 line += f"Confidence Score: {news['confidence']}\n"
                 f.write(line)
            f.write(f"\nSUMMARY: Total articles found: {len(dict_list)}")
        
        print(f"Report is at {full_path}")


def main():
     data = read_json()
     article = create_dict(data)
     create_report(article)

if __name__ == "__main__":
     main()