import requests
try:
        url = 'https://f6.dnkiri.com/TV/Snowdrop/Snowdrop.E09.(NKIRI.COM).niovnfindfinvoindfinbginbofignboingfnib.mkv'
        # url = 'https://youtu.be/O6nnVHPjcJU'
        # headers = {
                # 'X-Requested-With': 'ECVPHttpRequest',
                # }
        r = requests.get(url=url)
        print(r.ok)
except Exception as ex:
        b = ex
        r = None


if r is not None:
        with open('Snowdrop.E09.mp4', 'wb') as f:
                f.write(r.content)
        print('Successfully downloaded')
else:
        print('Error {}'.format(ex))