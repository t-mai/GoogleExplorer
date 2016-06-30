from xgoogle.scraper import GoogleScraper, ScraperError
try:
  gs = GoogleScraper("gion matsuri", random_agent=True, debug=True)
  gs.results_per_page = 10
  results = gs.get_results()
  for res in results:
    print "Result title: %s" % res.title.encode("utf8")
    print "Result description: %ss" % res.desc.encode("utf8")
    print "Result url: %s" % res.url.encode("utf8")
    print "Content of url: %s" % res.content.encode("utf8")
    print
except ScraperError, e:
  print "Search failed: %s" % e