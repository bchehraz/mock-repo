# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("../vtc-angular")
# Your mock repo
mock_repo = git.Repo("./")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['babak.chehraz@gmail.com', 'bchehraz@redcort.com'])

importer.import_repository()
