import re
import os
import sys
import pickle
from collections import defaultdict
from simple_table import SimpleTable

show_regex = re.compile('FPIP[0-9]{3}')
state_file = '.fpiplogs_state.pkl'

if os.path.exists(state_file):
    shows = pickle.load(open(state_file, 'rb'))
else:
    shows = defaultdict(set)

for line in sys.stdin:
    parts = line.split()

    match = None
    partial = None

    if '000' in parts or '206' in parts:
        partial = True
        match = show_regex.findall(line)

    elif '200' in parts:
        partial = False
        match = show_regex.findall(line)

    if match:
        key = match[0] + " (Partial/Stream)" if partial else match[0]
        shows[key].add(hash(line))


print SimpleTable([(show, len(dls)) for show, dls in shows.items()], ('Show', 'Unique'))

pickle.dump(shows, open(state_file, 'wb'))
