import container.helper.ip_address


def formatFilterArguments(kwargs):
    args = []

    if kwargs.get("source_ip") is not None:
        kwargs["source_ip"] = container.helper.ip_address.replace_ip_string(kwargs["source_ip"], False)
        args.append({"$regexMatch": {"input": "$$t.Source-IP", "regex": ".*" + kwargs["source_ip"] + ".*"}})

    if kwargs.get("destination_ip") is not None:
        kwargs["destination_ip"] = container.helper.ip_address.replace_ip_string(kwargs["destination_ip"], False)
        args.append(
            {"$regexMatch": {"input": "$$t.Destination-IP", "regex": ".*" + kwargs["destination_ip"] + ".*"}})

    if kwargs.get("source_port") is not None:
        args.append({"$eq": ["$$t.Source-Port", int(kwargs["source_port"])]})

    if kwargs.get("start_src_port") is not None:
        args.append({"$gte": ["$$t.Source-Port", int(kwargs["start_src_port"])]})

    if kwargs.get("end_src_port") is not None:
        args.append({"$lte": ["$$t.Source-Port", int(kwargs["end_src_port"])]})

    if kwargs.get("destination_port") is not None:
        args.append({"$eq": ["$$t.Destination-Port", int(kwargs["destination_port"])]})

    if kwargs.get("start_dst_port") is not None:
        args.append({"$gte": ["$$t.Destination-Port", int(kwargs["start_dst_port"])]})

    if kwargs.get("end_dst_port") is not None:
        args.append({"$lte": ["$$t.Destination-Port", int(kwargs["end_dst_port"])]})

    if kwargs.get("protocol") is not None:
        kwargs["protocol"] = kwargs["protocol"].upper()
        args.append({"$eq": ["$$t.Protocol", kwargs["protocol"]]})

    if kwargs.get("start_length") is not None:
        args.append({"$gte": ["$$t.Length", int(kwargs["start_length"])]})

    if kwargs.get("end_length") is not None:
        args.append({"$lte": ["$$t.Length", int(kwargs["end_length"])]})

    if kwargs.get("start_ttl") is not None:
        args.append({"$gte": ["$$t.TTL", int(kwargs["start_ttl"])]})

    if kwargs.get("end_ttl") is not None:
        args.append({"$lte": ["$$t.TTL", int(kwargs["end_ttl"])]})

    if len(args) == 0:
        args.append({"$gte": ["$$t.TTL", 0]})

    return args


def formatDateArguments(kwargs):
    if kwargs["date"] is not None and kwargs["hour"] is not None:
        return {"$match": {"$and": [{"date": kwargs["date"]}, {"hour": kwargs["hour"]}]}}
    elif kwargs["date"] is not None:
        return {"$match": {"date": kwargs["date"]}}
    elif kwargs["hour"] is not None:
        return {"$match": {"hour": kwargs["hour"]}}
    else:
        return None


def formatLimitArgument(limit):
    return int(limit) if limit is not None and int(limit) < 500 else 100


def formatTableData(table_collection):
    table_dataset = []

    for record in table_collection:
        record["Traffic"]["Source-IP"] = container.helper.ip_address.replace_ip_string(record["Traffic"]["Source-IP"],
                                                                                       False)
        record["Traffic"]["Destination-IP"] = container.helper.ip_address.replace_ip_string(
            record["Traffic"]["Destination-IP"], False)
        table_dataset.append(record["Traffic"])

    return {"dataset": table_dataset}
