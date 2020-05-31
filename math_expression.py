import tornado.ioloop
import tornado.web
from os import listdir
from os.path import isfile, join, isdir

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<html><head><title>SIGGRAPH 2019 Papers</title></head><body>")
        # sig19
        mypath = "resource/Siggraph2019"
        for f in sorted(listdir(mypath)):
        	paper_dir = "{}/{}".format(mypath, f)
        	if isdir(paper_dir):
        		self.write("<h1>{}</h1>".format(f)) 
        		self.write("<dl>") 
        		for paper in listdir(paper_dir):
        			internal_dir = "{}/{}".format(paper_dir, paper)
        			if isdir(internal_dir):
        				display_name = paper.replace('.', ':')
        				self.write("<dt><h2><a href=\"{}/{}.pdf\">{}</a></h2></dt>".format(internal_dir, paper, display_name)) 
        				for file in sorted(listdir(internal_dir)):
        					img_name = "{}/{}".format(internal_dir, file)
        					if ".png" in file:  
        						self.write("<img alt=\"Paper Video\" src=\"{}\" border=\"0\">".format(img_name)) 
        						self.write("<br>") 
        		self.write("</dl>") 
        # examples
        example = "resource/Online_examples"
        for f in sorted(listdir(example)):
        	paper_dir = "{}/{}".format(example, f)
        	if isdir(paper_dir):
        		self.write("<h1>{}</h1>".format(f)) 
        		self.write("<dl>") 
        		for img in sorted(listdir(paper_dir)):
        			img_name = "{}/{}".format(paper_dir, img)
        			if ".png" in img:  
						self.write("<img alt=\"Paper Video\" src=\"{}\" border=\"0\">".format(img_name)) 
						self.write("<br>") 
        		self.write("</dl>") 
        # classic
        classic = "resource/Classic_papers"
        for f in sorted(listdir(classic)):
        	paper_dir = "{}/{}".format(classic, f)
        	if isdir(paper_dir): 
        		self.write("<h1><a href=\"{}/{}.pdf\">{}</a></h1>".format(paper_dir, f, f)) 
        		self.write("<dl>") 
        		for img in sorted(listdir(paper_dir)):
        			img_name = "{}/{}".format(paper_dir, img)
        			if ".png" in img:  
						self.write("<img alt=\"Paper Video\" src=\"{}\" border=\"0\">".format(img_name)) 
						self.write("<br>") 
        		self.write("</dl>") 

        self.write("</body></html>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/resource/Siggraph2019/(.*)', tornado.web.StaticFileHandler, {'path': 'resource/Siggraph2019'}), 
        (r'/resource/Online_examples/(.*)', tornado.web.StaticFileHandler, {'path': 'resource/Online_examples'}),  
        (r'/resource/Classic_papers/(.*)', tornado.web.StaticFileHandler, {'path': 'resource/Classic_papers'}), 
        (r'/resource/(.*)', tornado.web.StaticFileHandler, {'path': 'resource'}), 
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()