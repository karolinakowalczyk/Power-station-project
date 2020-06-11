from random import randint

class Malfunctions:
    def __init__(self, name, status):
        self.name = name
        self.status = status
        self.days = self.randomize_days()
        self.hours = self.randomize_hours()
        self.minutes = self.randomize_minutes()
        self.time = self.count_time()

    def get_malname(self):
        return self.name

    def get_status(self):
        return self.status

    def get_days(self):
        return self.days

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.minutes

    def randomize_minutes(self):
        minutes = randint(0, 59)
        return minutes

    def randomize_hours(self):
        hours = randint(0, 23)
        return hours

    def randomize_days(self):
        if self.status == "easy":
            days = 0
            return days
        elif self.status == "medium":
            days = randint(1, 3)
            return days
        elif self.status == "serious":
            days = randint(4, 6)
            return days
        else:
            print("I can't randomize time for unknown status.")

    def count_time(self):
        return self.days*24*60 + self.hours*60 + self.minutes

    def get_time(self):
        return self.time


mal1 = Malfunctions("Zerwanie linii", "easy")
mal2 = Malfunctions("Zerwanie 3 linii", "medium")
mal3 = Malfunctions("Zerwanie więcej niż 3 linii", "easy")
mal4 = Malfunctions("Awaria sieciowa", "easy")
mal5 = Malfunctions("Awaria zasilania", "medium")
mal6 = Malfunctions("Brak surowców", "easy")
mal7 = Malfunctions("Wybuch reaktora xD", "serious")

mal_list = []
mal_list.append(mal1)
mal_list.append(mal2)
mal_list.append(mal3)
mal_list.append(mal4)
mal_list.append(mal5)
mal_list.append(mal6)
mal_list.append(mal7)