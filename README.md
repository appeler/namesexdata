## International Name Sex Data

Are men covered more often in business news than women? To answer the question and questions like these using text corpora, we need a way to infer gender based on the (first) name. In the US, one can easily infer the gender based on the first name using the data made available by the SSA and the Census. No such comparable data, however, exists for many other countries (and languages). 

Here we investigate a way of getting such data for 'Indian' names. We pair Google image search (via Google custom search API) with [clarifai.com](http://clarifai.com). In particular, we search for images using first names, and then get tags of those images via [clarifai](http://clarifai.com). We next count tags carrying information about gender--- man, men, boy, woman, women, girl. And classify based on whether 'male' tags are more common (probable) than 'female'. We validate the method using a dataset of names for which the gender is known. 

A few caveats and notes:   
1. Images that we find via Google image search are not constrained to a country (though this constraint can be added).   
2. Images returned by Google image search are sometimes close replicas, if not duplicates, of each others. This should not matter, but it is something to be aware of.   
3. Even if we were to get images hosted on websites located in a country (or some version of this), they would still not a representative set of people (in a country, in that language) with that name.   
4. Most names are not given uniquely to males or females. Instead, there is a distribution. For instance, some people named Jesse are men, others women. We elide over this point in the validation exercise. If we had good data on gender of first names, we wouldn't be doing all this to begin with.   
5. The gender distribution of a name changes over time, and by country.   
6. Some information about the gender associated with a name in countries (languages) where we don't have data may be recovered from SSA and Census data in US, and similar such data from other countries by exploiting the fact that these countries attract immigrants from various countries. For instance, one can infer gender of the name 'Gaurav' via [https://api.genderize.io/?name=gaurav](https://api.genderize.io/?name=gaurav).   
7. Inferring gender based on a limited set of tags returned by clarifai is still a clunky way of getting data about gender from images. Read more [here](http://gbytes.gsood.com/2015/12/31/clarifaing-the-future-of-clarifai-some-thoughts/) on that.   
8. Rather than use clarifai alone, it may be a better idea to use it as one of the signals for a more general classifier. For instance, building a general inferential engine that uses clarifai, but also these available data from other countries and whether male/female pronouns are more common in sentences using that name.      
