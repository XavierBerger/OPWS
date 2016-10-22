from bottle import route, run, static_file, template

name="My Web Site"

pages = {
  1 : { 'Intro': '''<h1>Scrolling Nav</h1>'''
                 '''<p><strong>Usage Instructions:</strong> '''
                 '''Make sure to include the <code>scrolling-nav.js</code>, <code>jquery.easing.min.js</code>, and <code>scrolling-nav.css</code> files. To make a link smooth scroll to another section on the page, give the link the <code>.page-scroll</code> class and set the link target to a corresponding ID on the page.</p>
                    <a class="btn btn-default page-scroll" href="#about">Click Me to Scroll Down!</a>
                    '''},
  2 : { 'About': '''<h1>About Section</h1>'''},
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
