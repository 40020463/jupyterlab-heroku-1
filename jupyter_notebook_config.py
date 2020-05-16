# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password = "sha256:f19629243b3c:371ae8747a706a0f443b66bb9fd4e8d86a3e73caa51f8be88bfaf66697132e0b"
