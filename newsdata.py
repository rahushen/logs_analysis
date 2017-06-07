#!/usr/bin/env python3
import psycopg2
import sys


def connect_to_db(db='news'):
    """Connects to the news database.
       Program quits if can't connect to db.
    """
    try:
        print("Connecting to Db {}".format(db))
        conn = psycopg2.connect(dbname=db)
        return conn
    except Exception as e:
        print("Couldn't connect to Db {}. Error: {}".format(db, e))
        sys.exit(1)


def top_three_articles(conn):
    """Prints the top three articles and how many views they have"""
    cursor.execute('''select title, count(*) as views from views_table
                      group by title order by views desc''')
    # Fetch top three only
    rows = cursor.fetchmany(3)
    print("The top three articles are:")
    for row in rows:
        print("\t%s : %d views" % row)


def most_popular_authors(cursor):
    """Prints the list of authors based on popularity"""
    cursor.execute('''select name, count(*) as views from views_table
                      group by name order by views desc''')
    rows = cursor.fetchall()
    print("The most popular authors are:")
    for row in rows:
        print("\t%s : %d views" % row)


def fail_percentage_over_one(cursor):
    """Prints days where the webserver failed more than 1 percent requests"""
    # join views to calculate new table with log_date and
    # precentage_failed. Then use a subselect query to get only entries with
    # precentage_failed > 1.
    cursor.execute('''select log_date, percentage_failed
                      from (select total_requests.log_date,
                      ((failed_reqs * 100.0) / total_reqs) as percentage_failed
                      from total_requests, failed_requests
                      where total_requests.log_date = failed_requests.log_date)
                      as total_failed where percentage_failed > 1.0''')
    rows = cursor.fetchall()
    print("Days with failure precentage greater than 1 are :")
    for row in rows:
        date, fail_percent = row
        print('\t%s with a fail percentage of %s' % (str(date),
                                                     str(fail_percent)))


if __name__ == '__main__':
    conn = connect_to_db()
    print("Analyzing Logs now....")
    cursor = conn.cursor()
    top_three_articles(cursor)
    most_popular_authors(cursor)
    fail_percentage_over_one(cursor)
    conn.close()
