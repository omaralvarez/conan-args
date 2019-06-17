from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools


class argsConan(ConanFile):
    name = "args"
    version = "6.2.1"
    description = "A simple header-only C++ argument parser library https://github.com/Taywee/args"
    license = "MIT"
    url = "https://github.com/omaralvarez/conan-args"
    repo_url = "https://github.com/Taywee/args"
    author = "Richberger, Pavel Belikov"
    exports_sources = "*.hxx"
    no_copy_source = True

    def source(self):
        self.run_command("git clone -b '6.2.1' --single-branch --depth 1 %s" % (self.repo_url))
    
    def run_command(self, cmd, cwd=None):
        self.output.info(cmd)
        self.run(cmd, True, cwd)

    def build(self):
        pass

    def package(self):
        self.copy(pattern="*.hxx", dst="include")

    def package_id(self):
        self.info.header_only()