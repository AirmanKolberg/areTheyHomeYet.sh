from functions import arrive_home

timeout_message = 'Request timed out'
ping_counter = 0

ip_to_track = input('\nType IP to track:\n')
response = arrive_home(ip_to_track)

while timeout_message in str(response):
    response = arrive_home(ip_to_track)
    ping_counter += 1
    print(f'Nothing on Ping #{str(ping_counter)}.')

print('Connected')
