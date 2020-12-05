import locale
import datetime


def test_locale():
    date_1 = datetime.datetime(2020, 10, 31)
    date_2 = datetime.datetime(1995, 11, 25)
    date_3 = datetime.datetime(1995, 10, 1, 8, 0, 56)
    print(date_1)
    print(date_2)
    format_date = locale.nl_langinfo(locale.D_T_FMT)
    print(format_date)
    print(date_3.strftime(format_date))


if __name__ == "__main__":
    test_locale()