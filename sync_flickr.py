#!/usr/bin/python
import flickr_api as f
import sys
import os

#photo_dir="/share/Multimedia/Photos/"
photo_dir="./"
execute = 0
##############################################
def download_set( user, photoset_idx ):
##############################################
    try :
        ps = user.getPhotosets()[photoset_idx]

        # Get Year to be used as a root folder
        alb_year = ps.title.split()[0]
        alb_dir = photo_dir+"/"+alb_year

        # now directory for an actuall set
        set_dir = alb_dir+"/"+ps.title
    
        if not os.path.exists(alb_dir) : os.mkdir(alb_dir)
        if not os.path.exists(set_dir) : os.mkdir(set_dir)
        os.chdir(set_dir)
        
        print "Downloading..."
        for p in ps.getPhotos() :
            # if title is empty, set it to set name
            if not p.title :
                title = ps.title
            else :
                title = p.title
            # let's check if this is a video or photo
            if not p.media == "video" :
                ext = "jpg"
            else :
                ext = "mp4"

            if not os.path.exists(title+"_"+p.id+"."+ext) :
                print "   "+title+"_"+p.id+"."+ext
                #print p.getInfo()
                if execute : p.save(title+"_"+p.id+"."+ext)
        
    except IndexError : pass
    return


##############################################
# Main code starts here
##############################################
try :
    #username = sys.argv[1]
    #try :
    #    access_token = sys.argv[2]
    #    f.set_auth_handler(access_token)
    #except IndexError : pass
    
    #u = f.Person.findByUserName(username)
    f.set_auth_handler("filename")
    u = f.test.login() 

    ps = u.getPhotosets()
    
    for i,p in enumerate(ps) :
        print i,p.title
        if 13  == i : download_set( u, i )
        #download_set( u,i )
except IndexError :
    print "usage: python show_albums.py username [access_token_file]"
    print "Displays the list of photosets belonging to a user"


