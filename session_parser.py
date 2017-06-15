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
                url = 'http://oob.vpod' + tmp + '.dc-01.com:8080/guacamole'
                sessionline['url'] = url
                # Format output for CLUS classes
                # print("Session Name: %s\tURL: %s" % (sessionline['sessionname'], sessionline['url']))
                print("%s\t%s" % (sessionline['sessionname'], sessionline['url']))
