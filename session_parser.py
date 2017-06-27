# Use the SessionDetails.csv file to create a friendly formatted version to pass out to students.


inputfilename = 'SessionDetails.csv'
outputfilename = 'dCloud_Parsed_Session_Details.txt'

with open(inputfilename, 'r') as f:
    with open(outputfilename, 'w') as g:
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
                sessionline['usernames'] = sessionline['usernames'].split(';')[0]
                tmp = sessionline['usernames'].split('user1')[0]
                tmp = tmp.split('v')[1]
                url = 'http://oob.vpod' + tmp + '.dc-01.com'
                sessionline['url'] = url
                intro = """Welcome to the CiscoLive 2017 edition of the FTD Basics lab!
You have 4 hours right now to work on the lab but there is 8 hours of content for you to explore.  So, use this lab time
to learn about FTD device registration to the FMC and the intricacies of managing FTD with FMC.

Since the whole lab cannot be completed in the time allotted we've extended the lab window for the next 7 days.  Feel free
to work on the remaining parts of the lab if/when you have some time.  If you are unable to complete the lab just reach out
to me and I can spin up a new pod for you at a later date.

We encourage interaction!  Ask questions as you work through the lab.  You can reach me at dmickels@cisco.com after this
session's time has expired.

"""
                userinfo = '{}\nSteps 1 and 2 on page 3 of the lab guide have already been done for you:\n\t' \
                           '{}\n\tUsername: dcloud\n\tPassword: {}'.format(
                    sessionline['sessionname'],
                    sessionline['url'],
                    sessionline['sessionid'])
                g.write(intro)
                g.write('{}\n\n\n\n'.format(userinfo))
