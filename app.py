#!./env/Scripts/python.exe


'''
TODO: print cwd after chaning directory

'''


from selenium import webdriver
from dotenv import load_dotenv
import sys
import os

load_dotenv()

browser = webdriver.Firefox()
url = "https://www.github.com/login"
browser.get(url)

username = browser.find_element("xpath",'//*[@id="login_field"]')
username.click()
username.send_keys(os.getenv("USER"))

password = browser.find_element("xpath",'//*[@id="password"]')
password.click()
password.send_keys(os.getenv("PASS"))

submit = browser.find_element("xpath","/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[11]")
submit.click()


browser.get("https://github.com/new")

if len(sys.argv) > 1:
    pass
else:
    print("[-] No Repository name was provided!")
    print("[*] use help argument to get more info.")
    exit()


repo_name = sys.argv[1]
print(repo_name)

field_name = browser.find_element("xpath",'//*[@id="repository_name"]')
field_name.send_keys(repo_name)

# make the repository private
browser.find_element("xpath",'//*[@id="repository_visibility_private"]').click()
# create the repo
browser.find_element("css selector",'html body.logged-in.env-production.page-responsive.js-page-new-repo.intent-mouse div.logged-in.env-production.page-responsive.js-page-new-repo div.application-main main div.container-md.my-6.px-3.px-md-4.px-lg-5 form#new_repository.js-braintree-encrypt.js-repo-form div.js-with-permission-fields button.btn-primary.btn').submit()

# Setting and hooking up the local repo to github
cwd = os.getcwd()
os.system("mkdir "+os.path.join(cwd,repo_name))
os.chdir(repo_name)
print("[*] New Folder Created.")
print(os.getcwd())

os.system('echo "# ' + repo_name + '" >> README.md')
print("[*] Created README")
os.system('git init')
os.system('git add README.md')
os.system('git commit -m "first commit"')
os.system('git branch -M main')

git_link = "https://github.com/thatsyogeshjjr/"+repo_name+".git"
os.system("git remote add origin "+git_link)
os.system("git push -u origin main")
print("[*] Setting up remote repository")
print("[*] Finished.")

