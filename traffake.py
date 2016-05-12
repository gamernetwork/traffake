import sys
from faker import Faker
from numpy import random
from locust import HttpLocust, TaskSet, task
#from collections import Counter

"""Traffaker
Traffic faker for benchmarking large editorial sites.
"""

# How many distinct articles on my website
URLS = 10000

# How many sections on my website
SECTIONS = 6

fake = Faker()
urls = []
sections = []
dist = []

# create some random directory (one level deep section) names
# (uses faker.providers.internet)
for a in range(0, SECTIONS):
    sections.append( fake.uri_path(1) )

# create some random URLs using the random categories
# distribute them UNEVENly
for a in range(0, URLS):
    urls.append( "/".join( (random.choice(sections), fake.slug(),) ) )
    dist.append( random.random_sample() )

# make first two articles MUCH more likely than the others
dist[0] = 50
if URLS > 1:
    dist[1] = 10

# normalise probabilities so they all add up to one (numpy.choice requirement)
s = sum(dist)
dist = [d/s for d in dist]

def get_article_url():
    return random.choice(urls, p=dist)

class ReaderTaskSet(TaskSet):
    @task(1)
    def article(self):
        #self.client.get( '/' + get_article_url(), name="/[section]/[slug]/" )
        self.client.get( '/' + get_article_url() )

class Siege(HttpLocust):
    task_set = ReaderTaskSet
    min_wait = 0
    max_wait = 0
