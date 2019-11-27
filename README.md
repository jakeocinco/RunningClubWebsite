# University of Cincinnati Running Club Website
This is a website that I have developed for the use of the University of Cincinnati Running club, it was also done as a honors experience for the University Honors Program.

The website is currently being hosted at https://runningclubwebsite.herokuapp.com/.

The goal of this site was to create a hub that the running club can use to disseminate information as well as become a portal for all club activities. The site built of the the club's current webpage (http://ucrunningclub.weebly.com/), and attempted to do everything that that website did in a more straight forward and visually appealing way, while also allowing club leadership to update information from an admin page rather than updating the static text on the screen. Where I believe this project fell short is that I was unable to implement sign ups, it is something I could do in the future but decided against it for the time being as I did not want to force users to share their information with a site that may not be secure.


## Technologies
This product was developed using a plethora of different technologies:
  * HTML/CSS - Like almost all webpages some degree of HTML and CSS had to be used to create static text on the screens. I tried to opt for as much user generated content and code as possible but there still had to be a rather large amount of these languages to provide content and style.
  * Bootstrap - While CSS was responsible for styling some of the text, I was really able to take advantage of bootstraps abilities. I often used their text stylings as it appears much more modern than the default HTML font. More importantly it provided me with a grid system that I used to organize content within a page; wether that be separating it into clusters or aligning it just right.
  * Python - Python was the primary development tool that I used for this application. I was able to use it to communicate with the databases and pull the user generated data as well as compute more complex operations than I could complete with HTML. I also used the Django development tool, which is a python library.
    * Django - Django is a python library that mainly functions as a web development tool and server. Through Django I was able to serve custom generated HTML files that featured User added information as well use forms of iteration and templating within the HTML code to minimize the need to rewrite common code. Django generates database code directly from python, which prevented me from needing to learn a new language.
  * SQLite and PostgreSQL - These were the two web databases that I used in this application, SQLite was used during the development faze and PostgreSQL is currently being used in the deployed application. Luckily, thanks to the Django library, I was able to interface with these databases directly from python.
