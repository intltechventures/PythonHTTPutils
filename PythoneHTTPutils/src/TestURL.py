'''
Created on Sep 11, 2012

Simple test program to explore Python HTTP.client methods

References:
http://docs.python.org/dev/py3k/library/http.client.html

http://www.w3.org/Protocols/
http://tools.ietf.org/rfc/index
http://www.w3.org/Protocols/Specs.html

RFC 2616 Hypertext Transfer Protocol -- HTTP/1.1
http://www.ietf.org/rfc/rfc2616.txt


@author: Kelvin
'''
import http.client

if __name__ == '__main__':
    h1 = http.client.HTTPConnection('www.google.com')
    h1.request("GET", "/index.html")                                # 200 returned
                                                                    # 302 returned if "index.html" - resource moved
                                                                    
    response = h1.getresponse()
    print("response: ", response)
    print("status: ", response.status, "reason", response.reason)
    data = response.read()
    print("data: ", data)
    print("status: ", response.status, "reason", response.reason)
    for header in response.getheaders():
        print("\tHeader: ", header)
    h1.close()