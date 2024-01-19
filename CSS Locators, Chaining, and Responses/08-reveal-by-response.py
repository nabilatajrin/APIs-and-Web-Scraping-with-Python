# Get the URL to the website loaded in response
this_url = 'https://www.datacamp.com/courses/all'

# Get the title of the website loaded in response
this_title = response.xpath('/html/head/title/text()').extract_first()

# Print out our findings
print_url_title( this_url, this_title )
