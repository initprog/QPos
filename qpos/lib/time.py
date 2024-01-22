import datetime as dt

def dayGreeting():
  nt = dt.datetime.now()
  now = nt.strftime("%H%M%S")

  if now > '060000' and now < '120001': return 'Good morning'
  elif now > '120000' and now < '180001': return 'Good afternoon'
  elif now > '180000' and now < '000001': return 'Good evening'
  else: return 'Good night'