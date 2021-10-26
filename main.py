import config, csv, utility
from instapy import InstaPy
from instapy.util import smart_run

# Get all link post
link_temp = utility.get_test_data('data/link_target.csv')
link = []
for i in range(len(link_temp)):
    link.append(link_temp[i][0])

# Get all user/pass for buff 
userData = utility.get_test_data('data/account.csv')

def bot():
    print ("*****************PTMH********************")
    number = 0
    for akun in userData:
        number = number+1
        commentData = utility.get_test_data_random('data/comment.csv')
        print ("User", number, "buff is:", akun[0], "and Text comment is:", commentData)
        session = InstaPy(username=akun[0],
                        password=akun[1],
                        headless_browser=False)
        with smart_run(session):
                try:
                    session.login()
                    # Set like
                    # session.set_do_like(enabled=config.like, percentage=100)

                    # Get random one text comment in file csv for post on instagram
                    session.set_do_comment(enabled=config.comment, percentage=100)
                    session.set_comments(commentData)
                    session.interact_by_URL(link)
                    session.end()
                except Exception as e:
                    print ("[-] Failed ...")
                    print ("[-] Message : " + str(e))
                    print ("------------------------------------------------")

bot()