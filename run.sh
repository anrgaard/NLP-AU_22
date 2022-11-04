# run this using bash run.sh (assuming you're in the NLP-AU_22 folder)

# from python3 import the module pip and from that install pandas
pip install -m pip install --upgrade pip
python3 -m pip install pandas

# run the code
# python3 nbs/class_07_livecoding.py -n Astrid -a 28

# or 
python3 nbs/class_07_livecoding.py -n $1 -a $2
# run using bash run.sh Astrid 28