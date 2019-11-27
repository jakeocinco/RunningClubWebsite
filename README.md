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


## Site Tour and Features
* Landing Page (https://runningclubwebsite.herokuapp.com/)
  * This page is very simple and at face value provides a quick run down of our running club, it offers a quick paragraph of general information as well as information on how to get involved. Below that it features a little bit of our social media as well as Vlog from our trip to Nationals in 2017. On the top right it also features a 'Contact Us' button, this is important as it provides any potential new members with a place to reach out to club leadership who will get back to them with info on how to join. Below that is a little bit of news to keep everyone updated with the recent accomplishments of the club.
* News Page (https://runningclubwebsite.herokuapp.com/news/)
  * This page very simply shows a news feed of all of the articles that we have written after attending races and event. If you want to find events from specific months, you can use our archive panel on the right to open up those articles in their own page. You call also accomplish this by appending the url with either '/[four digit year]/' or '/[four digit year]/[two digit month]/' to get all articles from that year or that specific month. All of this content can be updated by administrators who update the 'Posts' model on the admin page.
* Schedule Page (https://runningclubwebsite.herokuapp.com/schedule/)
 * This page features the club schedule in the coming season, it features the name of the event with the location and prospective start time. They are all ordered with the soonest event first. These can also be added by adding an entry to the 'Meet' model on the admin page. There administrators will also have the ability to add signup link which they can decide to show or hide at anytime.
* Records Page (https://runningclubwebsite.herokuapp.com/records/)
  * The records page features the Top 10 times for men and women in all Cross country events. It can also show a user the individual times of any club runner, if they look up their name in the search box at the top of the screen. A user can search by full, first, or last name. The search will return any results that contain the query. For example, I am in their under both my given first name and my used first name, so searching my last name will yield both results.
* Information Section
  * About Page
    * The about page is a very simple page that give a little bit of the clubs history and what our goals are, it also provides some important links for users.
  * Routes Page
    * The routes page features the routes that are most commonly used by the club team for practices starting at Gettler Stadium. It shows a picture, followed by the routes name, distance, and a break down of directions. These can be updated by administrators on the admin page by adding to the 'Route' model. These are not as simple to create as it requires adding XML formatted text to allow the server a standard format when parsing the routes.
      * Here is a sample of what the XML may look like:
        * This is the parent tag for the route - <Route name="routeName">
        * This is a standard direction - <Direction> <Text>Standard Direction</Text> </Direction>
        * This is a standard direction with a subcomment - <Direction> <Text>Standard Direction</Text> <Sub>comment.</Sub></Direction>
        * This is a direction with an option in it -
          <Option>
            <Direction><Text>Direction 1a</Text></Direction>
            <Direction><Text>Direction 1b</Text></Direction>
          </Option>
  * FAQ Page
    * The FAQ page provides a hub for any frequently asked questions users may have. These can again be added at the 'FAQ' model in the admin page.
