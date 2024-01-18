import logging

from oslo_config import cfg
from aprsd import packets, plugin, threads, utils
from aprsd.utils import trace

import {{cookiecutter.module_name}}
from {{cookiecutter.module_name}} import conf  # noqa

CONF = cfg.CONF
LOG = logging.getLogger("APRSD")


class {{cookiecutter.plugin_class_name}}(plugin.{{cookiecutter.plugin_parent_object}}):
{% if cookiecutter.plugin_parent_object == "APRSDRegexCommandPluginBase" %}
    version = {{cookiecutter.module_name}}.__version__
    # Change this regex to match for your plugin's command
    # Tutorial on regex here: https://regexone.com/
    # Look for any command that starts with w or W
    command_regex = "^[wW]"
    # the command is for ?
    # Change this value to a 1 word description of the plugin
    # this string is used for help
    command_name = "weather"
{% endif %}
    enabled = False

    def setup(self):
        """Allows the plugin to do some 'setup' type checks in here.

        If the setup checks fail, set the self.enabled = False.  This
        will prevent the plugin from being called when packets are
        received."""
        # Do some checks here?
        self.enabled = True

    def create_threads(self):
        """This allows you to create and return a custom APRSDThread object.

        Create a child of the aprsd.threads.APRSDThread object and return it
        It will automatically get started.

        You can see an example of one here:
        https://github.com/craigerl/aprsd/blob/master/aprsd/threads.py#L141
        """
        if self.enabled:
            # You can create a background APRSDThread object here
            # Just return it for example:
            # https://github.com/hemna/aprsd-weewx-plugin/blob/master/aprsd_weewx_plugin/aprsd_weewx_plugin.py#L42-L50
            #
            return []

    @trace.trace
    def process(self, packet: packets.core.Packet):
{% if cookiecutter.plugin_parent_object == "APRSDRegexCommandPluginBase" %}
        """This is called when a received packet matches self.command_regex.

        This is only called when self.enabled = True and the command_regex
        matches in the contents of the packet["message_text"]."""
{% elif cookiecutter.plugin_parent_object == "APRSDWatchListPluginBase" %}
        """This is called when a received packet matches the watchlist.

        This is only called when self.enabled = True and callsign in
        packet.from_call is in the config's watchlist setting."""
{% endif %}
        LOG.info("{{cookiecutter.plugin_class_name}} Plugin")

        from_callsign = packet.from_call
        message = packet.message_text

        # Now we can process
        return "some reply message"
