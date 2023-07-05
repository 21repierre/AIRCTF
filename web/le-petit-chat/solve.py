from hashlib import sha1
from src import app

print(app.base_url + "/file/flag.txt?exp=2688558310&sig=" + sha1(f"{app.base_url}/file/flag.txt?exp=2688558310".encode()).hexdigest())