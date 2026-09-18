## International Name Sex Data
[![Build Status](https://travis-ci.org/appeler/namesexdata.svg?branch=master)](https://travis-ci.org/appeler/namesexdata)
[![Appveyor Build status](https://ci.appveyor.com/api/projects/status/pxxj91y3ngw42wt2?svg=true)](https://ci.appveyor.com/project/appeler/namesexdata)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/namesexdata)](http://cran.r-project.org/package=namesexdata)
![](http://cranlogs.r-pkg.org/badges/grand-total/namesexdata)

The datasets in this package support the [namesex](https://github.com/soodoku/namesex) package. The [namesex](https://github.com/soodoku/namesex) package provides validated ML models to estimate sex of the person based on first name using the data in this package.  

### The package contains the following datasets:

* [Indian Politician Data](https://github.com/soodoku/indian-politician-bios)  
* [Brazilian Politician Data](https://github.com/lukesonnet/brazilNames)
* [Swedish Politician Data](https://github.com/soodoku/namesexdata/tree/master/data-raw/se)
* [Indian Names Google Photo and Clarifai Data](https://github.com/soodoku/clarifai_gender)

### Installation

To get the current development version from GitHub:

```r
# install.packages("devtools")
devtools::install_github("appeler/namesexdata")
```

### Privacy

The raw Brazilian candidate files in `data-raw/br/data/rawData/` are archived
TSE (Tribunal Superior Eleitoral) exports. Their direct identifiers — CPF,
título eleitoral, and e-mail — have been blanked, here and throughout the
repository's history. The package uses only first name and sex; the blanked
columns were never read, and the shipped datasets are unchanged. To request
removal of other personal data, open an issue or e-mail the maintainer listed
in `DESCRIPTION`.

### License

Scripts are released under the [MIT License](https://opensource.org/licenses/MIT).
