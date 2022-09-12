def main():
    time = input("What time is it? ").replace(" ", ":")

    cnv = convert(time)
    if time.endswith('p.m.'):
        cnv = cnv + 12

    if 7.0 <= cnv <= 8.0:
        print("breakfast time")
    elif 12.0 <= cnv <= 13.0:
        print("lunch time")
    elif 18.0 <= cnv <= 19.0:
        print("dinner time")


def convert(x):
    if x.endswith('p.m.') or x.endswith('a.m.'):
        hours, minutes, apm = x.split(':')
    else:
        hours, minutes = x.split(':')

    hours = float(hours)
    minutes = float(minutes)
    time2 = hours + minutes / 60
    return time2

if __name__ == "__main__":
    main()