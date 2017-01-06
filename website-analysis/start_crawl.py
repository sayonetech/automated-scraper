import os,psycopg2,subprocess,time






os.chdir('/home/auto-scraper-website')


DB_NAME=os.environ['DB_NAME']
DB_USER=os.environ['DB_USER']
DB_PASSWORD=os.environ['DB_PASSWORD']
DB_HOST=os.environ['DB_HOST']
params = {'database': DB_NAME,'user': DB_USER,'password': DB_PASSWORD,'host': DB_HOST,'port': '5432'}
db_con = None



try:
#Create a database sessio
 db_con = psycopg2.connect(**params)
except psycopg2.DatabaseError as e:
 print ('Error %s' % e)

cursor = db_con.cursor()
try:
  cursor.execute("SELECT url_link,status FROM api_url ")
  rows = cursor.fetchall()
  start_urls=[]
  print"START"
  for row in rows:
    start_urls.append(row[0])

  for url in start_urls:
    cmd=['scrapy crawl auto -a link='+str(url)]
    with open('mylog.log', 'w') as logfile:
      pgm=[subprocess.Popen(c.split()) for c in cmd]
      time.sleep(30)
except:
    print"Database Connection Error"

