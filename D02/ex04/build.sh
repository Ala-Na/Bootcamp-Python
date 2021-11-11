python3 -m pip install --upgrade pip 
python3 -m pip install --upgrade wheel
python3 -m pip install --upgrade setuptools

if [-d "dist"]
then
    rm -rf dist
    mkdir dist
else
    mkdir dist

python3 setup.cfg install
python3 setup.cfg bdist_wheel -w dist 