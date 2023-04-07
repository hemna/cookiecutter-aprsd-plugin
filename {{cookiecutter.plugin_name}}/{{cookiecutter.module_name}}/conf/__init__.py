from oslo_config import cfg

from {{cooiecutter.module_name}}.conf import main


CONF = cfg.CONF
main.register_opts(CONF)