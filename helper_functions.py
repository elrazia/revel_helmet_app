def parse_rekognition_labels(response):
    resp = [ ("Label: ", "Confidence(%): ") ]
    for label in response["Labels"]:
        if (label["Name"] == "Helmet") and (label["Confidence"] >= 98):
            obj = label["Name"]
            conf = round(label["Confidence"],2)
            return f"I am {conf}% confident that there is a {obj} in the photo provided."
        resp.append( (label["Name"], str( round( label["Confidence"],2 ) ) ) )
    return """              No helmet found in photo provided.
              Here are some other objects I detected,
              and how confident I am that they are present: \n\n""" + "\n".join(x + " " + y for x,y in resp)
