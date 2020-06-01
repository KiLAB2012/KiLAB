from instapy import InstaPy
from instapy import smart_run

def get_login():
    username = {}

    try:
        list_file = open('Combo.txt', 'r')

        for line in list_file:
            (name, password) = line.split(':')
            username[name] = password.strip()

            insta_username = "" + name + ""
            insta_password = "" + password + ""
            session = InstaPy(username=insta_username,
                              password=insta_password,
                              headless_browser=False)

            with smart_run(session):
                session.follow_by_list(followlist=['skyewigley'])
                session.end()

    except FileNotFoundError as err:
        print(err)

    return "Logged Into " + name + " Using " + password + "!"

print(get_login())
