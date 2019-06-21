import dateparser

t = dateparser.parse(" 05/22/2019 18:45 PDT")

print(t)

t2 = dateparser.parse("2019-05-31T13:53:31+00:00")

print(t2)