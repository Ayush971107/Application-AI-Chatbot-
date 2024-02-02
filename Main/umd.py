from email import header
from bs4 import BeautifulSoup

import requests
from lxml import etree

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


f = open('UMD.txt','w')

URL = 'https://www.appily.com/colleges/university-of-maryland-college-park'
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

f.write("Merit Scholarships:\n 1. The Banneker/Key Scholarship \nIt is the most prestigious merit scholarship offered to incoming UMD freshmen. It can cover up to the full \ncost of tuition, mandatory fees, housing and food, a book allowance, and includes admission to the Honors \nCollege.In selecting Banneker/Key Scholars, the selection committee seeks to identify potential \nacademic leaders, who as individuals and as a group, will enrich and benefit from \nthe campus learning environment.\nAll freshman applicants who are admitted to the Honors College are considered for the Banneker/Key Scholarship. \nNo additional application materials are required. The selection committee carefully reviews the entire application \nof each early action deadline applicant, and semifinalists for the scholarship are invited to an interview in \nlate February or early March as part of the final selection process.\n link - https://financialaid.umd.edu/resources-policies/bannekerkey-scholarship-policy\n 2.President's Scholarship\nThe President's Scholarship provides four-year scholarship ranging from $2,000 to $12,500 per year. Both in-state \nand out-of-state applicants are eligible to receive the President's Scholarship. \nRecipients are identified through evaluation of admission application materials including academic achievement\n, extracurricular activities, awards, honors and an essay. Selected students will be notified of their scholarship by \nApril 1.\nlink - https://financialaid.umd.edu/resources-policies/presidents-scholarship-policy\n 3. Dean's Scholarship\nThe Dean's Scholarship offers an annual merit scholarship of $1,500 for freshman year or $4,500 per year for both \nfreshman and sophomore years. The Dean's Scholarship is not renewable, and only in-state applicants are eligible. \nRecipients are identified through evaluation of admission application materials including academic achievement\n, extracurricular activities, awards, honors and an essay. Each fall, roughly 400 new recipients of the Dean's \nScholarship are welcomed to the incoming class. Selected students will be notified of their scholarship by April 1.\nhttps://financialaid.umd.edu/resources-policies/deans-scholarship-policy\n")
f.write("Other helpful Scholarship tool - https://financialaid.umd.edu/resources-policies/scholarship-search\n")
f.write("On campus Housing - On Campus UMD has 9,601 beds in our 39 residence halls. Students may choose from many \nresidence hall housing options including traditional rooms, semi-suites, suites and apartments. \nlink - https://reslife.umd.edu/terp-housing/residence-halls#four-year")
f.write("\n here are several off-campus housing available around the University which are just a few minutes walk away. \nSome of these apartments include Tempo, Alloy, UView,\n For More information visit the link - https://ochdatabase.umd.edu/housing\n")
f.write("General Information: University of Maryland is also referred to as UMD. It's students are called the terps.\n")
#f.write("To know about Transfer credits - https://app.transfercredit.umd.edu/")
f.write("AP Credits transfers: https://apstudents.collegeboard.org/getting-credit-placement/search-policies/college/3633\n")
f.write("Information about majors offered: https://academiccatalog.umd.edu/undergraduate/programs/\n")
f.write("Diversity and inclusion resources: https://spp.umd.edu/our-community/diversity-inclusion-belonging-spp/inclusion-resources\n")

#f.write("Merit Scholarships: https://admissions.umd.edu/tuition/freshman-merit-scholarships\n")
#f.write("Need Based Scholarships: https://academiccatalog.umd.edu/undergraduate/fees-expenses-financial-aid/need-based-financial-assistance/\n")
#f.write("External Scholarships: https://gateway.campuslogic.com/ui/termsconsent\n")

f.close()



def text_to_pdf(input_file, output_file):
    # Read content from the text file
    with open(input_file, 'r', encoding='utf-8') as file:
        text_content = file.read()

    # Create a PDF file
    pdf_canvas = canvas.Canvas(output_file, pagesize=letter)
    
    # Set font and size
    pdf_canvas.setFont("Helvetica", 12)

    # Add the text content to the PDF
    x, y = 10, 750  # Starting coordinates
    line_height = 14  # Height between lines

    for line in text_content.split('\n'):
        pdf_canvas.drawString(x, y, line)
        y -= line_height

    # Save the PDF
    pdf_canvas.save()

# Example usage
text_file_path = 'UMD.txt'  # Replace with the path to your text file
pdf_file_path = 'umdData.pdf'  # Replace with the desired output PDF file path

text_to_pdf(text_file_path, pdf_file_path)