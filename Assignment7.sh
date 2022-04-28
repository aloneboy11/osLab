# making zip file with password
touch test.py
zip myZip.zip test.py -e
rm test.py

# making rar file and then unrar it
touch rarTest.py
rar a myRar.rar rarTest.py
rm rarTest.py
unrar e myRar.rar
