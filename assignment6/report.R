
sf <- read.table("datasciencecoursera/assignment6/sanfrancisco_incidents_summer_2014.csv",header=TRUE,sep=",",stringsAsFactors = FALSE)
st <- read.table("datasciencecoursera/assignment6/seattle_incidents_summer_2014.csv",header=TRUE,sep=",",stringsAsFactors = FALSE)

sf$Time <- as.POSIXct(sf$Time, format = "%H:%M")
sf_freq<-as.data.frame(table(as.POSIXlt(sf$Time)$hour))
library(ggplot2)
qplot(as.numeric(sf_freq$Var1),sf_freq$Freq,geom="line",xlab="Hour of the day",ylab="Number of Crimes", main="Crimes by Hour in San Francisco")
st$Occurred.Date.or.Date.Range.Start <- as.POSIXct(st$Occurred.Date.or.Date.Range.Start, format = "%m/%d/%Y %I:%M:%S %p")
st_freq<-as.data.frame(table(as.POSIXlt(st$Occurred.Date.or.Date.Range.Start)$hour))
qplot(as.numeric(st_freq$Var1),st_freq$Freq,geom="line",xlab="Hour of the day",ylab="Number of Crimes", main="Crimes by Hour in Seattle")

table(sf$Category[as.POSIXlt(sf$Time)$hour==19])
qplot(sf$Category[as.POSIXlt(sf$Time)$hour==19 &(sf$Category=="LARCENY/THEFT" | 
                                                  sf$Category=="ASSAULT" | 
                                                  sf$Category=="WARRANTS" | 
                                                  sf$Category=="MISSING PERSON" | 
                                                  sf$Category=="VEHICLE THEFT" | 
                                                  sf$Category=="OTHER OFFENSES") ],xlab="",ylab="Number of Crimes", main="Crimes at 19:00 in San Francisco")

table(st$Summarized.Offense.Description[as.POSIXlt(st$Occurred.Date.or.Date.Range.Start)$hour==13])
qplot(st$Summarized.Offense.Description[as.POSIXlt(st$Occurred.Date.or.Date.Range.Start)$hour==13 &(st$Summarized.Offense.Description=="OTHER PROPERTY" | 
                                                                                                      st$Summarized.Offense.Description=="VEHICLE THEFT" | 
                                                                                                      st$Summarized.Offense.Description=="BURGLARY" | 
                                                                                                      st$Summarized.Offense.Description=="WARRANT ARREST" | 
                                                                                                      st$Summarized.Offense.Description=="CAR PROWL" | 
                                                                                                      st$Summarized.Offense.Description=="FRAUD") ],xlab="",ylab="Number of Crimes", main="Crimes at 13:00 in Seattle")

sf$Date <- as.POSIXct(sf$Date, format = "%m/%d/%Y")
sf_cat <- aggregate(sf$Date,by=list(sf$Date,sf$Category),FUN=length)
ggplot(data=sf_cat,aes(x=Grop))

