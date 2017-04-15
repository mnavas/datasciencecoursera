Summer 2014 Crime Informative
================

Summer 2014 Crime Informative
----------------

The following report shows how crime behaves in San Francisco and Seattle during the summer of 2014. Let review the results.

Crime pick in San Francisco is during night, espeficically during the 19:00 hour

sf <- read.table("datasciencecoursera/assignment6/sanfrancisco_incidents_summer_2014.csv",header=TRUE,sep=",",stringsAsFactors = FALSE)
st <- read.table("datasciencecoursera/assignment6/seattle_incidents_summer_2014.csv",header=TRUE,sep=",",stringsAsFactors = FALSE)

sf$Time <- as.POSIXct(sf$Time, format = "%H:%M")
sf_freq<-as.data.frame(table(as.POSIXlt(sf$Time)$hour))
library(ggplot2)
qplot(as.numeric(sf_freq$Var1),sf_freq$Freq,geom="line",xlab="Hour of the day",ylab="Number of Crimes", main="Crimes by Hour in San Francisco")

![crimes_hour_sf](/assignment6/crimes_hour_sf.jpeg)

In the other hand crime pick in Seattle is reached in the afternoon during the 13:00 hour

st$Occurred.Date.or.Date.Range.Start <- as.POSIXct(st$Occurred.Date.or.Date.Range.Start, format = "%m/%d/%Y %I:%M:%S %p")
st_freq<-as.data.frame(table(as.POSIXlt(st$Occurred.Date.or.Date.Range.Start)$hour))
qplot(as.numeric(st_freq$Var1),st_freq$Freq,geom="line",xlab="Hour of the day",ylab="Number of Crimes", main="Crimes by Hour in Seattle")

![crimes_hour_st](/assignment6/crimes_hour_st.jpeg)

In San Francisco the most common crime during the 19:00 hour is larceny and theft.

table(sf$Category[as.POSIXlt(sf$Time)$hour==19])
qplot(sf$Category[as.POSIXlt(sf$Time)$hour==19 &(sf$Category=="LARCENY/THEFT" | 
                                                  sf$Category=="ASSAULT" | 
                                                  sf$Category=="WARRANTS" | 
                                                  sf$Category=="MISSING PERSON" | 
                                                  sf$Category=="VEHICLE THEFT" | 
                                                  sf$Category=="OTHER OFFENSES") ],xlab="",ylab="Number of Crimes", main="Crimes at 19:00 in San Francisco")

![crimes_19_sf](/assignment6/crimes_19_sf.jpeg)

In Seattle the most important crime is robbery of properties that are not cars, followed by car prowl.

table(st$Summarized.Offense.Description[as.POSIXlt(st$Occurred.Date.or.Date.Range.Start)$hour==13])
qplot(st$Summarized.Offense.Description[as.POSIXlt(st$Occurred.Date.or.Date.Range.Start)$hour==13 &(st$Summarized.Offense.Description=="OTHER PROPERTY" | 
                                                                                                      st$Summarized.Offense.Description=="VEHICLE THEFT" | 
                                                                                                      st$Summarized.Offense.Description=="BURGLARY" | 
                                                                                                      st$Summarized.Offense.Description=="WARRANT ARREST" | 
                                                                                                      st$Summarized.Offense.Description=="CAR PROWL" | 
                                                                                                      st$Summarized.Offense.Description=="FRAUD") ],xlab="",ylab="Number of Crimes", main="Crimes at 13:00 in Seattle")

![crimes_19_st](/assignment6/crimes_19_st.jpeg)

The most common crime of larceny/theft in San Francisco reached its pick during August 16 for the summer of 2014

sf$Date <- as.POSIXct(sf$Date, format = "%m/%d/%Y")
sf_cat <- aggregate(sf$Date,by=list(sf$Date,sf$Category),FUN=length)

library(ggplot2)
ggplot(sf_cat[sf_cat$Group.2=="LARCENY/THEFT" | 
                sf_cat$Group.2=="ASSAULT" | 
                sf_cat$Group.2=="WARRANTS" | 
                sf_cat$Group.2=="MISSING PERSON" | 
                sf_cat$Group.2=="VEHICLE THEFT" | 
                sf_cat$Group.2=="OTHER OFFENSES",], aes(x=Group.1, y=x, group=Group.2, colour=Group.2 ))+geom_line()+xlab("Date")+ylab("Number of Crimes")+ggtitle("Crimes in San Francisco")


![crimesbytype_sf](/assignment6/crimesbytype_sf.jpeg)

The crime of car prowl in Seattle reached two picks during June 25 and 4th of July for the summer of 2014

st$Date <- as.character(format(st$Occurred.Date.or.Date.Range.Start, format = "%m/%d/%Y"))
st$Date <- as.POSIXct(st$Date, format = "%m/%d/%Y")
st_cat <- aggregate(st$Date,by=list(st$Date,st$Summarized.Offense.Description),FUN=length)
ggplot(st_cat[  st_cat$Group.2=="OTHER PROPERTY" | 
                  st_cat$Group.2=="VEHICLE THEFT" | 
                  st_cat$Group.2=="BURGLARY" | 
                  st_cat$Group.2=="WARRANT ARREST" | 
                  st_cat$Group.2=="CAR PROWL" | 
                  st_cat$Group.2=="FRAUD",], aes(x=Group.1, y=x, group=Group.2, colour=Group.2 ))+geom_line()+xlab("Date")+ylab("Number of Crimes")+ggtitle("Crimes in San Seattle")

![crimesbytype_st](/assignment6/crimesbytype_st.jpeg)
