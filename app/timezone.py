import geoip2.database
from geoip2.errors import AddressNotFoundError
from datetime import datetime
from pytz import timezone, all_timezones, country_timezones, utc

# take the given data and if timezone given, try to use it.
# Otherwise, try to see get the timezone via the IP-address lookup
# then return the timezone
def processTZ(timezone, ip):
    tz = None
    if(timezone):
        tz = getTimezoneName(timezone)
    else:
        tz = getIPtoTZ(ip)
    return tz


# takes an IP and returns its timezone
def getIPtoTZ(ip):
    reader = geoip2.database.Reader('/usr/share/GeoIP/GeoLite2-City.mmdb')
    try:
        response = reader.city(ip)
        if (response):
            return response.location.time_zone
    except AddressNotFoundError:
        pass
    return utc

# take an datetime and adjusts it for its timezone
def convertTZ(old_datetime, tz):
    return tz.localize(old_datetime)

# takes a timezone value and tries to find the correctly assocated value in pytz
def getTimezoneName(timezone):
    #see if it's already a valid time zone name
    if timezone in all_timezones:
        return timezone

    #if it's a number value, then use the Etc/GMT code
    try:
        offset = int(timezone)
        if offset > 0:
            offset = '+' + str(offset)
        else:
            offset = str(offset)
        return 'Etc/GMT' + offset
    except ValueError:
        pass

    # try to match the timezone abbreviation to any time zone
    set_zones = set()
    for name in all_timezones:
        tzone = timezone(name)
        for utcoffset, dstoffset, tzabbrev in getattr(tzone, '_transition_info', [[None, None, datetime.now(tzone).tzname()]]):
            if tzabbrev.upper() == timezone.upper():
                set_zones.add(name)

    return min(set_zones, key=len)