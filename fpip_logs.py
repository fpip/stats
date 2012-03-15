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
    if ' 200 ' not in line:
        continue

    match = show_regex.findall(line)
    if match:
        shows[match[0]].add(hash(line))

print SimpleTable([(show, len(dls)) for show, dls in shows.items()], ('Show', 'Unique'))

pickle.dump(shows, open(state_file, 'wb'))
