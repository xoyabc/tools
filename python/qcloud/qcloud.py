from QcloudApi.qcloudapi import QcloudApi

import json
import yaml
import sys

conf_file="api.yaml"

class MyApi:

    def __init__(self, config,module,action,params):
	self.config = config
	self.module = module
	self.action = action
	self.params = params

    def request_put(self):
        service = QcloudApi(self.module, self.config)
        str_results = service.call(self.action, self.params)
        json_results = json.loads(str_results)
        return json_results

    def cvm_list(self):
	json_results = self.request_put()
	print json_results
	for i in json_results['Response']['InstanceSet']:
		name = i['InstanceName']
		wanip = i['PublicIpAddresses'][0]
		lanip = i['PrivateIpAddresses'][0]
		os = i['OsName']
		cpu = i['CPU']
		mem = i['Memory']
		info = "type=%s\tname=%s\t\twanip=%s\tlanip=%s\tconf=%score*%sG\tos=%s" % (module,name,wanip,lanip,cpu,mem,os)
		print info

    def lb_list(self):
        json_results = self.request_put()
        return json_results

def read_config(conf_file):
    f = open(conf_file)
    conf_yaml = yaml.load(f)
    config = conf_yaml
    return config


def main():
    config = read_config(conf_file)
    params = {'Limit':100}
    module = 'lb'
    action = 'DescribeLoadBalancers'
    s1 = MyApi(config,module,action,params)
    print s1.module
    a = s1.lb_list()
    print a

if __name__ == '__main__':
    sys.exit(main())

