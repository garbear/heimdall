from collections import namedtuple

def PredicateBuilder(short, namespace, properties):
    predicate = namedtuple(short, properties + [ "xmlns" ])
    predicate.xmlns = namespace

    for prop in properties:
        setattr(predicate, prop, namespace + prop)

    return predicate

# Good but needed?
rdf = PredicateBuilder("rdf", "http://www.w3.org/TR/rdf-schema/", [ "Class" ])

# Certain
dc = PredicateBuilder("dc", "http://purl.org/dc/elements/1.1/", [ "title", "creator", "description", "type", "format", "identifier", "date" ])
owl = PredicateBuilder("owl", "http://www.w3.org/2002/07/owl#", [ "sameAs", "differentFrom" ])
foaf = PredicateBuilder("foaf", "http://xmlns.com/foaf/spec/", [ "Agent", "Group", "Organization", "Person", "Document", "Image", "thumbnail", "homepage" ])

# Uncertain
media = PredicateBuilder("media", "http://purl.org/media#", [ "duration", "rating" ])
video = PredicateBuilder("video", "http://purl.org/video#", [ ])
audio = PredicateBuilder("audio", "http://purl.org/audio#", [ ])

upnp = PredicateBuilder("upnp", "urn:schemas-upnp-org:metadata-1-0/upnp/", [ "artist", "album", "originalTrackNumber" ])
