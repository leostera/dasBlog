def go_to_index(selenium):
	"Opens the root of the website and waits for the page to load for 30 seconds."
	selenium.open('/')
	selenium.wait_for_page_to_load("30000")

def click(selenium,link,wait="30000"):
	"Helper function to click on a link from the index while waiting for the page to load"		
	selenium.click(link)
	selenium.wait_for_page_to_load(wait)

def click_and_check_content(testclass,link,content,wait="30000"):
	"Helper function that goes to a link and checks that some text is present in that page."
	go_to_index(testclass.selenium)
	click(testclass.selenium,link,wait)
	testclass.failUnless(testclass.selenium.is_text_present(content))

def open_and_check_content(testclass,url,content,wait="30000"):
	testclass.selenium.open(url)
	testclass.failUnless(testclass.selenium.is_text_present(content))
		
def admin_login(testclass):
	"Logs into the admin panel and verifies it's in there."
	testclass.selenium.open('/admin')
	testclass.selenium.type("id=id_username", "lea")
	testclass.selenium.type("id=id_password", "torosentadomirandoalnorte")
	click(testclass.selenium,"css=input[type=\"submit\"]")
	testclass.failUnless(testclass.selenium.is_text_present("Welcome, Leandro") )