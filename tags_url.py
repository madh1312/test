import subprocess as sp
import os 
import sys 
import re

#os.chdir('c:/Users/c.kummari/20210810_GitHub_Repos/terraform-aws-s3')
os.chdir('/Users/cloudbinary/git-python/test')
git_url = sp.getoutput('git config --get remote.origin.url')
git_tag = sp.getoutput('git tag --sort=committerdate | tail -1')

tagged_link = "%s?ref=%s" % (git_url,git_tag)
print(tagged_link)

#defining the replace method
def replace(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        #read the file contentsz
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)
#source = "git@github.com:sede-x/terraform-aws-s3.git?ref=v0.10"
def search(file_path):
    with open("main.tf","r+") as Input :
        for link in Input:
            link_list = re.findall(r'source\s=\s"[(.\/\.\s \"\")|git@github.com|https://github.com]\S+"$',link)
            print(link_list)

            for links in link_list:
                olink = links
                print(olink)
                return olink
        
     

file_path = "main.tf"
text = search(file_path)
subs = 'source = "%s" ' % tagged_link
print(subs)

#calling the replace method
replace(file_path, text, subs)
