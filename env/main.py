
import network_as_code as nac

from network_as_code.models.device import DeviceIpv4Addr
 
# We begin by creating a Network as Code client
client = nac.NetworkAsCodeClient(
    token="ba0b53b7a6mshceae568341af5b8p156840jsneff0344ae13b"
)

my_device = client.devices.get(
    "device@testcsp.net",
    ipv4_address=DeviceIpv4Addr(
        public_address="233.252.0.2",
        private_address="192.0.2.25",
        public_port=80
    ),
    ipv6_address="2001:db8:1234:5678:9abc:def0:fedc:ba98",
    # The phone number does not accept spaces or parentheses
    phone_number="+36721601234567"
)
 
# For estimations, use the is_there object
# followed by the `verify_location()` method
# with the geo-coordinates and maximum age in seconds.
# If the amount in seconds is not given, the default will be 60 seconds.
is_there = my_device.verify_location(
    longitude=60.252,
    latitude=25.227,
    radius=10_000,
    max_age=3600
)

# Specify the maximum amount of time accepted
# to get location information, it's a mandatory parameter.
# If the amount in seconds is not given, the default will be 60 seconds.
location = my_device.location(max_age=3600)
# The location object contains fields for longitude, latitude and also elevation
longitude = location.longitude
latitude = location.latitude
 
 
print(longitude)
print(latitude)
print(location.civic_address)





