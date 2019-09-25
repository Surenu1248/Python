# 1.Given a list, url = [www.annauniv.edu, www.google.com,www.ndtv.com,www.website.org,www.bis.org.in,www.rbi.org.in];
# Sort the list based on the top level domain (edu, com, org, in) using custom sorting

lst = ["www.annauniv.edu", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]


def list_sorting(str1):
    pref_order = ["edu", "com", "org", "in"]
    tld = str1.split('.')[-1]
    tl = tld
    return pref_order.index(tld)


print(sorted(lst, key=list_sorting))
