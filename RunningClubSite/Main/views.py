import smtplib
import email
import sys

from django.shortcuts import render
from .models import Meet
from .models import FAQ
from .models import Post
from .models import Executives
from .models import Route
import xlrd

from .news import newsMain

import xml.etree.ElementTree as ET
from PIL import Image


Months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November', 12:'December'}
AboutUsLinks = [{'Title':"University of Cincinnati",'Link':"www.uc.edu"},{'Title':"NIRCA",'Link':"www.clubrunning.org"},{'Title':"UC Running Club Campus Link",'Link':"campuslink.uc.edu/organization/runningclub"}]

def readExcel(records, races, name):

    validData = False
    name = name.lower()

    raceLen = {
        '5k':0,
        '6k':1,
        '8k':2,
        'Half Marathon':3
    }

    wb = xlrd.open_workbook('Main/UC_records.xlsx')
    sheet = wb.sheet_by_index(0)
    numCols = sheet.ncols
    for nCols in range(1,numCols):
        if sheet.cell_value(1,nCols) != '':
            raceDist = sheet.cell_value(1,nCols)
            numRows = sheet.nrows
            for nRows in range(1,numRows):
                if sheet.cell_value(nRows,nCols) == '':
                    break
                elif name in sheet.cell_value(nRows,nCols).strip().lower():
                    nameFound = False

                    for rr in races:
                        if sheet.cell_value(nRows,nCols).strip().lower() == rr['name'].lower():
                            raceArr = rr['races']
                            r = raceArr[raceLen[raceDist]]

                            r['distance'] = raceDist
                            r['time'] = sheet.cell_value(nRows,nCols + 1)
                            r['meet'] = sheet.cell_value(nRows,nCols + 2)
                            r['year'] = str(sheet.cell_value(nRows,nCols + 3))[0:4]
                            r['valid'] = True
                            validData = True

                            nameFound = True

                    if not nameFound:
                        races += [{'name':sheet.cell_value(nRows,nCols).strip(),'races':[{'distance':'0k','time':'0:0','meet':'NA','year':'1970'} for x in range(4)]}]

                        raceArr = races[-1]['races']
                        r = raceArr[raceLen[raceDist]]

                        r['distance'] = raceDist
                        r['time'] = sheet.cell_value(nRows,nCols + 1)
                        r['meet'] = sheet.cell_value(nRows,nCols + 2)
                        r['year'] = str(sheet.cell_value(nRows,nCols + 3))[0:4]
                        r['valid'] = True
                        validData = True

                    # this gives the place : str(sheet.cell_value(nRows,0)))
                    # maybe add each of the users times to the tables to see where they stand overall

                if nRows >= 3 and nRows < (3 + len(records[0])) and raceDist == '5k':
                    records[0][nRows - 3]['name'] = sheet.cell_value(nRows,nCols)
                    records[0][nRows - 3]['time'] = sheet.cell_value(nRows,nCols + 1)
                    records[0][nRows - 3]['overall'] = nRows - 2
                    records[0][nRows - 3]['year'] = str(sheet.cell_value(nRows,nCols + 3))[0:4]
                elif nRows >= 3 and nRows < (3 + len(records[1])) and raceDist == '8k':
                    record = records[1][nRows - 3]
                    records[1][nRows - 3]['name'] = sheet.cell_value(nRows,nCols)
                    records[1][nRows - 3]['time'] = sheet.cell_value(nRows,nCols + 1)
                    records[1][nRows - 3]['overall'] = nRows - 2
                    records[1][nRows - 3]['year'] = str(sheet.cell_value(nRows,nCols + 3))[0:4]



    sheet = wb.sheet_by_index(1)
    numCols = sheet.ncols
    for nCols in range(1,numCols):
        if sheet.cell_value(1,nCols) != '':
            raceDist = sheet.cell_value(1,nCols)
            numRows = sheet.nrows
            for nRows in range(1,numRows):
                if sheet.cell_value(nRows,nCols) == '':
                    break
                elif name in sheet.cell_value(nRows,nCols).strip().lower():
                    nameFound = False
                    for rr in races:
                        if sheet.cell_value(nRows,nCols).strip().lower() == rr['name'].lower():
                            raceArr = rr['races']
                            r = raceArr[raceLen[raceDist]]

                            r['distance'] = raceDist
                            r['time'] = sheet.cell_value(nRows,nCols + 1)
                            r['meet'] = sheet.cell_value(nRows,nCols + 2)
                            r['year'] = str(sheet.cell_value(nRows,nCols + 3))[0:4]
                            r['valid'] = True
                            validData = True

                            nameFound = True

                    if not nameFound:
                        races += [{'name':sheet.cell_value(nRows,nCols).strip(),'races':[{'distance':'0k','time':'0:0','meet':'NA','year':'1970'} for x in range(4)]}]

                        raceArr = races[-1]['races']
                        r = raceArr[raceLen[raceDist]]

                        r['distance'] = raceDist
                        r['time'] = sheet.cell_value(nRows,nCols + 1)
                        r['meet'] = sheet.cell_value(nRows,nCols + 2)
                        r['year'] = str(sheet.cell_value(nRows,nCols + 3))[0:4]
                        r['valid'] = True
                        validData = True


                if nRows >= 3 and nRows < (3 + len(records[2])) and raceDist == '5k':
                    records[2][nRows - 3]['name'] = sheet.cell_value(nRows,nCols)
                    records[2][nRows - 3]['time'] = sheet.cell_value(nRows,nCols + 1)
                    records[2][nRows - 3]['overall'] = nRows - 2
                    records[2][nRows - 3]['year'] = str(sheet.cell_value(nRows,nCols + 3))[0:4]
                elif nRows >= 3 and nRows < (3 + len(records[3])) and raceDist == '6k':
                    record = records[1][nRows - 3]
                    records[3][nRows - 3]['name'] = sheet.cell_value(nRows,nCols)
                    records[3][nRows - 3]['time'] = sheet.cell_value(nRows,nCols + 1)
                    records[3][nRows - 3]['overall'] = nRows - 2
                    records[3][nRows - 3]['year'] = str(sheet.cell_value(nRows,nCols + 3))[0:4]

    sheet = wb.sheet_by_index(2)
    numCols = sheet.ncols
    for nCols in range(1,numCols):
        if sheet.cell_value(1,nCols) != '':
            numRows = sheet.nrows
            for nRows in range(1,numRows):
                if sheet.cell_value(nRows,nCols) == '':
                    break
                elif name in sheet.cell_value(nRows,nCols).strip().lower():
                    nameFound = False
                    for rr in races:
                        if sheet.cell_value(nRows,nCols).strip().lower() == rr['name'].lower():
                            raceArr = rr['races']
                            r = raceArr[raceLen['Half Marathon']]

                            r['distance'] = 'Half Marathon'
                            r['time'] = sheet.cell_value(nRows,nCols + 1)
                            r['meet'] = 'NIRCA Half Marathon'
                            r['year'] = str(sheet.cell_value(nRows,nCols + 2))[0:4]
                            r['valid'] = True
                            validData = True

                            nameFound = True

                    if not nameFound:
                        races += [{'name':sheet.cell_value(nRows,nCols).strip(),'races':[{'distance':'0k','time':'0:0','meet':'NA','year':'1970'} for x in range(4)]}]

                        raceArr = races[-1]['races']
                        r = raceArr[raceLen[raceDist]]

                        r['distance'] = raceDist
                        r['time'] = sheet.cell_value(nRows,nCols + 1)
                        r['meet'] = sheet.cell_value(nRows,nCols + 2)
                        r['year'] = str(sheet.cell_value(nRows,nCols + 3))[0:4]
                        r['valid'] = True
                        validData = True

    return validData


def emailfnc (first, last, email, gradyear):

    receivers = ['ucrunningclubcontact@gmail.com']
    subject = last + " - Club Interest"

    sender = 'ucrunningclubcontact@gmail.com'
    password = 'Catsby90!'

    # It seems that it does not really work when ':' are used in the email content.
    content =  "Name - " + last + ", " + first + ". Email - " + email + ". Grad year - " + gradyear + "."
    print(content)


    message = "From: Club Interest <ucrunningclubcontact@gmail.com> \nTo: Club Interest <ucrunningclubcontact@gmail.com>\nSubject: " + subject + "\n" + content

    try:
       emailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
       emailserver.login(sender,password)
       emailserver.sendmail(sender, receivers, message)
       emailserver.quit()
    except Exception:
       print ("Email was not sent successfully. Try again.")

# Create your views here.
def home(request):

    posts = Post.objects.all()
    for p in posts:
        if len(p.content) > 140:
            str = p.content
            p.content = str[0:140] + "..."

    fname = ""
    lname = ""
    email = ""
    year = ""
    try:
        fname = request.POST['first_name']
        print(fname)
        lname = request.POST['last_name']
        print(lname)
        email = request.POST['email']
        print(email)
        year = request.POST['optradio']
        print(year)

        emailfnc(fname, lname, email, year)
    except:
        print('No valid name')



    socialMedia = [{'site':'Twitter','handle':'@UCClubRunning','url':'https://twitter.com/ucclubrunning'}, {'site':'Instagram','handle':'@UCClubRunning','url':'https://www.instagram.com/ucclubrunning/'}]

    context = {
        'homeActive' : True,
        'stories' : posts[0:3],
        'socialMedia' : socialMedia
    }
    return render(request, 'Main/home.html',context)


# Create your views here.
def about(request):
    context = {
        'infoActive' : True,
        'AboutUsLinks': AboutUsLinks,
    }
    return render(request, 'Main/about.html', context)

# Create your views here.
def news(request, year = '', month=''):
    #User.objects.all().order_by(
    posts = []
    archives = []
    archivesDate = []

    for n in Post.objects.all().order_by('-date_posted'):


        if (Months[n.date_posted.month] + ' ' + str(n.date_posted.year)) not in archivesDate:
            archivesDate += [Months[n.date_posted.month] + ' ' + str(n.date_posted.year)]
            archives += [{
                            'Date':Months[n.date_posted.month] + ' ' + str(n.date_posted.year),
                            'Y':n.date_posted.year,
                            'M':n.date_posted.month
                        }]

        if str(n.date_posted.year) == year or len(year) == 0:
            #print(str(n.date_posted.month) + '==' + month)
            if str(n.date_posted.month) == month or len(month) == 0:
                paragraphs = n.content.splitlines()
                post = {
                    'title': n.title,
                    'author': n.author,
                    'date_posted': n.date_posted,
                    'content': paragraphs
                }
                posts += [post]


    context = {
        'newsActive' : True,
        'posts' : posts,
        'archives' : archives
    }
    return render(request, 'Main/news.html',context)

# Create your views here.
def records(request,fullName=''):

    name = fullName.replace('_',' ')

    races =  []#[{'distance':'0k','time':'0:0','meet':'NA','year':'1970'} for x in range(4)]
    athlete = []
    records = [[{'name':'__','time':'0:0','year':'1970','overall':-1} for x in range(10)] for xx in range(4)]

    isCross = True
    crossColor = "F8F8F8"
    trackColor = "E8E8E8"
    crossText = "000000"
    trackText = "5F5F5F"
    try:
        name = request.POST['u_name']
    except:
        name = "_____"
        print('No valid name')

    try:
        b = request.POST['sport']
        if b == "Track":
            isCross = False
            crossColor = trackColor
            trackColor = "F8F8F8"
            crossText = "5F5F5F"#5F5F5F
            trackText = "000000"
    except:
        print('No valid sport')

    validData = readExcel(records,races,name)

    context = {
        'recordsActive' : True,
        'races' : races,
        'name': name,
        'validData' : validData,
        'mens5kRecords': records[0],
        'mens8kRecords': records[1],
        'womens5kRecords': records[2],
        'womens6kRecords': records[3],
        'CrossCountry': isCross,
        'CrossColor' : trackColor,
        'TrackColor' : crossColor,
        'CrossText' : trackText,
        'TrackText' : crossText
    }

    return render(request, 'Main/records.html',context)

# Create your views here.
def schedule(request):
    context = {
        'scheduleActive' : True,
        'meets' :  Meet.objects.all()
    }
    return render(request, 'Main/schedule.html',context)

# Create your views here.
def FAQs(request):
    context = {
        'infoActive' : True,
        'faq' :  FAQ.objects.all()
    }
    return render(request, 'Main/FAQ.html',context)

def Exec(request):
    #.order_by('-date_posted'):
    wholeExec = []

    exec = Executives.objects.all().order_by('-order').reverse()

    for e in exec:
        email = True
        picture = False
        if e.email.lower() == "none":
            email = False

        urlStr = ""
        if len(str(e.picture)) > 4:
            picstring = str(e.picture)
            urlStr = picstring[len('media/'):len(picstring)]
            print(e.picture)
            print(urlStr)

            picture = True


        wholeExec += [{"exec2": e, 'about':e.about.splitlines(), 'isValidEmail': email, 'isValidPicture': picture, 'picUrl':urlStr}]



    context = {
        'infoActive' : True,
        'exec' : wholeExec,#Executives.objects.all().order_by('-order').reverse(),
    }
    return render(request, 'Main/Exec.html',context)

def Routes(request):
    routes = Route.objects.all().order_by('-order').reverse()


    routesContext = []
    for r in routes:
        routeArr = []
        num = 1

        ## This is code that parses the directions of the routes
        # TODO probably better to make this dict but come back to that
        routestring = str(r.directions)
        root = ET.parse(routestring).getroot()
        for c in root.getchildren():

            if c.tag == 'Direction':
                route = {'direction':'__','comment':[]}

                for cc in c.getchildren():
                    if cc.tag == 'Text':
                        route['direction'] = str(num) + ". " + cc.text
                        #routeArr += [str(num) + ". " + cc.text]
                    if cc.tag == 'Sub':
                        route['comment'] += [" - " + cc.text]
                        #routeArr += [" - " + cc.text]
                routeArr += [route]
            if c.tag == 'Option':

                let = 'a'
                for cc in c.getchildren():
                    if cc.tag == 'Direction':
                        route = {'direction':'__','comment':[]}
                        for ccc in cc.getchildren():
                            if ccc.tag == 'Text':
                                route['direction'] = str(num) + let + ". " + ccc.text
                                #routeArr += [str(num) + let + ". " + ccc.text]
                            if ccc.tag == 'Sub':
                                route['comment'] += [" - " + ccc.text]
                                #routeArr += [" - " + ccc.text]
                        routeArr += [route]
                    let = chr(ord(let) + 1)

            num = num + 1

        ## This is code for the image
        # TODO maybe pass something in the context that shows what height and width percentages to display the image at
        urlStr = ""
        width = 0
        height = 0

        if len(str(r.picture)) > 4:

            picstring = str(r.picture)
            urlStr = picstring[len('media/'):len(picstring)]

            im = Image.open(picstring)
            width, height = im.size

            print("pre-height: " + str(height) + ", pre-width: " + str(width))
            normalize = max([width, height]) * 1.0
            width = (width / normalize) * ( 100.0)
            height = (height / normalize) * ( 100.0)

            print("height: " + str(height) + ", width: " + str(width))

        # TODO remake route context to encompass all the old info with new directions and image size
        routesContext += [{'name':r.name,'instructions':routeArr,'picture':urlStr, 'size': {'h':height,'w':width}}]

    threes = []
    thirdCounter = 0
    for r in routesContext:
        if thirdCounter % 3 == 0:
            threes += [[]]
        threes[int(thirdCounter/3)] += [r]
        thirdCounter += 1

    for r in routesContext:
        if thirdCounter % 3 == 0:
            threes += [[]]
        threes[int(thirdCounter/3)] += [r]
        thirdCounter += 1


    #for t in threes:
    #    for tt in t:
    #        print(t.name)
    ## TODO -- consider grouping routes into three ( or some derivable number optimal to screen size) to make each row look more uniform
    ## OR pass pictures separatly and make sure that they all match up (seems unsafe though)
    context = {
        'infoActive'    : True,
        'routes'        : routesContext,
        'routes2'       : threes
    }
    return render(request, 'Main/routes.html',context)
