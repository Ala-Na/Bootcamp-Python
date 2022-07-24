from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('good.csv', header = True) as file:
        data = file.getdata()
        header = file.getheader()
        print(list(data))
        print(list(header))

    print("")

    with CsvReader('other.csv', header = True, sep='|') as file:
        data = file.getdata()
        header = file.getheader()
        print(list(data))
        print(list(header))

    print("")

    with CsvReader('other.csv', header = False, sep='|', skip_top=2) as file:
        data = file.getdata()
        print(list(data))

    print("")

    with CsvReader('other.csv', header = True, sep='|', skip_top=2) as file:
        data = file.getdata()
        header = file.getheader()
        print(list(data))
        print(list(header))

    print("")

    with CsvReader('other.csv', header = True, sep='|', skip_bottom=1) as file:
        data = file.getdata()
        header = file.getheader()
        print(list(data))
        print(list(header))

    print("")

    with CsvReader('other.csv', header = True, sep='|', skip_top=1, skip_bottom=1) as file:
        data = file.getdata()
        header = file.getheader()
        print(list(data))
        print(list(header))
