# Author: Luke Sonnet
# Purpose: Adds row of ratios, sorts by them and total count, and returns
#          final dataset
#
# R v: 3.2.5

dat <- read.csv("../data/brazilNamesSexCounts.csv", as.is=T)

## Clean up some clear errors and convert to lower
dat$firstName <- tolower(gsub("[\\,\\?\\'\\.]", "", dat$firstName))
dat$firstName <- gsub("0", "o", dat$firstName)

## combine some rows that now have the same name
sum(duplicated(dat$firstName))
dat <- aggregate(dat[c('total', 'female', 'male')], by=dat['firstName'], sum)

## Generate ratios
dat$totalFound <- dat$female + dat$male

dat$pr_women <- dat$female/dat$totalFound

out <- dat[order(dat$pr_women, dat$firstName, dat$totalFound),]

write.csv(out, "../data/brazilNamesSexRatio.csv", row.names=F)
