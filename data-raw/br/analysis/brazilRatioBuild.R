# Author: Luke Sonnet
# Purpose: Adds row of ratios, sorts by them and total count, and returns
#          final dataset
#
# R v: 3.2.5

dat <- read.csv("../data/brazilNamesSexCounts.csv", as.is=T)

## Clean up some clear errors and convert to lower
dat$first_name <- tolower(gsub("[\\,\\?\\'\\.]", "", dat$firstName))
dat$first_name <- gsub("0", "o", dat$first_name)

## combine some rows that now have the same name
sum(duplicated(dat$first_name))
dat <- aggregate(dat[c('total', 'female', 'male')], by=dat['first_name'], sum)

## Generate ratios
dat$total_found <- dat$female + dat$male

dat$pr_women <- dat$female/dat$total_found

out <- dat[order(dat$pr_women, dat$first_name, dat$total_found),]

## Create mean without accents
out$first_name_noaccent <- as.factor(iconv(out$first_name, to = "UTF-8//TRANSLIT"))
pr_women_noaccent <- by(out, out$first_name_noaccent, function(x) weighted.mean(x$pr_women, x$total_found))
out$pr_women_noaccent <- pr_women_noaccent[out$first_name_noaccent]
out$first_name_noaccent <- as.character(out$first_name_noaccent)
out$pr_women_noaccent <- c(unname(out$pr_women_noaccent))

write.csv(out, "../data/brazilNamesSexRatio.csv", row.names=F)
