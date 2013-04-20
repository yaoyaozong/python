# -*- coding: utf-8 -*-
# change WAN username & password
#
import sys, urllib2, base64

if __name__ == '__main__':
    # IP for the router
    ip = '192.168.203.1'
    # 验证的用户名和密码
    login_user = 'admin'
    login_pw = 'admin'
    if len(sys.argv) < 3: 
        pppoe_user = '87654321'
        pppoe_pw = '87654321'
    else:
        pppoe_user = sys.argv[1]
        pppoe_pw = sys.argv[2]

    print 'pppoe_user = ' + pppoe_user
    print 'pppoe_pw = ' + pppoe_pw

    #Change the PPPoE username
    url = 'http://' + ip + '/userRpm/PPPoECfgRpm.htm?wantype=2&acc=' + pppoe_user + '&psw=' + pppoe_pw + '&VnetPap=0&linktype=2&Save=%B1%A3+%B4%E6'
    auth = 'Basic ' + base64.b64encode(login_user+':'+login_pw)
    heads = {'Referer' : url,
        'Authorization' : auth
    }
    #Send out the request
    request = urllib2.Request(url, None, heads)
    response = urllib2.urlopen(request)
    print response.read()

