# -*- coding: utf-8 -*-
from .venv_command import VenvCommand


class ExportCommand(VenvCommand):
    """
    Export locked packages in a pip-freeze compatible way.

    export
        { --no-dev : Do not export dev dependencies. }
    """

    help = """The <info>export</info> command list all locked packages with the pinned version in the same format used by pip."""

    def handle(self):
        from poetry.installation.installer import PipInstaller

        installer = PipInstaller(
            self.venv,
            self.output,
        )

        # requires = self.poetry.package.requires + self.poetry.package.dev_requires
        # print(requires)

        with_dev_reqs = not self.option("no-dev")
        locked_repo = self.poetry.locker.locked_repository(with_dev_reqs)

        for package in locked_repo.packages:
            self.line(installer.requirement(package))
