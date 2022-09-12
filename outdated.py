months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    answer = input("Date: ")
    try:
        m, d, y = answer.split("/")
        if (int(m) >= 1 and int(m) <= 12) and (int(d) >= 1 and int(d) <= 31):
            break

    except:
        try:
            m, d, y = answer.split(" ")
            for i in months:
                if m == i:
                    m = months.index(i) + 1
            d_proper = False
            if d.endswith(","):
                d_proper = True
                d = d.replace(",", "")
            if (int(m) >= 1 and int(m) <= 12) and (int(d) >= 1 and int(d) <= 31) and d_proper == True:
                break
        except:
            pass

print(f"{int(y)}-{int(m):02}-{int(d):02}")