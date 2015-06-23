import web

urls = (
	'/', 'Index'
	
	)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
	def GET(self):
		greeting = "Hello ssWorld"
		return render.index(greeting = greeting)


'''class first:
	"""docstring for first"""
	def GET(self):
		message = "First page"
		return render.index(greeting = greeting)'''
		


if __name__ == "__main__":
	app.run()
	