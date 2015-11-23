def buildTileRequestDocument(tileorigin=None, tilesource=None, x=None, y=None, z=None, extension=None, status=None, datetime=None, ip=None):
    r = {
        'ip': ip,
        'origin': tileorigin if tileorigin else "",
        'source': tilesource,
        'location': str(z)+'/'+str(x)+'/'+str(y),
        'x': x,
        'y': y,
        'z': z,
        'extension': extension,
        'status': status,
        'year': datetime.strftime('%Y'),
        'month': datetime.strftime('%Y-%m'),
        'date': datetime.strftime('%Y-%m-%d'),
        'hour': datetime.strftime('%Y-%m-%d %H'),
        'minute': datetime.strftime('%Y-%m-%d %H:%M'),
        'date_iso': datetime.isoformat()
    }
    return r
