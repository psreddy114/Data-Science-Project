# Readubg text data fuke ubti R ebvuribne

data <- read.table("C:/Users/SHASHI/OneDrive/Documents/R TEXT FILE.txt")
print(data)
fix(data)


data <- read.table("C:/Users/SHASHI/oneDrive/Documents/OrdersDataSet.csv")
print(data)
fix(data)
View(data)

# Converting Text file into data frame in R environemnt

Text_data_frame <- as.data.frame(data)
print(Text_data_frame)


csvdata <- read.csv("C:/Users/SHASHI/OneDrive/Documents/CSVSample.csv")
fix(csvdata)
View(csvdata)

# Converting CSV file into data frame in R environemnt

CSV_data_frame <- as.data.frame(csvdata)
print(csvdata)

# Reading semi structure text file into R Environment

Semistrdata <- read.table("C:/Users/SHASHI/OneDrive/Documents/Semistructuresample.txt",sep=",")
fix(Semistrdata)
View(Semistrdata)

# Converting Semi structure file into data frame in R enviroment

Semistrdata_data_frame <- as.data.frame(Semistrdata)
print(Semistrdata)

# Reading Semi structure text file with slash into R environment

slashdata <- read.table("C:/Users/SHASHI/OneDrive/Documents/Text Data Slash Delimited File.txt",sep="/")
View(slashdata)
fix(slashdata)


# Converting Semi structure file into data frame in R enviroment
slashdata_data_frame <- as.data.frame(slashdata)
print(slashdata)
View(slashdata)

# Reading excel data file into R environment

install.packages("readxl")
library(readxl)

Exceldata <- read_excel("C:/Users/SHASHI/OneDrive/Documents/ExcelSample.xlsx")
View(Exceldata)

# COnverting Excel file into Data Frame

excel_data_frame <- as.data.frame(Exceldata)

View(excel_data_frame)

install.packages("rjson")
library("rjson")

# Reading JSON file into R environment

jsondata <- fromJSON(file = "C:/Users/SHASHI/OneDrive/Documents/JSONSAMPLE.json")

print(jsondata)
fix(jsondata)
View(jsondata)

# Converting JSON file in Data Frame in R environment

json_data_frame <- as.data.frame(jsondata)

print(json_data_frame)

excel_data_frame <- as.data.frame(Exceldata)

View(excel_data_frame)

install.packages("RCurl")
install.packages("XML")
install.packages("stringr")
install.packages("plyr")


# Reading url data into R environment

urldata <- "http://www.geos.ed.ac.uk/~weather/jcmb_ws/"
View(urldata)
fix(urldata)
print(urldata)

webpage <- read_html(urldata)

install.packages("RMySQL")
mysqlconnection = dbConnect(MySQL(), user = 'root', password = '', dbname = 'sakila',
                            host = 'localhost')
dbListTables(mysqlconnection)

install.packages("XML")
library("methods")
library(XML)
library(rowr)
library(ggploy2)


doc <- xmlparse("C:/Users/SHASHI/OneDrive/Documents/XMLSample.xml")

# Reading xls file into R environment

file <- "C:/Users/SHASHI/OneDrive/Documents/Excelfile.xls"
filexlsx <- "C:/Users/SHASHI/OneDrive/Documents/Excelsample.xlsx"

xlsfile <- read_xls(file)
View(xlsfile)

xlsxfile <- read_xlsx(filexlsx)
View(xlsxfile)


#Reading XML file in to R environment

xmlfile <- ("C:/Users/SHASHI/OneDrive/Documents/XMLSample.xml")
View(xmlfile)
fix(xmlfile)


Excel_data <- read_excel(file.choose())


# Exporting R DATA FRAME IN TO  CSV format in my Desktop location.



write.csv(json_data_frame,"C:\\Users\\SHASHI\\OneDrive\\Documents\\JSONTOCSV.csv")
file.show("json.csv")

# Reading XML file in to R environment

xmlfile <- ("C:/Users/SHASHI/OneDrive/Documents/XMLSample.xml")
xml_data_frame <- as.data.frame(xmlfile)
fix(df)

write.csv(df,"C:/Users/SHASHI/OneDrive/Documents/XMLTOCSV.csv")


# Reading HTML file in to R environment

install.packages("RCurl")
install.packages("stringr")
install.packages("plyr")
install.packages("httr")
install.packages("XML")
# Read the URL.

url <- "http://www.geos.ed.ac.uk/~weather/jcmb_ws/"
url
library("RCurl")
library("stringr")
library("plyr")
library("httr")
library("XML")


# Gather the html links present in the webpage.

# links <- getHTMLLinKs(url, externalonly = TRUE)

links<-getHTMLLinks(rawToChar(GET(url)$content))
links
# Identify only the links which point to the JCMB 2015 files.

filenames <- links[str_detect(links,"JCMB_2015")]
filenames
# Store the file names as a list.
filenames_list<-as.list(filenames)

# Create a function to download the files by passing the URL and filename list.
