from requests import get


class is_JMG7173_live_Exception(Exception):
    pass


jmg7173_channel_url = (
    "https://www.youtube.com/channel/UCtpDukzC0DT31_eoM2YcxEQ"
)


def is_JMG7173_live() -> bool:
    r = get(jmg7173_channel_url)
    if not r.ok:
        raise is_JMG7173_live_Exception(
            "Couldn't get JMG7173's Youtube Channel"
        )
    return 'yt-badge-live' in r.text


if __name__ == "__main__":
    print(
        'Yes' if is_JMG7173_live() else 'No'
    )
