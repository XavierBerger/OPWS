from bottle import route, run, static_file, template
import sysinfo

name="My Web Site"

pages = {
  1 : { 'Intro': '''<h1>System Information</h1>'''
                 '''<p>This is an example of usage of OPWS.</p>'''
                 '''<a class="btn btn-default page-scroll" href="#system">View system information!</a>'''},
  2 : { 'System': '''<h1>System Information</h1>'''
                 '''<pre>''' + sysinfo.getsysinfo() + '''</pre>'''},
  3 : { 'Services': '''<h1>Services Section</h1>'''},
  4 : { 'Contact': '''<h1>Contact Section</h1>'''},
  }

@route('/')
def index():
  menu=""
  section=""
  for index, sections in pages.iteritems():
    for sectionTitle, sectionContent in sections.iteritems():
      if index == 1 : 
        visibility="class=hidden"
      else:
        visibility=""
      if ( index % 2 == 0 ) :
        backgroung = "grey"
      else :
        backgroung ="white"
      sectionName="".join(sectionTitle.split()).lower()
      menu += template('menu', visibility=visibility, sectionTitle=sectionTitle, sectionName=sectionName )
      section += template('section', sectionName=sectionName, sectionContent=sectionContent, backgroung=backgroung )
  return template('index', name=name, menu=menu, section=section)

@route('/js/<filename>')
def js(filename):
    return static_file(filename, root='./js/')

@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='./css/')
        
run(host='localhost', port=8080, debug=True)
