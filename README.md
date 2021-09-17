# web-scraping-challenge

The mission to mars web scraping challenge!

First, I collect the data I need using a jupyter notebook. To do this, I use splinter and beautiful soup to scrape the multiple webpages and store that data into variables.

Then after exporting the jupyter notebook into a .py file I edit it to turn the entire notebook into a function and return a dictionary of the data that was scraped.

Then, I created a flask app with two routes. One route which calls the scrape function from my executable and updates that data into a mongo database. The second route displays that data.

Finally, I created an index.html that displays all the data that was scraped.