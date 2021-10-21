# general
X<-read.csv("RainfallData.csv",header=TRUE,na.strings = "NA")
View(X)
library(tidyverse)
# header can be skipped

# Question 1
x <- X %>% filter(SUBDIVISION=="Assam & Meghalaya")
View(x)
plot(x$YEAR,x$ANNUAL, xlab="Year", ylab="Annual Rainfall", 
      main="Annual Rainfall Data for Assam and Meghalaya")
abline(h=mean(x$ANNUAL),col="red")

# Question 2
x <- X %>% filter(SUBDIVISION=="Punjab")
View(x)
barplot(x$OND~x$YEAR, xlab="Year", ylab="Rainfall: OCT-DEC", 
        main="Rainfall Data for Punjab: OCT-DEC")
abline(h=mean(x$OND),col="blue")

# Question 3
x <- X %>% filter(SUBDIVISION=="North Interior Karnataka")
View(x)
boxplot(x$JJAS,horizontal=TRUE, xlab="Rainfall Data: Jun-Sep",
        main="Rainfall Data:North Interior Karnataka: JUN-SEP")
        
# Question 4
x <- X %>% filter(SUBDIVISION=="Kerala")
View(x)
hist(x$ANNUAL, xlab="Annual Rainfall", main="Annual Rainfall: Kerala")

# Question 5
x <- X %>% filter(SUBDIVISION=="Coastal Karnataka" & YEAR==1957)
View(x)
z<-as.numeric(c(x$JF,x$MAM,x$JJAS,x$OND))
zlabel<-c("Jan-Feb","Mar-May","Jun-Sep","Oct-Dec")
pie(z,zlabel,main="Rainfall in Coastal Karnataka in 1957")
#as.numeric can be avoided for this data set

# Question 6
x <- X %>% filter(SUBDIVISION=="Konkan & Goa")
View(x)
stem(x$ANNUAL)

# Question 7
par(mfrow=c(2,1))
x <- X %>% filter(SUBDIVISION=="Vidarbha")
y <- X %>% filter(SUBDIVISION=="Matathwada")
View(x)
View(y)
plot(x$YEAR,x$ANNUAL,xlab="Year", ylab="Annual Rainfall", 
     main="Annual Rainfall: Vidarbha")
abline(h=mean(x$ANNUAL),col="green")
plot(y$YEAR,y$ANNUAL,xlab="Year", ylab="Annual Rainfall", 
     main="Annual Rainfall: Matathwada")
abline(h=mean(y$ANNUAL),col="green")   
#abline after each plot

# Question 8
par(mfrow=c(1,2))
x <- X %>% filter(SUBDIVISION=="Telangana")
y <- X %>% filter(SUBDIVISION=="Coastal Andhra Pradesh")
View(x)
View(y)
plot(x$YEAR,x$ANNUAL,xlab="Year", ylab="Annual Rainfall", 
      main="Annual Rainfall: Telangana")
abline(h=mean(x$ANNUAL),col="red")
plot(y$YEAR,y$ANNUAL,xlab="Year", ylab="Annual Rainfall", 
     main="Annual Rainfall: Coastal Andhra Pradesh")
abline(h=mean(y$ANNUAL),col="red")

# Question 9
par(mfrow=c(2,1))
x <- X %>% filter(SUBDIVISION=="Rayalseema")
y <- X %>% filter(SUBDIVISION=="Telangana")
barplot(x$OND~x$YEAR, xlab="Year", ylab="Rainfall: Oct-Dec", 
        main="Rainfall:Rayalseema: Oct-Dec")
abline(h=mean(x$OND),col="blue")
barplot(y$OND~y$YEAR, xlab="Year", ylab="Rainfall: Oct-Dec",
        main="Rainfall:Telangana:Oct-Dec")
abline(h=mean(y$OND),col="blue")

# Question 10
par(mfrow=c(1,2))
x <- X %>% filter(SUBDIVISION=="East Rajasthan")
y <- X %>% filter(SUBDIVISION=="West Rajasthan")
View(x)
View(y)
barplot(x$OND~x$YEAR, xlab="Year", ylab="Rainfall: Oct-Dec", 
        main="Rainfall:East Rajasthan: Oct-Dec")
abline(h=mean(x$OND),col="red")
barplot(y$OND~y$YEAR, xlab="Year", ylab="Rainfall: Oct-Dec",
        main="Rainfall:West Rajasthan:Oct-Dec")
abline(h=mean(y$OND),col="red")

# Question 11
par(mfrow=c(3,1))
x <- X %>% filter(SUBDIVISION=="North Interior Karnataka")
y <- X %>% filter(SUBDIVISION=="South Interior Karnataka")
View(x)
View(y)
boxplot(x$ANNUAL, horizontal = TRUE, xlab="Annual Rainfall", 
        main="Annual Rainfall:North Interior Karnataka")
boxplot(y$ANNUAL, horizontal = TRUE, xlab="Annual Rainfall", 
        main="Annual Rainfall:South Interior Karnataka")
boxplot(y$JF, horizontal = TRUE, xlab="Rainfall:Jan-Feb", 
        main="Rainfall:South Interior Karnataka: Jan-Feb")
        
# Question 12 
par(mfrow=c(1,2))
x <- X %>% filter(SUBDIVISION=="East Madhya Pradesh")
y <- X %>% filter(SUBDIVISION=="West Madhya Pradesh")
View(x)
View(y)
boxplot(x$ANNUAL, horizontal = TRUE, xlab="Annual Rainfall", 
         main="Annual Rainfall:East Madhya Pradesh")
boxplot(y$MAM, horizontal = TRUE, xlab="Rainfall:Mar-May", 
         main="Rainfall:West Madhya Pradesh: Mar-May")
         
# Question 13
par(mfrow=c(1,2))
x <- X %>% filter(SUBDIVISION=="Jharkhand")
y <- X %>% filter(SUBDIVISION=="Bihar")
View(x)
View(y)
hist(x$ANNUAL, xlab="Year", main="Annual Rainfall:Jharkhand")
hist(y$ANNUAL, xlab="Year", main="Annual Rainfall:Bihar")

# Question 14
par(mfrow=c(3,1))
x <- X %>% filter(SUBDIVISION=="Gujarat Region")
y <- X %>% filter(SUBDIVISION=="Saurashtra & Kutch")
z <- X %>% filter(SUBDIVISION=="Madhya Maharashtra")
View(x)
View(y)
View(z)
hist(x$ANNUAL, xlab="Year", main="Annual Rainfall:Gujarat Region")
hist(y$ANNUAL, xlab="Year", main="Annual Rainfall:Saurashtra & Kutch")
hist(z$ANNUAL, xlab="Year", main="Annual Rainfall:Madhya Maharashtra")
        
# Question 15
par(mfrow=c(1,2))
x <- X %>% filter(SUBDIVISION=="Assam & Meghalaya" & YEAR==1962)
y <- X %>% filter(SUBDIVISION=="Naga Mani Mizo Tripura" & YEAR==1962)
View(x)
View(y)
z<-as.numeric(c(x$JF,x$MAM,x$JJAS,x$OND))
zlabel<-c("Jan-Feb","Mar-May","Jun-Sep","Oct-Dec")
pie(z,zlabel,main="Rainfall in Assam & Meghalaya in 1962")
w<-as.numeric(c(y$JF,y$MAM,y$JJAS,y$OND))
wlabel<-c("Jan-Feb","Mar-May","Jun-Sep","Oct-Dec")
pie(w,wlabel,main="Rainfall in Naga Mani Mizo Tripura in 1962")

# Question 16
par(mfrow=c(3,1))
x <- X %>% filter(SUBDIVISION=="Orissa" & YEAR==2001)
y <- X %>% filter(SUBDIVISION=="Gangetic West Bengal" & YEAR==2001)
z <- X %>% filter(SUBDIVISION=="Sub Himalayan West Bengal & Sikkim" & YEAR==2001)
View(x)
View(y)
View(z)
a<-as.numeric(c(x$JF,x$MAM,x$JJAS,x$OND))
alabel<-c("Jan-Feb","Mar-May","Jun-Sep","Oct-Dec")
pie(a,alabel,main="Rainfall in Orissa in 2001")
b<-as.numeric(c(y$JF,y$MAM,y$JJAS,y$OND))
pie(b,alabel,main="Rainfall in Gangetic West Bengal in 2001")
c<-as.numeric(c(z$JF,z$MAM,z$JJAS,z$OND))
pie(c,alabel,main="Rainfall in Sub Himalayan West Bengal & Sikkim in 2001")

# Question 17
par(mfrow=c(1,2))
x <- X %>% filter(SUBDIVISION=="Jammu & Kashmir")
y <- X %>% filter(SUBDIVISION=="Uttarakhand")
View(x)
View(y)
stem(x$ANNUAL)
stem(y$ANNUAL)  # How to place them next to each other?

# Question 18
par(mfrow=c(2,1))
x <- X %>% filter(SUBDIVISION=="Andaman & Nicobar Islands")
y <- X %>% filter(SUBDIVISION=="Haryana Delhi & Chandigarh")
View(x)
View(y)
stem(x$ANNUAL)
stem(y$ANNUAL)  # How to place them below each other?
