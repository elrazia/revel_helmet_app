from textwrap import dedent
def object_not_found():
    out = """\n
          No helmet found in photo provided.
          Here are some other objects I detected,
          and how confident I am that they are present: \n
          """
    return dedent(out)

def parse_rekognition_labels(response):
    resp = [ ("Label: ", "Confidence(%): ") ]
    for label in response["Labels"]:
        if (label["Name"] == "Helmet") and (label["Confidence"] >= 98):
            obj = label["Name"]
            conf = round(label["Confidence"],2)
            return f"I am {conf}% confident that there is a {obj} in the photo provided."
        resp.append( (label["Name"], str( round( label["Confidence"],2 ) ) ) )
    return object_not_found() + "\n".join(label_name + " " + confidence_level for label_name,confidence_level in resp)
