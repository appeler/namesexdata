"
Indian Pol. Data

"
# setwd("data-raw/in/")
indian_pols <- read.csv("data/myNetas.csv")
indian_pols <- indian_pols[, c("politician_name", "gender")]
Encoding(indian_pols$politician_name) <- "utf8"
use_data(indian_pols, compress="bzip2", overwrite=TRUE)
