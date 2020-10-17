from datetime import timedelta, datetime
from time import strftime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import os
import locale


# locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
ToDay = datetime.now()
n = ToDay.weekday()
MonDate = ToDay + timedelta(days=-n)
NextMonDate = MonDate + timedelta(days=+7)

BackgroundsColors = [[1, 1, 1, 1] for i in range(6)]
if n != 6:
    BackgroundsColors[n] = [0.5, 0.5, 0.5, 1]

try:
    DayInfoFile = open("DayInfoFile.txt", "r")
    dayinfo = ["" for i in range(200)]
    dayinfostr = DayInfoFile.read().splitlines()

    for i in range(len(dayinfostr)):
        dayinfo[i] = dayinfostr[i]

except FileNotFoundError:
    DayInfoFile = open("DayInfoFile.txt", "w+")
    dayinfo = ["" for i in range(200)]

try:
    UniversityInfo = open("UniversityInfo.txt", "r+")
    universityinfo = UniversityInfo.read().splitlines()

    if len(universityinfo) != 15:
        for i in range(15):
            UniversityInfo.writelines("1\n")
    UniversityInfo.close()

except FileNotFoundError:
    UniversityInfo = open("UniversityInfo.txt", "w+")
    universityinfo = []

    for i in range(15):
        universityinfo.append(1)
        UniversityInfo.writelines("1\n")
    UniversityInfo.close()

try:
    WeeksInfo = open("WeeksInfo.txt", "r+")
    weeksinfo = WeeksInfo.read().splitlines()

    if len(universityinfo) != 15:
        for i in range(15):
            WeeksInfo.writelines("0\n")
    WeeksInfo.close()

except FileNotFoundError:
    WeeksInfo = open("WeeksInfo.txt", "w+")
    weeksinfo = [0]
    weeksinfo.append(str(ToDay.isocalendar()[1]))
    WeeksInfo.writelines("0\n")
    WeeksInfo.writelines(str(ToDay.isocalendar()[1]) + "\n")

    for i in range(15):
        weeksinfo.append(0)
        WeeksInfo.writelines("0\n")
    WeeksInfo.close()

weeksinfo[0] = abs(int(ToDay.isocalendar()[1]) - int(weeksinfo[1]))
next_weekinfo = weeksinfo[0] + 1

os.remove("WeeksInfo.txt")
WeeksInfo = open("WeeksInfo.txt", "w")

for i in weeksinfo:
    WeeksInfo.writelines(str(i) + "\n")

WeeksInfo.close()

Monday = "Понедельник" + "\n" + str(MonDate.date())[5:7] + " Месяц" + "\n" + str(MonDate.date())[8:10] + " Число"
Tuesday = "Вторник" + "\n" + str((MonDate + timedelta(days=1)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=1)).date())[8:10] + " Число"
Wednesday = "Среда" + "\n" + str((MonDate + timedelta(days=2)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=2)).date())[8:10] + " Число"
Thursday = "Четверг" + "\n" + str((MonDate + timedelta(days=3)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=3)).date())[8:10] + " Число"
Friday = "Пятница" + "\n" + str((MonDate + timedelta(days=4)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=4)).date())[8:10] + " Число"
Saturday = "Суббота" + "\n" + str((MonDate + timedelta(days=5)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=5)).date())[8:10] + " Число"

NextMonday = "Понедельник" + "\n" + str(NextMonDate.date())[5:7] + " Месяц" + "\n" + str(NextMonDate.date())[8:10] + " Число"
NextTuesday = "Вторник" + "\n" + str((NextMonDate + timedelta(days=1)).date())[5:7] + " Месяц" + "\n" + str((NextMonDate + timedelta(days=1)).date())[8:10] + " Число"
NextWednesday = "Среда" + "\n" + str((NextMonDate + timedelta(days=2)).date())[5:7] + " Месяц" + "\n" + str((NextMonDate + timedelta(days=2)).date())[8:10] + " Число"
NextThursday = "Четверг" + "\n" + str((NextMonDate + timedelta(days=3)).date())[5:7] + " Месяц" + "\n" + str((NextMonDate + timedelta(days=3)).date())[8:10] + " Число"
NextFriday = "Пятница" + "\n" + str((NextMonDate + timedelta(days=4)).date())[5:7] + " Месяц" + "\n" + str((NextMonDate + timedelta(days=4)).date())[8:10] + " Число"
NextSaturday = "Суббота" + "\n" + str((NextMonDate + timedelta(days=5)).date())[5:7] + " Месяц" + "\n" + str((NextMonDate + timedelta(days=5)).date())[8:10] + " Число"

dayid = 0
university_amount = universityinfo[0]
university_deleteid = -1

isnext_week = False


class CalendarWindow(Screen):

    def on_enter(self):

        try:
            if university_amount == 1 or university_amount == "1":
                self.monday_var_1color.background_color = [1, 1, 1, 1]
                self.tuesday_var_1color.background_color = [1, 1, 1, 1]
                self.wednesday_var_1color.background_color = [1, 1, 1, 1]
                self.thursday_var_1color.background_color = [1, 1, 1, 1]
                self.friday_var_1color.background_color = [1, 1, 1, 1]
                self.saturday_var_1color.background_color = [1, 1, 1, 1]

            if university_amount == 4 or university_amount == "4":
                if type(universityinfo[2]) == str:
                    color = [universityinfo[2][1], universityinfo[2][4], universityinfo[2][7], universityinfo[2][10]]
                else:
                    color = [universityinfo[2][0], universityinfo[2][1], universityinfo[2][2], universityinfo[2][3]]

                if type(universityinfo[3]) == str:
                    days = universityinfo[3].split(",")
                else:
                    days = [universityinfo[3][0], universityinfo[3][1], universityinfo[3][2], universityinfo[3][3], universityinfo[3][4], universityinfo[3][5]]

                if days[0] == "[True" or days[0] == True:
                    self.monday_var_1color.background_color = color
                else:
                    self.monday_var_1color.background_color = [1, 1, 1, 1]

                if days[1] == " True" or days[1] == True:
                    self.tuesday_var_1color.background_color = color
                else:
                    self.tuesday_var_1color.background_color = [1, 1, 1, 1]

                if days[2] == " True" or days[2] == True:
                    self.wednesday_var_1color.background_color = color
                else:
                    self.wednesday_var_1color.background_color = [1, 1, 1, 1]

                if days[3] == " True" or days[3] == True:
                    self.thursday_var_1color.background_color = color
                else:
                    self.thursday_var_1color.background_color = [1, 1, 1, 1]

                if days[4] == " True" or days[4] == True:
                    self.friday_var_1color.background_color = color
                else:
                    self.friday_var_1color.background_color = [1, 1, 1, 1]

                if days[5] == " True]" or days[5] == True:
                    self.saturday_var_1color.background_color = color
                else:
                    self.saturday_var_1color.background_color = [1, 1, 1, 1]

                self.monday_var_2color.background_color = [1, 1, 1, 1]
                self.tuesday_var_2color.background_color = [1, 1, 1, 1]
                self.wednesday_var_2color.background_color = [1, 1, 1, 1]
                self.thursday_var_2color.background_color = [1, 1, 1, 1]
                self.friday_var_2color.background_color = [1, 1, 1, 1]
                self.saturday_var_2color.background_color = [1, 1, 1, 1]

                self.monday_var_3color.background_color = [1, 1, 1, 1]
                self.tuesday_var_3color.background_color = [1, 1, 1, 1]
                self.wednesday_var_3color.background_color = [1, 1, 1, 1]
                self.thursday_var_3color.background_color = [1, 1, 1, 1]
                self.friday_var_3color.background_color = [1, 1, 1, 1]
                self.saturday_var_3color.background_color = [1, 1, 1, 1]

                self.monday_var_4color.background_color = [1, 1, 1, 1]
                self.tuesday_var_4color.background_color = [1, 1, 1, 1]
                self.wednesday_var_4color.background_color = [1, 1, 1, 1]
                self.thursday_var_4color.background_color = [1, 1, 1, 1]
                self.friday_var_4color.background_color = [1, 1, 1, 1]
                self.saturday_var_4color.background_color = [1, 1, 1, 1]

            if university_amount == 7 or university_amount == "7":
                if type(universityinfo[2]) == str:
                    color1 = [universityinfo[2][1], universityinfo[2][4], universityinfo[2][7], universityinfo[2][10]]
                else:
                    color1 = [universityinfo[2][0], universityinfo[2][1], universityinfo[2][2], universityinfo[2][3]]

                if type(universityinfo[5]) == str:
                    color2 = [universityinfo[5][1], universityinfo[5][4], universityinfo[5][7], universityinfo[5][10]]
                else:
                    color2 = [universityinfo[5][0], universityinfo[5][1], universityinfo[5][2], universityinfo[5][3]]

                if type(universityinfo[3]) == str:
                    days1 = universityinfo[3].split(",")
                else:
                    days1 = [universityinfo[3][0], universityinfo[3][1], universityinfo[3][2], universityinfo[3][3], universityinfo[3][4], universityinfo[3][5]]

                if type(universityinfo[6]) == str:
                    days2 = universityinfo[6].split(",")
                else:
                    days2 = [universityinfo[6][0], universityinfo[6][1], universityinfo[6][2], universityinfo[6][3], universityinfo[6][4], universityinfo[6][5]]

                if days1[0] == "[True" or days1[0] == True:
                    self.monday_var_1color.background_color = color1
                else:
                    self.monday_var_1color.background_color = [1, 1, 1, 1]

                if days1[1] == " True" or days1[1] == True:
                    self.tuesday_var_1color.background_color = color1
                else:
                    self.tuesday_var_1color.background_color = [1, 1, 1, 1]

                if days1[2] == " True" or days1[2] == True:
                    self.wednesday_var_1color.background_color = color1
                else:
                    self.wednesday_var_1color.background_color = [1, 1, 1, 1]

                if days1[3] == " True" or days1[3] == True:
                    self.thursday_var_1color.background_color = color1
                else:
                    self.thursday_var_1color.background_color = [1, 1, 1, 1]

                if days1[4] == " True" or days1[4] == True:
                    self.friday_var_1color.background_color = color1
                else:
                    self.friday_var_1color.background_color = [1, 1, 1, 1]

                if days1[5] == " True]" or days1[5] == True:
                    self.saturday_var_1color.background_color = color1
                else:
                    self.saturday_var_1color.background_color = [1, 1, 1, 1]

                if days2[0] == "[True" or days2[0] == True:
                    self.monday_var_2color.background_color = color2
                else:
                    self.monday_var_2color.background_color = [1, 1, 1, 1]

                if days2[1] == " True" or days2[1] == True:
                    self.tuesday_var_2color.background_color = color2
                else:
                    self.tuesday_var_2color.background_color = [1, 1, 1, 1]

                if days2[2] == " True" or days2[2] == True:
                    self.wednesday_var_2color.background_color = color2
                else:
                    self.wednesday_var_2color.background_color = [1, 1, 1, 1]

                if days2[3] == " True" or days2[3] == True:
                    self.thursday_var_2color.background_color = color2
                else:
                    self.thursday_var_2color.background_color = [1, 1, 1, 1]

                if days2[4] == " True" or days2[4] == True:
                    self.friday_var_2color.background_color = color2
                else:
                    self.friday_var_2color.background_color = [1, 1, 1, 1]

                if days2[5] == " True]" or days2[5] == True:
                    self.saturday_var_2color.background_color = color2
                else:
                    self.saturday_var_2color.background_color = [1, 1, 1, 1]

                self.monday_var_3color.background_color = [1, 1, 1, 1]
                self.tuesday_var_3color.background_color = [1, 1, 1, 1]
                self.wednesday_var_3color.background_color = [1, 1, 1, 1]
                self.thursday_var_3color.background_color = [1, 1, 1, 1]
                self.friday_var_3color.background_color = [1, 1, 1, 1]
                self.saturday_var_3color.background_color = [1, 1, 1, 1]

                self.monday_var_4color.background_color = [1, 1, 1, 1]
                self.tuesday_var_4color.background_color = [1, 1, 1, 1]
                self.wednesday_var_4color.background_color = [1, 1, 1, 1]
                self.thursday_var_4color.background_color = [1, 1, 1, 1]
                self.friday_var_4color.background_color = [1, 1, 1, 1]
                self.saturday_var_4color.background_color = [1, 1, 1, 1]

            if university_amount == 10 or university_amount == "10":
                if type(universityinfo[2]) == str:
                    color1 = [universityinfo[2][1], universityinfo[2][4], universityinfo[2][7], universityinfo[2][10]]
                else:
                    color1 = [universityinfo[2][0], universityinfo[2][1], universityinfo[2][2], universityinfo[2][3]]

                if type(universityinfo[5]) == str:
                    color2 = [universityinfo[5][1], universityinfo[5][4], universityinfo[5][7], universityinfo[5][10]]
                else:
                    color2 = [universityinfo[5][0], universityinfo[5][1], universityinfo[5][2], universityinfo[5][3]]

                if type(universityinfo[8]) == str:
                    color3 = [universityinfo[8][1], universityinfo[8][4], universityinfo[8][7], universityinfo[8][10]]
                else:
                    color3 = [universityinfo[8][0], universityinfo[8][1], universityinfo[8][2], universityinfo[8][3]]

                if type(universityinfo[3]) == str:
                    days1 = universityinfo[3].split(",")
                else:
                    days1 = [universityinfo[3][0], universityinfo[3][1], universityinfo[3][2], universityinfo[3][3], universityinfo[3][4], universityinfo[3][5]]

                if type(universityinfo[6]) == str:
                    days2 = universityinfo[6].split(",")
                else:
                    days2 = [universityinfo[6][0], universityinfo[6][1], universityinfo[6][2], universityinfo[6][3], universityinfo[6][4], universityinfo[6][5]]

                if type(universityinfo[9]) == str:
                    days3 = universityinfo[9].split(",")
                else:
                    days3 = [universityinfo[9][0], universityinfo[9][1], universityinfo[9][2], universityinfo[9][3], universityinfo[9][4], universityinfo[9][5]]

                if days1[0] == "[True" or days1[0] == True:
                    self.monday_var_1color.background_color = color1
                else:
                    self.monday_var_1color.background_color = [1, 1, 1, 1]

                if days1[1] == " True" or days1[1] == True:
                    self.tuesday_var_1color.background_color = color1
                else:
                    self.tuesday_var_1color.background_color = [1, 1, 1, 1]

                if days1[2] == " True" or days1[2] == True:
                    self.wednesday_var_1color.background_color = color1
                else:
                    self.wednesday_var_1color.background_color = [1, 1, 1, 1]

                if days1[3] == " True" or days1[3] == True:
                    self.thursday_var_1color.background_color = color1
                else:
                    self.thursday_var_1color.background_color = [1, 1, 1, 1]

                if days1[4] == " True" or days1[4] == True:
                    self.friday_var_1color.background_color = color1
                else:
                    self.friday_var_1color.background_color = [1, 1, 1, 1]

                if days1[5] == " True]" or days1[5] == True:
                    self.saturday_var_1color.background_color = color1
                else:
                    self.saturday_var_1color.background_color = [1, 1, 1, 1]

                if days2[0] == "[True" or days2[0] == True:
                    self.monday_var_2color.background_color = color2
                else:
                    self.monday_var_2color.background_color = [1, 1, 1, 1]

                if days2[1] == " True" or days2[1] == True:
                    self.tuesday_var_2color.background_color = color2
                else:
                    self.tuesday_var_2color.background_color = [1, 1, 1, 1]

                if days2[2] == " True" or days2[2] == True:
                    self.wednesday_var_2color.background_color = color2
                else:
                    self.wednesday_var_2color.background_color = [1, 1, 1, 1]

                if days2[3] == " True" or days2[3] == True:
                    self.thursday_var_2color.background_color = color2
                else:
                    self.thursday_var_2color.background_color = [1, 1, 1, 1]

                if days2[4] == " True" or days2[4] == True:
                    self.friday_var_2color.background_color = color2
                else:
                    self.friday_var_2color.background_color = [1, 1, 1, 1]

                if days2[5] == " True]" or days2[5] == True:
                    self.saturday_var_2color.background_color = color2
                else:
                    self.saturday_var_2color.background_color = [1, 1, 1, 1]

                if days3[0] == "[True" or days3[0] == True:
                    self.monday_var_3color.background_color = color3
                else:
                    self.monday_var_3color.background_color = [1, 1, 1, 1]

                if days3[1] == " True" or days3[1] == True:
                    self.tuesday_var_3color.background_color = color3
                else:
                    self.tuesday_var_3color.background_color = [1, 1, 1, 1]

                if days3[2] == " True" or days3[2] == True:
                    self.wednesday_var_3color.background_color = color3
                else:
                    self.wednesday_var_ecolor.background_color = [1, 1, 1, 1]

                if days3[3] == " True" or days3[3] == True:
                    self.thursday_var_3color.background_color = color3
                else:
                    self.thursday_var_3color.background_color = [1, 1, 1, 1]

                if days3[4] == " True" or days3[4] == True:
                    self.friday_var_3color.background_color = color3
                else:
                    self.friday_var_3color.background_color = [1, 1, 1, 1]

                if days3[5] == " True]" or days3[5] == True:
                    self.saturday_var_3color.background_color = color3
                else:
                    self.saturday_var_2color.background_color = [1, 1, 1, 1]

                self.monday_var_4color.background_color = [1, 1, 1, 1]
                self.tuesday_var_4color.background_color = [1, 1, 1, 1]
                self.wednesday_var_4color.background_color = [1, 1, 1, 1]
                self.thursday_var_4color.background_color = [1, 1, 1, 1]
                self.friday_var_4color.background_color = [1, 1, 1, 1]
                self.saturday_var_4color.background_color = [1, 1, 1, 1]

            if university_amount == 13 or university_amount == "13":
                if type(universityinfo[2]) == str:
                    color1 = [universityinfo[2][1], universityinfo[2][4], universityinfo[2][7], universityinfo[2][10]]
                else:
                    color1 = [universityinfo[2][0], universityinfo[2][1], universityinfo[2][2], universityinfo[2][3]]

                if type(universityinfo[5]) == str:
                    color2 = [universityinfo[5][1], universityinfo[5][4], universityinfo[5][7], universityinfo[5][10]]
                else:
                    color2 = [universityinfo[5][0], universityinfo[5][1], universityinfo[5][2], universityinfo[5][3]]

                if type(universityinfo[8]) == str:
                    color3 = [universityinfo[8][1], universityinfo[8][4], universityinfo[8][7], universityinfo[8][10]]
                else:
                    color3 = [universityinfo[8][0], universityinfo[8][1], universityinfo[8][2], universityinfo[8][3]]

                if type(universityinfo[11]) == str:
                    color4 = [universityinfo[11][1], universityinfo[11][4], universityinfo[11][7], universityinfo[11][10]]
                else:
                    color4 = [universityinfo[11][0], universityinfo[11][1], universityinfo[11][2], universityinfo[11][3]]

                if type(universityinfo[3]) == str:
                    days1 = universityinfo[3].split(",")
                else:
                    days1 = [universityinfo[3][0], universityinfo[3][1], universityinfo[3][2], universityinfo[3][3], universityinfo[3][4], universityinfo[3][5]]

                if type(universityinfo[6]) == str:
                    days2 = universityinfo[6].split(",")
                else:
                    days2 = [universityinfo[6][0], universityinfo[6][1], universityinfo[6][2], universityinfo[6][3], universityinfo[6][4], universityinfo[6][5]]

                if type(universityinfo[9]) == str:
                    days3 = universityinfo[9].split(",")
                else:
                    days3 = [universityinfo[9][0], universityinfo[9][1], universityinfo[9][2], universityinfo[9][3], universityinfo[9][4], universityinfo[9][5]]

                if type(universityinfo[12]) == str:
                    days4 = universityinfo[12].split(",")
                else:
                    days4 = [universityinfo[12][0], universityinfo[12][1], universityinfo[12][2], universityinfo[12][3], universityinfo[12][4], universityinfo[12][5]]

                if days1[0] == "[True" or days1[0] == True:
                    self.monday_var_1color.background_color = color1
                else:
                    self.monday_var_1color.background_color = [1, 1, 1, 1]

                if days1[1] == " True" or days1[1] == True:
                    self.tuesday_var_1color.background_color = color1
                else:
                    self.tuesday_var_1color.background_color = [1, 1, 1, 1]

                if days1[2] == " True" or days1[2] == True:
                    self.wednesday_var_1color.background_color = color1
                else:
                    self.wednesday_var_1color.background_color = [1, 1, 1, 1]

                if days1[3] == " True" or days1[3] == True:
                    self.thursday_var_1color.background_color = color1
                else:
                    self.thursday_var_1color.background_color = [1, 1, 1, 1]

                if days1[4] == " True" or days1[4] == True:
                    self.friday_var_1color.background_color = color1
                else:
                    self.friday_var_1color.background_color = [1, 1, 1, 1]

                if days1[5] == " True]" or days1[5] == True:
                    self.saturday_var_1color.background_color = color1
                else:
                    self.saturday_var_1color.background_color = [1, 1, 1, 1]

                if days2[0] == "[True" or days2[0] == True:
                    self.monday_var_2color.background_color = color2
                else:
                    self.monday_var_2color.background_color = [1, 1, 1, 1]

                if days2[1] == " True" or days2[1] == True:
                    self.tuesday_var_2color.background_color = color2
                else:
                    self.tuesday_var_2color.background_color = [1, 1, 1, 1]

                if days2[2] == " True" or days2[2] == True:
                    self.wednesday_var_2color.background_color = color2
                else:
                    self.wednesday_var_2color.background_color = [1, 1, 1, 1]

                if days2[3] == " True" or days2[3] == True:
                    self.thursday_var_2color.background_color = color2
                else:
                    self.thursday_var_2color.background_color = [1, 1, 1, 1]

                if days2[4] == " True" or days2[4] == True:
                    self.friday_var_2color.background_color = color2
                else:
                    self.friday_var_2color.background_color = [1, 1, 1, 1]

                if days2[5] == " True]" or days2[5] == True:
                    self.saturday_var_2color.background_color = color2
                else:
                    self.saturday_var_2color.background_color = [1, 1, 1, 1]

                if days3[0] == "[True" or days3[0] == True:
                    self.monday_var_3color.background_color = color3
                else:
                    self.monday_var_3color.background_color = [1, 1, 1, 1]

                if days3[1] == " True" or days3[1] == True:
                    self.tuesday_var_3color.background_color = color3
                else:
                    self.tuesday_var_3color.background_color = [1, 1, 1, 1]

                if days3[2] == " True" or days3[2] == True:
                    self.wednesday_var_3color.background_color = color3
                else:
                    self.wednesday_var_3color.background_color = [1, 1, 1, 1]

                if days3[3] == " True" or days3[3] == True:
                    self.thursday_var_3color.background_color = color3
                else:
                    self.thursday_var_3color.background_color = [1, 1, 1, 1]

                if days3[4] == " True" or days3[4] == True:
                    self.friday_var_3color.background_color = color3
                else:
                    self.friday_var_3color.background_color = [1, 1, 1, 1]

                if days3[5] == " True]" or days3[5] == True:
                    self.saturday_var_3color.background_color = color3
                else:
                    self.saturday_var_3color.background_color = [1, 1, 1, 1]

                if days4[0] == "[True" or days4[0] == True:
                    self.monday_var_4color.background_color = color4
                else:
                    self.monday_var_4color.background_color = [1, 1, 1, 1]

                if days4[1] == " True" or days4[1] == True:
                    self.tuesday_var_4color.background_color = color4
                else:
                    self.tuesday_var_4color.background_color = [1, 1, 1, 1]

                if days4[2] == " True" or days4[2] == True:
                    self.wednesday_var_4color.background_color = color4
                else:
                    self.wednesday_var_4color.background_color = [1, 1, 1, 1]

                if days4[3] == " True" or days4[3] == True:
                    self.thursday_var_4color.background_color = color4
                else:
                    self.thursday_var_4color.background_color = [1, 1, 1, 1]

                if days4[4] == " True" or days4[4] == True:
                    self.friday_var_4color.background_color = color4
                else:
                    self.friday_var_4color.background_color = [1, 1, 1, 1]

                if days4[5] == " True]" or days4[5] == True:
                    self.saturday_var_4color.background_color = color4
                else:
                    self.saturday_var_4color.background_color = [1, 1, 1, 1]

        except:
            pass

    def on_monday(self):
        global dayid
        dayid = 1

    def on_tuesday(self):
        global dayid
        dayid = 2

    def on_wednesday(self):
        global dayid
        dayid = 3

    def on_thursday(self):
        global dayid
        dayid = 4

    def on_friday(self):
        global dayid
        dayid = 5

    def on_saturday(self):
        global dayid
        dayid = 6

    def set_next_week(self):
        global weeksinfo
        global next_weekinfo
        global isnext_week

        was_changes = False

        nextweek = 100 * (int(next_weekinfo) % 2)
        nowweek = 100 * (int(weeksinfo[0]) % 2)

        if not isnext_week:
            isnext_week = True
            was_changes = True

            self.monday_var.text = NextMonday + "\n" + dayinfo[1 + nextweek] + "\n" + dayinfo[2 + nextweek] + "\n" + dayinfo[3 + nextweek] + "\n" + dayinfo[4 + nextweek] + "\n" + dayinfo[5 + nextweek] + "\n" + dayinfo[6 + nextweek] + "\n" + dayinfo[7 + nextweek]
            self.monday_var.background_color = BackgroundsColors[0]

            self.tuesday_var.text = NextTuesday + "\n" + dayinfo[11 + nextweek] + "\n" + dayinfo[12 + nextweek] + "\n" + dayinfo[13 + nextweek] + "\n" + dayinfo[14 + nextweek] + "\n" + dayinfo[15 + nextweek] + "\n" + dayinfo[16 + nextweek] + "\n" + dayinfo[17 + nextweek]
            self.tuesday_var.background_color = BackgroundsColors[1]

            self.thursday_var.text = NextThursday + "\n" + dayinfo[31 + nextweek] + "\n" + dayinfo[32 + nextweek] + "\n" + dayinfo[33 + nextweek] + "\n" + dayinfo[34 + nextweek] + "\n" + dayinfo[35 + nextweek] + "\n" + dayinfo[36 + nextweek] + "\n" + dayinfo[37 + nextweek]
            self.thursday_var.background_color = BackgroundsColors[3]

            self.wednesday_var.text = NextWednesday + "\n" + dayinfo[21 + nextweek] + "\n" + dayinfo[22 + nextweek] + "\n" + dayinfo[23 + nextweek] + "\n" + dayinfo[24 + nextweek] + "\n" + dayinfo[25 + nextweek] + "\n" + dayinfo[26 + nextweek] + "\n" + dayinfo[27 + nextweek]
            self.wednesday_var.background_color = BackgroundsColors[2]

            self.thursday_var.text = NextThursday + "\n" + dayinfo[31 + nextweek] + "\n" + dayinfo[32 + nextweek] + "\n" + dayinfo[33 + nextweek] + "\n" + dayinfo[34 + nextweek] + "\n" + dayinfo[35 + nextweek] + "\n" + dayinfo[36 + nextweek] + "\n" + dayinfo[37 + nextweek]
            self.thursday_var.background_color = BackgroundsColors[3]

            self.friday_var.text = NextFriday + "\n" + dayinfo[41 + nextweek] + "\n" + dayinfo[42 + nextweek] + "\n" + dayinfo[43 + nextweek] + "\n" + dayinfo[44 + nextweek] + "\n" + dayinfo[45 + nextweek] + "\n" + dayinfo[46 + nextweek] + "\n" + dayinfo[47 + nextweek]
            self.friday_var.background_color = BackgroundsColors[4]

            self.saturday_var.text = NextSaturday + "\n" + dayinfo[51 + nextweek] + "\n" + dayinfo[52 + nextweek] + "\n" + dayinfo[53 + nextweek] + "\n" + dayinfo[54 + nextweek] + "\n" + dayinfo[55 + nextweek] + "\n" + dayinfo[56 + nextweek] + "\n" + dayinfo[57 + nextweek]
            self.saturday_var.background_color = BackgroundsColors[5]

        if isnext_week and not was_changes:
            isnext_week = False
            self.monday_var.text = Monday + "\n" + dayinfo[1 + nowweek] + "\n" + dayinfo[2 + nowweek] + "\n" + dayinfo[3 + nowweek] + "\n" + dayinfo[4 + nowweek] + "\n" + dayinfo[5 + nowweek] + "\n" + dayinfo[6 + nowweek] + "\n" + dayinfo[7 + nowweek]
            self.monday_var.background_color = BackgroundsColors[0]

            self.tuesday_var.text = Tuesday + "\n" + dayinfo[11 + nowweek] + "\n" + dayinfo[12 + nowweek] + "\n" + dayinfo[13 + nowweek] + "\n" + dayinfo[14 + nowweek] + "\n" + dayinfo[15 + nowweek] + "\n" + dayinfo[16 + nowweek] + "\n" + dayinfo[17 + nowweek]
            self.tuesday_var.background_color = BackgroundsColors[1]

            self.thursday_var.text = Thursday + "\n" + dayinfo[31 + nowweek] + "\n" + dayinfo[32 + nowweek] + "\n" + dayinfo[33 + nowweek] + "\n" + dayinfo[34 + nowweek] + "\n" + dayinfo[35 + nowweek] + "\n" + dayinfo[36 + nowweek] + "\n" + dayinfo[37 + nowweek]
            self.thursday_var.background_color = BackgroundsColors[3]

            self.wednesday_var.text = Wednesday + "\n" + dayinfo[21 + nowweek] + "\n" + dayinfo[22 + nowweek] + "\n" + dayinfo[23 + nowweek] + "\n" + dayinfo[24 + nowweek] + "\n" + dayinfo[25 + nowweek] + "\n" + dayinfo[26 + nowweek] + "\n" + dayinfo[27 + nowweek]
            self.wednesday_var.background_color = BackgroundsColors[2]

            self.thursday_var.text = Thursday + "\n" + dayinfo[31 + nowweek] + "\n" + dayinfo[32 + nowweek] + "\n" + dayinfo[33 + nowweek] + "\n" + dayinfo[34 + nowweek] + "\n" + dayinfo[35 + nowweek] + "\n" + dayinfo[36 + nowweek] + "\n" + dayinfo[37 + nowweek]
            self.thursday_var.background_color = BackgroundsColors[3]

            self.friday_var.text = Friday + "\n" + dayinfo[41 + nowweek] + "\n" + dayinfo[42 + nowweek] + "\n" + dayinfo[43 + nowweek] + "\n" + dayinfo[44 + nowweek] + "\n" + dayinfo[45 + nowweek] + "\n" + dayinfo[46 + nowweek] + "\n" + dayinfo[47 + nowweek]
            self.friday_var.background_color = BackgroundsColors[4]

            self.saturday_var.text = Saturday + "\n" + dayinfo[51 + nowweek] + "\n" + dayinfo[52 + nowweek] + "\n" + dayinfo[53 + nowweek] + "\n" + dayinfo[54 + nowweek] + "\n" + dayinfo[55 + nowweek] + "\n" + dayinfo[56 + nowweek] + "\n" + dayinfo[57 + nowweek]
            self.saturday_var.background_color = BackgroundsColors[5]


class AddUniversityWindow(Screen):
    global university_amount
    color_button_index = 0
    day_button_indexes = [False for i in range(6)]
    can_add_university = True
    button_var1_color = [0, 0, 1, 1]
    button_var2_color = [0, 1, 0, 1]
    button_var3_color = [1, 0, 0, 1]
    button_var4_color = [1, 1, 0, 1]
    button_var5_color = [1, 0, 1, 1]
    button_var6_color = [0, 1, 1, 1]

    def on_enter(self):
        self.day_button_indexes = [False for i in range(6)]

        if str(universityinfo[2]) == "[0, 0, 1, 1]" or str(universityinfo[5]) == "[0, 0, 1, 1]" or str(universityinfo[8]) == "[0, 0, 1, 1]" or str(universityinfo[11]) == "[0, 0, 1, 1]":
            self.button_var1.background_color = [0.5, 0.5, 1, 1]
            self.button_var1_color = [0.5, 0.5, 1, 1]
        else:
            self.button_var1.background_color = [0, 0, 1, 1]
            self.button_var1_color = [0, 0, 1, 1]

        if str(universityinfo[2]) == "[0, 1, 0, 1]" or str(universityinfo[5]) == "[0, 1, 0, 1]" or str(universityinfo[8]) == "[0, 1, 0, 1]" or str(universityinfo[11]) == "[0, 1, 0, 1]":
            self.button_var2.background_color = [0.5, 1, 0.5, 1]
            self.button_var2_color = [0.5, 1, 0.5, 1]
        else:
            self.button_var2.background_color = [0, 1, 0, 1]
            self.button_var2_color = [0, 1, 0, 1]

        if str(universityinfo[2]) == "[1, 0, 0, 1]" or str(universityinfo[5]) == "[1, 0, 0, 1]" or str(universityinfo[8]) == "[1, 0, 0, 1]" or str(universityinfo[11]) == "[1, 0, 0, 1]":
            self.button_var3.background_color = [0.5, 0.5, 1, 1]
            self.button_var3_color = [0.5, 0.5, 1, 1]
        else:
            self.button_var3.background_color = [1, 0, 0, 1]
            self.button_var3_color = [1, 0, 0, 1]

        if str(universityinfo[2]) == "[1, 1, 0, 1]" or str(universityinfo[5]) == "[1, 1, 0, 1]" or str(universityinfo[8]) == "[1, 1, 0, 1]" or str(universityinfo[11]) == "[1, 1, 0, 1]":
            self.button_var4.background_color = [1, 1, 0.8, 1]
            self.button_var4_color = [1, 1, 0.8, 1]
        else:
            self.button_var4.background_color = [1, 1, 0, 1]
            self.button_var4_color = [1, 1, 0, 1]

        if str(universityinfo[2]) == "[1, 0, 1, 1]" or str(universityinfo[5]) == "[1, 0, 1, 1]" or str(universityinfo[8]) == "[1, 0, 1, 1]" or str(universityinfo[11]) == "[1, 0, 1, 1]":
            self.button_var5.background_color = [1, 0.8, 1, 1]
            self.button_var5_color = [1, 0.8, 1, 1]
        else:
            self.button_var5.background_color = [1, 0, 1, 1]
            self.button_var5_color = [1, 0, 1, 1]

        if str(universityinfo[2]) == "[0, 1, 1, 1]" or str(universityinfo[5]) == "[0, 1, 1, 1]" or str(universityinfo[8]) == "[0, 1, 1, 1]" or str(universityinfo[11]) == "[0, 1, 1, 1]":
            self.button_var6.background_color = [0.8, 1, 1, 1]
            self.button_var6_color = [0.8, 1, 1, 1]
        else:
            self.button_var6.background_color = [0, 1, 1, 1]
            self.button_var6_color = [0, 1, 1, 1]

        self.button_var7.background_color = [1, 1, 1, 1]
        self.button_var8.background_color = [1, 1, 1, 1]
        self.button_var9.background_color = [1, 1, 1, 1]
        self.button_var10.background_color = [1, 1, 1, 1]
        self.button_var11.background_color = [1, 1, 1, 1]
        self.button_var12.background_color = [1, 1, 1, 1]

        if int(university_amount) >= 13:
            self.text_input_var.text = "Больше нельзя добавить"
            self.can_add_university = False

        else:
            self.text_input_var.text = ""

    def set_butonncolor(self, button_index):

        if button_index == 1:
            self.button_var1.background_color = [0.5, 0.5, 1, 1]
            self.button_var2.background_color = self.button_var2_color
            self.button_var3.background_color = self.button_var3_color
            self.button_var4.background_color = self.button_var4_color
            self.button_var5.background_color = self.button_var5_color
            self.button_var6.background_color = self.button_var6_color
            self.color_button_index = self.button_var1

        if button_index == 2:
            self.button_var1.background_color = self.button_var1_color
            self.button_var2.background_color = [0.5, 1, 0.5, 1]
            self.button_var3.background_color = self.button_var3_color
            self.button_var4.background_color = self.button_var4_color
            self.button_var5.background_color = self.button_var5_color
            self.button_var6.background_color = self.button_var6_color
            self.color_button_index = self.button_var2

        if button_index == 3:
            self.button_var1.background_color = self.button_var1_color
            self.button_var2.background_color = self.button_var2_color
            self.button_var3.background_color = [1, 0.5, 0.5, 1]
            self.button_var4.background_color = self.button_var4_color
            self.button_var5.background_color = self.button_var5_color
            self.button_var6.background_color = self.button_var6_color
            self.color_button_index = self.button_var3

        if button_index == 4:
            self.button_var1.background_color = self.button_var1_color
            self.button_var2.background_color = self.button_var2_color
            self.button_var3.background_color = self.button_var3_color
            self.button_var4.background_color = [1, 1, 0.8, 1]
            self.button_var5.background_color = self.button_var5_color
            self.button_var6.background_color = self.button_var6_color
            self.color_button_index = self.button_var4

        if button_index == 5:
            self.button_var1.background_color = self.button_var1_color
            self.button_var2.background_color = self.button_var2_color
            self.button_var3.background_color = self.button_var3_color
            self.button_var4.background_color = self.button_var4_color
            self.button_var5.background_color = [1, 0.8, 1, 1]
            self.button_var6.background_color = self.button_var6_color
            self.color_button_index = self.button_var5

        if button_index == 6:
            self.button_var1.background_color = self.button_var1_color
            self.button_var2.background_color = self.button_var2_color
            self.button_var3.background_color = self.button_var3_color
            self.button_var4.background_color = self.button_var4_color
            self.button_var5.background_color = self.button_var5_color
            self.button_var6.background_color = [0.8, 1, 1, 1]
            self.color_button_index = self.button_var6

        if button_index == 7:
            if self.button_var7.background_color == [1, 1, 1, 1]:
                self.button_var7.background_color = [0, 0, 1, 1]
                self.day_button_indexes[0] = True

            else:
                self.button_var7.background_color = [1, 1, 1, 1]
                self.day_button_indexes[0] = False

        if button_index == 8:
            if self.button_var8.background_color == [1, 1, 1, 1]:
                self.button_var8.background_color = [0, 0, 1, 1]
                self.day_button_indexes[1] = True
            else:
                self.button_var8.background_color = [1, 1, 1, 1]
                self.day_button_indexes[1] = False

        if button_index == 9:
            if self.button_var9.background_color == [1, 1, 1, 1]:
                self.button_var9.background_color = [0, 0, 1, 1]
                self.day_button_indexes[2] = True

            else:
                self.button_var9.background_color = [1, 1, 1, 1]
                self.day_button_indexes[2] = False

        if button_index == 10:
            if self.button_var10.background_color == [1, 1, 1, 1]:
                self.button_var10.background_color = [0, 0, 1, 1]
                self.day_button_indexes[3] = True

            else:
                self.button_var10.background_color = [1, 1, 1, 1]
                self.day_button_indexes[3] = False

        if button_index == 11:
            if self.button_var11.background_color == [1, 1, 1, 1]:
                self.button_var11.background_color = [0, 0, 1, 1]
                self.day_button_indexes[4] = True

            else:
                self.button_var11.background_color = [1, 1, 1, 1]
                self.day_button_indexes[4] = False

        if button_index == 12:
            if self.button_var12.background_color == [1, 1, 1, 1]:
                self.button_var12.background_color = [0, 0, 1, 1]
                self.day_button_indexes[5] = True

            else:
                self.button_var12.background_color = [1, 1, 1, 1]
                self.day_button_indexes[5] = False

    def set_university_values(self):
        global university_amount

        if self.day_button_indexes[0] == True or self.day_button_indexes[1] == True or self.day_button_indexes[2] == True or self.day_button_indexes[3] == True or self.day_button_indexes[4] == True or self.day_button_indexes[5] == True:
            print("|dsfgdsfgs")
            if type(self.color_button_index) != int and self.text_input_var.text != "" and int(universityinfo[0]) != 13 and self.can_add_university and str(self.color_button_index.base_color) != str(universityinfo[2]) and str(self.color_button_index.base_color) != str(universityinfo[5]) and str(self.color_button_index.base_color) != str(universityinfo[8]) and str(self.color_button_index.base_color) != str(universityinfo[11]):
                universityinfo[0] = str(int(universityinfo[0]) + 3)
                universityinfo[int(university_amount)] = self.text_input_var.text
                universityinfo[int(university_amount) + 1] = self.color_button_index.base_color
                universityinfo[int(university_amount) + 2] = self.day_button_indexes
                university_amount = int(university_amount) + 3
                os.remove("UniversityInfo.txt")
                UniversityInfo = open("UniversityInfo.txt", "w")

                for i in universityinfo:
                    UniversityInfo.writelines(str(i) + "\n")
                UniversityInfo.close()


class ChangeUniversityWindow(Screen):
    global university_amount
    week_days = 0
    days1 = 0
    days2 = 0
    days3 = 0
    days4 = 0
    text1 = 0
    text2 = 0
    text3 = 0
    text4 = 0

    def on_enter(self):

        if university_amount == 1:
            self.box_var1.opacity = 0
            self.box_var2.opacity = 0
            self.box_var3.opacity = 0
            self.box_var4.opacity = 0

        if university_amount == 4:
            self.box_var2.opacity = 0
            self.box_var3.opacity = 0
            self.box_var4.opacity = 0

        if university_amount == 7:
            self.box_var3.opacity = 0
            self.box_var4.opacity = 0

        if university_amount == 10:
            self.box_var4.opacity = 0

        if university_amount != 1:
            self.week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
            self.days1 = str(universityinfo[3])[1:len(str(universityinfo[3])) - 1].split(", ")
            self.days2 = str(universityinfo[6])[1:len(str(universityinfo[6])) - 1].split(", ")
            self.days3 = str(universityinfo[9])[1:len(str(universityinfo[9])) - 1].split(", ")
            self.days4 = str(universityinfo[12])[1:len(str(universityinfo[12])) - 1].split(", ")
            self.text1 = ""
            self.text2 = ""
            self.text3 = ""
            self.text4 = ""

        if university_amount == "4" or university_amount == 4:
            self.text1 += universityinfo[1]
            count1 = 0
            for i in range(len(self.days1)):
                if self.days1[i] == "True":
                    count1 += 1
                    if count1 == 3:
                        self.text1 += "\n"
                    else:
                        self.text1 += " "
                    self.text1 += self.week_days[i]

            self.box_var1.opacity = 100
            self.button_var1.text = self.text1

            self.color_button_var1.background_color = str(universityinfo[2])[1:len(str(universityinfo[2])) - 1].split(", ")

        if university_amount == "7" or university_amount == 7:
            self.text1 += universityinfo[1]
            self.text2 += universityinfo[4]
            count1 = 0
            count2 = 0

            for i in range(len(self.days1)):
                if self.days1[i] == "True":
                    count1 += 1
                    if count1 == 3:
                        self.text1 += "\n"
                    else:
                        self.text1 += " "
                    self.text1 += self.week_days[i]

                if self.days2[i] == "True":
                    count2 += 1
                    if count2 == 3:
                        self.text2 += "\n"
                    else:
                        self.text2 += " "
                    self.text2 += self.week_days[i]

            self.box_var1.opacity = 100
            self.button_var1.text = self.text1
            self.box_var2.opacity = 100
            self.button_var2.text = self.text2

            self.color_button_var1.background_color = str(universityinfo[2])[1:len(str(universityinfo[2])) - 1].split(", ")
            self.color_button_var2.background_color = str(universityinfo[5])[1:len(str(universityinfo[5])) - 1].split(", ")

        if university_amount == "10" or university_amount == 10:
            self.text1 += universityinfo[1]
            self.text2 += universityinfo[4]
            self.text3 += universityinfo[7]
            count1 = 0
            count2 = 0
            count3 = 0

            for i in range(len(self.days1)):
                if self.days1[i] == "True":
                    count1 += 1
                    if count1 == 3:
                        self.text1 += "\n"
                    else:
                        self.text1 += " "
                    self.text1 += self.week_days[i]

                if self.days2[i] == "True":
                    count2 += 1
                    if count2 == 3:
                        self.text2 += "\n"
                    else:
                        self.text2 += " "
                    self.text2 += self.week_days[i]

                if self.days3[i] == "True":
                    count3 += 1
                    if count3 == 3:
                        self.text3 += "\n"
                    else:
                        self.text3 += " "
                    self.text3 += self.week_days[i]

            self.box_var1.opacity = 100
            self.button_var1.text = self.text1
            self.box_var2.opacity = 100
            self.button_var2.text = self.text2
            self.box_var3.opacity = 100
            self.button_var3.text = self.text3

            self.color_button_var1.background_color = str(universityinfo[2])[1:len(str(universityinfo[2])) - 1].split(", ")
            self.color_button_var2.background_color = str(universityinfo[5])[1:len(str(universityinfo[5])) - 1].split(", ")
            self.color_button_var3.background_color = str(universityinfo[8])[1:len(str(universityinfo[8])) - 1].split(", ")

        if university_amount == "13" or university_amount == 13:
            self.text1 += universityinfo[1]
            self.text2 += universityinfo[4]
            self.text3 += universityinfo[7]
            self.text4 += universityinfo[10]
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0

            for i in range(len(self.days1)):
                if self.days1[i] == "True":
                    count1 += 1
                    if count1 == 3:
                        self.text1 += "\n"
                    else:
                        self.text1 += " "
                    self.text1 += self.week_days[i]

                if self.days2[i] == "True":
                    count2 += 1
                    if count2 == 3:
                        self.text2 += "\n"
                    else:
                        self.text2 += " "
                    self.text2 += self.week_days[i]

                if self.days3[i] == "True":
                    count3 += 1
                    if count3 == 3:
                        self.text3 += "\n"
                    else:
                        self.text3 += " "
                    self.text3 += self.week_days[i]

                if self.days4[i] == "True":
                    count4 += 1
                    if count4 == 3:
                        self.text4 += "\n"
                    else:
                        self.text4 += " "
                    self.text4 += self.week_days[i]

            self.box_var1.opacity = 100
            self.button_var1.text = self.text1
            self.box_var2.opacity = 100
            self.button_var2.text = self.text2
            self.box_var3.opacity = 100
            self.button_var3.text = self.text3
            self.box_var4.opacity = 100
            self.button_var4.text = self.text4

            self.color_button_var1.background_color = str(universityinfo[2])[1:len(str(universityinfo[2])) - 1].split(", ")
            self.color_button_var2.background_color = str(universityinfo[5])[1:len(str(universityinfo[5])) - 1].split(", ")
            self.color_button_var3.background_color = str(universityinfo[8])[1:len(str(universityinfo[8])) - 1].split(", ")
            self.color_button_var4.background_color = str(universityinfo[11])[1:len(str(universityinfo[11])) - 1].split(", ")

    def on_leave(self):
        self.text1 = ""
        self.text2 = ""
        self.text3 = ""
        self.text4 = ""

    def set_1university_id(self):
        global university_deleteid
        university_deleteid = 1

    def set_2university_id(self):
        global university_deleteid
        university_deleteid = 4

    def set_3university_id(self):
        global university_deleteid
        university_deleteid = 7

    def set_4university_id(self):
        global university_deleteid
        university_deleteid = 10


class ChangeDayInfoWindow(Screen):
    def on_enter(self):
        global weeksinfo
        global isnext_week
        global next_weekinfo

        if isnext_week:
            week = 100 * (int(next_weekinfo) % 2)
        else:
            week = 100 * (int(weeksinfo[0]) % 2)

        if dayid == 1:
            self.first_text.text = dayinfo[1 + week]
            self.second_text.text = dayinfo[2 + week]
            self.third_text.text = dayinfo[3 + week]
            self.fourth_text.text = dayinfo[4 + week]
            self.fifth_text.text = dayinfo[5 + week]
            self.sixth_text.text = dayinfo[6 + week]
            self.seventh_text.text = dayinfo[7 + week]
        if dayid == 2:
            self.first_text.text = dayinfo[11 + week]
            self.second_text.text = dayinfo[12 + week]
            self.third_text.text = dayinfo[13 + week]
            self.fourth_text.text = dayinfo[14 + week]
            self.fifth_text.text = dayinfo[15 + week]
            self.sixth_text.text = dayinfo[16 + week]
            self.seventh_text.text = dayinfo[17 + week]
        if dayid == 3:
            self.first_text.text = dayinfo[21 + week]
            self.second_text.text = dayinfo[22 + week]
            self.third_text.text = dayinfo[23 + week]
            self.fourth_text.text = dayinfo[24 + week]
            self.fifth_text.text = dayinfo[25 + week]
            self.sixth_text.text = dayinfo[26 + week]
            self.seventh_text.text = dayinfo[27 + week]
        if dayid == 4:
            self.first_text.text = dayinfo[31 + week]
            self.second_text.text = dayinfo[32 + week]
            self.third_text.text = dayinfo[33 + week]
            self.fourth_text.text = dayinfo[34 + week]
            self.fifth_text.text = dayinfo[35 + week]
            self.sixth_text.text = dayinfo[36 + week]
            self.seventh_text.text = dayinfo[37 + week]
        if dayid == 5:
            self.first_text.text = dayinfo[41 + week]
            self.second_text.text = dayinfo[42 + week]
            self.third_text.text = dayinfo[43 + week]
            self.fourth_text.text = dayinfo[44 + week]
            self.fifth_text.text = dayinfo[45 + week]
            self.sixth_text.text = dayinfo[46 + week]
            self.seventh_text.text = dayinfo[47 + week]
        if dayid == 6:
            self.first_text.text = dayinfo[51 + week]
            self.second_text.text = dayinfo[52 + week]
            self.third_text.text = dayinfo[53 + week]
            self.fourth_text.text = dayinfo[54 + week]
            self.fifth_text.text = dayinfo[55 + week]
            self.sixth_text.text = dayinfo[56 + week]
            self.seventh_text.text = dayinfo[57 + week]

    def set_values(self):
        global weeksinfo
        global isnext_week
        global next_weekinfo

        if isnext_week:
            week = 100 * (int(next_weekinfo) % 2)
        else:
            week = 100 * (int(weeksinfo[0]) % 2)

        if dayid == 1:
            self.parent.calendar_var.monday_var.text = Monday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[1 + week] = self.first_text.text
            dayinfo[2 + week] = self.second_text.text
            dayinfo[3 + week] = self.third_text.text
            dayinfo[4 + week] = self.fourth_text.text
            dayinfo[5 + week] = self.fifth_text.text
            dayinfo[6 + week] = self.sixth_text.text
            dayinfo[7 + week] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 2:
            self.parent.calendar_var.tuesday_var.text = Tuesday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[11 + week] = self.first_text.text
            dayinfo[12 + week] = self.second_text.text
            dayinfo[13 + week] = self.third_text.text
            dayinfo[14 + week] = self.fourth_text.text
            dayinfo[15 + week] = self.fifth_text.text
            dayinfo[16 + week] = self.sixth_text.text
            dayinfo[17 + week] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                if i != "\n":
                    DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 3:
            self.parent.calendar_var.wednesday_var.text = Wednesday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[21 + week] = self.first_text.text
            dayinfo[22 + week] = self.second_text.text
            dayinfo[23 + week] = self.third_text.text
            dayinfo[24 + week] = self.fourth_text.text
            dayinfo[25 + week] = self.fifth_text.text
            dayinfo[26 + week] = self.sixth_text.text
            dayinfo[27 + week] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                if i != "\n":
                    DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 4:
            self.parent.calendar_var.thursday_var.text = Thursday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[31 + week] = self.first_text.text
            dayinfo[32 + week] = self.second_text.text
            dayinfo[33 + week] = self.third_text.text
            dayinfo[34 + week] = self.fourth_text.text
            dayinfo[35 + week] = self.fifth_text.text
            dayinfo[36 + week] = self.sixth_text.text
            dayinfo[37 + week] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                if i != "\n":
                    DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 5:
            self.parent.calendar_var.friday_var.text = Friday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[41 + week] = self.first_text.text
            dayinfo[42 + week] = self.second_text.text
            dayinfo[43 + week] = self.third_text.text
            dayinfo[44 + week] = self.fourth_text.text
            dayinfo[45 + week] = self.fifth_text.text
            dayinfo[46 + week] = self.sixth_text.text
            dayinfo[47 + week] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                if i != "\n":
                    DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 6:
            self.parent.calendar_var.saturday_var.text = Saturday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[51 + week] = self.first_text.text
            dayinfo[52 + week] = self.second_text.text
            dayinfo[53 + week] = self.third_text.text
            dayinfo[54 + week] = self.fourth_text.text
            dayinfo[55 + week] = self.fifth_text.text
            dayinfo[56 + week] = self.sixth_text.text
            dayinfo[57 + week] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                if i != "\n":
                    DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()


class DeleteUniversityWindow(Screen):
    global university_deleteid

    def delete_university(self):
        global university_amount
        global universityinfo

        university_amount = int(university_amount) - 3
        universityinfo[0] = int(universityinfo[0]) - 3
        universityinfo[university_deleteid] = "1"
        universityinfo[university_deleteid + 1] = "1"
        universityinfo[university_deleteid + 2] = "1"

        universityinfo_cop = []
        count = 0
        for i in range(0, 15):
            if universityinfo[i] != "1" and universityinfo[i] != 1:
                universityinfo_cop.append(universityinfo[i])
            if universityinfo[i] == "1" or universityinfo[i] == 1:
                count += 1

        for i in range(count):
            universityinfo_cop.append("1")

        universityinfo = universityinfo_cop

        os.remove("UniversityInfo.txt")
        UniversityInfo = open("UniversityInfo.txt", "w")

        for i in universityinfo:
            UniversityInfo.writelines(str(i) + "\n")
        UniversityInfo.close()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("sborka.kv")


class SborkaApp(App):

    def build(self):
        return kv

    def on_start(self):
        global weeksinfo
        week = 100 * (int(weeksinfo[0]) % 2)

        self.root.calendar_var.monday_var.text = Monday + "\n" + dayinfo[1 + week] + "\n" + dayinfo[2 + week] + "\n" + dayinfo[3 + week] + "\n" + dayinfo[4 + week] + "\n" + dayinfo[5 + week] + "\n" + dayinfo[6 + week] + "\n" + dayinfo[7 + week]
        self.root.calendar_var.monday_var.background_color = BackgroundsColors[0]

        self.root.calendar_var.tuesday_var.text = Tuesday + "\n" + dayinfo[11 + week] + "\n" + dayinfo[12 + week] + "\n" + dayinfo[13 + week] + "\n" + dayinfo[14 + week] + "\n" + dayinfo[15 + week] + "\n" + dayinfo[16 + week] + "\n" + dayinfo[17 + week]
        self.root.calendar_var.tuesday_var.background_color = BackgroundsColors[1]

        self.root.calendar_var.wednesday_var.text = Wednesday + "\n" + dayinfo[21 + week] + "\n" + dayinfo[22 + week] + "\n" + dayinfo[23 + week] + "\n" + dayinfo[24 + week] + "\n" + dayinfo[25 + week] + "\n" + dayinfo[26 + week] + "\n" + dayinfo[27 + week]
        self.root.calendar_var.wednesday_var.background_color = BackgroundsColors[2]

        self.root.calendar_var.thursday_var.text = Thursday + "\n" + dayinfo[31 + week] + "\n" + dayinfo[32 + week] + "\n" + dayinfo[33 + week] + "\n" + dayinfo[34 + week] + "\n" + dayinfo[35 + week] + "\n" + dayinfo[36 + week] + "\n" + dayinfo[37 + week]
        self.root.calendar_var.thursday_var.background_color = BackgroundsColors[3]

        self.root.calendar_var.friday_var.text = Friday + "\n" + dayinfo[41 + week] + "\n" + dayinfo[42 + week] + "\n" + dayinfo[43 + week] + "\n" + dayinfo[44 + week] + "\n" + dayinfo[45 + week] + "\n" + dayinfo[46 + week] + "\n" + dayinfo[47 + week]
        self.root.calendar_var.friday_var.background_color = BackgroundsColors[4]

        self.root.calendar_var.saturday_var.text = Saturday + "\n" + dayinfo[51 + week] + "\n" + dayinfo[52 + week] + "\n" + dayinfo[53 + week] + "\n" + dayinfo[54 + week] + "\n" + dayinfo[55 + week] + "\n" + dayinfo[56 + week] + "\n" + dayinfo[57 + week]
        self.root.calendar_var.saturday_var.background_color = BackgroundsColors[5]

        if university_amount == 4 or university_amount == "4":
            color = [universityinfo[2][1], universityinfo[2][4], universityinfo[2][7], universityinfo[2][10]]
            days = universityinfo[3].split(",")

            if days[0] == "[True":
                self.root.calendar_var.monday_var_1color.background_color = color

            if days[1] == " True":
                self.root.calendar_var.tuesday_var_1color.background_color = color

            if days[2] == " True":
                self.root.calendar_var.wednesday_var_1color.background_color = color

            if days[3] == " True":
                self.root.calendar_var.thursday_var_1color.background_color = color

            if days[4] == " True":
                self.root.calendar_var.friday_var_1color.background_color = color

            if days[5] == " True]":
                self.root.calendar_var.saturday_var_1color.background_color = color

        if university_amount == 7 or university_amount == "7":
            if type(universityinfo[2]) == str:
                color1 = [universityinfo[2][1], universityinfo[2][4], universityinfo[2][7], universityinfo[2][10]]
            else:
                color1 = [universityinfo[2][0], universityinfo[2][1], universityinfo[2][2], universityinfo[2][3]]

            if type(universityinfo[5]) == str:
                color2 = [universityinfo[5][1], universityinfo[5][4], universityinfo[5][7], universityinfo[5][10]]
            else:
                color2 = [universityinfo[5][0], universityinfo[5][1], universityinfo[5][2], universityinfo[5][3]]

            if type(universityinfo[3]) == str:
                days1 = universityinfo[3].split(",")
            else:
                days1 = [universityinfo[3][0], universityinfo[3][1], universityinfo[3][2], universityinfo[3][3],
                         universityinfo[3][4], universityinfo[3][5]]

            if type(universityinfo[6]) == str:
                days2 = universityinfo[6].split(",")
            else:
                days2 = [universityinfo[6][0], universityinfo[6][1], universityinfo[6][2], universityinfo[6][3],
                         universityinfo[6][4], universityinfo[6][5]]

            if days1[0] == "[True" or days1[0] == True:
                self.root.calendar_var.monday_var_1color.background_color = color1

            if days1[1] == " True" or days1[1] == True:
                self.root.calendar_var.tuesday_var_1color.background_color = color1

            if days1[2] == " True" or days1[2] == True:
                self.root.calendar_var.wednesday_var_1color.background_color = color1

            if days1[3] == " True" or days1[3] == True:
                self.root.calendar_var.thursday_var_1color.background_color = color1

            if days1[4] == " True" or days1[4] == True:
                self.root.calendar_var.friday_var_1color.background_color = color1

            if days1[5] == " True]" or days1[5] == True:
                self.root.calendar_var.saturday_var_1color.background_color = color1

            if days2[0] == "[True" or days2[0] == True:
                self.root.calendar_var.monday_var_2color.background_color = color2

            if days2[1] == " True" or days2[1] == True:
                self.root.calendar_var.tuesday_var_2color.background_color = color2

            if days2[2] == " True" or days2[2] == True:
                self.root.calendar_var.wednesday_var_2color.background_color = color2

            if days2[3] == " True" or days2[3] == True:
                self.root.calendar_var.thursday_var_2color.background_color = color2

            if days2[4] == " True" or days2[4] == True:
                self.root.calendar_var.friday_var_2color.background_color = color2

            if days2[5] == " True]" or days2[5] == True:
                self.root.calendar_var.saturday_var_2color.background_color = color2

        if university_amount == 10 or university_amount == "10":
            if type(universityinfo[2]) == str:
                color1 = [universityinfo[2][1], universityinfo[2][4], universityinfo[2][7], universityinfo[2][10]]
            else:
                color1 = [universityinfo[2][0], universityinfo[2][1], universityinfo[2][2], universityinfo[2][3]]

            if type(universityinfo[5]) == str:
                color2 = [universityinfo[5][1], universityinfo[5][4], universityinfo[5][7], universityinfo[5][10]]
            else:
                color2 = [universityinfo[5][0], universityinfo[5][1], universityinfo[5][2], universityinfo[5][3]]

            if type(universityinfo[8]) == str:
                color3 = [universityinfo[8][1], universityinfo[8][4], universityinfo[8][7], universityinfo[8][10]]
            else:
                color3 = [universityinfo[8][0], universityinfo[8][1], universityinfo[8][2], universityinfo[8][3]]

            if type(universityinfo[3]) == str:
                days1 = universityinfo[3].split(",")
            else:
                days1 = [universityinfo[3][0], universityinfo[3][1], universityinfo[3][2], universityinfo[3][3],
                         universityinfo[3][4], universityinfo[3][5]]

            if type(universityinfo[6]) == str:
                days2 = universityinfo[6].split(",")
            else:
                days2 = [universityinfo[6][0], universityinfo[6][1], universityinfo[6][2], universityinfo[6][3],
                         universityinfo[6][4], universityinfo[6][5]]

            if type(universityinfo[9]) == str:
                days3 = universityinfo[9].split(",")
            else:
                days3 = [universityinfo[9][0], universityinfo[9][1], universityinfo[9][2], universityinfo[9][3],
                         universityinfo[9][4], universityinfo[9][5]]

            if days1[0] == "[True" or days1[0] == True:
                self.root.calendar_var.monday_var_1color.background_color = color1

            if days1[1] == " True" or days1[1] == True:
                self.root.calendar_var.tuesday_var_1color.background_color = color1

            if days1[2] == " True" or days1[2] == True:
                self.root.calendar_var.wednesday_var_1color.background_color = color1

            if days1[3] == " True" or days1[3] == True:
                self.root.calendar_var.thursday_var_1color.background_color = color1

            if days1[4] == " True" or days1[4] == True:
                self.root.calendar_var.friday_var_1color.background_color = color1

            if days1[5] == " True]" or days1[5] == True:
                self.root.calendar_var.saturday_var_1color.background_color = color1

            if days2[0] == "[True" or days2[0] == True:
                self.root.calendar_var.monday_var_2color.background_color = color2

            if days2[1] == " True" or days2[1] == True:
                self.root.calendar_var.tuesday_var_2color.background_color = color2

            if days2[2] == " True" or days2[2] == True:
                self.root.calendar_var.wednesday_var_2color.background_color = color2

            if days2[3] == " True" or days2[3] == True:
                self.root.calendar_var.thursday_var_2color.background_color = color2

            if days2[4] == " True" or days2[4] == True:
                self.root.calendar_var.friday_var_2color.background_color = color2

            if days2[5] == " True]" or days2[5] == True:
                self.root.calendar_var.saturday_var_2color.background_color = color2

            if days3[0] == "[True" or days3[0] == True:
                self.root.calendar_var.monday_var_3color.background_color = color3

            if days3[1] == " True" or days3[1] == True:
                self.root.calendar_var.tuesday_var_3color.background_color = color3

            if days3[2] == " True" or days3[2] == True:
                self.root.calendar_var.wednesday_var_3color.background_color = color3

            if days3[3] == " True" or days3[3] == True:
                self.root.calendar_var.thursday_var_3color.background_color = color3

            if days3[4] == " True" or days3[4] == True:
                self.root.calendar_var.friday_var_3color.background_color = color3

            if days3[5] == " True]" or days3[5] == True:
                self.root.calendar_var.saturday_var_3color.background_color = color3

        if university_amount == 13 or university_amount == "13":
            if type(universityinfo[2]) == str:
                color1 = [universityinfo[2][1], universityinfo[2][4], universityinfo[2][7], universityinfo[2][10]]
            else:
                color1 = [universityinfo[2][0], universityinfo[2][1], universityinfo[2][2], universityinfo[2][3]]

            if type(universityinfo[5]) == str:
                color2 = [universityinfo[5][1], universityinfo[5][4], universityinfo[5][7], universityinfo[5][10]]
            else:
                color2 = [universityinfo[5][0], universityinfo[5][1], universityinfo[5][2], universityinfo[5][3]]

            if type(universityinfo[8]) == str:
                color3 = [universityinfo[8][1], universityinfo[8][4], universityinfo[8][7], universityinfo[8][10]]
            else:
                color3 = [universityinfo[8][0], universityinfo[8][1], universityinfo[8][2], universityinfo[8][3]]

            if type(universityinfo[11]) == str:
                color4 = [universityinfo[11][1], universityinfo[11][4], universityinfo[11][7], universityinfo[11][10]]
            else:
                color4 = [universityinfo[11][0], universityinfo[11][1], universityinfo[11][2], universityinfo[11][3]]

            if type(universityinfo[3]) == str:
                days1 = universityinfo[3].split(",")
            else:
                days1 = [universityinfo[3][0], universityinfo[3][1], universityinfo[3][2], universityinfo[3][3],
                         universityinfo[3][4], universityinfo[3][5]]

            if type(universityinfo[6]) == str:
                days2 = universityinfo[6].split(",")
            else:
                days2 = [universityinfo[6][0], universityinfo[6][1], universityinfo[6][2], universityinfo[6][3],
                         universityinfo[6][4], universityinfo[6][5]]

            if type(universityinfo[9]) == str:
                days3 = universityinfo[9].split(",")
            else:
                days3 = [universityinfo[9][0], universityinfo[9][1], universityinfo[9][2], universityinfo[9][3],
                         universityinfo[9][4], universityinfo[9][5]]

            if type(universityinfo[12]) == str:
                days4 = universityinfo[12].split(",")
            else:
                days4 = [universityinfo[12][0], universityinfo[12][1], universityinfo[12][2], universityinfo[12][3],
                         universityinfo[12][4], universityinfo[12][5]]

            if days1[0] == "[True" or days1[0] == True:
                self.root.calendar_var.monday_var_1color.background_color = color1

            if days1[1] == " True" or days1[1] == True:
                self.root.calendar_var.tuesday_var_1color.background_color = color1

            if days1[2] == " True" or days1[2] == True:
                self.root.calendar_var.wednesday_var_1color.background_color = color1

            if days1[3] == " True" or days1[3] == True:
                self.root.calendar_var.thursday_var_1color.background_color = color1

            if days1[4] == " True" or days1[4] == True:
                self.root.calendar_var.friday_var_1color.background_color = color1

            if days1[5] == " True]" or days1[5] == True:
                self.root.calendar_var.saturday_var_1color.background_color = color1

            if days2[0] == "[True" or days2[0] == True:
                self.root.calendar_var.monday_var_2color.background_color = color2

            if days2[1] == " True" or days2[1] == True:
                self.root.calendar_var.tuesday_var_2color.background_color = color2

            if days2[2] == " True" or days2[2] == True:
                self.root.calendar_var.wednesday_var_2color.background_color = color2

            if days2[3] == " True" or days2[3] == True:
                self.root.calendar_var.thursday_var_2color.background_color = color2

            if days2[4] == " True" or days2[4] == True:
                self.root.calendar_var.friday_var_2color.background_color = color2

            if days2[5] == " True]" or days2[5] == True:
                self.root.calendar_var.saturday_var_2color.background_color = color2

            if days3[0] == "[True" or days3[0] == True:
                self.root.calendar_var.monday_var_3color.background_color = color3

            if days3[1] == " True" or days3[1] == True:
                self.root.calendar_var.tuesday_var_3color.background_color = color3

            if days3[2] == " True" or days3[2] == True:
                self.root.calendar_var.wednesday_var_3color.background_color = color3

            if days3[3] == " True" or days3[3] == True:
                self.root.calendar_var.thursday_var_3color.background_color = color3

            if days3[4] == " True" or days3[4] == True:
                self.root.calendar_var.friday_var_3color.background_color = color3

            if days3[5] == " True]" or days3[5] == True:
                self.root.calendar_var.saturday_var_3color.background_color = color3

            if days4[0] == "[True" or days4[0] == True:
                self.root.calendar_var.monday_var_4color.background_color = color4

            if days4[1] == " True" or days4[1] == True:
                self.root.calendar_var.tuesday_var_4color.background_color = color4

            if days4[2] == " True" or days4[2] == True:
                self.root.calendar_var.wednesday_var_4color.background_color = color4

            if days4[3] == " True" or days4[3] == True:
                self.root.calendar_var.thursday_var_4color.background_color = color4

            if days4[4] == " True" or days4[4] == True:
                self.root.calendar_var.friday_var_4color.background_color = color4

            if days4[5] == " True]" or days4[5] == True:
                self.root.calendar_var.saturday_var_4color.background_color = color4

        if (weeksinfo[0] + 1) % 2 == 0:
            self.root.calendar_var.week_var.text = "                                  четная неделя"

        if (weeksinfo[0] + 1) % 2 == 1:
            self.root.calendar_var.week_var.text = "                                  нечетная неделя"


if __name__ == "__main__":
    SborkaApp().run()

