# Traffake

A (https://github.com/locustio/locust)[Locust] based traffic faker for testing analyses

Generates loads of fake URLs and a hits them in a non-uniform distribution, designed
to vaguely approximate the visitation patterns of real traffic on large editorial sites.

# Use me

(For python 2)

```
git clone git@github.com:gamernetwork/traffake.git
cd traffake
virtualenv env
env/bin/pip install -r requirements.txt
env/bin/locust -f traffake.py -P <local-port> --host=http://<host-to-test>:<port-to-test>
```

Visit http://localhost:<localport>/ and get testing.


