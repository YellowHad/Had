import datetime
import operator

if __name__ == '__main__':
    birthdates = {'Patrick': datetime.date(1987, 8, 22),
                  'Reini': datetime.date(1979, 12, 17),
                  'Boxi': datetime.date(1982, 1, 12),
                  'Thomas': datetime.date(1975, 11, 16),
                  'Marko': datetime.date(1989, 10, 21),
                  'Martin': datetime.date(1990, 11, 16)}

    days_left_dict = {}
    today = datetime.datetime.now().date()

    for k, v in birthdates.iteritems():
        age_this_year = today.year - v.year
        days_left = (datetime.date(today.year, v.month, v.day) - today).days
        if days_left >= 0:
            days_left_dict[k] = (days_left, v)

    sorted_birthday_memos = sorted(days_left_dict.items(), key = operator.itemgetter(1))
    for birthday_memo in sorted_birthday_memos:
        name, details = birthday_memo
        days_left, date = details
        print "{:12s} has birthday in {:3d} days. || Date of Birth({})".format(name, days_left, date)