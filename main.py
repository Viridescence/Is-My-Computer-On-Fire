import requests

"""
This algorithm fetches the contents of www.ismycomputeronfire.com
for extremely accurate diagnostics on the state of a computer.
This is effectively a webscraper scraping a website without a 
JSON structure. If the website creator changes the contents, this
should pick it up.

Note: This is a joke. If you took until now to catch on, well done.

Viridescence
"""

def ismycomputeronfire(): 
    response = requests.get("https://www.ismycomputeronfire.com")  # Get site
    rtext = response.text
    rtext = rtext.replace("title=\"Probably not...\"","")  # Remove unneccesary title
    rtext = rtext.split("<h1 >")[1]
    rtext = rtext.split("</h1>")[0]
    if "no" in rtext.lower():
        return "No."
    else:
        return rtext
