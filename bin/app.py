import web

urls = (
	'/', 'Index',
	'/form1','Form1'
	
	)

app = web.application(urls, globals())

render = web.template.render('templates/', base= "layout")

class Index(object):
	def GET(self):
		form = web.input(name = "Sid")
		greeting = "Hello, %s" % form.name
		return render.index(greeting = greeting)


class Form1(object):
	"""docstring for Form1"""
	def GET(self):
		return render.hello_form()

	def POST(self):
		form = web.input(name = "NOBODY")
		greeting = "%s, %s" %(form.greet, form.name)
		return render.index(greeting = greeting)
		


if __name__ == "__main__":
	app.run()
	