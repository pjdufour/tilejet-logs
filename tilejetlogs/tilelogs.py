def buildTileRequestDocument(tileorigin, tilesource, x, y, z, status, datetime, ip):
    r = {
        'ip': ip,
        'origin': tileorigin if tileorigin else "",
        'source': tilesource,
        'location': z+'/'+x+'/'+y,
        'z': z,
        'status': status,
        'year': datetime.strftime('%Y'),
        'month': datetime.strftime('%Y-%m'),
        'date': datetime.strftime('%Y-%m-%d'),
        'date_iso': datetime.isoformat()
    }
    return r
