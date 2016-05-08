# Author: Luke Sonnet
# Purpose: Adds row of ratios, sorts by them and total count, and returns
#          final dataset
#
# R v: 3.2.3

dat <- read.csv("../data/brazilNamesSexCounts.csv", as.is=T)

## Generate ratios
dat$totalFound <- dat$female + dat$male

dat$prFemale <- dat$female/dat$totalFound

out <- dat[order(dat$prFemale, dat$firstName, dat$totalFound),]

## Clean up errant commas
out$firstName <- gsub(",", "", out$firstName)

write.csv(out, "../data/brazilNamesSexRatio.csv", row.names=F)