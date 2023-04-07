from oslo_config import cfg


plugin_group = cfg.OptGroup(
    name="{{cookiecutter.module_name}}",
    title="APRSD Slack Plugin settings",
)

plugin_opts = [
#    cfg.StrOpt(
#        "plugin_secret",
#        default=None,
#        help="Your plugin secret",
#    ),
]

ALL_OPTS = plugin_opts


def register_opts(cfg):
    cfg.register_group(plugin_group)
    cfg.register_opts(ALL_OPTS, group=plugin_group)


def list_opts():
    return {
        plugin_group.name: plugin_opts,
    }
