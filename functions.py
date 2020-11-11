from pythonping import ping


def arrive_home(ip_address):
    ping_response = ping(ip_address,
                         size=6,
                         count=1)
    return ping_response
