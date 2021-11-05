from WanakaTime import WanakaTime


def run():
    wanakatime = WanakaTime()

    while wanakatime.active:
        wanakatime.menu()


run()
