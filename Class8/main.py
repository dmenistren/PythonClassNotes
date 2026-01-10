from utils import *
from auth import Auth

con, cur = db_conn()
auth = Auth(con, cur)
