
def get_base_url(env: str = "demo.applitools") -> str:

    url = ""

    if env == "demo.applitools":
        url = "https://demo.applitools.com/"

    elif env == "practicetestautomation":
        url = "https://practicetestautomation.com/practice-test-login/"

    return url

def get_base_api_url(server: str = "restful_booker") -> str:

    api_base_url = ""

    if server == "restful_booker":
        api_base_url = "https://restful-booker.herokuapp.com/"

    return api_base_url
