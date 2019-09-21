from hh_parcer import hh_parcer
from insdb import insert_to_db


if __name__=='__main__':
    vacs = hh_parcer()
    insert_to_db(vacs)
   

