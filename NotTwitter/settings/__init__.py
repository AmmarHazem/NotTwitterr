from NotTwitter.settings.production import *

try:
    from NotTwitter.settings.settings import *
except:
    # AWS
    from NotTwitter.aws.conf import *

