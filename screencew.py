import gtk.gdk
import dropbox
import os

client = dropbox.client.DropboxClient('<access-token>')
print 'linked account: ', client.account_info()
w = gtk.gdk.get_default_root_window()
sz = w.get_size()
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
if (pb != None):
    pb.save("screenshot.png","png")

f = open('screenshot.png', 'rb')
response = client.put_file('/came-from-desk.png', f)
print 'uploaded: ', response
os.remove("screenshot.png")
print "File Removed!"

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata


