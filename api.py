import datetime as dt
from ipaddress import ip_network, ip_address
import netaddr

from flask import Flask, jsonify, request


class UserStatusSearch:

    RECORDS = [
        {'user_id': 1, 'created_at': '2017-01-01T10:00:00', 'status': 'paying'},
        {'user_id': 1, 'created_at': '2017-03-01T19:00:00', 'status': 'paying'},
        {'user_id': 1, 'created_at': '2017-02-01T12:00:00', 'status': 'cancelled'},
        {'user_id': 3, 'created_at': '2017-10-01T10:00:00', 'status': 'paying'},
        {'user_id': 3, 'created_at': '2016-02-01T05:00:00', 'status': 'cancelled'},
    ]

    def __init__(self):
        self.treeMap = {}
        for record in UserStatusSearch.RECORDS:
            if record['user_id'] not in self.treeMap:
                self.treeMap[record['user_id']] = {}
            self.treeMap[record['user_id']][record['created_at']] = record['status']

    def get_status(self, user_id, date):
        try:
            value = self.treeMap[user_id][date.strftime('%Y-%m-%dT%H:%M:%S')]
            return value
        except:
            return 'non-paying'
            
        

class IpRangeSearch:

    RANGES = {
        'london': [
            {'start': '10.10.0.0', 'end': '10.10.255.255'},
            {'start': '192.168.1.0', 'end': '192.168.1.255'},
        ],
        'munich': [
            {'start': '10.12.0.0', 'end': '10.12.255.255'},
            {'start': '172.16.10.0', 'end': '172.16.11.255'},
            {'start': '192.168.2.0', 'end': '192.168.2.255'},
        ]
    }

    def __init__(self):
        # self.sorted_cidrs = []
        self.cidrs = []
        for key, value in IpRangeSearch.RANGES.items():
            for val in value:
                cidr = netaddr.iprange_to_cidrs(val['start'], val['end'])
                net = ip_network(str(cidr[0]))
                self.cidrs.append((key, net))

    def get_city(self, ip):
        for cidr_tuple in self.cidrs:
            if (ip_address(ip) in cidr_tuple[1]):
                return cidr_tuple[0]
        return 'unknown'
        
        # net = ip_network("10.10.0.0/16")
        # cidrs = netaddr.iprange_to_cidrs('172.16.10.0', '172.16.11.255')
        # net2 = ip_network(str(cidrs[0]))
        # print(net)
        # print("************************")
        # print(net2)
        # print(ip_address(ip) in net2)


app = Flask(__name__)
user_status_search = UserStatusSearch()
ip_range_search = IpRangeSearch()


@app.route('/user_status/<user_id>')
def user_status(user_id):
    """
    Return user status for a given date

    /user_status/1?date=2017-10-10T10:00:00
    """
    date = dt.datetime.strptime(str(request.args.get('date')), '%Y-%m-%dT%H:%M:%S')

    return jsonify({'user_status': user_status_search.get_status(int(user_id), date)})


@app.route('/ip_city/<ip>')
def ip_city(ip):
    """
    Return city for a given ip

    /ip_city/10.0.0.0
    """
    return jsonify({'city': ip_range_search.get_city(ip)})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
