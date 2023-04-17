import csv

superbowl_data = []


class Super_bowl_reasult:
    def __init__(
        self, date, winner, win_pts, loser, lose_pts, mvp, stadium, city, state
    ):
        self.date = date.split(" ")
        self.year = self.date[-1]
        self.winner = winner
        try:
            self.winpts = int(win_pts)
        except ValueError:
            self.winpts = win_pts
        self.lose = loser
        try:
            self.losepts = int(lose_pts)
        except ValueError:
            self.losepts = lose_pts
        self.mvp = mvp
        self.stadium = stadium
        self.city = city
        self.state = state

#3b adding items to the list
def read_csv():
    with open("program/superbowl.csv", "r", encoding="utf-8") as nfl_file:
        reader = csv.reader(nfl_file, delimiter=",")
        next(reader)
        for row in reader:
            try:
                temp_reasult = Super_bowl_reasult(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                )
                superbowl_data.append(temp_reasult)
            except ValueError:
                print("The following has value error")
                print(row)

#3c_part_1
def get_list_by_data(list_to_sort, sort_type, sort_attr):
    temp_list = []
    for bowl in list_to_sort:
        if sort_type == "year":
            if bowl.year == sort_attr:
                temp_list.append(bowl)
    return temp_list

#3b get attribute from the list
def final_reasults(final_list):
    if len(final_list) < 1:
        print("No data available for the following search")
    else:
        for bowl in final_list:
            print(f"Date of The Superbowl:          {bowl.date[0]} {bowl.date[1]}, {bowl.date[2]}")
            print(f"Location:                       {bowl.stadium}, {bowl.city}, {bowl.state}")
            print(f"Winner of the SuperBowl:        {bowl.winner} by {bowl.winpts}")
            print(f"MVP:                            {bowl.mvp}")
            print(f"Loser of the SuperBowl:         {bowl.lose} by {bowl.losepts}")
        print("-" * 30)
            


def start():
    read_csv()
    print("---Super Bowl Encyclopedia---")
    print("This program reads a Superbowl dataset and allows user to sort by inputting keywords to search")
    while True:
        year = ""
        while year == "":
            year = input("Please choose  year from 1967 to 2022: ")
            if year not in ["1967","1968","1969""1970","1971","1972","1973","1974","1975","1976","1977","1978",
            "1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992",
            "1993", "1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006",
            "2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020",
            "2021", "2022"]:
                print("Only choose from 1967 to 2022")
                year = ""
                #3c part 2/3d first call
        year_list = get_list_by_data(superbowl_data, "year", year)
        final_reasults(year_list)
        restart = input("Do you want to go again? [y/n]: ").lower()
        if restart[0] == "n":
            print("Thank you for using")
            break

start()
