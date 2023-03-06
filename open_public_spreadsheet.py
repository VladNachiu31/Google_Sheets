import pandas

url_sheet1 = "google_url/tq?tqx=out:csv&sheet=2013"

url_sheet2 = "google_url/tq?tqx=out:csv&sheet=2014"

data1 = pandas.read_csv(url_sheet1)
data2 = pandas.read_csv(url_sheet2)