## DNS verifier plugin for Certbot
[![Build Status](https://travis-ci.org/fzhyzamt/certbot-dns-verifier.svg?branch=master)](https://travis-ci.org/fzhyzamt/certbot-dns-verifier)
[![codecov](https://codecov.io/gh/fzhyzamt/certbot-dns-verifier/branch/master/graph/badge.svg)](https://codecov.io/gh/fzhyzamt/certbot-dns-verifier)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/fzhyzamt/certbot-dns-verifier/blob/master/LICENSE)


### Support dns providers
- DNSPod

### Install

> You must install certbot before starting to install the plugin, see [Get Certbot](https://certbot.eff.org/docs/install.html)

```bash
$ cd /opt/eff.org/certbot/venv
$ source bin/activate
$ pip install certbot-dns-verifier
$ deactivate
```
After installed, You should see plugin in list

```bash
$ certbot plugins
```

If you use `sudo pip`, maybe used pip is system, you should use `sudo /opt/eff.org/certbot/venv/bin/pip`

### Credentials File

You can get the api id and token in the [DNSPod console](https://www.dnspod.cn/console/user/security).
```ini
# /root/.secrets/certbot/dnspod.ini
certbot_dns_verifier:dns_dnspod_api_id = 12345
certbot_dns_verifier:dns_dnspod_api_token = foo
```

### Obtain Certificates

```bash
certbot certonly -a certbot-dns-verifier:dns-dnspod \
			--certbot-dns-verifier:dns-dnspod-credentials /root/.secrets/certbot/dnspod.ini \
			-d "*.example.com" -d "example.com" \
			--server https://acme-v02.api.letsencrypt.org/directory \
			--renew-hook "systemctl reload nginx"
```

After successful, the command line for obtain for a certificate will be saved to config,
example: `/etc/letsencrypt/renewal/example.com.conf`  
This file saves the parameters when applying for a certificate.


### Auto renew Certificates

Because the configuration of the application certificate has been saved,
refreshing the certificate will no longer require additional parameters.

```bash
# test renew
$ certbot renew --dry-run

# renew
$ certbot renew --quiet
```

> Because the certificate is sent with the instruction to refresh the nginx, renew will also perform the refresh.

### Errors

- Unsafe permissions on credentials configuration file: /path/secret.ini

```bash
$ chmod 600 /path/secret.ini
```
