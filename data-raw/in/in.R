"
Indian Pol. Data

"
# setwd("data-raw/in/")
indian_pols <- read.csv("data/myNetas.csv")
indian_pols <- indian_pols[, c("politician_name", "gender")]

# Cleaning
indian_pols$politician_name <- gsub(" \\(Winner\\)", "", indian_pols$politician_name)
indian_pols$politician_name <- tolower(indian_pols$politician_name)

# Just first names

# Keep unique only
indian_pols <- indian_pols[!duplicated(indian_pols$politician_name), ]

# Fix encoding
Encoding(indian_pols$politician_name) <- "latin1"
devtools::use_data(indian_pols, compress="bzip2", overwrite=TRUE)
