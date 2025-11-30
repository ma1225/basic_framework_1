import requests
from utils.configs.url_links import get_base_api_url

class BookingManagementCalls:

    def __init__(self):
        pass

    @staticmethod
    def post_booking_order_call(auth_token: str, first_name: str, last_name: str, total_price: int, deposit_paid: bool, check_in_date: str, check_out_date: str, additional_needs: str = ""):
        """
        :param auth_token: Auth token needed for sending the API request
        :param first_name: First name of customer on order
        :param last_name: Last name of customer on order
        :param total_price: Total price of the booking order
        :param deposit_paid: True or False if the deposit was paid
        :param check_in_date: Check in start date
        :param check_out_date: Check out end date
        :param additional_needs: Additional customer needs if was filled
        :return: API response with booking order info
        """

        api_base_url = get_base_api_url()
        endpoint = "booking"
        headers = {"Content-Type": "application/json", "Authorization": auth_token}
        json_body = {"firstname": first_name, "lastname": last_name,
                     "totalprice": total_price, "depositpaid": deposit_paid, "bookingdates": {"checkin" : check_in_date, "checkout" : check_out_date},
                     "additionalneeds": additional_needs}


        response = requests.post(f"{api_base_url}/{endpoint}", headers=headers, json=json_body)

        return response

    @staticmethod
    def get_all_booking_orders_call(auth_token: str, wildcard_params: str = None):
        """
        :param auth_token: Auth token needed for sending the API request
        :param wildcard_params: Wildcard parameters in API request (for example: "firstname=sally&lastname=brown")
        :return: Response with booking order info
        """

        api_base_url = get_base_api_url()
        endpoint = "booking"
        headers = {"Content-Type": "application/json", "Authorization": auth_token}

        if wildcard_params:
            response = requests.get(f"{api_base_url}/{endpoint}?{wildcard_params}", headers=headers)
        else:
            response = requests.get(f"{api_base_url}/{endpoint}", headers=headers)

        return response

    @staticmethod
    def get_booking_order_by_id_call(auth_token: str, booking_id: int):
        """
        :param auth_token: Auth token needed for sending the API request
        :param booking_id: ID of the booking order
        :return: Response with booking order info by provided booking order ID
        """

        api_base_url = get_base_api_url()
        endpoint = "booking"
        headers = {"Content-Type": "application/json", "Authorization": auth_token}

        response = requests.get(f"{api_base_url}/{endpoint}/{str(booking_id)}", headers=headers)

        return response
