from email import header
from bs4 import BeautifulSoup
import requests
from lxml import etree

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

f = open('howard.txt','w')

URL = 'https://www.appily.com/colleges/howard-university'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

uni_name = soup.select('#block-fingerprint-content > div > article > div.college-overview--wrap > div.college-overview--inner.college-overview--sidebar > div.college-overview--main > div.college-overview--intro > div.college-overview--intro-heading > h1')
f.write("University: "+ uni_name[0].get_text(strip=True)+"\n")

acceptance_rate = soup.find('div', class_='field field--name-field-acceptance-rate field--type-integer field--label-hidden field__item')
f.write("Acceptance Rate: "+acceptance_rate.contents[0]+"\n")
#print(acceptance_rate.contents[0])

location = soup.find('div', class_='college-overview--info--location')
f.write("Location: " + location.contents[0]+"\n")
#print(location.contents[0])

#ea_deadline = soup.select('#block-fingerprint-content > div > article > div.college-overview--wrap > div.college-overview--inner.college-overview--sidebar > div.college-overview--main > section:nth-child(6) > div > div > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td')
div_tags = soup.find_all('div', class_="college-overview--admissions-deadlines")
for div_tag in div_tags:
    td_tags = div_tag.find_all('td')
early_action_deadline = td_tags[1]
regular_action_deadline = td_tags[3]
reply_deadline = td_tags[4]
f.write("Early Action Deadline: " + early_action_deadline.text + "\n")
f.write("Regular Deadline: " + regular_action_deadline.text + "\n")
f.write("Reply Deadline: " + reply_deadline.text + "\n")

outofstate_tution = soup.find('div',class_ = 'field field--name-field-out-of-state-tuition field--type-integer field--label-hidden field__item')
f.write("Out of State Tuition: " + outofstate_tution.contents[0]+"\n")
#print(outofstate_tution.contents[0])

instate_tution = soup.find('div',class_ = 'field field--name-field-in-state-tuition field--type-integer field--label-hidden field__item')
f.write("InState Tution: "+ instate_tution.contents[0]+"\n")
#print(instate_tution.contents[0])

room_board = soup.find('div',class_ = 'field field--name-field-room-and-board field--type-integer field--label-hidden field__item')
f.write("Room & Board Cost: "+ room_board.contents[0]+"\n")

avg_SAT = soup.select('#block-fingerprint-content > div > article > div.college-overview--wrap > div.college-overview--inner.college-overview--sidebar > div.college-overview--main > section:nth-child(7) > div.college-section--bordered.layout--33-33-33 > div:nth-child(3) > div:nth-child(3) > b')
#print(el[0].get_text(strip=True))

f.write("Average SAT Score: "+avg_SAT[0].get_text(strip=True)+"\n")

avg_ACT = soup.select('#block-fingerprint-content > div > article > div.college-overview--wrap > div.college-overview--inner.college-overview--sidebar > div.college-overview--main > section:nth-child(7) > div.college-section--bordered.layout--33-33-33 > div:nth-child(3) > div:nth-child(1) > b')
f.write("Average ACT Score: "+ avg_ACT[0].get_text(strip=True)+"\n")

avg_Aid = soup.find('div',class_='field field--name-field-average-grant-amount field--type-integer field--label-hidden field__item')

f.write("Average Aid Offered: "+ avg_Aid.contents[0]+"\n")


f.write("Scholarships:/n 1. Donor Scholarship Application - Howard University is accepting donor scholarship applications \nfor the 2023-2024 academic year. Students can submit one application to be considered for multiple scholarships. \nPriority is given to those who complete the Free Application for Federal Student Aid (FAFSA), while international \nstudents should submit the International Student Financial Aid Application (ISFAA) for better chances. Creating a \nHandshake Profile and maintaining good social standing are additional considerations. The application deadline is \nMarch 31, 2023, and notifications will be sent in the Fall. The Office of Financial Aid aims to assist students in \ncompleting their education at Howard University.\n2.Daniels Scholarship\n3.Gilman Scholarship\n")

f.write("For more info: https://financialservices.howard.edu/financial-aid/grants-scholarships-and-other-opportunities\n")
f.write("For Other Scholarships:https://financialservices.howard.edu/sites/financialaid.howard.edu/files/2022-12/External%20Scholarships%202023%2012-15-22.pdf")

f.write("On Campus housing-\nHoward University has nine Residence Halls on campus and 2 Residence Halls off-campus in private apartment complexes. Each residence hall has 24/7 controlled \nentry and front desk service, laundry facilities, and other amenities. The halls are managed by our Campus Apartments and WISH partners with additional facilities support.\nFor more info about dorm housing  - https://studentaffairs.howard.edu/housing/residence-halls.\n")
f.write("Off campus housing- https://howard.offcampuspartners.com/")

#f.write("The students of the university are called Hoyas. Their moto is Hoya Hoya Saxa. \n")
f.write("\nMajors offered: https://admission.howard.edu/undergraduate/academic-programs\n")
f.write("Diversity and inclusion resources: https://studentaffairs.howard.edu/diversity-inclusion\n")
f.write("AP Credits transfer information: https://apstudents.collegeboard.org/getting-credit-placement/search-policies/college/789")

f.close()
def text_to_pdf(input_file, output_file):
    # Read content from the text file
    with open(input_file, 'r', encoding='utf-8') as file:
        text_content = file.read()

    # Create a PDF file
    pdf_canvas = canvas.Canvas(output_file, pagesize=letter)
    
    # Set font and size
    pdf_canvas.setFont("Helvetica", 8)

    # Add the text content to the PDF
    x, y = 10, 750  # Starting coordinates
    line_height = 14  # Height between lines

    for line in text_content.split('\n'):
        pdf_canvas.drawString(x, y, line)
        y -= line_height

    # Save the PDF
    pdf_canvas.save()

# Example usage
text_file_path = 'howard.txt'  # Replace with the path to your text file
pdf_file_path = 'howardData.pdf'  # Replace with the desired output PDF file path

text_to_pdf(text_file_path, pdf_file_path)