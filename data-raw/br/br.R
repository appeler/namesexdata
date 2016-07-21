"
Brazilian Pol. Data

"

brazilian_pols <- read.csv("data/brazilNamesSexRatio.csv",
                           stringsAsFactors = F)
Encoding(brazilian_pols$firstName) <- "utf8"
devtools::use_data(brazilian_pols, compress="xz", overwrite=TRUE)
