
import configparser
import io
import subprocess
import textwrap

tconfig = None


class TDTBaseException(Exception):
    pass


class TConfig(object):
    def __init__(self, config_text, section='DEFAULT', defaults={}):
        self._section = section

        self._config = configparser.ConfigParser(defaults=defaults)
        try:
            conf_str = "[{}]\n".format(self._section) + config_text
            conf_fp = io.StringIO(conf_str)
            self._config.read_file(conf_fp)
        except FileNotFoundError:
            pass

    def get(self, tag):
        try:
            val = self._config.get(self._section, tag)
        except configparser.NoOptionError:
            raise TDTBaseException("Option not found: " + tag)

        return val


def get_var(tag):
    global tconfig

    if tconfig is None:
        cp = subprocess.run(
            ["todo.txt", "--info"],
            capture_output=True,
            encoding="utf-8"
        )
        
        if cp.stdout:
            tconfig = TConfig(cp.stdout)
        else:
            # TODO - this is a temporary autopkgtest kluge
            text = textwrap.dedent(
                """
                    executable = /usr/bin/topydo
                    task_path = /tmp/topydo.conf
                """
            )
            tconfig = TConfig(text)


    return tconfig.get(tag)
