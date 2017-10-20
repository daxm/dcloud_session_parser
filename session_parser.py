# Use the SessionDetails.csv file to create a friendly formatted version to pass out to students.
import os.path

# Change AnyConnect URL to match your data center's AVC URL.
anyconnect_url = 'dcloud-sjc-anyconnect.cisco.com'

# Change intro to match your event's name.  (Anything between the triple quotes will be printed exactly as shown.)
intro = """Welcome to the SDA Test Drive event!

Following is your login credentials for your dCloud session.
"""

inputfilename = 'SessionDetails.csv'
outputdirectory = 'ToPrint'

fn = os.path.join(os.path.dirname(__file__), inputfilename)
with open(fn, 'r') as f:
    for fline in f:
        fsplit = fline.split(',')  # There are 9 columns in the SessionDetails.csv
        sessionline = {
            'sessionid': fsplit[0],
            'sessionname': fsplit[1],
            'usernames': fsplit[2],
            'password': fsplit[3],
            'start': fsplit[4],
            'stop': fsplit[5],
            'dnsassets': fsplit[6],
            'sharedwith': fsplit[7],
            'endpointkit': fsplit[8]
        }
        # We are only interested in sessions that are started.
        if sessionline['usernames'] != 'Not Started' and sessionline['usernames'] != ' Usernames':
            vpn_user1 = sessionline['usernames'].split(';')[0]
            tmp = vpn_user1.split('user1')[0]
            tmp = tmp.split('v')[1]
            url = 'http://oob.vpod' + tmp + '.dc-01.com'
            sessionline['url'] = url
            password = sessionline['password'].split('"')[1]

            userinfo = '\nAnyConnect VPN Connection Information:' \
                       '\n\tConnect to: {}' \
                       '\n\tUsername: {}' \
                       '\n\tPassword: {}'.format(anyconnect_url, vpn_user1, password)
            outputfilename = '{} -- {}.txt'.format(sessionline['sessionname'], sessionline['sessionid'])
            gn = os.path.join(os.path.dirname(__file__), outputdirectory, outputfilename)
            with open(gn, 'w') as g:
                g.write(intro)
                g.write('{}\n\n\n\n'.format(userinfo))

