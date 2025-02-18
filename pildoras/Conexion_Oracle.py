#coding: utf-8
import cx_Oracle
con = cx_Oracle.connect('CAPEX_19', 'BEMORE19', '192.168.44.4:1522/CAPEX')
dsn_tns = cx_Oracle.makedsn('192.168.44.4', 1522, 'CAPEX')
print (con.version)
con.close()
print (dsn_tns)
