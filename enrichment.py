import json
import requests
from collections import defaultdict

class Enrichment:
  def __init__(self):
    self.transactions = []
    self.newTransactions = []
    self.aggregateMap = {}
    self.user_status_url = "http://0.0.0.0:5000/user_status/"
    self.ip_city_url = "http://0.0.0.0:5000/ip_city/"

    for line in open('transactions.json', 'r'):
        self.transactions.append(json.loads(line))
    for transaction in self.transactions:
      self.aggregateMap[transaction['user_id']] = defaultdict(int)
    

  def addFields(self):
    with open('enrichedTransactions.json', 'w') as outfile:
      for transaction in self.transactions:
        user_status_slug = "{}?date={}".format(transaction['user_id'], transaction['created_at'])
        ip_slug = "{}".format(transaction['ip'])

        user_status_response = requests.get(self.user_status_url+user_status_slug)
        city_response = requests.get(self.ip_city_url+ip_slug)
        
        transaction['user_status'] = user_status_response.json()['user_status']
        transaction['city'] = city_response.json()['city']
        self.newTransactions.append(transaction)
        json.dump(transaction, outfile)
        outfile.write("\n")
  
  def calculateAggregate(self):
    self.addFields()
    for transaction in self.newTransactions:
      self.aggregateMap[transaction['user_id']][transaction['city']] += transaction['product_price']
    with open('aggregate.json', 'w') as outfile:
      json.dump(self.aggregateMap, outfile)


if __name__ == '__main__':
  enrichment = Enrichment()
  enrichment.calculateAggregate()
