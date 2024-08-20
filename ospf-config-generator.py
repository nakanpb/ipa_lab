$ mkdir config
$ pip install pyyaml
$ cat ospf-config-generator.py
from jinja2 import Environment, FileSystemLoader
import yaml

loader = FileSystemLoader("templates")
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = env.get_template("router-ospf.j2")

with open("data/routers-ospf.yml") as f:
    routers = yaml.safe_load(f)

for router in routers:
    router_conf = "config/" + router["management_ip"] + "-exercise-ospf.txt"
    with open(router_conf, "w") as f:
        f.write(template.render(router))
$ python3 ospf-config-generator.py
$ ls config
172.31.110.3-exercise-ospf.txt 172.31.110.4-exercise-ospf.txt
$