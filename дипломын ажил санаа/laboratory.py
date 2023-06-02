import requests


def synthesize(text):
    url = "https://api.chimege.com/v1.2/synthesize"
    headers = {
        'Content-Type': 'plain/text',
        'Token': '7beeec813d70ad2efdab4f623968557af4fdc4f35a844894e9b3929230f38137',
    }

    r = requests.post(
        url, data=text.encode('utf-8'), headers=headers)

    with open("output.wav", 'wb') as out:
        out.write(r.content)


print(synthesize('Сайн байна уу таньд юугаар туслах вэ?'))
