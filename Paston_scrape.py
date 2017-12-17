import requests, json, re

home_page = requests.get("http://name.umdl.umich.edu/Paston")

from bs4 import BeautifulSoup
soup = BeautifulSoup(home_page.content, 'html.parser')

Paston_main=[]

Paston_dictionary_list = []

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


        # a_content = new_variable.find_all("p")
        # letter_content=""
        # for some_content in a_content:
        #      letter_content = letter_content + some_content.text

        new_dictionary={"Writer":a_writer,"Recipient":a_name}
        Paston_dictionary_list.append(new_dictionary)

json.dump(Paston_dictionary_list,open("Paston_Letters_4.json","w"),indent=4)

#If needed later, add to new_dictionary statement: "Year":a_year,
