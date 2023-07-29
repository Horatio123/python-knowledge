import requests
import json


def get_rules(url_request):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "cookie": "MW_Doc_Template=WEB||||||||||; AGL_USER_ID=bff2daad-2d8b-4946-a7c2-ae49007eb522; __qca=P0-1549400026-1665391888694; MW_toc_clicked=false; lc_user_prefs=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkludGNJbk5vYjNkZmMyVmhjbU5vWDNCaGJtVnNYQ0k2Ym5Wc2JDeGNJbVZ0WVdsc1hDSTZYQ0o1YVc1cmRXNHVZMmhsYmtCc2IzUjFjMk5oY25NdVkyOXRMbU51WENKOUlnPT0iLCJleHAiOiIyMDI0LTAyLTA2VDAzOjE3OjA5LjU2M1oiLCJwdXIiOm51bGx9fQ%3D%3D--cf803e9b10a6a20edd47b70001cbab8765e16fd4; s_fid=645A8D139B630475-02D957EBFF76950D; ki_t=1665392314582%3B1676516682709%3B1676516682709%3B5%3B16; ki_r=; mwa=%7B%22expiration%22%3A-1%2C%22id%22%3A%22Y4OZpp%22%7D; at_check=true; _sdsat_eid=; AMCVS_B1441C8B533095C00A490D4D%40AdobeOrg=1; s_cc=true; _ft__source=undefined; _ft__flag=1677836888424; mwa_prefs=%7B%22domain%22%3A%22cn%22%2C%22lang%22%3A%22en%22%2C%22v%22%3A2%7D; s_sq=%5B%5BB%5D%5D; _abck=5F2DAC578E58ECA730C88932B339B589~0~YAAQtArgerQmYzKGAQAA0wF4sQml/mIrzBENrwOoVA9QuKOKsuqqFjxMbnmrTKJRk5tFwbh+bxztgl/iU6EimulrQo0YwbbaFQS7fcbZr/8+06S6bISCiRuc1g9lqbbTIZ8Io2XzNIpOsskPRkj4PcrmNKSnnDvemlfadlif8yq7WlrgiCW5KoiTRplGzz9s0cV8e6a4PV78LqRpDkfbh9So0GJl7KHkSD8fJFm5cBD7flMRRUzxzo/EOFCaVbNtoJ0HhE3XSga02tWO0ludXf6G4CdvvIer3pjW3+fudZgo+i7Z9W274Uc7G6ihXp/1lVHWglkBSRgnlSV87sCTTi2T94Z5KQEQ0QvPRMpIRi9qryX98ErQkCW2DKvkMfQQw481Y0lXawxjStRxJhe+VOAsd2kRX8AfnzM=~-1~-1~-1; bm_sz=6B7A147169A0B1275C28AFEFAA8D5629~YAAQtArgerYmYzKGAQAA0wF4sRNKPaomUR/A7jk03GjrH7Hu1qXTuVdH5VGaHVIK7Wr4aapTiGZeVsoz7NIl8t+BDLU/v5T1WE3cPlCRcylRCwemkNX5LAX7sng3RTnivRk3fN1U5duZnwrbJRd2FVmzubWRDv7KPcqO0uPXnGSV51zlUFRYTWgrD0oScskVd4wgauV6+MDS8+LSLmgcdqhOQjB8RIf3ORgMj1kK4lDgCODlXzOaNPDDdawHo7UcRZyX9UFUWcV0SYNkHZ/NwSqToACkyJfBnDMDwm9AWV1olbIlQg==~3162930~3486512; bm_mi=570EEF1F019A1BECB2A63BA31D12CA7A~YAAQtArgerkmYzKGAQAAFQR4sRO3a2IPpARd1Gm4W4Kew8Z8T9wo+wAlTQoVRmH7W1H6ij8KqF8QqwV6bdtEu9W/w/8NlHy3o//q44MKYGolSJTBHVZ+3HVaLx5alBqCR/yBnEVWXbT3u4eaU9VI/DUIddxRihUFqaFhc4xh6sTxn7chvSY8oFFPNbZeoOtXeGCS+Kqs0/jf2CU2ccIJkKonA9u8sPX5BvtDAAbT1TrZd1a0rXy0ywAcfa/Ua7OrVz8PkKE/UKPaquNED6EwsdiWVsc6ppOHmnxib0vabEZGTBkkvcFOAvTYLQ+Y88piNlyHE7nI3WTuYaF8l7F5j3VCaA==~1; ak_bmsc=CCF214904BB8CAF7628FD86707D0BF94~000000000000000000000000000000~YAAQtArger4mYzKGAQAA2Ql4sRMHhUgNxNJOLduKFrcNI8yzWvsP+ijvZyLJoWvV3TTN3Onplh1OGP+7mujAuDtrE1/xWPApMftB3//yMySIgVhxax+ronn2EvwAik96Uw62H6Fch7KHyPA6KINf5Pjo1Dx51TuZD6+RSsasMY8OqhqfDzFjsKDSgPNEOwDPCV/7jeur76vOXfT0FKp6jps8vS0taJEAT8Ke2gIsea8T4DIad0OgjKFiMabOJKQ9VOIhibRFFTmWQKB1MuE3cartVLls3vOE8mqn7jw1qFetzbyg/9gKce/+OKwn8v0vNwsrG6ZEoShGGjdVkNylea/y6jLyEqABh9WJrFKJ0UPmud77N0GqSmGd+usvNKOKu6LveeErb4wvCeHH7NT2jJj3feI6f5smc9l61YW8PCcSSeGOPYLbLn9bWpO7L6DEQBw=; mwa_session=%7B%22id%22%3A%22Y4OZpp%22%2C%22token%22%3A%22MiwxOWFxaHJlZ21iY282cDUxNXUweG4wYjltczh1bzZwcXhmaXZqenBtOHVmZzlua3RwcSxHeFg3aDNISW50UTJkUWVTdjFkZDF1RjJSSDd6U2lWQzIvMEkxM2RWRlFnZmZyb1pGcUY0VE9kbjZhYm5KZXpyN1JlWG1QeDV0R1lTTUsxUlltRm9mTFEyRUFPUDcvVHdiTWZYV251ZjcxMnNRWlRZZ05Pcm9VMDhoY0hsNGpGWHdQbkVZOExNVDF5eHZjRFlqSmlnZUQ5QWEvOVFYOGJVN2tpSDk0c3g2enV3Mi9qN0FLaWdzREx3TnhJbTVlRDg%3D%22%7D; mwa_SID=Y4OZpp; s_inv=174707; AMCV_B1441C8B533095C00A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19422%7CMCMID%7C78051377753187739950603738283123242709%7CMCAAMLH-1678619485%7C11%7CMCAAMB-1678619485%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1678021885s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; Hm_lvt_2fadae56228ee5ddcc7462d4b42f519c=1677046219,1677640299,1677723937; _ft__slotid=undefined; _ft__aid=2003439; _ft__adid=undefined; _ft__pvid=undefined; _ft__groupid=undefined; _ft__vendorid=undefined; _ft__rtbtime=undefined; _ft__device_id=undefined; _ft__first_pvid=undefined; _ft__os=undefined; _ft__device_id_type=undefined; _ft__cid=; s_tslv=1678014695786; mbox=PC#42f2c715348840798335f1e4d7cb68df.32_0#1741259497|session#968c69f15470453f9b7c7845aef24a16#1678016557; Hm_lpvt_2fadae56228ee5ddcc7462d4b42f519c=1678014696; _ft__depth=9; mwa_profile=%7B%22profile%22%3A%7B%22profilePicture%22%3A%2227865536_1665384832040_DEF.jpg%22%2C%22loginDisplayName%22%3A%22%E9%93%B6%E5%9D%A4%22%2C%22accessToMO%22%3Afalse%7D%2C%22id%22%3A%22Y4OZpp%22%7D; JSESSIONID=1787eda89f4356b57a413213eb35; bm_sv=436D3ED37A11B8539CA50B61292AEB78~YAAQtArgekYnYzKGAQAA4394sRM4uynCJbWGLK3Vw+JEO8/ciI4iO2B6n29bgB5+4AeNK4wxsaBmJHO3ey5HlNsRGEsfovfCdEVLCulOIdvcZVOFyH3721SnSwQsHPbBvTSK9LYPGxi7xgIvd6qfbqN9TvFu24xKdknv3AIgsvugr8y5yYWqQmI8bVJXWAYdvDe4fdKo05hcwS2qi2zQmHQxCszPAryaH/tUBtRhVV/GTGSH/tUAQcCT/qzgfrX4XDtD~1; RT=\"z=1&dm=ww2.mathworks.cn&si=d8a32555-3f5f-4feb-9710-8c829924b843&ss=levam5we&sl=3&tt=2hn&obo=2&rl=1&nu=12vd8ubp6&cl=9vl&ld=spy&r=1n8gk6pe&ul=sq0\""}
    # url_request = "https://ww2.mathworks.cn/help/releases/R2022b/bugfinder/dynamic-memory-checks.html"
    # url_request = "https://ww2.mathworks.cn/help/releases/R2022b/bugfinder/numerical-checks.html"

    # url_request = "https://ww2.mathworks.cn/help/releases/R2022b/bugfinder/defect-reference.html"
    # print(url_request)
    # res = requests.get(url=url_request, headers=headers)
    rules = []
    session = requests.Session()
    response = session.get(url_request, headers=headers)
    # print(response.text)
    lines = response.text.split("<a href=\"ref/")
    for line in lines:
        if line.find("<code class=\"runtimecheck\">") != -1:
            rule_name = line.split("<code class=\"runtimecheck\">")[1].split("</code")[0].split("\n")
            if len(rule_name) > 1:
                name = rule_name[0].strip() + " " + rule_name[1].strip()
            else:
                name = rule_name[0].strip()
            rule = {"html": line.split("<code class=\"runtimecheck\">")[0].split("\"")[0], "name": name}
            # print(line.split("<code class=\"runtimecheck\">")[0].split("\"")[0])
            # print(line.split("<code class=\"runtimecheck\">")[1].split("\n")[0].split("</code")[0])
            rules.append(rule)
    return rules


def get_impact(url_request):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "cookie": "MW_Doc_Template=WEB||||||||||; AGL_USER_ID=bff2daad-2d8b-4946-a7c2-ae49007eb522; __qca=P0-1549400026-1665391888694; MW_toc_clicked=false; lc_user_prefs=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkludGNJbk5vYjNkZmMyVmhjbU5vWDNCaGJtVnNYQ0k2Ym5Wc2JDeGNJbVZ0WVdsc1hDSTZYQ0o1YVc1cmRXNHVZMmhsYmtCc2IzUjFjMk5oY25NdVkyOXRMbU51WENKOUlnPT0iLCJleHAiOiIyMDI0LTAyLTA2VDAzOjE3OjA5LjU2M1oiLCJwdXIiOm51bGx9fQ%3D%3D--cf803e9b10a6a20edd47b70001cbab8765e16fd4; s_fid=645A8D139B630475-02D957EBFF76950D; ki_t=1665392314582%3B1676516682709%3B1676516682709%3B5%3B16; ki_r=; mwa=%7B%22expiration%22%3A-1%2C%22id%22%3A%22Y4OZpp%22%7D; at_check=true; _sdsat_eid=; AMCVS_B1441C8B533095C00A490D4D%40AdobeOrg=1; s_cc=true; _ft__source=undefined; _ft__flag=1677836888424; mwa_prefs=%7B%22domain%22%3A%22cn%22%2C%22lang%22%3A%22en%22%2C%22v%22%3A2%7D; s_sq=%5B%5BB%5D%5D; _abck=5F2DAC578E58ECA730C88932B339B589~0~YAAQtArgerQmYzKGAQAA0wF4sQml/mIrzBENrwOoVA9QuKOKsuqqFjxMbnmrTKJRk5tFwbh+bxztgl/iU6EimulrQo0YwbbaFQS7fcbZr/8+06S6bISCiRuc1g9lqbbTIZ8Io2XzNIpOsskPRkj4PcrmNKSnnDvemlfadlif8yq7WlrgiCW5KoiTRplGzz9s0cV8e6a4PV78LqRpDkfbh9So0GJl7KHkSD8fJFm5cBD7flMRRUzxzo/EOFCaVbNtoJ0HhE3XSga02tWO0ludXf6G4CdvvIer3pjW3+fudZgo+i7Z9W274Uc7G6ihXp/1lVHWglkBSRgnlSV87sCTTi2T94Z5KQEQ0QvPRMpIRi9qryX98ErQkCW2DKvkMfQQw481Y0lXawxjStRxJhe+VOAsd2kRX8AfnzM=~-1~-1~-1; bm_sz=6B7A147169A0B1275C28AFEFAA8D5629~YAAQtArgerYmYzKGAQAA0wF4sRNKPaomUR/A7jk03GjrH7Hu1qXTuVdH5VGaHVIK7Wr4aapTiGZeVsoz7NIl8t+BDLU/v5T1WE3cPlCRcylRCwemkNX5LAX7sng3RTnivRk3fN1U5duZnwrbJRd2FVmzubWRDv7KPcqO0uPXnGSV51zlUFRYTWgrD0oScskVd4wgauV6+MDS8+LSLmgcdqhOQjB8RIf3ORgMj1kK4lDgCODlXzOaNPDDdawHo7UcRZyX9UFUWcV0SYNkHZ/NwSqToACkyJfBnDMDwm9AWV1olbIlQg==~3162930~3486512; bm_mi=570EEF1F019A1BECB2A63BA31D12CA7A~YAAQtArgerkmYzKGAQAAFQR4sRO3a2IPpARd1Gm4W4Kew8Z8T9wo+wAlTQoVRmH7W1H6ij8KqF8QqwV6bdtEu9W/w/8NlHy3o//q44MKYGolSJTBHVZ+3HVaLx5alBqCR/yBnEVWXbT3u4eaU9VI/DUIddxRihUFqaFhc4xh6sTxn7chvSY8oFFPNbZeoOtXeGCS+Kqs0/jf2CU2ccIJkKonA9u8sPX5BvtDAAbT1TrZd1a0rXy0ywAcfa/Ua7OrVz8PkKE/UKPaquNED6EwsdiWVsc6ppOHmnxib0vabEZGTBkkvcFOAvTYLQ+Y88piNlyHE7nI3WTuYaF8l7F5j3VCaA==~1; ak_bmsc=CCF214904BB8CAF7628FD86707D0BF94~000000000000000000000000000000~YAAQtArger4mYzKGAQAA2Ql4sRMHhUgNxNJOLduKFrcNI8yzWvsP+ijvZyLJoWvV3TTN3Onplh1OGP+7mujAuDtrE1/xWPApMftB3//yMySIgVhxax+ronn2EvwAik96Uw62H6Fch7KHyPA6KINf5Pjo1Dx51TuZD6+RSsasMY8OqhqfDzFjsKDSgPNEOwDPCV/7jeur76vOXfT0FKp6jps8vS0taJEAT8Ke2gIsea8T4DIad0OgjKFiMabOJKQ9VOIhibRFFTmWQKB1MuE3cartVLls3vOE8mqn7jw1qFetzbyg/9gKce/+OKwn8v0vNwsrG6ZEoShGGjdVkNylea/y6jLyEqABh9WJrFKJ0UPmud77N0GqSmGd+usvNKOKu6LveeErb4wvCeHH7NT2jJj3feI6f5smc9l61YW8PCcSSeGOPYLbLn9bWpO7L6DEQBw=; mwa_session=%7B%22id%22%3A%22Y4OZpp%22%2C%22token%22%3A%22MiwxOWFxaHJlZ21iY282cDUxNXUweG4wYjltczh1bzZwcXhmaXZqenBtOHVmZzlua3RwcSxHeFg3aDNISW50UTJkUWVTdjFkZDF1RjJSSDd6U2lWQzIvMEkxM2RWRlFnZmZyb1pGcUY0VE9kbjZhYm5KZXpyN1JlWG1QeDV0R1lTTUsxUlltRm9mTFEyRUFPUDcvVHdiTWZYV251ZjcxMnNRWlRZZ05Pcm9VMDhoY0hsNGpGWHdQbkVZOExNVDF5eHZjRFlqSmlnZUQ5QWEvOVFYOGJVN2tpSDk0c3g2enV3Mi9qN0FLaWdzREx3TnhJbTVlRDg%3D%22%7D; mwa_SID=Y4OZpp; s_inv=174707; AMCV_B1441C8B533095C00A490D4D%40AdobeOrg=-1124106680%7CMCIDTS%7C19422%7CMCMID%7C78051377753187739950603738283123242709%7CMCAAMLH-1678619485%7C11%7CMCAAMB-1678619485%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1678021885s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; Hm_lvt_2fadae56228ee5ddcc7462d4b42f519c=1677046219,1677640299,1677723937; _ft__slotid=undefined; _ft__aid=2003439; _ft__adid=undefined; _ft__pvid=undefined; _ft__groupid=undefined; _ft__vendorid=undefined; _ft__rtbtime=undefined; _ft__device_id=undefined; _ft__first_pvid=undefined; _ft__os=undefined; _ft__device_id_type=undefined; _ft__cid=; s_tslv=1678014695786; mbox=PC#42f2c715348840798335f1e4d7cb68df.32_0#1741259497|session#968c69f15470453f9b7c7845aef24a16#1678016557; Hm_lpvt_2fadae56228ee5ddcc7462d4b42f519c=1678014696; _ft__depth=9; mwa_profile=%7B%22profile%22%3A%7B%22profilePicture%22%3A%2227865536_1665384832040_DEF.jpg%22%2C%22loginDisplayName%22%3A%22%E9%93%B6%E5%9D%A4%22%2C%22accessToMO%22%3Afalse%7D%2C%22id%22%3A%22Y4OZpp%22%7D; JSESSIONID=1787eda89f4356b57a413213eb35; bm_sv=436D3ED37A11B8539CA50B61292AEB78~YAAQtArgekYnYzKGAQAA4394sRM4uynCJbWGLK3Vw+JEO8/ciI4iO2B6n29bgB5+4AeNK4wxsaBmJHO3ey5HlNsRGEsfovfCdEVLCulOIdvcZVOFyH3721SnSwQsHPbBvTSK9LYPGxi7xgIvd6qfbqN9TvFu24xKdknv3AIgsvugr8y5yYWqQmI8bVJXWAYdvDe4fdKo05hcwS2qi2zQmHQxCszPAryaH/tUBtRhVV/GTGSH/tUAQcCT/qzgfrX4XDtD~1; RT=\"z=1&dm=ww2.mathworks.cn&si=d8a32555-3f5f-4feb-9710-8c829924b843&ss=levam5we&sl=3&tt=2hn&obo=2&rl=1&nu=12vd8ubp6&cl=9vl&ld=spy&r=1n8gk6pe&ul=sq0\""}
    # url_request = "https://ww2.mathworks.cn/help/releases/R2022b/bugfinder/ref/bitwiseoperationonnegativevalue.html"
    # url_request = "https://ww2.mathworks.cn/help/releases/R2022b/bugfinder/ref/floatdivisionbyzero.html"

    # print(url_request)
    # res = requests.get(url=url_request, headers=headers)
    rules = []
    session = requests.Session()
    response = session.get(url_request, headers=headers)
    return response.text.split(">Impact")[1].split("</strong>")[1].split("</span>")[0].strip()


def process_group():
    fo = open("mathwork_defects.html", "r")
    groups = []
    for line in fo.readlines():
        line = line.strip()
        if line.find("dcenter_c1title") != -1:
            # print(line.split("href=")[1].split('>')[0])
            # print(line.split("href=")[1].split('>')[1].split('<')[0])
            group = {"html": line.split("href=\"")[1].split('\">')[0], "name": line.split("href=")[1].split('>')[1].split('<')[0]}
            groups.append(group)
            # line.strip('(')
            # info = line.replace('(', '').split(',')
            # site = {"stcode": info[0].replace('\'', ''), "name": info[1].replace('\'', ''), "lng":float(info[2].replace('\'', '')), "lat": float(info[3].replace('\'', '')), "abcode": info[4].replace('\'', ''), "createTime": info[6].replace('\'', ''), "pictures": []}
            # sites.append(site)
    # 关闭文件
    fo.close()
    return groups


if __name__ == '__main__':
    ps_rules = []
    rule_url = "https://ww2.mathworks.cn/help/releases/R2022b/bugfinder/"
    impact_url = "https://ww2.mathworks.cn/help/releases/R2022b/bugfinder/ref/"
    defects_groups = process_group()
    # print(defects_groups)
    # defects_rules = get_rules()
    # print(defects_rules)
    for defects_group in defects_groups:
        print(defects_group.get("html"))
        print(defects_group.get("name"))
        defects_rules = get_rules(rule_url + defects_group.get("html"))

        for defects_rule in defects_rules:
            print(defects_rule.get("html"))
            print(defects_rule.get("name"))

            impact = get_impact(impact_url + defects_rule.get("html"))
            ps_rule = {"group": defects_group.get("name"), "name": defects_rule.get("name"), "impact": impact}
            ps_rules.append(ps_rule)

    print(ps_rules)
    file = open('res.json', 'w', encoding='utf-8')
    json.dump(ps_rules, file, ensure_ascii=False)

    # get_impact()

