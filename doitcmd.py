"""
Helpers for creating tasks that exectue shell commands.
"""

__version__ = (0, 1, 0)

from doit.tools import Interactive



class BaseCommand(object):
    """Base class to create tasks that execute a shell command.

    It provides:

      - conversion of a param dict to a command options string
      - handle/control wheather the command should be as `sudo`
      - handle/control wheather the command is going to be execute interactively

    :var str cmd_template: python str template for command
                           eg. `install {opts} {source} {dest}`

    :var dict base_options: default command options
    :var bool sudo: If `True` prepend `sudo` to command
    :var bool Interactive: If `True` use `doit.tools.Interactive` on action.

    Usage: see `doitsys.copy.Copy`
    """
    cmd_template = None
    base_options = {}
    sudo = False
    interactive = False


    def __init__(self, sudo=None, interactive=None, options=None):
        if sudo is not None:
            self.sudo = sudo
        if interactive is not None:
            self.interactive = interactive
        self.options = {}
        self.options.update(self.base_options)
        if options:
            self.options.update(options)


    @staticmethod
    def opt_str(*opt_list):
        """command line option formatter

        :param list-dict opt_list: list of dict with command options
        :return string: formatted options for a command line

        If the value of an option is `True`, option is added wihtout a value.
        If opt name lenght is just one characher use only one dash.
        """
        options = {}
        for opt_dict in opt_list:
            options.update(opt_dict)

        # format options as strings
        parts = []
        for name, val in sorted(options.items()):
            if val is False or val is None:
                continue
            dashes = '-' if len(name) == 1 else '--'
            opt_val = ' {}'.format(val) if val is not True else ''
            parts.append(dashes + name + opt_val)
        return ' '.join(parts)


    def action(self, cmd_str):
        """Modify action adding sudo / Interactive.

        :param str cmd_str: command string
        :return: An action for a doit task (might be a plain string)
        """
        if self.sudo:
            cmd_str = 'sudo ' + cmd_str
        if self.interactive:
            return Interactive(cmd_str)
        else:
            return cmd_str


    def __call__(self): # pragma: no cover
        """return a task dictionary (to be implement on sub-class)"""
        raise NotImplementedError()



def cmd(cmd_str, sudo=None, **task_params):
    """short-cut to return a task that executes a simple command

    :param str cmd_str: the command to be executed
    :param bool sudo: execute to command as `sudo`
    :param dict task_params: extra doit task params (file_dep, task_dep...)
    :return dict: doit task metadata
    """
    _cmd = BaseCommand(sudo=sudo)
    task = {
        'name': cmd_str,
        'actions': [_cmd.action(cmd_str)],
        }
    task.update(task_params)
    return task


def interactive(cmd_str, sudo=None, **task_params):
    """short-cut to return a task that executes a simple command interactively

    :param str cmd_str: the command to be executed
    :param bool sudo: execute to command as `sudo`
    :param dict task_params: extra doit task params (file_dep, task_dep...)
    :return dict: doit task metadata
    """
    _cmd = BaseCommand(sudo=sudo, interactive=True)
    task = {
        'name': cmd_str,
        'actions': [_cmd.action(cmd_str)],
        }
    task.update(task_params)
    return task
