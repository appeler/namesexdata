# File: brazilGenderRatio.R
#
# Purpose: Adds row of ratios, sorts by them and total count, and returns
#          final dataset
#
# Authors: Luke Sonnet (Feb 2015)
#
# History:
#    12 Feb 2015: Initial code
#
# R v: 3.1.2

dat <- read.csv("brazilNamesGenderCounts.csv", as.is=T)

## Generate ratios
dat$totalFound <- dat$female + dat$male

table(dat$total)

dat$prFemale <- dat$female/dat$totalFound

out <- dat[order(dat$prFemale, dat$firstName, dat$totalFound),]

## Clean up errant commas
out <- apply(out, 2, function(x) gsub(",", "", x))

write.csv(out, "brazilNamesGenderRatio.csv", row.names=F)
