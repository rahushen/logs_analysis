# Logs Analysis
Project for the Udacity Full Stack Development NanoDegree.

In this project I built a python program that analyzes a database and answers a few questions.

## Table of contents

- [Install](#install)
- [Quick start](#quick-start)
- [Creator](#creator)

### What's included

The following files are included in the download :

```
.
├── README.md
├── newsdata.py
└── output.txt
```

## Quick start

This Program uses Python 3. Please install Python3 before proceeding. psycopg2 should be installed. The database provided in the instructor notes should be loaded.

Three views have already been created on the database. To create these views follow the below steps:

### views_table

create view views_table as select articles.title, authors.name from authors,articles,log where path like '%'||slug and authors.id = articles.author;

### failed_requests

create view failed_requests as select date(time) as log_date, count(\*) as failed_reqs from log where status = '404 NOT FOUND' group by log_date;

### total_requests

create view total_requests as select date(time) as log_date, count(\*) as total_reqs from log group by log_date;

### Run the script

- Verify that the file 'newsdata.py' has execution permissions.

- Run the python Program
  './newsdata.py'


## Creator

**Rahul shenoy**
- <https://github.com/rahushen>
