# this is a zip downloader for udacity
# intro to java course
# this will not be maintened
# to run
# python stealer.py



import subprocess as sub



def download_zips(lessons):
    counter = 1
    try:
        while counter <= lessons:
            url = "https://s3.amazonaws.com/udacity-hosted-downloads/lesson{}.zip".format(counter)
            outfile = "zip{}".format(counter)
            sub.call(["curl", url, "-o", outfile])
            print(".....curling..zip....file....{}.......".format(counter))
            counter += 1
        print('..........Java Lessons Downloaded.......')
    except:
        print("......ERROR......Try...Again....")

download_zips(4)
