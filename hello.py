print("hello how are you")
def count_in_file():
    filename = input("Please enter the filename: ")
    try:
        opening = open(filename)
    except:
        print("The filename you entered does not exit", filename)
        quit()

    read = opening.read()
    count = 0
    good1 = "good"
    for good1 in read:
        count += 1
    print("you have " + str(count) + " " + "'" + good1 + "'" + " in your document")

def count():
    word = input("Please enter word you wish to search for in the text: ")
    text = """the quick brown fox jumps over the lazy dog.  he went to school the other day. He like going to school. Welcome to XAMPP for Windows 7.3.9
You have successfully installed XAMPP on this system! Now you can start using Apache, MariaDB, PHP and other components. You can find more info in the FAQs section or check the HOW-TO Guides for getting started with PHP applications.

XAMPP is meant only for development purposes. It has certain configuration settings that make it easy to develop locally but that are insecure if you want to have your installation accessible to others. If you want have your XAMPP accessible from the internet, make sure you understand the implications and you checked the FAQs to learn how to protect your site. Alternatively you can use WAMP, MAMP or LAMP which are similar packages which are more suitable for production.

Start the XAMPP Control Panel to check the server status.

Community
XAMPP has been around for more than 10 years – there is a huge community behind it. You can get involved by joining our Forums, adding yourself to the Mailing List, and liking us on Facebook, following our exploits on Twitter, or adding us to your Google+ circles.

Contribute to XAMPP translation at translate.apachefriends.org.
Can you help translate XAMPP for other community members? We need your help to translate XAMPP into different languages. We have set up a site, translate.apachefriends.org, where users can contribute translations.

Install applications on XAMPP using Bitnami
Apache Friends and Bitnami are cooperating to make dozens of open source applications available on XAMPP, for free. Bitnami-packaged applications include Wordpress, Drupal, Joomla! and dozens of others and can be deployed with one-click installers. Visit the Bitnami XAMPP page for details on the currently available apps."""
    separate = text.split()
    #word = "the"
    count = 0
    try:
        for word1 in separate:
            if word1 == word:
                count += 1
    except:
        print("Word not found in text")
    print("The number of " + "'" + word + "'" + " in the text is " + str(count))


def recount():
    name = input("Enter filename: ")
    show = open(name)
    words = {}
    for line in show:
        divide = line.split()
        for word2 in divide:
            words[word2] = words.get(word2, 0) + 1

    print(word2, words)


recount()

#for item in range(0, 10):
    #print("You are welcomed")
