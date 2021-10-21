# Declare a variable to store the data set
captaincy <- read.csv("CaptaincyData.csv") 

# View the stored data set 
View(captaincy)

captaincy[3,]                     # To view row 3
captaincy[3]                      # To view column 3
captaincy[c(2,3),]                # To view rows 2 and 3
captaincy[c(2,3,4),]              # To view rows 2, 3 and 4
captaincy[captaincy$played==25,]  # To view row with played = 25
captaincy[1]                      # To view column 1
captaincy["names"]                # To view the column with title "names"
captaincy[c("names","won")]       # To view the columns names and won

# To view columns names, played and won for which victory > 0.3
subData <- subset(captaincy, victory>0.3, 
                  select = c("names","played","won"))  
print(subData)

captaincy[[4]][3]                 # To view the value at row 3, column 4

# To view columns names,played and lost when played > 20, lost < 14
x <- subset(captaincy, played>20 & lost<14,
            select=c("names","played","lost"))
print(x)

############################

library(dplyr)

# Clear R work space
rm(list = ls()) 

# Declare a variable to read and store moviesData  
movies <- read.csv("moviesData.csv")

# View movies data frame
View(movies)

# To filter movies with comedy genre
moviesComedy <- filter(movies,genre == "Comedy")
View(moviesComedy)

# To filter movies with comedy or drama genre
moviesComDr <- filter(movies,genre == "Comedy" | 
                        genre == "Drama")
View(moviesComDr)

# To filter movies with comedy or drama genre
moviesComDrP <- filter(movies,genre %in% 
                         c("Comedy","Drama"))
View(moviesComDrP)

# To filter movies with comedy genre and a imdb rating > 7.5
moviesComIm <- filter(movies,genre=="Comedy" & 
                        imdb_rating>=7.5)
View(moviesComIm)

# To arrange movies by ascending order of imdb rating
moviesImA <- arrange(movies,imdb_rating)
View(moviesImA)

# To arrange movies by descending order of imdb rating
moviesImD <- arrange(movies,desc(imdb_rating))
View(moviesImD)

# To arrange movies by genre and imdb rating
moviesGeIm <- arrange(movies,genre,imdb_rating) 
View(moviesGeIm)

# To view the columns movies, title, genre and imdb_rating
moviesTGI <- select(movies,title,genre,imdb_rating)
View(moviesTGI)

# To view the column title and all the columns that start with "thtr"
moviesTHT <- select(movies,title,starts_with("thtr"))
View(moviesTHT)

# To rename the column name thtr_rel_year to rel_year
moviesR <- rename(movies,rel_year="thtr_rel_year")
View(moviesR)

# To View columns from title to audience_score
moviesLess <- select(movies,title:audience_score)
View(moviesLess)

# To add new column CriAud to calculate the difference between critic and audience score
moviesMu <- mutate(moviesLess, CriAud = critics_score -
                     audience_score)
View(moviesMu)

