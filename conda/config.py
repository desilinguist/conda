from os import getenv, listdir
from os.path import abspath, expanduser, isdir, join
import logging
import platform
import sys
import yaml

from conda import __version__
from environment import environment


log = logging.getLogger(__name__)


CIO_DEFAULT_REPOS = [
    'http://repo.continuum.io/pkgs'
]

INFO_STRING = '''
               target : %s
             platform : %s
conda command version : %s
       root directory : %s
   packages directory : %s
      repository URLS : %s
environment locations : %s
'''

VERSION = __version__

ROOT_DIR = sys.prefix

ROOT = ROOT_DIR # This is deprecated, do not use in new code

PACKAGES_DIR = join(ROOT_DIR, 'pkgs')


class config(object):

    __slots__ = ['_rc']

    def __init__(self):
        self._rc = None

        # try to load .condarc file from users home directory
        try:
            home = getenv('USERPROFILE') or getenv('HOME')
            self._rc = yaml.load(open(join(home, '.condarc')))
            log.debug('loaded user .condarc')
            # TODO: test validity of dict (check keys)
        except:
            pass

        # otherwise try to load the system .condarc
        if not self._rc:
            try:
                self._rc = yaml.load(open(join(ROOT_DIR, '.condarc')))
                log.debug('loaded system .condarc')
                # TODO: test validity of dict (check keys)
            except:
                pass

    @property
    def conda_version(self):
        return VERSION

    @property
    def target(self):
        env_target = getenv('CIO_TARGET')
        if env_target:
            return env_target

        if 'AnacondaPro' in sys.version:
            return 'pro'
        elif 'AnacondaCE' in sys.version:
            return 'ce'
        else:
            return 'unknown'

    @property
    def platform(self):
        sys_map = {'linux2': 'linux', 'darwin': 'osx', 'win32': 'win'}
        bits = int(platform.architecture()[0][:2])
        system = sys_map.get(sys.platform, 'unknown')
        return '%s-%d' % (system, bits)

    @property
    def root_dir(self):
        return ROOT_DIR

    @property
    def packages_dir(self):
        return PACKAGES_DIR

    @property
    def system_location(self):
        return join(ROOT_DIR, 'envs')

    @property
    def user_locations(self):
        locations = []
        if self._rc:
            locations.extend(self._rc.get('locations', []))
        return sorted(abspath(expanduser(location)) for location in locations)

    @property
    def locations(self):
        return sorted(self.user_locations + [self.system_location])

    @property
    def default_environment(self):
        return environment(self, ROOT_DIR)

    @property
    def environments(self):
        envs = []
        for location in self.locations:
            for fn in listdir(location):
                prefix = join(location, fn)
                if isdir(prefix):
                    try:
                        envs.append(environment(self, prefix))
                    except RuntimeError as e:
                        log.info('%s' % e)
        envs.append(self.default_environment)
        return sorted(envs)

    @property
    def repo_base_urls(self):
        if getenv('CIO_TEST'):
            return ['http://filer/test-pkgs', 'http://filer/pkgs']
        elif self._rc:
            return self._rc['repositories']
        else:
            return CIO_DEFAULT_REPOS

    @property
    def repo_package_urls(self):
        return [
            '%s/%s/' % (url, self.platform) for url in self.repo_base_urls
        ]

    @property
    def available_packages(self):
        res = set()
        for fn in listdir(self.packages_dir):

            if sys.platform == 'win32':
                if not fn.endswith('.tar.bz2'):
                    continue
                pkg_filename = fn
            else:
                if not isdir(join(self.packages_dir, fn)):
                    continue
                pkg_filename = fn + '.tar.bz2'

            try:
                res.add(self.index.lookup_from_filename(pkg_filename))
            except KeyError:
                pass

        return res

    def lookup_environment(self, prefix):
        envs = dict((env.prefix, env) for env in self.environments)
        try:
            return envs[prefix]
        except:
            log.debug('creating environment for prefix: %s' % prefix)
            return environment(self, prefix)

    def __str__(self):
        return INFO_STRING % (
            self.target,
            self.platform,
            self.conda_version,
            self.root_dir,
            self.packages_dir,
            self.repo_package_urls,
            self.locations,
        )

    def __repr__(self):
        return 'config()'