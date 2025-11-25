import requests
from utils.configs.url_links import get_base_api_url

class BookingManagementCalls:

    def __init__(self):
        pass

    @staticmethod
    def post_booking_order_call(auth_token: str, first_name: str, last_name: str, total_price: int, deposit_paid: bool, check_in_date: str, check_out_date: str, additional_needs: str):

        api_base_url = get_base_api_url()
        endpoint = "booking"
        headers = {"Content-Type": "application/json", "Authorization": auth_token}
        json_body = {"firstname": first_name, "lastname": last_name,
                     "totalprice": total_price, "depositpaid": deposit_paid, "bookingdates": {"checkin" : check_in_date, "checkout" : check_out_date},
                     "additionalneeds": additional_needs}


        response = requests.post(f"{api_base_url}/{endpoint}", headers=headers, json=json_body)

        return response
