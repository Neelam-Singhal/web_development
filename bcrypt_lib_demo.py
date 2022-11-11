'''
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
>>> bcrypt.generate_password_hash('texting')
b'$2b$12$0prDFZ7tBgmvt37uNgZIm.6J5P5SMenO7j8u4WqW5qV.BIsASRFhC'

>>> bcrypt.generate_password_hash('texting').decode('utf-8')
'$2b$12$lBTwwo10oomU08pMz3s5DuKVGD4mNDmEL4AG5vmQ1gx5NKRdS7WtW'

>>> bcrypt.generate_password_hash('texting').decode('utf-8')
'$2b$12$HHF2Wguv.TgMCtK18CguWONfex7P3ChmrPBLWp3SYAQG/CtDEpcSK'

>>> hashed_pwd = bcrypt.generate_password_hash('texting').decode('utf-8')

>>> bcrypt.check_password_hash(hashed_pwd, 'pass')
False
>>> bcrypt.check_password_hash(hashed_pwd, 'testing')
False
>>> bcrypt.check_password_hash(hashed_pwd, 'texting')
True
>>>


'''