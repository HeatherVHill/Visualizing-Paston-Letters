# - scrape main page with BS to get list of URLs using the "a" items [href?]

import requests, json, re

home_page = requests.get("http://name.umdl.umich.edu/Paston")

from bs4 import BeautifulSoup
soup = BeautifulSoup(home_page.content, 'html.parser')

Paston_main=[]

Paston_dictionary_list = []

letter_id_counter=1

writer = soup.find_all("a", href=re.compile("rgn=div2"))

for variable in writer:
     Paston_main.append(variable.attrs["href"])

for individual_link in Paston_main:
    link_request = requests.get(individual_link)
    print("On page",individual_link,"of")
    link_request_content = BeautifulSoup(link_request.content,'html.parser')

    first_person_span = link_request_content.find("span", attrs={"class":"divhead"})
    first_person = first_person_span.find("a")
    a_writer = first_person.text

    all_divs = link_request_content.find_all("div", attrs = {"class": "textindentlevelx"})

    for new_variable in all_divs:

        try:
            a_person = new_variable.find("h3")
            a_string = a_person.text
            p = re.compile('\A\D*')
            a_cap_name = p.findall(a_string)
            a_trailing_name = a_cap_name[0].title()
            a_name = a_trailing_name.rstrip()

        except:
            a_name = "No recipient information"

        # try:
        #     a_person = new_variable.find("h3")
        #     a_string = a_person.text
        #     q = re.search("14\d*-\d*")
        #     a_year = q.findall(a_string)
        # except:
        #     a_person = new_variable.find("h3")
        #     a_string = a_person.text
        #     q = re.search("14\d*")
        #     a_year = q.findall(a_string)
            ##a_year = "Time information unavailable"


        a_content = new_variable.find_all("p")
        letter_content=""
        for some_content in a_content:
             letter_content = letter_content + some_content.text

        new_dictionary={"Writer":a_writer,"Recipient":a_name}
        Paston_dictionary_list.append(new_dictionary)
        letter_id_counter = letter_id_counter + 1

json.dump(Paston_dictionary_list,open("Paston_Letters_4.json","w"),indent=4)

#If needed later, add to new_dictionary statement: "Year":a_year,

#-----------------------------------
    # a_person = individual_link.find("h3")
    # a_name = a_person.text


#Add code to pull out pieces you want based on old code
#Put code in JSON file
#Use regex in JSON file to break down date and names (could pull just things that begin with "To..." since those will actually be letters, not wills or charters)


#writer = soup.find_all("div", attrs = {"class": "indentlevel1"})


# for variable in writer:
#     full_link = variable.find("a")
#     if full_link.has_attr("href"):
#         Paston_main.append(full_link.attrs["href"])
#
# Paston_main_set = set(Paston_main)
#
# Paston_full_links = []
#
# for variable in writer:
#     full_link_all = variable.findall("a")
#     if full_link_all.has_attr("href"):
#         Paston_full_links.append(full_link_all.attrs["href"])
#

        # individual_link = full_link.find("div",attrs = {"class":"resindentlevelx"})
        # print(individual_link)

        #need to do a second scrape and just do "find" as opposed to "findall" to pull out first link in each section
#        if ("div", attrs = "class":"resindentlevelx")
#            print(full_link.attrs["href"])



#     - put URLs into a list
#link_list = []



# - for variable in list - so pull out each URL as a new variable and enter it into a function



#     - scrape each URL and pull out the h2, h3, and p as described in the original Paston scrape, putting it into a dictionary


#     - create a csv file that enters sections in the dictionary



#Next week:         - once this file is made, I think I can use regex to pull out specific sections I want, like date and recipient; I think I could also then put the p sections through something, like put it all together and then search each section for the subject terms



#             -like maybe I'll put in all the basic HTML pieces into the dictionary, then I'll be able to use that file to pull out individual pieces of information. It'll be easier to get information from a dictionary because I can just use the key and not have to worry so much about pulling large amounts from the web...
