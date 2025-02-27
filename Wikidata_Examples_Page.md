# Example Queries with Wikidata

Wikidata query service can be found at <a href="https://query.wikidata.org/">Wikidata Query Service</a>

 The query service page looks like in the following:
 

## Find the capitals of every countries

```sparql
SELECT ?country ?countryLabel ?capital ?capitalLabel 
WHERE {
  ?country wdt:P31 wd:Q6256.
  ?country wdt:P36 ?capital.
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 10

```

![Example one](assests/images/exp1.png)


## Find random cities and their capitals

```sparql
SELECT ?city ?cityLabel ?country ?countryLabel
WHERE {
  ?city wdt:P31 wd:Q515.   # The entity must be a city (P31 = instance of, Q515 = city)
  ?city wdt:P17 ?country.  # Get the country the city belongs to (P17 = country)
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 10
 ```

![Example second](assests/images/exp2.png)

## List of Food and Their Main Ingredients

```sparql
SELECT ?food ?foodLabel ?ingredient ?ingredientLabel
WHERE {
  ?food wdt:P31 wd:Q2095.      # (P31 = instance of, Q2095 = food)
  ?food wdt:P186 ?ingredient.   # (P186 = made from material)
```


![Example third](assests/images/exp3.png)

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 10
```
