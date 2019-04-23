# Running Remotely
If you want to run this on a remote server, you can forward the connection through SSH tunneling.

$ ssh -L 8888:localhost:8888 xarc0
$ ~/.local/bin/jupyter notebook --no-browser

Then just copy/paste the url into your local browser.
