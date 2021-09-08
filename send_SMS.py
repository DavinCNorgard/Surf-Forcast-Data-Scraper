from twilio.rest import Client
import sys
import datetime
import scraper

la_peruse_info = scraper.LaPeruse()

wave_height = la_peruse_info[0]
wave_period = la_peruse_info[1]
swell_size = wave_height[1].split(' ')

swell_size = swell_size[2]
swell_size = float(swell_size)

account_sid = 'AC694d00904b775b76a46011c864c84999'
auth_token = '1772986cd190c88e82e155bceda618c0'

client = Client(account_sid, auth_token)

if swell_size >= 8.0:

    formatted = 'CURRENT FORECAST ' + '\n' + str(datetime.datetime.now()) +  '\n' + wave_height[0] + wave_height[1] + '\n' + wave_period[0] + wave_period[1]
    
    client.messages.create(
        to="2502216574",
        from_="+17206051942",
        body=formatted
    )

if swell_size >= 15.0:

    formatted = 'RED ALERT ' + '\n' + str(datetime.datetime.now()) +  '\n' + wave_height[0] + wave_height[1] + '\n' + wave_period[0] + wave_period[1]

    client.messages.create(
        to="2502216574",
        from_="+17206051942",
        body=formatted
    )







