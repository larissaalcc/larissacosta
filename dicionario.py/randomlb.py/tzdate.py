from datetime import datetime
from zoneinfo import ZoneInfo
ist=datetime.now()
print(ist)

cet=ist.astimezone(ZoneInfo('Europe/madrid'))
print(cet)