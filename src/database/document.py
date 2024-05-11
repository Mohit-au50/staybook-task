class HotelDetails:
    def __init__(self):
        self.hotelName = ""  # string
        self.hotelEmailId = ""  # string
        self.hotelContactNumber = 0  # number
        self.hotelLandmark = ""  # string
        self.hotelAddress = ""  # string
        self.hotelStarRating = 0  # number
        self.hotelImageUrl = ""  # string

        self.hotelCity = ""  # string
        self.hotelState = ""  # string
        self.hotelPincode = ""  # string

        self.hotelSlugsDetails = {
            "hotel": "",  # string
            "hotelCity": "",  # string
            "hotelState": "",  # string
        }

        self.hotelLongitude = 0  # number
        self.hotelLatitude = 0  # number
        self.hotelMapUrl = ""  # string

        self.hotelPaymentOption = {
            "postpaid": False,  # boolean
            "prepaid": False,  # boolean
            "partial": False,  # boolean
        }

        self.hotelImagesList = [
            {
                "imageId": "",  # string
                "imageUrl": "",  # string
                "imageTitle": "",  # string
            },
            {
                "imageId": "",  # string
                "imageUrl": "",  # string
                "imageTitle": "",  # string
            },
            {
                "imageId": "",  # string
                "imageUrl": "",  # string
                "imageTitle": "",  # string
            },
            {
                "imageId": "",  # string
                "imageUrl": "",  # string
                "imageTitle": "",  # string
            },
        ]
