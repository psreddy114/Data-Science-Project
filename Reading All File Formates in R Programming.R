# Readubg text data fuke ubti R ebvuribne

data <- read.table("C:/Users/SHASHI/OneDrive/Documents/R TEXT FILE.txt")
print(data)
fix(data)


data <- read.table("C:/Users/SHASHI/oneDrive/Documents/OrdersDataSet.csv")
print(data)
fix(data)
View(data)


data <- read.csv("C:/Users/SHASHI/OneDrive/Documents/CSVSample.csv")
fix(data)
View(data)

# Reading semi structure text file into R Environment

Semistr <- read.table("C:/Users/SHASHI/OneDrive/Documents/Semistructuresample.txt",sep=",")
fix(Semistr)
View(Semistr)


# Reading Semi structure text file with slash into R environment

slashdata <- read.table("C:/Users/SHASHI/OneDrive/Documents/Text Data Slash Delimited File.txt",sep="/")
View(slashdata)
fix(slashdata)

# Reading excel data file into R environment

install.packages("readxl")
library(readxl)

Exceldata <- read_excel("C:/Users/SHASHI/OneDrive/Documents/ExcelSample.xlsx")
View(Exceldata)

install.packages("rjson")
library("rjson")
jsondata <- fromJSON(file = "C:/Users/SHASHI/OneDrive/Documents/JSONSAMPLE.json")

print(jsondata)
fix(jsondata)
View(jsondata)

json_data_frame <- as.data.frame(jsondata)

print(json_data_frame)

excel_data_frame <- as.data.frame(Exceldata)

View(excel_data_frame)

install.packages("RCurl")
install.packages("XML")
install.packages("stringr")
install.packages("plyr")
