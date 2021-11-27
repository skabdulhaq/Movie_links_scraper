import requests
from bs4 import BeautifulSoup
import smtplib




message = ""

def email_send(from_email, password, to_email, subject, message_):
    postman = smtplib.SMTP(host="smtp.gmail.com", port=587)
    postman.starttls()
    postman.login(user=from_email, password=password)
    postman.sendmail(from_addr=from_email, to_addrs=to_email
                     , msg=f"Subject:{subject}\n\n{message_}")
    postman.close()


def movie_rulz_crawler(url_of_movie):
    global message
    response_movie_links = requests.get(url_of_movie)
    movie_soup = BeautifulSoup(response_movie_links.text, "html.parser")
    all_torrent_links = movie_soup.find_all(name="a", class_="mv_button_css")

    for torrent in all_torrent_links:
        print(f"{torrent.getText().split()[-1]} {torrent.getText().split()[-2]}")
        print(torrent.get("href"))
        message = message + f"{torrent.getText().split()[-1]} {torrent.getText().split()[-2]}\n{torrent.get('href')}\n\n"


search = True
help_ = True
while search:
    if help_:
        print("Type Help To Know More")
    movie_url = input("Enter The Movierulz Url Hear =>> ")
    if movie_url.lower() == "exit" or movie_url.lower() == "quit":
        search = False
    elif movie_url.lower() == "help":
        print("Enter Url of Movie Page Hear Below From Movierulz")
        help_ = False
    else:
        try:
            movie_rulz_crawler(movie_url)
            print("Type Exit To Quit The Programme.")
            help_ = False
        except:
            print("Invalid Movierulz Link")
            help_ = False
    #Enter Your Gmail And Password Hear Below
    email_google = ""
    password_google = ""
    email_send(email_google, password_google, email_google, "Movie Links", message)
