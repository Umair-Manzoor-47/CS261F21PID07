
from os import fsdecode
import sys
from PyQt5 import QtTest, QtWidgets, QtCore
from PyQt5.QtWidgets import * 
import csv
from Project import Ui_MainWindow
import threading
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from datetime import datetime


# global varialbles
paused = False
pause_count = 0
Stopped = False


class GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)  
        self.gu = Ui_MainWindow()
        self.gu.setupUi(self)
        self.clickEvent()
        self.movies = None
        self.TDlist = []

    def clickEvent(self):
        self.gu.Start_Button.clicked.connect(self.thread)
        self.gu.Pause_button.clicked.connect(self.pause_func)
        self.gu.Stop_button.clicked.connect(self.stop_func)
        self.gu.Export.clicked.connect(self.export)
        self.gu.Button_Sort.clicked.connect(self.sort)

    def sort(self):
        idx = self.gu.Algorithm_list.currentIndex()
        col = self.gu.Column_CB_2.currentIndex()

    
    def pause_func(self):
        global paused, pause_count
        if pause_count == 0:
            paused = True
            self.gu.Pause_button.setText("Resume")
            pause_count = 1
        else:
            paused = False
            self.gu.Pause_button.setText("Pause")
            pause_count = 0

    
    def stop_func(self):
        global Stopped
        Stopped = True

    def load(self):

            pass
            # for row in range(len(title)):
            #         self.gu.tableWidget.setRowCount(len(title))
            #         self.gu.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem((title[j])))  
            #         self.gu.tableWidget.setItem(r, 1 , QtWidgets.QTableWidgetItem((year[j])))
            #         self.gu.tableWidget.setItem(r, 2 , QtWidgets.QTableWidgetItem((time[j])))
            #         self.gu.tableWidget.setItem(r, 3 , QtWidgets.QTableWidgetItem((rating[j])))
            #         self.gu.tableWidget.setItem(r, 4 , QtWidgets.QTableWidgetItem((genre[j])))
            #         self.gu.tableWidget.setItem(r, 5 , QtWidgets.QTableWidgetItem((votes[j])))
            #         self.gu.tableWidget.setItem(r, 6 , QtWidgets.QTableWidgetItem((synopsis[j])))
            #         self.gu.tableWidget.setItem(r, 7 , QtWidgets.QTableWidgetItem((director[j]))) 
            #         r += 1
            #         j += 1 
            #         self.gu.Movies_count.setText(str(r))
            
    def scrap(self):
        start_time = datetime.now()
        

        # header 
        headers = {"Accept-Language": "en-US,en;q=0.5"}

        # lists
        title = []
        year = []
        time=[]
        genre = []
        director = []
        rating=[]
        cast = []
        synopsis = []
        votes = []
        counter = 0
        page = "https://www.imdb.com/search/title/?release_date=1960-01-01,2021-10-31&page=1adv_nxt"


        
        global Stopped
        while page != None and counter < 19800 and Stopped == False:
            while paused:
                None
            page = requests.get(page)
            soup = BeautifulSoup(page.text, 'html.parser')
            Next_page = soup.find('div',attrs = {'id' : 'content-2-wide'}).find('div',attrs = {'class' : 'desc'}).find('a',attrs = {'class' : 'lister-page-next next-page'})
            
            movie_data = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})

            for store in movie_data:
                # titles
                name = store.h3.a.text
                title.append(name.strip())
                
                # year of release
                year_of_release = store.h3.find('span', class_ = "lister-item-year text-muted unbold").text.replace("(", "").replace(")", "")
                year.append(year_of_release.strip())
                
                # runtime
                runtime = store.p.find("span", class_ = 'runtime').text if store.p.find("span", class_ = 'runtime') else "Not given"
                runtime = runtime.split(" ")[0]
                time.append(runtime.strip())
                
                # rate
                rate = store.find('div', class_ = "inline-block ratings-imdb-rating").text.replace('\n', '') if store.find('div', class_ = "inline-block ratings-imdb-rating") else "Not rated"
                rating.append(rate.strip())
                
                # votes
                value = store.find_all('span', attrs = {'name': "nv"})
                vote = value[0].text if len(value) > 0 else 'Not voted'
                vote = vote.replace(",", "")
                votes.append(vote.strip())
                
                # Genre 
                gen = store.p.find("span", class_ = 'genre').text.replace("            ", "").replace("\n", "") if store.p.find('span', class_ = "genre") else "Not given"
                genre.append(gen.strip())
                
                # synopsis
                syno = store.find_all('p', class_ = 'text-muted')
                syno_ = syno[1].text.replace('\n', '') if len(syno) > 1 else 'No synopsis'
                synopsis.append(syno_.strip())

                # cast
                act = store.find_all('a', class_ = '') 
                actors_ = []
                for i in range (13, len(act)):     # there can be multiple actors at different indexes
                    actors_.append(act[i].text if len(act) > 13 else 'Unknown')
                cast.append(actors_)

                # director
                direct = store.find_all('a', class_ = '') 
                direct_ = direct[14].text if len(direct) > 14 else 'Unknown'
                director.append(direct_)
            j = 0
            r = 0
            sleep(2)
            for row in range(len(title)):
                    self.gu.tableWidget.setRowCount(len(title))
                    self.gu.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem((title[j])))  
                    self.gu.tableWidget.setItem(r, 1 , QtWidgets.QTableWidgetItem((year[j])))
                    self.gu.tableWidget.setItem(r, 2 , QtWidgets.QTableWidgetItem((time[j])))
                    self.gu.tableWidget.setItem(r, 3 , QtWidgets.QTableWidgetItem((rating[j])))
                    self.gu.tableWidget.setItem(r, 4 , QtWidgets.QTableWidgetItem((genre[j])))
                    self.gu.tableWidget.setItem(r, 5 , QtWidgets.QTableWidgetItem((votes[j])))
                    self.gu.tableWidget.setItem(r, 6 , QtWidgets.QTableWidgetItem((synopsis[j])))
                    self.gu.tableWidget.setItem(r, 7 , QtWidgets.QTableWidgetItem((director[j]))) 
                    r += 1
                    j += 1 
                    self.gu.Movies_count.setText(str(r))
            page = "https://www.imdb.com"+ str(Next_page['href'])
            counter += 1
        end_time = datetime.now()
        self.gu.Scraping_Time_count.setText(str(end_time - start_time))
         
        # 2D list
        self.TDlist.append(title, year, time, rating, genre, votes,  synopsis, director)

        # Data Frame
        self.movies = pd.DataFrame({"Title": title, "Releasing year" : year, "Watch Time": time,"Rating": rating, "Genre": genre, "Votes": votes,  "Synopsis": synopsis, "Cast": cast, "Director": director})

    def export(self):
        self.movies
        name = self.gu.Name_Csv.text() 
        name = str(name) + ".csv"
        print(name)
        # appending to csv
        self.movies.to_csv(name, index = False)
        return

    def thread(self):
        thread = threading.Thread(target= self.scrap)
        thread.start()

app = QApplication(sys.argv)
window = GUI()
window.show()
sys.exit(app.exec_())
