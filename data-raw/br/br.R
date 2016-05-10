"
Brazilian Pol. Data

"

brazilian_pols <- read.csv("data/brazilNamesSexRatio.csv")
Encoding(brazilian_pols$firstName) <- "utf8"
use_data(brazilian_pols, compress="xz", overwrite=TRUE)