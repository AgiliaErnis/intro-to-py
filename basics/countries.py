file = open("countries.txt", "r")

countries = []
countriesStartWith = []
for line in file:
    line = line.strip()
    countries.append(line)

file.close()


def filter_by_letter(starts_with):
    for country in countries:
        if country[0] == starts_with:
            countriesStartWith.append(country)


print(countries)
print(len(countries))
filter_by_letter('Z')
print(countriesStartWith)
print(len(countriesStartWith))

