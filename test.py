# -*- coding: utf-8 -*-
from sync.syncTrans import *

from fundata.client import init_api_client
from mysql.sqlConnect import sqlConnection,sqlDisconnection,sqlInsert,createTable
from mysql.dataHandler import api_transfer_sql,sqlColumn

if __name__ == "__main__":

   print(sync_match("2020-4-14 00:00:00",0,30105))
  

   







    
