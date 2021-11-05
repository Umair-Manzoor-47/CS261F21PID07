
import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import *
from numpy.lib.npyio import load 
from Project import Ui_MainWindow
import threading
import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import Algos as algo
from datetime import datetime
import Search


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
        self.gu.Export.setEnabled(False)
        self.gu.Pause_button.setEnabled(False)
        self.gu.Stop_button.setEnabled(False)
        self.Algorithm = [algo.Insertion(), algo.Bubble(), algo.Selection(), algo.Merge(), algo.Quick(), algo.Shell(), algo.Cocktail(), algo.Brick()]

    def clickEvent(self):
        self.gu.Start_Button.clicked.connect(self.thread)
        self.gu.Pause_button.clicked.connect(self.pause_func)
        self.gu.Stop_button.clicked.connect(self.stop_func)
        self.gu.Export.clicked.connect(self.export)
        self.gu.Button_Sort.clicked.connect(self.sort)
        self.gu.Search_Button.clicked.connect(self.search)

    def sort(self):
        start_time = datetime.now()
        idx = self.gu.Algorithm_list.currentIndex()
        col = self.gu.Column_CB_2.currentIndex()
        print(self.gu.Descending_Radio.isChecked())
         
        if self.gu.Descending_Radio.isChecked():
            if idx == 3 or idx == 4:
                self.Algorithm[idx].Descending(self.TDlist, col, 0, len(self.TDlist)-1)
                self.TDlist = self.getString(self.TDlist)
                self.load(self.TDlist)    
            else:
                A = self.Algorithm[idx].Descending(self.TDlist, int(col))
                A = self.getString(A)
                self.load(A)
        
        else:
            if idx == 3 or idx == 4:
                self.Algorithm[idx].Ascending(self.TDlist, col, 0, len(self.TDlist)-1)
                self.TDlist = self.getString(self.TDlist)
                self.load(self.TDlist)    
            else:
                A = self.Algorithm[idx].Ascending(self.TDlist, int(col))
                A = self.getString(A)
                self.load(A)
        
        end_time = datetime.now()

        self.gu.Sorting_Time_count.setText(str(end_time - start_time))
    def search(self,):
        idx = self.gu.Column_CB.currentIndex()
        entry = self.gu.keyword.text()
        if self.gu.Starts_radio.isChecked():
           result =  Search.starts(self.TDlist, idx, entry)

        elif self.gu.Ends_Radio.isChecked():
            result = Search.ends(self.TDlist, idx, entry)

        else:
            result = Search.ends(self.TDlist, idx, entry)
        
        self.load(result)


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
        self.gu.Export.setEnabled(True)

    def load(self, A):
            r = 0
            self.gu.tableWidget.setRowCount(len(A))
            for row in A:                   
                self.gu.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(row[0]))  
                self.gu.tableWidget.setItem(r, 1 , QtWidgets.QTableWidgetItem(row[1]))
                self.gu.tableWidget.setItem(r, 2 , QtWidgets.QTableWidgetItem(row[2]))
                self.gu.tableWidget.setItem(r, 3 , QtWidgets.QTableWidgetItem(row[3]))
                self.gu.tableWidget.setItem(r, 4 , QtWidgets.QTableWidgetItem(row[4]))
                self.gu.tableWidget.setItem(r, 5 , QtWidgets.QTableWidgetItem(row[5]))
                self.gu.tableWidget.setItem(r, 6 , QtWidgets.QTableWidgetItem(row[6]))
                self.gu.tableWidget.setItem(r, 7 , QtWidgets.QTableWidgetItem(row[7]))
                
                r += 1
                    
            
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
        synopsis = []
        votes = []
        counter = 0
        page = "https://www.imdb.com/search/title/?release_date=1960-01-01,2021-10-31&page=1adv_nxt"

        global Stopped
        while page != None and counter < 19800 and Stopped == False:
            while paused == True and Stopped == False:
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
                year_of_release = store.h3.find('span', class_ = "lister-item-year text-muted unbold").text.replace("(", "").replace(")", "").replace("I", "").replace("|", "").split("-")[0]
                year.append(year_of_release.strip())
                
                # runtime
                runtime = store.p.find("span", class_ = 'runtime').text.replace(" min", "") if store.p.find("span", class_ = 'runtime') else "0" + ".00"

                time.append(runtime)
                
                # rate
                rate = store.find('div', class_ = "inline-block ratings-imdb-rating").text.replace('\n', '') if store.find('div', class_ = "inline-block ratings-imdb-rating") else "_"
                rating.append(rate.strip())
                
                # votes
                value = store.find_all('span', attrs = {'name': "nv"})
                vote = value[0].text if len(value) > 0 else "_"
                vote = vote.replace(",", "")+ ".00"
                votes.append(vote)
                
                # Genre 
                gen = store.p.find("span", class_ = 'genre').text.replace("            ", "").replace("\n", "") if store.p.find('span', class_ = "genre") else "Not given"
                genre.append(gen.strip())
                
                # synopsis
                syno = store.find_all('p', class_ = 'text-muted')
                syno_ = syno[1].text.replace('\n', '') if len(syno) > 1 else 'No synopsis'
                synopsis.append(syno_.strip())

                # director
                direct = store.find_all('a', class_ = '') 
                direct_ = direct[14].text if len(direct) > 14 else '_'
                director.append(direct_)
            j = 0
            r = 0
            sleep(1)
            for row in range(len(title)):
                    self.gu.tableWidget.setRowCount(len(title))
                    self.gu.tableWidget.setItem(r, 0 , QtWidgets.QTableWidgetItem(str(title[j])))  
                    self.gu.tableWidget.setItem(r, 1 , QtWidgets.QTableWidgetItem(str(year[j])))
                    self.gu.tableWidget.setItem(r, 2 , QtWidgets.QTableWidgetItem(str(time[j])))
                    self.gu.tableWidget.setItem(r, 3 , QtWidgets.QTableWidgetItem(str(rating[j])))
                    self.gu.tableWidget.setItem(r, 4 , QtWidgets.QTableWidgetItem(str(genre[j])))
                    self.gu.tableWidget.setItem(r, 5 , QtWidgets.QTableWidgetItem(str(votes[j])))
                    self.gu.tableWidget.setItem(r, 6 , QtWidgets.QTableWidgetItem(str(synopsis[j])))
                    self.gu.tableWidget.setItem(r, 7 , QtWidgets.QTableWidgetItem(str(director[j]))) 
                    r += 1
                    j += 1 
                    self.gu.Movies_count.setText(str(r))
            page = "https://www.imdb.com"+ str(Next_page['href'])
            counter += 1
        end_time = datetime.now()
        self.gu.Scraping_Time_count.setText(str(end_time - start_time))
   
        # Data Frame
        self.movies = pd.DataFrame({"Title": title, "Releasing year" : year, "Watch Time": time,"Rating": rating, "Genre": genre, "Votes": votes,  "Synopsis": synopsis, "Director": director})
        #to 2D list
        
        self.TDlist = self.movies.values.tolist()
        Stopped = False
   
    def export(self):
        name = self.gu.Name_Csv.text()
        if name == "":
            name = "Movies_scrapped" 
        name = str(name) + ".csv"
        # appending to csv
        self.movies.to_csv(name, index = False)
        return

    def thread(self):
        self.gu.Stop_button.setEnabled(True)
        self.gu.Pause_button.setEnabled(True)
        thread = threading.Thread(target= self.scrap)
        
        thread.start()

    def getString(self, A):
        for i in A:
            i[2] = str(i[2])
            i[5] = str(i[5])
        
        return A

app = QApplication(sys.argv)
window = GUI()
window.show()
sys.exit(app.exec_())
