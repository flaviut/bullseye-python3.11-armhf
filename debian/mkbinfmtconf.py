# mkbinfmtconf.py
import importlib.util, sys, string, os.path

magic = "".join(["\\x%.2x" % c for c in importlib.util.MAGIC_NUMBER])

name = sys.argv[1]

sys.stdout.write(f":{name}:M::{magic}::/usr/bin/{name}:")
sys.stdout.write('\n')
