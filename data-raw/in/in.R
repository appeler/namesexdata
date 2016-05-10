"
Indian Pol. Data

"
# setwd("data-raw/in/")
indian_pols <- read.csv("data/myNetas.csv")
indian_pols <- indian_pols[, c("politician_name", "gender")]
save(indian_pols, file="data/indian_pols.Rdata")
