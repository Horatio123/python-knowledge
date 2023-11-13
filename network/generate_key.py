from OpenSSL import crypto


def generate_key():

    # 生成RSA密钥对
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # 生成X.509证书请求
    req = crypto.X509Req()
    subj = req.get_subject()
    subj.countryName = "CN"
    subj.stateOrProvinceName = "Beijing"
    subj.localityName = "Haidian"
    subj.organizationName = "ACME Inc."
    subj.commonName = "www.example.com"
    req.set_pubkey(key)
    req.sign(key, "sha256")

    # 使用颁发机构的私钥签署X.509证书
    cert = crypto.X509()
    cert.set_subject(subj)
    cert.set_serial_number(0)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # 设置有效期为1年
    cert.set_issuer(cert.get_subject())  # 将证书自签名
    cert.set_pubkey(req.get_pubkey())
    cert.sign(key, "sha256")

    # 将证书和密钥写入文件
    with open("server.crt", "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    with open("server.key", "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))


if __name__ == '__main__':
    generate_key()


