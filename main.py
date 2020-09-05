from datetime import timedelta, datetime
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

Monday = "Понедельник" + "\n" + str(MonDate.date())[5:7] + " Месяц" + "\n" + str(MonDate.date())[8:10] + " Число"
Tuesday = "Вторник" + "\n" + str((MonDate + timedelta(days=1)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=1)).date())[8:10] + " Число"
Wednesday = "Среда" + "\n" + str((MonDate + timedelta(days=2)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=2)).date())[8:10] + " Число"
Thursday = "Четверг" + "\n" + str((MonDate + timedelta(days=3)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=3)).date())[8:10] + " Число"
Friday = "Пятница" + "\n" + str((MonDate + timedelta(days=4)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=4)).date())[8:10] + " Число"
Saturday = "Суббота" + "\n" + str((MonDate + timedelta(days=5)).date())[5:7] + " Месяц" + "\n" + str((MonDate + timedelta(days=5)).date())[8:10] + " Число"
dayid = 0
university_amount = universityinfo[0]
university_deleteid = -1


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

                if days[1] == " True" or days[1] == True:
                    self.tuesday_var_1color.background_color = color

                if days[2] == " True" or days[2] == True:
                    self.wednesday_var_1color.background_color = color

                if days[3] == " True" or days[3] == True:
                    self.thursday_var_1color.background_color = color

                if days[4] == " True" or days[4] == True:
                    self.friday_var_1color.background_color = color

                if days[5] == " True]" or days[5] == True:
                    self.saturday_var_1color.background_color = color

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

                if days1[1] == " True" or days1[1] == True:
                    self.tuesday_var_1color.background_color = color1

                if days1[2] == " True" or days1[2] == True:
                    self.wednesday_var_1color.background_color = color1

                if days1[3] == " True" or days1[3] == True:
                    self.thursday_var_1color.background_color = color1

                if days1[4] == " True" or days1[4] == True:
                    self.friday_var_1color.background_color = color1

                if days1[5] == " True]" or days1[5] == True:
                    self.saturday_var_1color.background_color = color1

                if days2[0] == "[True" or days2[0] == True:
                    self.monday_var_2color.background_color = color2

                if days2[1] == " True" or days2[1] == True:
                    self.tuesday_var_2color.background_color = color2

                if days2[2] == " True" or days2[2] == True:
                    self.wednesday_var_2color.background_color = color2

                if days2[3] == " True" or days2[3] == True:
                    self.thursday_var_2color.background_color = color2

                if days2[4] == " True" or days2[4] == True:
                    self.friday_var_2color.background_color = color2

                if days2[5] == " True]" or days2[5] == True:
                    self.saturday_var_2color.background_color = color2

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

                if days1[1] == " True" or days1[1] == True:
                    self.tuesday_var_1color.background_color = color1

                if days1[2] == " True" or days1[2] == True:
                    self.wednesday_var_1color.background_color = color1

                if days1[3] == " True" or days1[3] == True:
                    self.thursday_var_1color.background_color = color1

                if days1[4] == " True" or days1[4] == True:
                    self.friday_var_1color.background_color = color1

                if days1[5] == " True]" or days1[5] == True:
                    self.saturday_var_1color.background_color = color1

                if days2[0] == "[True" or days2[0] == True:
                    self.monday_var_2color.background_color = color2

                if days2[1] == " True" or days2[1] == True:
                    self.tuesday_var_2color.background_color = color2

                if days2[2] == " True" or days2[2] == True:
                    self.wednesday_var_2color.background_color = color2

                if days2[3] == " True" or days2[3] == True:
                    self.thursday_var_2color.background_color = color2

                if days2[4] == " True" or days2[4] == True:
                    self.friday_var_2color.background_color = color2

                if days2[5] == " True]" or days2[5] == True:
                    self.saturday_var_2color.background_color = color2

                if days3[0] == "[True" or days3[0] == True:
                    self.monday_var_3color.background_color = color3

                if days3[1] == " True" or days3[1] == True:
                    self.tuesday_var_3color.background_color = color3

                if days3[2] == " True" or days3[2] == True:
                    self.wednesday_var_3color.background_color = color3

                if days3[3] == " True" or days3[3] == True:
                    self.thursday_var_3color.background_color = color3

                if days3[4] == " True" or days3[4] == True:
                    self.friday_var_3color.background_color = color3

                if days3[5] == " True]" or days3[5] == True:
                    self.saturday_var_3color.background_color = color3

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

                if days1[1] == " True" or days1[1] == True:
                    self.tuesday_var_1color.background_color = color1

                if days1[2] == " True" or days1[2] == True:
                    self.wednesday_var_1color.background_color = color1

                if days1[3] == " True" or days1[3] == True:
                    self.thursday_var_1color.background_color = color1

                if days1[4] == " True" or days1[4] == True:
                    self.friday_var_1color.background_color = color1

                if days1[5] == " True]" or days1[5] == True:
                    self.saturday_var_1color.background_color = color1

                if days2[0] == "[True" or days2[0] == True:
                    self.monday_var_2color.background_color = color2

                if days2[1] == " True" or days2[1] == True:
                    self.tuesday_var_2color.background_color = color2

                if days2[2] == " True" or days2[2] == True:
                    self.wednesday_var_2color.background_color = color2

                if days2[3] == " True" or days2[3] == True:
                    self.thursday_var_2color.background_color = color2

                if days2[4] == " True" or days2[4] == True:
                    self.friday_var_2color.background_color = color2

                if days2[5] == " True]" or days2[5] == True:
                    self.saturday_var_2color.background_color = color2

                if days3[0] == "[True" or days3[0] == True:
                    self.monday_var_3color.background_color = color3

                if days3[1] == " True" or days3[1] == True:
                    self.tuesday_var_3color.background_color = color3

                if days3[2] == " True" or days3[2] == True:
                    self.wednesday_var_3color.background_color = color3

                if days3[3] == " True" or days3[3] == True:
                    self.thursday_var_3color.background_color = color3

                if days3[4] == " True" or days3[4] == True:
                    self.friday_var_3color.background_color = color3

                if days3[5] == " True]" or days3[5] == True:
                    self.saturday_var_3color.background_color = color3

                if days4[0] == "[True" or days4[0] == True:
                    self.monday_var_4color.background_color = color4

                if days4[1] == " True" or days4[1] == True:
                    self.tuesday_var_4color.background_color = color4

                if days4[2] == " True" or days4[2] == True:
                    self.wednesday_var_4color.background_color = color4

                if days4[3] == " True" or days4[3] == True:
                    self.thursday_var_4color.background_color = color4

                if days4[4] == " True" or days4[4] == True:
                    self.friday_var_4color.background_color = color4

                if days4[5] == " True]" or days4[5] == True:
                    self.saturday_var_4color.background_color = color4

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

        self.button_var1.background_color = self.button_var1_color
        self.button_var2.background_color = self.button_var2_color
        self.button_var3.background_color = self.button_var3_color
        self.button_var4.background_color = self.button_var4_color
        self.button_var5.background_color = self.button_var5_color
        self.button_var6.background_color = self.button_var6_color

        if str(universityinfo[2]) == "[0, 0, 1, 1]":
            self.button_var1.background_color = [0.5, 0.5, 1, 1]
            self.button_var1_color = [0.5, 0.5, 1, 1]

        if str(universityinfo[2]) == "[0, 1, 0, 1]":
            self.button_var2.background_color = [0.5, 1, 0.5, 1]
            self.button_var2_color = [0.5, 1, 0.5, 1]

        if str(universityinfo[2]) == "[1, 0, 0, 1]":
            self.button_var3.background_color = [1, 0.5, 0.5, 1]
            self.button_var3_color = [1, 0.5, 0.5, 1]

        if str(universityinfo[2]) == "[1, 1, 0, 1]":
            self.button_var4.background_color = [1, 1, 0.8, 1]
            self.button_var4_color = [1, 1, 0.8, 1]

        if str(universityinfo[2]) == "[1, 0, 1, 1]":
            self.button_var5.background_color = [1, 0.8, 1, 1]
            self.button_var5_color = [1, 0.8, 1, 1]

        if str(universityinfo[2]) == "[0, 1, 1, 1]":
            self.button_var6.background_color = [0.8, 1, 1, 1]
            self.button_var6_color = [0.8, 1, 1, 1]

        if str(universityinfo[5]) == "[0, 0, 1, 1]":
            self.button_var1.background_color = [0.5, 0.5, 1, 1]
            self.button_var1_color = [0.5, 0.5, 1, 1]

        if str(universityinfo[5]) == "[0, 1, 0, 1]":
            self.button_var2.background_color = [0.5, 1, 0.5, 1]
            self.button_var2_color = [0.5, 1, 0.5, 1]

        if str(universityinfo[5]) == "[1, 0, 0, 1]":
            self.button_var3.background_color = [1, 0.5, 0.5, 1]
            self.button_var3_color = [1, 0.5, 0.5, 1]

        if str(universityinfo[5]) == "[1, 1, 0, 1]":
            self.button_var4.background_color = [1, 1, 0.8, 1]
            self.button_var4_color = [1, 1, 0.8, 1]

        if str(universityinfo[5]) == "[1, 0, 1, 1]":
            self.button_var5.background_color = [1, 0.8, 1, 1]
            self.button_var5_color = [1, 0.8, 1, 1]

        if str(universityinfo[5]) == "[0, 1, 1, 1]":
            self.button_var6.background_color = [0.8, 1, 1, 1]
            self.button_var6_color = [0.8, 1, 1, 1]

        if str(universityinfo[8]) == "[0, 0, 1, 1]":
            self.button_var1.background_color = [0.5, 0.5, 1, 1]
            self.button_var1_color = [0.5, 0.5, 1, 1]

        if str(universityinfo[8]) == "[0, 1, 0, 1]":
            self.button_var2.background_color = [0.5, 1, 0.5, 1]
            self.button_var2_color = [0.5, 1, 0.5, 1]

        if str(universityinfo[8]) == "[1, 0, 0, 1]":
            self.button_var3.background_color = [1, 0.5, 0.5, 1]
            self.button_var3_color = [1, 0.5, 0.5, 1]

        if str(universityinfo[8]) == "[1, 1, 0, 1]":
            self.button_var4.background_color = [1, 1, 0.8, 1]
            self.button_var4_color = [1, 1, 0.8, 1]

        if str(universityinfo[8]) == "[1, 0, 1, 1]":
            self.button_var5.background_color = [1, 0.8, 1, 1]
            self.button_var5_color = [1, 0.8, 1, 1]

        if str(universityinfo[8]) == "[0, 1, 1, 1]":
            self.button_var6.background_color = [0.8, 1, 1, 1]
            self.button_var6_color = [0.8, 1, 1, 1]

        if str(universityinfo[11]) == "[0, 0, 1, 1]":
            self.button_var1.background_color = [0.5, 0.5, 1, 1]
            self.button_var1_color = [0.5, 0.5, 1, 1]

        if str(universityinfo[11]) == "[0, 1, 0, 1]":
            self.button_var2.background_color = [0.5, 1, 0.5, 1]
            self.button_var2_color = [0.5, 1, 0.5, 1]

        if str(universityinfo[11]) == "[1, 0, 0, 1]":
            self.button_var3.background_color = [1, 0.5, 0.5, 1]
            self.button_var3_color = [1, 0.5, 0.5, 1]

        if str(universityinfo[11]) == "[1, 1, 0, 1]":
            self.button_var4.background_color = [1, 1, 0.8, 1]
            self.button_var4_color = [1, 1, 0.8, 1]

        if str(universityinfo[11]) == "[1, 0, 1, 1]":
            self.button_var5.background_color = [1, 0.8, 1, 1]
            self.button_var5_color = [1, 0.8, 1, 1]

        if str(universityinfo[11]) == "[0, 1, 1, 1]":
            self.button_var6.background_color = [0.8, 1, 1, 1]
            self.button_var6_color = [0.8, 1, 1, 1]

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
        if dayid == 1:
            self.first_text.text = dayinfo[1]
            self.second_text.text = dayinfo[2]
            self.third_text.text = dayinfo[3]
            self.fourth_text.text = dayinfo[4]
            self.fifth_text.text = dayinfo[5]
            self.sixth_text.text = dayinfo[6]
            self.seventh_text.text = dayinfo[7]
        if dayid == 2:
            self.first_text.text = dayinfo[11]
            self.second_text.text = dayinfo[12]
            self.third_text.text = dayinfo[13]
            self.fourth_text.text = dayinfo[14]
            self.fifth_text.text = dayinfo[15]
            self.sixth_text.text = dayinfo[16]
            self.seventh_text.text = dayinfo[17]
        if dayid == 3:
            self.first_text.text = dayinfo[21]
            self.second_text.text = dayinfo[22]
            self.third_text.text = dayinfo[23]
            self.fourth_text.text = dayinfo[24]
            self.fifth_text.text = dayinfo[25]
            self.sixth_text.text = dayinfo[26]
            self.seventh_text.text = dayinfo[27]
        if dayid == 4:
            self.first_text.text = dayinfo[31]
            self.second_text.text = dayinfo[32]
            self.third_text.text = dayinfo[33]
            self.fourth_text.text = dayinfo[34]
            self.fifth_text.text = dayinfo[35]
            self.sixth_text.text = dayinfo[36]
            self.seventh_text.text = dayinfo[37]
        if dayid == 5:
            self.first_text.text = dayinfo[41]
            self.second_text.text = dayinfo[42]
            self.third_text.text = dayinfo[43]
            self.fourth_text.text = dayinfo[44]
            self.fifth_text.text = dayinfo[45]
            self.sixth_text.text = dayinfo[46]
            self.seventh_text.text = dayinfo[47]
        if dayid == 6:
            self.first_text.text = dayinfo[51]
            self.second_text.text = dayinfo[52]
            self.third_text.text = dayinfo[53]
            self.fourth_text.text = dayinfo[54]
            self.fifth_text.text = dayinfo[55]
            self.sixth_text.text = dayinfo[56]
            self.seventh_text.text = dayinfo[57]

    def set_values(self):
        if dayid == 1:
            self.parent.calendar_var.monday_var.text = Monday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[1] = self.first_text.text
            dayinfo[2] = self.second_text.text
            dayinfo[3] = self.third_text.text
            dayinfo[4] = self.fourth_text.text
            dayinfo[5] = self.fifth_text.text
            dayinfo[6] = self.sixth_text.text
            dayinfo[7] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 2:
            self.parent.calendar_var.tuesday_var.text = Tuesday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[11] = self.first_text.text
            dayinfo[12] = self.second_text.text
            dayinfo[13] = self.third_text.text
            dayinfo[14] = self.fourth_text.text
            dayinfo[15] = self.fifth_text.text
            dayinfo[16] = self.sixth_text.text
            dayinfo[17] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                if i != "\n":
                    DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 3:
            self.parent.calendar_var.wednesday_var.text = Wednesday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[21] = self.first_text.text
            dayinfo[22] = self.second_text.text
            dayinfo[23] = self.third_text.text
            dayinfo[24] = self.fourth_text.text
            dayinfo[25] = self.fifth_text.text
            dayinfo[26] = self.sixth_text.text
            dayinfo[27] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                if i != "\n":
                    DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 4:
            self.parent.calendar_var.thursday_var.text = Thursday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[31] = self.first_text.text
            dayinfo[32] = self.second_text.text
            dayinfo[33] = self.third_text.text
            dayinfo[34] = self.fourth_text.text
            dayinfo[35] = self.fifth_text.text
            dayinfo[36] = self.sixth_text.text
            dayinfo[37] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                if i != "\n":
                    DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 5:
            self.parent.calendar_var.friday_var.text = Friday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[41] = self.first_text.text
            dayinfo[42] = self.second_text.text
            dayinfo[43] = self.third_text.text
            dayinfo[44] = self.fourth_text.text
            dayinfo[45] = self.fifth_text.text
            dayinfo[46] = self.sixth_text.text
            dayinfo[47] = self.seventh_text.text
            os.remove("DayInfoFile.txt")
            DayInfoFile = open("DayInfoFile.txt", "w")

            for i in dayinfo:
                if i != "\n":
                    DayInfoFile.writelines(i + "\n")
            DayInfoFile.close()

        if dayid == 6:
            self.parent.calendar_var.saturday_var.text = Saturday + "\n" + self.first_text.text + "\n" + self.second_text.text + "\n" + self.third_text.text + "\n" + self.fourth_text.text + "\n" + self.fifth_text.text + "\n" + self.sixth_text.text + "\n" + self.seventh_text.text
            dayinfo[51] = self.first_text.text
            dayinfo[52] = self.second_text.text
            dayinfo[53] = self.third_text.text
            dayinfo[54] = self.fourth_text.text
            dayinfo[55] = self.fifth_text.text
            dayinfo[56] = self.sixth_text.text
            dayinfo[57] = self.seventh_text.text
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
        self.root.calendar_var.monday_var.text = Monday + "\n" + dayinfo[1] + "\n" + dayinfo[2] + "\n" + dayinfo[3] + "\n" + dayinfo[4] + "\n" + dayinfo[5] + "\n" + dayinfo[6] + "\n" + dayinfo[7]
        self.root.calendar_var.monday_var.background_color = BackgroundsColors[0]

        self.root.calendar_var.tuesday_var.text = Tuesday + "\n" + dayinfo[11] + "\n" + dayinfo[12] + "\n" + dayinfo[13] + "\n" + dayinfo[14] + "\n" + dayinfo[15] + "\n" + dayinfo[16] + "\n" + dayinfo[17]
        self.root.calendar_var.tuesday_var.background_color = BackgroundsColors[1]

        self.root.calendar_var.wednesday_var.text = Wednesday + "\n" + dayinfo[21] + "\n" + dayinfo[22] + "\n" + dayinfo[23] + "\n" + dayinfo[24] + "\n" + dayinfo[25] + "\n" + dayinfo[26] + "\n" + dayinfo[27]
        self.root.calendar_var.wednesday_var.background_color = BackgroundsColors[2]

        self.root.calendar_var.thursday_var.text = Thursday + "\n" + dayinfo[31] + "\n" + dayinfo[32] + "\n" + dayinfo[33] + "\n" + dayinfo[34] + "\n" + dayinfo[35] + "\n" + dayinfo[36] + "\n" + dayinfo[37]
        self.root.calendar_var.thursday_var.background_color = BackgroundsColors[3]

        self.root.calendar_var.friday_var.text = Friday + "\n" + dayinfo[41] + "\n" + dayinfo[42] + "\n" + dayinfo[43] + "\n" + dayinfo[44] + "\n" + dayinfo[45] + "\n" + dayinfo[46] + "\n" + dayinfo[47]
        self.root.calendar_var.friday_var.background_color = BackgroundsColors[4]

        self.root.calendar_var.saturday_var.text = Saturday + "\n" + dayinfo[51] + "\n" + dayinfo[52] + "\n" + dayinfo[53] + "\n" + dayinfo[54] + "\n" + dayinfo[55] + "\n" + dayinfo[56] + "\n" + dayinfo[57]
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


if __name__ == "__main__":
    SborkaApp().run()

