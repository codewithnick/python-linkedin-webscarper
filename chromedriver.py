from tkinter import *
from time import *
def submit():
    root.destroy()
root=Tk()
a=StringVar()
b=StringVar()
c=IntVar()
l1=Label(root,text="enter the search string")
l1.grid(row=0,column=0)
l2=Label(root,text="enter the location")
l2.grid(row=1,column=0)
l3=Label(root,text="enter number of pages to be searched")
l3.grid(row=2,column=0)
e1=Entry(root,textvariable=a)
e1.grid(row=0,column=1)
e2= Entry(root,textvariable=b,width=15)
e2.grid(row=1,column=1)
e3= Entry(root,textvariable=c,text='1',width=15)
e3.grid(row=2,column=1)
b1=Button(root,text="submit",command=submit)
b1.grid(row=3,column=0)
root.mainloop()
search_string='"'+(a.get()).upper()+'"'
location='"'+(b.get()).upper()+'"'
countries=[]
c=c.get()
count=int(c)
print("pages =",count)
default='uk.'
############################################################################excel call###########################################################
from selenium import webdriver
import random
import time
import xlwt 
from xlwt import Workbook 
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0, 'Name') 
sheet1.write(0,1,' Title') 
sheet1.write(0,2,' Company') 
sheet1.write(0,3,' Location') 
sheet1.write(0,4,' Email')
sheet1.write(0,5,' linkedin link') 
driver = webdriver.Chrome('chromedriver')
row=1
col=0
##############################################################################function##################################################################33
def run(count,row):
    col=0
    linkedin_urls = driver.find_elements_by_class_name('iUh30')
    linkedin_urls = [url.text for url in linkedin_urls]
    sleep(0.5)
    print(linkedin_urls)
    for linkedin_url in linkedin_urls:
        name=title=company=location=email=' '
        if (linkedin_url !='' and linkedin_url !='https://www.linkedin.com/in/...'):
            linkedin_url=linkedin_url.replace(default,'https://www.',1)
            linkedin_url=linkedin_url.replace(' › ','/in/')+'/'
            print(linkedin_url)
            try:
                driver.get(linkedin_url)
                url.append(linkedin_url)
            except:
                pass
            try:
                name=driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[2]/div[1]/ul[1]/li[1]')
                name=name.text
                
                #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[2]/div[1]/ul[1]
                #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[2]/div[1]/ul[1]/li[1]
            except:
                ######################################## trying name in li tag########################################3
                try:
                    name=driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[2]/div[1]/ul[1]')
                    name=name.text
                    #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[2]/div[1]/ul[1]
                    #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[2]/div[1]/ul[1]/li[1]
                except:
                    
                    print("\n",linkedin_url,"name not found again")
                    pass
                print("\n",linkedin_url,"name not found")
                pass
            try:
                #title=driver.find_element_by_class_name('t-16 t-black t-bold')
                title=driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3')
                title=title.text
                #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3
                #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3
            except:
                print("\n",linkedin_url,"title not found")
                pass
            try:
                #company=driver.find_element_by_class_name('pv-entity__secondary-title t-14 t-black t-bold')
                company=driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3')
                company=company.text
                #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3
                #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/p[2]
                #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/p[2]
            except:
                print("\n",linkedin_url,"company not found")
                pass
            try:
                location=driver.find_element_by_xpath('/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h4/span[2]')
                location=location.text
                #/html/body/div[6]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h4/span[2]
            except:
                print("\n",linkedin_url,"location not found")
                pass
            #time.sleep((random.rand()%3)/2)
            try:
                driver.get(linkedin_url+'detail/contact-info/')
            except:
                pass
            try:
                email= driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/section/div/div[1]/div/section[3]/div/a')
                email=email.text
            except:
                print("\n",linkedin_url,"email not found")
                pass
            sheet1.write(row,col, name) 
            sheet1.write(row,col+1, title) 
            sheet1.write(row,col+2, company) 
            sheet1.write(row,col+3, location) 
            sheet1.write(row,col+4, email)
            sheet1.write(row,col+5, linkedin_url)
            row+=1
        wb.save('database.xls')
    #file.close()
#####################################################################next page 2#####################################################################3
    if count>0:
        x=count
        driver.get('https:www.google.com')
        #sleep(3)
        search_query = driver.find_element_by_name('q')
        search_query.send_keys('site:linkedin.com/in/ AND '+search_string+ ' AND ' +location)
        #sleep(5)
        search_query.send_keys('\n')
        #sleep(3)
        while(x>0):
            next_page = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[5]/div/span[1]/div/table/tbody/tr/td[12]/a/span[2]')
            # .click() to mimic button click
            next_page.click()
            x-=1
        count-=1
        run(count,row)
    else:
        driver.quit()
    return url
    

# imports
from selenium import webdriver
import time
#driver = webdriver.Chrome('chromedriver')
# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')
time.sleep(0.5)
# locate email form by_class_name
username = driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[1]/div[1]/input')
# send_keys() to simulate key strokes
username.send_keys('nikhilsingh892710@gmail.com')
# sleep for 0.5 seconds
#sleep(0.5)
# locate password form by_class_name
password = driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[1]/div[2]/input')
# send_keys() to simulate key strokes
password.send_keys('joiniisc')
#sleep(0.5)
# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('/html/body/nav/section[2]/form/div[2]/button')
# .click() to mimic button click
sign_in_button.click()
time.sleep(1)
driver.get('https:www.google.com')
#sleep(3)
search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND '+search_string+ ' AND ' +location)
#sleep(5)
search_query.send_keys('\n')
#sleep(3)

url=[]
run(count,row)

file=open('__pycache__/url.text','w')
for i in url:
    file.write(i+'\n')
file.close()






    
#run()
    
